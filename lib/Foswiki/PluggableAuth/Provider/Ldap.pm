# Extension for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2020-2025 Michael Daum http://michaeldaumconsulting.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details, published at
# http://www.gnu.org/copyleft/gpl.html

package Foswiki::PluggableAuth::Provider::Ldap;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Ldap

TODO

=cut

use strict;
use warnings;

use Net::LDAP qw(LDAP_REFERRAL);
use URI::ldap;
use Net::LDAP::Constant qw(LDAP_SUCCESS LDAP_SIZELIMIT_EXCEEDED LDAP_CONTROL_PAGED LDAP_NO_SUCH_OBJECT);
use Net::LDAP::Extension::SetPassword;
use Encode ();
use Error qw(:try);
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider ();
use Digest::MD5 ();
#use Data::Dump qw(dump);
use utf8;

our @ISA = qw(Foswiki::PluggableAuth::Provider );

our $IMAGEMAGICK_ENABLED;

BEGIN {
  eval 'use Image::Magick()';
  $IMAGEMAGICK_ENABLED = $@ ? 0 : 1;
}

=begin TML

---++ ClassMethod new(%params) -> $this

constructor

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{_ldap} = undef;
  $this->{_imageMagickInstalled} = 1 unless $@;

  return $this;
}

sub finish {
  my $this = shift;

  $this->SUPER::finish;

  $this->disconnect;
  undef $this->{_ldap};
  undef $this->{_encoding};
}

sub handlesLogin {
  my ($this, $request, $state) = @_;

  $this->writeDebug("called handlesLogin");

  return 0 unless $this->SUPER::handlesLogin($request, $state);

  my $authName = $request->param("username");
  return 0 unless defined $authName;

  $authName = lc($authName) unless $this->prop("CaseSensitiveLogin");
  $this->writeDebug("... loginName=$authName");

  my $user = $this->findAuthName($authName);
  return $this->handles($user) if defined $user;

  if ($this->prop("SyncOnLogin") || !$this->prop("PrefetchUsers")) {
    my $entry = $this->getEntryOfUser($authName);
    return 1 if defined $entry;
  }

  return 0;
}

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin, this=$this");

  my $authName = $request->param("username");
  my $password = $request->param("password");
  return unless defined $authName && $password;

  $authName = lc($authName) unless $this->prop("CaseSensitiveLogin");
  $this->writeDebug("... loginName=$authName");

  $this->writeDebug("... checking password");
  if ($this->checkPassword($authName, $password)) {

    my $user = $this->findAuthName($authName);

    my $doPrefetch = $this->prop("PrefetchUsers");
    my $doSyncUser = $this->prop("SyncOnLogin");

    # sync user topic on login
    if ($doSyncUser || !$doPrefetch) {

      my $entry = $this->getEntryOfUser($authName);
      throw Error::Simple($this->auth->maketext("Sorry, account not found")) unless defined $entry;

      my $userInfo = $this->extractUserInfo($entry);
      throw Error::Simple($this->auth->maketext("Sorry, account not found")) unless defined $userInfo;

      if ($user) {
        $user = $this->updateUser($user, $userInfo) if $doSyncUser;
      } else {
        $user = $this->addUser(%$userInfo);

        # refresh topic groups 
        $this->auth->getProvider("Topic")->cacheGroups();
      }
    }
  
    throw Error::Simple($this->auth->maketext("Sorry, account is disabled")) unless defined $user && $user->isEnabled;

    return $user;
  }

  $this->writeDebug("... failed");
  return;
}

sub checkGroupAccess {
  my ($this, $type, $group, $user) = @_;

  return 1 if $type =~ /^VIEW$/i;
  return 0;
}

sub checkPassword {
  my ($this, $authNameOrUser, $password) = @_;

  $this->writeDebug("called checkPassword($authNameOrUser)");

  my $dn = $this->getDnOfUser($authNameOrUser);
  return 0 unless $dn;
 
  my $isOk; 
  try {
    $this->writeDebug("... connecting with dn=$dn");
    $isOk = $this->connect($dn, $password);
  } catch Error with {
    $this->writeDebug("... ".shift);
    $isOk = 0;
  };

  return $isOk;
}

sub getDnOfUser {
  my ($this, $authNameOrUser) = @_;

  my $entry = $this->getEntryOfUser($authNameOrUser);

  return unless $entry;
  return $this->getDN($entry);
}

sub getEntryOfUser {
  my ($this, $authNameOrUser) = @_;

    $this->writeDebug("called getEntryOfUser($authNameOrUser)");

  my $loginName;
  my $email;

  if (ref($authNameOrUser)) {
    $loginName = $authNameOrUser->prop("loginName");
  } elsif ($Foswiki::cfg{PluggableAuth}{AllowLoginUsingEmailAddress} && $authNameOrUser =~ /@/) { # allow login with email address given loginNames don't have an @ in it
    $email = $authNameOrUser;
  } else {
    $loginName = $authNameOrUser;
  }

  return unless defined $loginName || defined $email;

  my $msg;
  my $entry;
  my $filter;

  if (defined $loginName) {
    $filter = $this->prop("LoginNameAttribute") . "=$loginName";
  } elsif (defined $email) {
    $filter = $this->prop("MailAttribute") . "=$email";
  }

  try {
    foreach my $userBase (@{$this->prop("UserBase")}) {
      $this->writeDebug("... filter=$filter, base=$userBase");

      $msg = $this->search(
        filter => $filter,
        base => $userBase,
        scope => $this->prop("UserScope"),
        deref => "always",
      );

      _checkError($msg); # throws an exception in case of an error
      #$this->writeDebug(".. mesg=".dump($msg));

      $entry = $msg->entry(0);
      #$this->writeDebug(".. entry=".dump($entry));

      last if defined $entry;
    }
  } catch Error with {
    _writeError(shift);
  };

  return $entry;
}

sub canSetEmail {
  return 0;
}

#sub canDelete {
#  return 0;
#}

sub canSetPassword {
  my ($this, $user) = @_;

  return 0 if defined($user) && !$this->handles($user);
  return $this->prop("AllowChangePassword");
}

sub setPassword {
  my ($this, $user, $newPassword, $oldPassword) = @_;

  $this->writeDebug("called setPassword()");
  throw Error::Simple($this->auth->maketext("Cannot change password")) 
    unless $this->canSetPassword($user);

  throw Error::Simple($this->auth->maketext("Invalid password")) 
    unless $this->isValidPassword($newPassword);

  # connect using the provided password for the user
  if (defined $oldPassword && $oldPassword ne "") {
    my $dn = $this->getDnOfUser($user);
    return unless $dn;

    return unless $this->connect($dn, $oldPassword);
  }

  my $error;
  try {
    my $msg = $this->ldap->set_password(
      oldpasswd => $oldPassword,
      newpasswd => $newPassword
    );

    _checkError($msg);
  } catch Error with {
    $error = shift;
    $this->writeDebug("error: $error");
  };

  throw Error::Simple($error) if defined $error;

  $this->writeDebug("...success");

  return 1;
}

sub ldap {
  my $this = shift;

  if (defined $this->{_ldap}) {
    my $now = time();
    if (!$this->{_createTime} || $this->{_createTime} + $this->prop("Timeout") < $now) {
      $this->writeDebug("... need to reconnect to ldap");
      $this->disconnect();
    }
  }

  $this->connect unless defined $this->{_ldap};

  return $this->{_ldap};
}

=begin TML

---++ connect($dn, $passwd, $host, $port) -> $boolean

Connect to LDAP server. If a $dn parameter and a $passwd is given then a bind is done.
Otherwise the communication is anonymous. You don't have to connect() explicitely
by calling this method. The methods below will do that automatically when needed.

=cut

sub connect {
  my ($this, $dn, $passwd, $host, $port) = @_;

  $this->writeDebug("called connect");
  $this->writeDebug("dn=$dn") if $dn;
  $this->writeDebug("passwd=***", 2) if $passwd;

  $host ||= $this->prop("Host");
  $port ||= $this->prop("Port");

  if ( $host =~ /,/) {
    # This server preference list relies on the behaviour of Net::LDAP
    # ldap://, ldaps:// URIs or host:port pairs are valid
    $host = [split (/\s*,\s*/, $host)];
  } 

  $this->writeDebug("... host=$host");

  if (defined $this->{_ldap}) {
    $this->writeDebug("... disconnecting first");
    $this->disconnect;
  }

  $this->{_ldap} = Net::LDAP->new(
    $host,
    port => $port,
    version => $this->prop("Version"),
    inet4 => $this->prop("IPv6") ? 0 : 1,
    inet6 => $this->prop("IPv6") ? 1 : 0,
    timeout => $this->prop("Timeout"),
  );
  
  throw Error::Simple("failed to connect to $host") unless $this->{_ldap};

  # TLS bind
  if ($this->prop("UseTLS")) {
    $this->writeDebug("... using TLS");
    my %args = (
      verify => $this->prop("TlsVerify")
    );

    my $caFile = $Foswiki::cfg{PluggableAuth}{CAFile};
    my $caPath = $Foswiki::cfg{PluggableAuth}{CAPath};
    $args{"cafile"} = $caFile if $caFile;
    $args{"capath"} = $caPath if $caPath && !$caFile;

    $args{"clientcert"} = $this->prop("TlsClientCert") if $this->prop("TlsClientCert");
    $args{"clientkey"} = $this->prop("TlsClientKey") if $this->prop("TlsClientKey");
    $args{"sslversion"} = $this->prop("TlsSSLVersion") if $this->prop("TlsSSLVersion");
    my $msg = $this->{_ldap}->start_tls(%args);
    _writeError($msg->{errorMessage}) if $msg->{errorMessage};
  }

  $passwd = $this->encode($passwd) if $passwd;

  # authenticated bind
  my $msg;
  if (defined($dn)) {
    throw Error::Simple("illegal call to connect()") unless defined($passwd);

    $dn = $this->encode($dn);
    $msg = $this->{_ldap}->bind($dn, password => $passwd);
    $this->writeDebug("... bind for $dn");
  }

  # sasl bind
  elsif ($this->prop("UseSASL")) {
    require Authen::SASL;
    my $mechanism = $this->prop("SASLMechanism");

    if ($mechanism =~ /\bGSSAPI\b/) {
      my $keytab = $this->prop("KeyTab");
      my $princ = $this->prop("PrincipalName");
      
      _writeError("keytab not definedd") unless $keytab;
      _writeError("principal name not definedd") unless $princ;

      system("kinit -k -t $keytab $princ") if $keytab && $princ;
    }

    my $sasl = Authen::SASL->new(
      mechanism => $mechanism,
    );
    
    #$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{KeyTab} = '/etc/nginx/http.keytab';

    if ($this->prop("BindDN") && $this->prop("BindPassword")) {
      $sasl->callback(
        user => $this->prop("BindDN"),
        pass => $this->prop("BindPassword"),
      );
      $this->writeDebug("... sasl bind to ".$this->prop("BindDN"));
      $msg = $this->{_ldap}->bind($this->prop("BindDN"), sasl => $sasl, version => $this->prop("Version"));

    } else {
      $this->writeDebug("... sasl bind without user or pass");
      $msg = $this->{_ldap}->bind(sasl => $sasl, version => $this->prop("Version"));
    }

  } 

  # simple bind
  elsif ($this->prop("BindDN") && $this->prop("BindPassword")) {
    $this->writeDebug("... proxy bind");
    $msg = $this->{_ldap}->bind($this->prop("BindDN"), password => $this->prop("BindPassword"));
  }

  # anonymous bind
  else {
    $this->writeDebug("... anonymous bind");
    $msg = $this->{_ldap}->bind;
  }

  _checkError($msg);

  # SMELL: not sure how to access the timer in IO::Socket::*, so we keep our own
  $this->{_createTime} = time();

  return 1;
}

=begin TML

---++ disconnect()

Unbind the LDAP object from the server. This method can be used to force
a reconnect and possibly rebind as a different user.

=cut

sub disconnect {
  my $this = shift;

  return unless $this->{_ldap};

  $this->writeDebug("called disconnect()");

  $this->{_ldap}->unbind;
  undef $this->{_ldap};
  undef $this->{_createTime};
}

sub refresh {
  my ($this, $debug) = @_;

  $this->{_debug} = $debug;
  $this->writeDebug("called refresh");

  my $userInfos = $this->cacheUsers();
  $this->cacheGroups($userInfos);

  # refresh topic groups ... disabled
  #$this->auth->getProvider("Topic")->cacheGroups();

  return $this->SUPER::refresh();
}

sub cacheUsers {
  my $this = shift;

  # delete all users of this provider if they have been previously imported and how the ImportUsers was switched off
  unless ($this->prop("ImportUsers")) {
    my $userIt = $this->eachUser();
    while ($userIt->hasNext) {
      my $user = $userIt->next;
      if ($this->prop("KeepOldUsers")) {
        $this->writeDebug("... old user found ... disabling " . $user->stringify);
        $user->disable;
      } else {
        $this->writeDebug("... old user found ... deleting " . $user->stringify);
        $user->delete;
      }
    }
    return;
  }

  return unless $this->prop("PrefetchUsers");

  my %userInfos = ();

  # collect all users from ldap
  foreach my $userBase (@{$this->prop("UserBase")}) {
    $this->findUsers($userBase, \%userInfos);
  }

  $this->writeDebug("found ".scalar(keys %userInfos)." users in ldap");

  # delete database users unless they still exist in ldap
  $this->writeDebug("checking existing users against ldap");
  my $userIt = $this->eachUser();
  while ($userIt->hasNext) {
    my $user = $userIt->next;
    my $userInfo = $userInfos{$user->prop("loginName")};
    if (defined $userInfo) {
      $this->writeDebug("... user ".$user->stringify." still exists");
      $userInfo->{enabled} = 1;
      $this->updateUser($user, $userInfo);
    } else {
      if ($this->prop("KeepOldUsers")) {
        $this->writeDebug("... disabling old user: ".$user->stringify);
        $user->disable;
      } else {
        $this->writeDebug("... deleting old user: ".$user->stringify);
        $user->delete;
      }
    }
  }

  # add ldap users if required
  $this->writeDebug("checking ldap users against existing users");
  foreach my $userInfo (values %userInfos) {
    my $user = $this->findUser(loginName => $userInfo->{loginName});
    $user //= $this->auth->getUserByID($userInfo->{id}, $this->prop("id"));

    if (defined $user && $user->prop("loginName")) {
      $user->load();
      if ($user->prop("pid") eq $this->prop("id")) {
        $this->writeDebug("... user already exists (1): ".$user->stringify);
        $this->updateUser($user, {enabled => 1});
        next;
      } 

      my $suffix = lc($this->prop("id"));
      $userInfo->{id} .= "_". $suffix unless $userInfo->{id} =~ /$suffix$/;

      $user = $this->auth->getUserByID($userInfo->{id}, $this->prop("id"))->load;
      if (defined $user && $user->prop("loginName")) {
        $this->writeDebug("... user already exists (2): ".$user->stringify);
        $this->updateUser($user, {enabled => 1});
        next;
      }
    } 

    $this->writeDebug("... adding new user: ".$userInfo->{id});
    $user = $this->addUser(%$userInfo);
  }

  return \%userInfos;
}

sub cacheGroups {
  my ($this, $userInfos) = @_;

  $userInfos //= {};

  my %groupInfos = ();

  # collect all groups from ldap
  if ($this->prop("ImportGroups")) {
    foreach my $groupBase (@{$this->prop("GroupBase")}) {
      $this->findGroups($groupBase, \%groupInfos);
    }
  }

  # collect all virtual groups
  if ($this->prop("VirtualGroups")) {
    foreach my $config (@{$this->prop("VirtualGroups")}) {
      $this->findVirtualGroups($config, \%groupInfos);
    }
  }

  # collect all virtual members
  if ($this->prop("VirtualMembers")) {
    foreach my $config (@{$this->prop("VirtualMembers")}) {
      $this->findVirtualMembers($config, \%groupInfos);
    }
  }

  # delete database groups unless they still exist in ldap
  $this->writeDebug("checking existing groups against ldap");
  my $groupIt = $this->auth->eachGroup(pid => $this->prop("id"));
  while ($groupIt->hasNext) {
    my $group = $groupIt->next;
    my $groupInfo = $groupInfos{$group->prop("id")};
    if ($groupInfo) {
      $this->writeDebug("... group $groupInfo->{wikiName} still exists: " . $group->stringify);
    } else {
      $this->writeDebug("... old group found ... deleting " . $group->stringify);
      $group->delete;
    }
  }

  # adding ldap groups if required
  $this->writeDebug("checking ldap groups against existing groups");
  foreach my $groupInfo (values %groupInfos) {
    if ($this->prop("IgnorePrivateGroups")) {
      if ( $this->auth->userExists(loginName => $groupInfo->{wikiName})
        || $this->auth->userExists(wikiName => $groupInfo->{wikiName}))
      {
        $this->writeDebug("... ignoring private group $groupInfo->{wikiName}");
        next;
      }
    }

    my $group = $this->auth->getGroupByID($groupInfo->{id})->load;
    if (defined $group) {
      $this->writeDebug("... group $groupInfo->{wikiName} already exists: " . $group->stringify);
    } else {
      $this->writeDebug("... adding group $groupInfo->{wikiName}");
      $group = $this->addGroup(%$groupInfo);
    }
  }
  
  # cache primary group members
  my %primaryMembers = ();
  foreach my $userInfo (values %$userInfos) {
    my $gid = $userInfo->{_primaryGroup};
    next unless $gid;
    $primaryMembers{$gid}{$userInfo->{id}} = 1;
  }

  # cache group_members
  my %seen = ();
  foreach my $groupInfo (values %groupInfos) {
    next if $seen{$groupInfo->{id}};
    $seen{$groupInfo->{id}} = 1;

    my %members = ();
    $this->writeDebug("caching members of group $groupInfo->{wikiName}");
    foreach my $item (@{$groupInfo->{_members}}) {
      if ($this->prop("MemberIndirection")) {
        my $info = $userInfos->{$item};
        if (defined $info) {
          $members{$info->{loginName}} = 1;
        } else {
          $info = $groupInfos{$item};
          if (defined $info) {
            $members{$info->{id}} = 1;
            #print STDERR "groupInfo{$item} wikiName=$info->{wikiName}\n";
          }
        }

        #_writeError("... woops, $item not found even though member of $groupInfo->{wikiName}") unless defined $info;
      } else {
        $members{$item} = 1;
      }
    }

    # add primary group members
    if (defined $groupInfo->{_primaryGroupId} && exists $primaryMembers{$groupInfo->{_primaryGroupId}}) {
      foreach my $uid (keys %{$primaryMembers{$groupInfo->{_primaryGroupId}}}) {
        $members{$uid} = 1;
      }
    }

    my $group = $this->auth->getGroupByID($groupInfo->{id}, $this->prop("id"));
    unless (defined $group) {
      _writeError("... woops, group $groupInfo->{id} not found");
      next;
    }

    # first delete all members
    $this->_deleteMembers($group);

    if (keys %members) {
      # add members to the group
      foreach my $name (keys %members) {
        #print STDERR "member name=$name\n";
        my $obj = $this->findUser(loginName => $name);
        if (defined $obj) {
          #$this->writeDebug("... adding user $name to group $groupInfo->{wikiName}");
          $this->addMemberToGroup($obj, $group);
          next;
        }
        $obj = $this->auth->findGroup(wikiName => $name, pid => $this->prop("id"));
        if (defined $obj) {
          if ($obj->prop("id") eq $group->prop("id")) {
            _writeError("... woops, group $name is a member of itself");
            next;
          }
          $this->writeDebug("... adding group $name to group $groupInfo->{wikiName}");
          $this->addMemberToGroup($obj, $group);
          next;
        }
        $this->writeDebug("... object $name not found for this provider, not adding it to $groupInfo->{wikiName}");
      }
    } else {
      $this->writeDebug("... found empty group $groupInfo->{wikiName}");
    }
  }

  return \%groupInfos;
}

sub findUsers {
  my ($this, $userBase, $userInfos) = @_;

  $this->writeDebug("called findUsers($userBase)");
  $userInfos //= {};

  # prepare search
  my %args = (
    filter => $this->prop("UserFilter"),
    base => $userBase,
    scope => $this->prop("UserScope"),
    deref => "always",
    attrs => [
      $this->prop("LoginNameAttribute") // "", 
      $this->prop("MailAttribute") // "", 
      $this->prop("FirstNameAttribute") // "", 
      $this->prop("MiddleNameAttribute") // "", 
      $this->prop("LastNameAttribute") // "", 
      $this->prop("DisplayNameAttribute") // "", 
      $this->prop("InitialsAttribute") // "", 
      $this->prop("PrimaryGroupAttribute") // "", 
      $this->prop("PictureAttribute") // "", 
      split(/\s*,\s/, $this->prop("WikiNameAttributes"))
    ],
  );

  # extablish callback
  $args{callback} = sub {
    my ($ldap, $entry) = @_;
    my $userInfo = $this->extractUserInfo($entry, 1);

    if (defined $userInfo) {
      $userInfos->{$userInfo->{loginName}} = $userInfos->{$userInfo->{_dn}} = $userInfo;
    }
  };

  $this->searchAll(%args);

  return $userInfos;
}

=begin TML

---++ extractUserInfo($entry, $force) -> \%userInfo

extrac userInfo from an LDAP::Entry to database. on error 
this method returns undef, and otherwise a hash with properties:

   * loginName
   * wikiName
   * email
   * firstName
   * middleName
   * lastName
   * displayName
   * initials
   * picture

=cut

sub extractUserInfo {
  my ($this, $entry, $force) = @_;

  #$this->writeDebug("called extractUserInfo()");

  my %userInfo = ();

  my $dn = $this->getDN($entry);
  $userInfo{_dn} = $dn;
  #$this->writeDebug("... dn=$dn");

  # get loginName
  my $loginName = $this->getValue($entry, $this->prop("LoginNameAttribute"));
  unless ($loginName) {
    $this->writeDebug("... no loginName for $dn ... skipping");
    return;
  }
  $loginName =~ s/^\s+//g;
  $loginName =~ s/\s+$//g;
  $loginName = lc($loginName) unless $this->prop("CaseSensitiveLogin");

  unless ($this->auth->isValidLoginName($loginName)) {
    $this->writeDebug("... not a valid loginName $loginName");
    return;
  }

  $userInfo{loginName} = $loginName;
  $userInfo{id} = $userInfo{loginName};
  $userInfo{pid} = $this->prop("id");

  # get wikiName
  my $prevUser = $force ? undef: $this->findUser(loginName => $loginName);

  # keep a wikiName once it has been computed
  if ($prevUser) {
    $this->writeDebug("found previous user ".$prevUser->stringify." for $loginName");
    $userInfo{wikiName} = $prevUser->prop("wikiName");
  } else {

    # compute a new wikiName
    my @parts = ();
    foreach my $attr (split(/\s*,\s*/, $this->prop("WikiNameAttributes"))) {
      my $value = $this->getValue($entry, $attr);
      next unless $value;
      $value =~ s/^\s+//g;
      $value =~ s/\s+$//g;
      #$this->writeDebug("... $attr=$value");
      push @parts, $value;
    }
    $userInfo{wikiName} = join(" ", @parts) if scalar(@parts);
    unless ($userInfo{wikiName}) {
      _writeError("... no WikiNameAttributes found for $dn ... ignoring");
      return;
    }
  }

  # get email addrs
  $userInfo{email} = $this->getValue($entry, $this->prop("MailAttribute"));

  $userInfo{firstName} = $this->getValue($entry, $this->prop("FirstNameAttribute"));
  $userInfo{middleName} = $this->getValue($entry, $this->prop("MiddleNameAttribute"));
  $userInfo{lastName} = $this->getValue($entry, $this->prop("LastNameAttribute"));
  $userInfo{displayName} = $this->getValue($entry, $this->prop("DisplayNameAttribute"));
  $userInfo{initials} = $this->getValue($entry, $this->prop("InitialsAttribute"));
  $userInfo{picture} = $this->cacheBlob($entry, $this->prop("PictureAttribute"), 1) // '';
  $userInfo{_primaryGroup} = $this->getValue($entry, $this->prop("PrimaryGroupAttribute"));

  unless ($userInfo{firstName}) {
    ($userInfo{firstName}) = $userInfo{wikiName} =~ /^([^\s]+)/;
  }
  unless ($userInfo{lastName}) {
    ($userInfo{lastName}) = $userInfo{wikiName} =~ /([^\s]+)$/;
  }

  unless ($userInfo{initials}) {
    $userInfo{initials} = Foswiki::PluggableAuth::extractInitials($userInfo{displayName});
  }
  unless ($userInfo{initials}) {
    $userInfo{initials} = Foswiki::PluggableAuth::extractInitials(($userInfo{firstName}||'') . " ". ($userInfo{middleName} ||'') . " " . ($userInfo{lastName}||''));
  }
  unless ($userInfo{initials}) {
    $userInfo{initials} = Foswiki::PluggableAuth::extractInitials(Foswiki::Func::spaceOutWikiWord($userInfo{wikiName}));
  }

  #$this->writeDebug("... userInfo=".dump(\%userInfo));
  #$this->writeDebug("... loginName=$userInfo{loginName}, firstName=$userInfo{firstName}, lastName=$userInfo{lastName}, displayName=$userInfo{displayName}, wikiName=".Foswiki::PluggableAuth::wikify($userInfo{wikiName}));

  return \%userInfo;
}

sub updatePictureOfUser {
  my ($this, $user) = @_;

  #$this->writeDebug("called updatePictureOfUser()");

  # find other image with a t attribute
  my $meta = $user->readTopic();
  my $thumbnailExists = 0;
  if ($meta) {
    foreach my $att ($meta->find("FILEATTACHMENT")) {
      if ($att->{attr} && $att->{attr} =~ /t/) {
        $thumbnailExists = 1;
        last;
      }
    }
  }

  if (!$thumbnailExists && $this->prop("PictureAttribute")) {
    my $entry = $this->getEntryOfUser($user);
    if ($entry) {
      my $url = $this->cacheBlob($entry, $this->prop("PictureAttribute"), 1);
      return $url if $url;
    }
  }
 
  return $this->SUPER::updatePictureOfUser($user); 
}

sub findVirtualMembers {
  my ($this, $config, $groupInfos) = @_;

  return unless defined $config;

  $this->writeDebug("called findVirtualMembers()");
  my $virtualGroup = $groupInfos->{$config->{group}} // {
    wikiName => $config->{group},
    id => $config->{group},
    pid => $this->prop("id"),
    _members => [],
  };

  # get virtual members
  # prepare search
  my %args = (
    filter => $config->{filter},
    base => $config->{base},
    scope => $config->{scope} // "sub",
    deref => "always",
    attrs => [
      $config->{nameAttr}
    ],
  );

  # extablish callback
  $args{callback} = sub {
    my ($ldap, $entry) = @_;

    my $authName = $this->getValue($entry, $config->{nameAttr});
    $authName = lc($authName) unless $this->prop("CaseSensitiveLogin");

    my $memberInfo = {
      id => $authName,
      pid => $this->prop("id"),
      _dn => $this->getDN($entry),
    };

    $this->writeDebug("... found virtual member $memberInfo->{id}");

    push @{$virtualGroup->{_members}}, $memberInfo->{id};
  };

  $this->searchAll(%args);

  $groupInfos->{$virtualGroup->{id}} = $virtualGroup;

  return $groupInfos;
}

sub findVirtualGroups {
  my ($this, $config, $groupInfos) = @_;

  return unless defined $config;

  $this->writeDebug("called findVirtualGroups()");

  unless ($config->{nameAttr} && $config->{filter} && $config->{base}) {
    _writeErrorr("invalid virtual group definition");
    return;
  }

  # get virtual groups
  my %virtualGroupInfos = ();

  # prepare search
  my %args = (
    filter => $config->{filter},
    base => $config->{base},
    scope => $config->{scope} // "sub",
    deref => "always",
    attrs => [
      $config->{nameAttr}
    ],
  );

  # extablish callback
  $args{callback} = sub {
    my ($ldap, $entry) = @_;

    my $groupName = $this->getValue($entry, $config->{nameAttr});
    $groupName = $this->auth->rewriteName($groupName, $config->{rewriteGroupNames});
    $groupName =~ s/^\s+//g;
    $groupName =~ s/\s+$//g;
    $groupName = $this->auth->normalizeGroupName($groupName);

    my $groupInfo = {
      wikiName => $groupName,
      id => $groupName,
      pid => $this->prop("id"),
      _dn => $this->getDN($entry),
      _members => []
    };

    $this->writeDebug("... found virtual group $groupInfo->{wikiName}");

    $virtualGroupInfos{$groupInfo->{id}} = $groupInfo;
  };

  $this->searchAll(%args);

  # get members of virtual groups
  foreach my $virtualGroup (values %virtualGroupInfos) {
    my %virtualMembers = ();
    $this->findUsers($virtualGroup->{_dn}, \%virtualMembers);

    foreach my $userInfo (values %virtualMembers) {
      #$this->writeDebug("... adding $userInfo->{loginName} to virtual group $virtualGroup->{wikiName}");

      push @{$virtualGroup->{_members}}, $userInfo->{loginName};
    }
    $groupInfos->{$virtualGroup->{id}} = $groupInfos->{$virtualGroup->{_dn}} = $virtualGroup;
  }

  return $groupInfos;
}

sub findGroups {
  my ($this, $groupBase, $groupInfos) = @_;

  $this->writeDebug("called findGroups($groupBase)");
  $groupInfos //= {};

  # prepare search
  my %args = (
    filter => $this->prop("GroupFilter"),
    base => $groupBase,
    scope => $this->prop("GroupScope"),
    deref => "always",
    attrs => [
      $this->prop("GroupAttribute"), 
      $this->prop("PrimaryGroupAttribute"),
      $this->prop("InnerGroupAttribute"), 
      $this->prop("MemberAttribute"), 
    ],
  );

  # extablish callback
  $args{callback} = sub {
    my ($ldap, $entry) = @_;
    my $groupInfo = $this->extractGroupInfo($entry);
    if (defined $groupInfo) {
      $groupInfo->{id} //= $groupInfo->{wikiName};
      $groupInfo->{pid} //= $this->prop("id");
      $groupInfos->{$groupInfo->{id}} = $groupInfos->{$groupInfo->{_dn}} = $groupInfo;
    }
  };

  $this->searchAll(%args);

  return $groupInfos;
}

sub extractGroupInfo {
  my ($this, $entry) = @_;

  #$this->writeDebug("called extractGroupInfo()");

  my %groupInfo = ();

  my $dn = $this->getDN($entry);
  $groupInfo{_dn} = $dn;
  #$this->writeDebug("... dn=$dn");

  my $groupName = $this->getValue($entry, $this->prop("GroupAttribute"));
  unless ($groupName) {
    $this->writeDebug("... no groupName for $dn ... skipping");
    return;
  }

  $groupName =~ s/^\s+//g;
  $groupName =~ s/\s+$//g;
  $groupName = $this->auth->normalizeGroupName($groupName);
  unless ($this->auth->isValidGroupName($groupName)) {
    $this->writeDebug("... not a valid groupName $groupName ... skipping");
    return;
  }

  $groupInfo{wikiName} = $groupName;
  $groupInfo{id} = $groupName;
  $groupInfo{_primaryGroupId} = $this->getValue($entry, $this->prop("PrimaryGroupAttribute")) // $groupName;

  # fetch members of this group

  # SMELL: Microsoft Active Directory has got a non-standard range syntax for ranges of entries.
  # instead of storing members in the requested "members" attribute they are returned in a "members;range=0-12345" 
  # property. This is the case even tough we didn't ask for ranges. So below code needs to iterate over all
  # returned attributes that resemble a "members;range=.*"

  my %members = ();
  my $memberAttribute = $this->prop("MemberAttribute");
  foreach my $key ($entry->attributes) {
    next unless $key =~ /^$memberAttribute(;range=.*)?$/;
    $this->writeDebug(".... found members in attribute $key");
    $members{$_} = 1 foreach $this->getValues($entry, $key);  
  }

  # fetch all inner groups of this group
  if ($this->prop("MemberAttribute") ne $this->prop("InnerGroupAttribute")) {
    foreach my $innerGroup ($this->getValue($entry, $this->prop("InnerGroupAttribute"))) {
      next unless $innerGroup;
      $innerGroup =~ s/^\s+//g;
      $innerGroup =~ s/\s+$//g;
      $members{$innerGroup} = 1;
    }
  }

  $groupInfo{_members} = [keys %members];

  return \%groupInfo;
}

=begin TML

---++ search($filter, %args) -> $msg

Returns an Net::LDAP::Search object for the given query on success and undef
otherwise. If $args{base} is not defined $ldap->{base} is used.  If $args{scope} is not
defined 'sub' is used (searching down the subtree under $args{base}. If no $args{sizelimit} is
set all matching records are returned.  The $attrs is a reference to an array
of all those attributes that matching entries should contain.  If no $args{attrs} is
defined all attributes are returned.

Typical usage:
<verbatim>
$ldap->search(
  filter=>'uid=TestUser',
  callback => sub {
    my ($ldap, $entry) = @_;
    return unless defined $entry;
    # process entry
  }
);
</verbatim>

=cut

sub search {
  my ($this, %args) = @_;

  $this->writeDebug("called search");

  $args{base} = $this->prop("BaseDN") unless $args{base};
  $args{base} = $this->encode($args{base});
  $args{scope} = 'sub' unless $args{scope};
  $args{sizelimit} = 0 unless $args{sizelimit};
  $args{attrs} = ['*'] unless $args{attrs};
  $args{filter} = $this->encode($args{filter}) if $args{filter};

  if (defined($args{callback}) && !defined($args{_origCallback})) {

    $args{_origCallback} = $args{callback};

    $args{callback} = sub {
      my ($ldap, $entry) = @_;

      # bail out when done
      return unless defined $entry;

      # follow references
      if ($entry->isa("Net::LDAP::Reference")) {
        unless ($this->prop("IgnoreReferrals")) {
          foreach my $link ($entry->references) {
            $this->writeDebug("following reference $link");
            $this->_followLink($link, %args);
          }
         }
      } else {
        # call the orig callback
        $args{_origCallback}($ldap, $entry);
      }
    };
  }

  #$this->writeDebug("called search args=".dump(\%args));

  my $msg = $this->ldap->search(%args);
  my ($errorCode, $errorMessage) = _checkError($msg);

  # we set a sizelimit so it is ok that it exceeds
  if ($args{sizelimit} && $errorCode == LDAP_SIZELIMIT_EXCEEDED) {
    $this->writeDebug("sizelimit exceeded");
    return $msg;
  }

  if ($errorCode == LDAP_REFERRAL) {
    unless ($this->prop("IgnoreReferrals")) {
      my @referrals = $msg->referrals;
      foreach my $link (@referrals) {
        $this->writeDebug("following referral $link");
        $this->_followLink($link, %args);
      }
    }
  } elsif ($errorCode != LDAP_SUCCESS) {
    $this->writeDebug("error in search: $errorMessage");
  }

  return $msg;
}

sub searchAll {
  my ($this, %args) = @_;

  $this->writeDebug("called searchAll");

  # use the control LDAP extension only if a valid pageSize value has been provided
  my $page;
  my $pageSize = $this->prop("PageSize") // 0;
  if ($pageSize) {
    require Net::LDAP::Control::Paged;
    $page = Net::LDAP::Control::Paged->new(size => $pageSize);
    $args{control} = [$page];
    $this->writeDebug("... searching ldap with page size=$pageSize");
  } else {
    $this->writeDebug("... searching ldap in one chunk");
  }

  # perform search, either in paging loop or in as one chunk
  if ($page) {
    my $cookie;

    while (1) {
      my $msg = $this->search(%args);
      _checkError($msg); # throws an exception in case of an error

      # get cookie from paged control to remember the offset
      my ($resp) = $msg->control(LDAP_CONTROL_PAGED) or last;

      $cookie = $resp->cookie or last;
      if ($cookie) {
        # set cookie in paged control
        $page->cookie($cookie);
      } else {
        # found all
        $this->writeDebug("... ok, no more cookie");
        last;
      }
    }

    # clean up
    if ($cookie) {
      $page->cookie($cookie);
      $page->size(0);
      $this->search(%args);
    }
    $this->writeDebug("... done reading pages");

  } else {

    my $msg = $this->search(%args);
    _checkError($msg); # throws an exception in case of an error
  }

  return 1;
}

sub _followLink {
  my ($this, $link, %args) = @_;

  $this->writeDebug("following ldap url $link");

  # prevent recursion
  $this->{_followingLink} //= {};
  return if $this->{_followingLink}{$link};
  $this->{_followingLink}{$link} = 1;

  my $uri = URI::ldap->new($link);

  # remember old connection
  my $oldLdap = $this->{_ldap};
  $this->{_ldap} = undef;

  my %thisArgs = %args;
  $thisArgs{base} = $uri->dn;
  $thisArgs{port} = $uri->port;

  # trick in new connection
  $this->connect(undef, undef, $uri->host, $uri->port);
  $this->search(%thisArgs);
  $this->disconnect();

  # restore old connection
  $this->{_ldap} = $oldLdap;
  delete $this->{_followingLink}{$link};

  $this->writeDebug("done following ldap url $link");
}

=begin TML

---++ cacheBlob($entry, $attribute, $refresh) -> $pubUrlPath

Takes an Net::LDAP::Entry and an $attribute name, and stores its value into a
file. Returns the pubUrlPath to it. This can be used to store binary large
objects like images (jpegPhotos) into the filesystem accessible to the httpd
which can serve it in return to the client browser. 

Filenames containing the blobs are named using a hash value that is generated
using its DN and the actual attribute name whose value is extracted from the 
database. If the blob already exists in the cache it is _not_ extracted once
again except the $refresh parameter is defined.

=cut

sub cacheBlob {
  my ($this, $entry, $attr, $refresh) = @_;

  #$this->writeDebug("called cacheBlob()");
  return unless defined $attr;
  return unless $IMAGEMAGICK_ENABLED;

  my $dir = $Foswiki::cfg{PubDir} . '/' . $Foswiki::cfg{SystemWebName} . '/PluggableAuthContrib';
  mkdir($dir, 0775) unless -e $dir;
  $dir .= '/blobs';
  mkdir($dir, 0775) unless -e $dir;

  my $dn = $this->getDN($entry);
  $dn = Foswiki::PluggableAuth::transliterate($dn);

  my $key = Digest::MD5::md5_hex($dn . $attr);
  my $fileName = "$key.jpeg";
  my $filePath = $dir . '/' . $fileName;

  if ($refresh || !-f $filePath) {
    #$this->writeDebug("caching blob for $attr to $filePath");

    my $value = $entry->get_value($attr); # not using getValue() as this is a blob
    return unless $value;

    my $image = Image::Magick->new();
    $image->BlobToImage($value);

    $image->Write($filePath);

  } else {
    $this->writeDebug("already got blob");
  }

  #$this->writeDebug("done cacheBlob()");
  return $Foswiki::cfg{PubUrlPath} . '/' . $Foswiki::cfg{SystemWebName} . '/PluggableAuthContrib/blobs/' . $fileName;
}

sub indexUser {
  my ($this, $user, $indexer, $doc, $meta, $text) = @_;

  $this->SUPER::indexUser($user, $indexer, $doc, $user, $meta, $text);

  $this->writeDebug("indexing user ".$user->stringify);

  my $personAttributes = $this->prop("PersonAttributes");
  return unless $personAttributes && keys %$personAttributes;

  my $entry = $this->getEntryOfUser($user);
  unless ($entry) {
    $this->writeDebug("... disabling user in solr");
    $this->indexSolrField($doc, 'state', 'disabled');
    return;
  }

  foreach my $attr ($entry->attributes()) {
    my $label = $personAttributes->{$attr};
    next unless defined $label;

    my $value;
    my @values;

    if ($label eq 'thumbnail') {
      $value = $this->cacheBlob($entry, $attr);
      next unless defined $value && $value ne '';

      $doc->add_fields($label => $value);
    } else {

      my $field = $meta->get('FIELD', $label);
      if ($field) {
        $value = $field->{value};
        @values = split(/\s*,\s*/, $value) if $value;
      }

      unless ($value) {
        @values = $this->getValues($entry, $attr);
        next unless @values;
        $value = join(", ", @values); 
      }

      $value =~ s/^\s+|\s+$//g;

      $this->indexSolrField($doc, 'field_' . $label . '_s', $value);
      $this->indexSolrField($doc, 'field_' . $label . '_lst', \@values);
      $this->indexSolrField($doc, 'field_' . $label . '_search', $value);
  
    }

    $this->writeDebug("... adding $label=$value");
  }
}

sub encoding {
  my $this = shift;

  unless ($this->{_encoding}) {
    my $charset = $this->prop("charSet") // 'UTF-8';
    $this->writeDebug("charset=$charset");

    $this->{_encoding} = Encode::find_encoding($charset);
  }

  return $this->{_encoding};
}

sub encode {
  my ($this, $string) = @_;

  return $this->encoding->encode($string);
}

sub decode {
  my ($this, $string) = @_;

  return $this->encoding->decode($string);
}

sub getDN {
  my ($this, $entry) = @_;

  my $dn = $entry->dn;
  $dn = $this->decode($dn);

  # do some cleanup
  $dn =~ s/–/-/g;

  return $dn;
}

sub getValue {
  my ($this, $entry, $key) = @_;

  return unless $key;
  my $val = $entry->get_value($key);
  return unless defined $val;

  return $this->decode($val);
}

sub getValues {
  my ($this, $entry, $key) = @_;

  my $ref = $entry->get_value($key, asref => 1);

  my @vals = ();
  if (defined $ref) {
    foreach my $val (@$ref) {
      $val =~ s/^\s+//g;
      $val =~ s/\s+$//g;
      $val = $this->decode($val);
      push @vals, $val;
    }
  }
 
  return @vals; 
}

### static helper
sub _checkError {
  my $msg = shift;

  my $code = $msg->code();

  throw Error::Simple($msg->error_name() . "($code): " . $msg->error())
    unless $code == LDAP_SUCCESS || 
           $code == LDAP_REFERRAL || 
           $code == LDAP_SIZELIMIT_EXCEEDED || 
           $code == LDAP_NO_SUCH_OBJECT; 

  return wantarray ? ($code, $msg->error) : $code;
}

sub _writeError {
  print STDERR "PluggableAuth::Provider::Ldap - ERROR: $_[0]\n";
}


1;
