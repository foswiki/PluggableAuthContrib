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

package Foswiki::Users::PluggableUserMapping;

=begin TML

---+ package Foswiki::Users::PluggableUserMapping

This is the user mapping connecting to the Foswiki::PluggableAuth service

=cut

use strict;
use warnings;

use Foswiki::ListIterator ();
use Foswiki::Sandbox ();
use Foswiki::UserMapping ();
use Foswiki::PluggableAuth ();
use Error qw(:try);

our @ISA = ('Foswiki::UserMapping');

use constant TRACE => 0;

=begin TML 

---++ ClassMethod new($session) -> $pluggableUserMapping

create a new Foswiki::Users::PluggableUserMapping object and constructs connects to the auth database

=cut

sub new {
  my ($class, $session) = @_;

  my $this = bless($class->SUPER::new($session), $class);

  $this->{_login2cUID} = {};
  $this->{_isGroup} = {};
  $this->{_isInGroup} = {};
  $this->{_isUnknown} = {};

  return $this;
}

=begin TML

---++ ObjectMethod auth()

returns the Foswiki::PluggableAuth singleton object

=cut

sub auth {
  my $this = shift;

  unless ($this->{_auth}) {
    $this->{_auth} = Foswiki::PluggableAuth->new();
  }

  return $this->{_auth};
}

=begin TML

---++ ObjectMethod finish()

Complete processing after the client's HTTP request has been responded

=cut

sub finish {
  my $this = shift;

  $this->{_auth}->finish if defined $this->{_auth};
  undef $this->{_auth};
  undef $this->{_login2cUID};
  undef $this->{_isGroup};
  undef $this->{_isInGroup};
  undef $this->{_isUnknown};
  undef $this->{_handlesUser};

  $this->SUPER::finish();
}

=begin TML

---++ ObjectMethod supportsRegistration() -> $boolean

Return true if there is a provider that supports user registration (can create new users)

Default is *false*

=cut

sub supportsRegistration {
  my $this = shift;

  my $provider = $this->auth->getRegistrationProvider();
  return 0 unless defined $provider;
  return $provider->canRegisterUser;
}

=begin TML

---++ ObjectMethod addUser($loginName, $wikiname, $password, $emails) -> $cUID

adds a user to the given

=cut

sub addUser {
  my ($this, $loginName, $wikiName, $password, $emails) = @_;

  #print STDERR "called addUser(loginName=$loginName, wikiName=$wikiName, password=$password, emails=$emails)\n";

  my $provider = $this->auth->getRegistrationProvider();
  return unless defined $provider;

  my $user = $provider->registerUser(
    loginName => $loginName,
    wikiName => $wikiName,
    email => defined($emails) ? (ref($emails) ? @$emails[0] : $emails) : undef,
    password => $password,
  );

  unless (defined $user) {
    _writeDebug("woops no user after registration");
    throw Error::Simple("Invalid user registration");
    return;
  }

  return $user->prop("id");
}

=begin TML

---++ ObjectMethod handlesUser($cUID, $loginName, $wikiname) -> $boolean

Called by the Foswiki::Users object to determine which loaded mapping
to use for a given user (must be fast).

The user can be identified by any of $cUID, $loginName or $wikiname. Any of
these parameters may be undef, and they should be tested in order; cUID
first, then login, then wikiname.

=cut

sub handlesUser {
  my ($this, $cUID, $loginName, $wikiName) = @_;

  return 0 if $loginName && $loginName =~ /^baseusermapping/i;
  return 0 if $cUID && $cUID =~ /^baseusermapping/i;
  return 0 if $wikiName && $wikiName =~ /^baseusermapping/i;
  return 0 unless $loginName || $cUID || $wikiName; 

  my $key = ($cUID // 'undef').'::'.($loginName//'undef').'::'.($wikiName//'undef');

  _writeDebug("called handlesUser($key)") if TRACE;

  return $this->{_handlesUser}{$key} if defined $this->{_handlesUser}{$key};

  my $res = $this->auth->userExists(
    id => [$cUID, $loginName],
    loginName => $loginName,
    wikiName => $wikiName
  ) ? 1 : 0;

  _writeDebug("...res=$res") if TRACE;

  $this->{_handlesUser}{$key} = $res;

  return $res;
}

=begin TML

---++ ObjectMethod login2cUID($loginName, $dontcheck) -> $cUID

Convert a login name to the corresponding canonical user name. The
canonical name can be any string of 7-bit alphanumeric and underscore
characters, and must correspond 1:1 to the login name.
(undef on failure)

(if dontcheck is true, return a cUID for a nonexistant user too.
This is used for registration)

=cut

sub login2cUID {
  my ($this, $name, $dontcheck) = @_;

  #writeDebug("called login2cUID($name)");

  my $res = $this->{_login2cUID}{$name};
  unless (defined $res) {
    if ($this->isGroup($name)) {
      $res = $name;
    } else {

      my $user = $this->auth->findUser(
        id => $name, 
        loginName => $name, 
        wikiName => $name
      );

      if (defined $user) {
        $res = $user->prop("id");
      } else {
        $res = $this->auth->generateID("user");
      }
    }

    $this->{_login2cUID}{$name} = $res;
  }

  return $res;
}

=begin TML

---++ ObjectMethod getLoginName($cUID) -> login

Converts an internal cUID to that user's login
(undef on failure)

=cut

sub getLoginName {
  my ($this, $cUID) = @_;

  my $user = $this->auth->getUserByID($cUID);
  return $user->prop("loginName") if defined $user;
  return;
}

=begin TML

---++ ObjectMethod getWikiName($cUID) -> $wikiname

Map a canonical user name to a wikiname. If it fails to find a
WikiName, it will attempt to find a matching loginname, and use
an escaped version of that.

If there is no matching wikiName or loginName, it returns undef.

=cut

sub getWikiName {
  my ($this, $cUID) = @_;

  my $user = $this->auth->getUserByID($cUID);
  return $user->prop("wikiName") if defined $user;
  return;
}

=begin TML

---++ ObjectMethod removeUser($cUID) -> $boolean

Delete the user entry from this mapper. Throws an Error::Simple if
user removal is not supported (the default).

=cut

sub removeUser {
  my ($this, $cUID) = @_;
  
  my $user = $this->auth->getUserByID($cUID);
  return $user->delete if defined $user;
  return;
}


=begin TML

---++ ObjectMethod userExists($cUID) -> $boolean

Determine if the user already exists or not. Whether a user exists
or not is determined by the password manager.

=cut

sub userExists {
  my ($this, $cUID) = @_;

  # Do this to avoid a password manager lookup
  return 1 if $this->{session}{user} && $cUID eq $this->{session}{user};

  my $user = $this->auth->getUserByID($cUID)->load();
  return (defined $user && !$user->isUnknown) ? 1:0;
}

=begin TML

---++ ObjectMethod eachUser() -> iterator returing cUIDs

returns a list iterator for all known users

=cut

sub eachUser {
  my $this = shift;

  return $this->auth->eachUserIDs(enabled => 1);
}

=begin TML

---++ ObjectMethod isGroup($name) -> boolean

Establish if a user refers to a group or not. If $name is not
a group name it will probably be a canonical user id, though that
should not be assumed.

=cut

sub isGroup {
  my ($this, $name) = @_;

  return 1 if $name eq $Foswiki::cfg{SuperAdminGroup};
  return 1 if $name =~ /^group\-/;

  my $res = $this->{_isGroup}{$name};

  unless (defined $res) {
    my $group = $this->auth->findGroup(wikiName => $name);
    $res = defined($group) ? 1 : 0;

    $this->{_isGroup}{$name} = $res;
  }

  return $res;
}

=begin TML

---++ ObjectMethod eachGroup() -> $iterator

Get an iterator over the list of all the group names.

=cut

sub eachGroup {
  my $this = shift;

  my @all = sort map {$_->prop("wikiName")} $this->auth->eachGroup(@_)->all;
  return Foswiki::ListIterator->new(\@all);
}

=begin TML

---++ ObjectMethod eachGroupMember($group, $expand) -> $iterator

Return a iterator over the canonical user ids of users that are members
of this group. Should only be called on groups.

Note that groups may be defined recursively, so a group may contain other
groups. Unless $expand is set to false, this method should *only* return
users i.e.  all contained groups should be fully expanded.

=cut

sub eachGroupMember {
  my ($this, $name, $expand) = @_;

  if (defined $expand && ref($expand)) {
    $expand = $expand->{expand};
  }

  my $group = $this->auth->findGroup(wikiName => $name);
  return Foswiki::ListIterator->new([]) unless defined $group;
  my @all = sort map {$_->prop("id")} $group->eachMember($expand)->all;

  return Foswiki::ListIterator->new(\@all);
}


=begin TML

---++ ObjectMethod eachMembership($cUID) -> $iterator

Return an iterator over the names of groups that $cUID is a member of.

=cut

sub eachMembership {
  my ($this, $cUID) = @_;

  my $user = $this->auth->getUserByID($cUID);
  return Foswiki::ListIterator->new([]) unless defined $user;
  my @all = sort map {$_->prop("id")} $user->eachMembership()->all;

  return Foswiki::ListIterator->new(\@all);
}

=begin TML

---++ ObjectMethod groupAllowsView($groupName, $cUID) -> boolean

returns 1 if the group is able to be viewed by the current logged in user

implemented using topic VIEW permissions

=cut

sub groupAllowsView {
  my ($this, $groupName, $cUID) = @_;

  $cUID //= $this->{session}{user};
  return 1 if $this->{session}->{users}->isAdmin($cUID);

  my $group = $this->auth->findGroup(
    id => $groupName,
    wikiName => $groupName
  );

  return 1 unless defined $group; # WTF: not a known group, yet still returning true matching, WTF
  #return 0 unless defined $group; 

  my $user = $this->auth->getUserByID($cUID);
  return 0 unless defined $user;

  return $group->allowsView($user);
}

=begin TML

---++ ObjectMethod groupAllowsChange($group, $cUID) -> boolean

returns 1 if the group is able to be modified by user

implemented using topic CHANGE permissions

=cut

sub groupAllowsChange {
  my ($this, $groupName, $cUID) = @_;

  $cUID //= $this->{session}{user};

  my $group = $this->auth->findGroup(wikiName => $groupName);
  return 0 unless defined $group;

  my $user = $this->auth->getUserByID($cUID);
  return 0 unless defined $user;
  
  return $group->allowsChange($user);
}

=begin TML

---++ ObjectMethod addUserToGroup( $user, $groupName, $create ) -> $boolean

adds the user specified by the user to the group.

Mapper should throws Error::Simple if errors are encountered.  For example,
if the group does not exist, and the create flag is not supplied:
<pre>
    throw Error::Simple( $this->{session}
        ->i18n->maketext('Group does not exist and create not permitted')
    ) unless ($create);
</pre>

=cut

sub addUserToGroup {
  my ($this, $userName, $groupName, $create) = @_;

  $userName //= $this->{session}{user};
  return if $userName eq '';

  my $group = $this->auth->findGroup(wikiName => $groupName);
  return 0 unless defined $group;

  my $user = $this->auth->findUser(
    loginName => $userName,
    wikiName => $userName
  );

  unless (defined $user) {
    print STDERR "woops, cannot add user '$user' to group '$groupName' - user not found\n";
    return;
  }

  my $provider = $group->getProvider();

  throw Error::Simple("provider '".$provider->prop("id")."' cannot add user '$userName' to group '$groupName'")
    unless $provider->canChangeMembership($user, $group);

  return $group->addMember($user);
}

=begin TML

---++ ObjectMethod removeUserFromGroup( $user, $groupName ) -> $boolean

Mapper should throws Error::Simple if errors are encountered.  For example,
if the user does not exist in the group:
<pre>
   throw Error::Simple(
      $this->{session}->i18n->maketext(
         'User [_1] not in group, cannot be removed', $cuid
      )
   );
</pre>

=cut

sub removeUserFromGroup {
  my ($this, $userName, $groupName, $create) = @_;

  $userName //= $this->{session}{user};
  my $user = 
    $this->auth->findUser(loginName => $userName, id => $userName);

  return 0 unless defined $user;

  my $group = $this->auth->findGroup(wikiName => $groupName);
  return 0 unless defined $group;

  my $provider = $group->getProvider();

  throw Error::Simple("provider '".$provider->prop("id")."' cannot remove user '$userName' from group '$groupName'")
    unless $provider->canChangeMembership($user, $group);

  return $group->removeMember($user);
}

=begin TML

---++ ObjectMethod isAdmin( $user ) -> $boolean

True if the user is an administrator.

=cut

sub isAdmin {
  my ($this, $user) = @_;

  $user //= $this->{session}{user};

  my $sag = $Foswiki::cfg{SuperAdminGroup};

  return 1 if $user eq $sag;
  return $this->isInGroup($user, $sag);
}

=begin TML 

---++ ObjectMethod isInGroup($cUID, $groupName, $options ) -> $boolean

Test if the user identified by $cUID is in the given group. 
 $options is a hash array of options effecting the search.
Available options are:

   * =expand => 1=  0/1 - should nested groups be expanded when searching for the cUID?   Default is 1 - expand nested groups

=cut

sub isInGroup {
  my ($this, $cUID, $groupName, $options) = @_;

  $cUID //= $this->{session}{user};

  my $key = $cUID."::".$groupName;
  my $res = $this->{_isInGroup}{$key};
  unless (defined $res) {

    $res = 0;

    my $group = $this->auth->findGroup(wikiName => $groupName);

    if (defined $group) {
      my $user = $this->auth->getUserByID($cUID);
      $res = $group->hasMember($user, $options?$options->{expand}:undef) if defined $user;
    }

    $this->{_isInGroup}{$key} = $res;
  }

  return $res;
}

=begin TML

---++ ObjectMethod findUserByEmail( $email ) -> \@users

   * =$email= - email address to look up

Return a list of canonical user names for the users that have this email
registered with the password manager or the user mapping manager.

=cut

sub findUserByEmail {
  my ($this, $email) = @_;

  return if $this->{_isUnknown}{email}{$email};

  my $user = $this->auth->findUser(email => $email);
  return [$user->prop("id")] if defined $user && $user->isEnabled;

  $this->{_isUnknown}{email}{$email} = 1;
  return [];
}

=begin TML

---++ ObjectMethod findUserByWikiName($wikiname) -> list of cUIDs associated with that wikiname
   * =$wikiname= - wikiname to look up

Return a list of canonical user names for the users that have this wikiname.
Since a single wikiname might be used by multiple login ids, we need a list.

Note that if $wikiname is the name of a group, the group will *not* be
expanded.

=cut

sub findUserByWikiName {
  my ($this, $wikiName) = @_;

  return if $this->{_isUnknown}{wikiName}{$wikiName};

  my $user = $this->auth->findUser(wikiName => $wikiName);
  return [$user->prop("id")] if defined $user && $user->isEnabled;

  $this->{_isUnknown}{wikiName}{$wikiName} = 1;
  return [];
}

=begin TML

---++ ObjectMethod getEmails($name) -> @emailAddress

If $name is a cUID, return that user's email addresses. If it is a group,
return the addresses of everyone in the group.

=cut

sub getEmails {
  my ($this, $name) = @_;

  my @emails = ();

  my $group = $this->auth->findGroup(wikiName => $name);
  if (defined $group) {
    @emails = $group->getEmailsOfMembers();
  } else {
    my $user = $this->auth->findUser(
      id => $name, 
      loginName => $name, 
      wikiName => $name
    );

    push @emails, $user->prop("email") if defined $user;
  }

  return @emails;
}

=begin TML

---++ ObjectMethod getRegistrationDate($name) -> $epoch

return that user's registration date. 

=cut

sub getRegistrationDate {
  my ($this, $name) = @_;

  $name //= $this->{session}{user};

  my $user = $this->auth->findUser(
    id => $name,
    loginName => $name,
    wikiName => $name
  );

  return $user->prop("registrationDate") if defined $user;
  return;
}

=begin TML

---++ ObjectMethod setEmails($name, @emails)

Set the email address(es) for the given user.

=cut

sub setEmails {
  my ($this, $name, @emails) = @_;

  $name //= $this->{session}{user};

  my $user = $this->auth->findUser(
    id => $name,
    loginName => $name,
    wikiName => $name
  );

  return $user->setEmail(join(";", sort @emails)) if defined $user && $user->isEnabled;
  return;
}

=begin TML

---++ ObjectMethod checkPassword( $name, $password ) -> $boolean

Finds if the password is valid for the given login. This is called using
a login name rather than a cUID because the user may not have been mapped
at the time it is called.

=cut

sub checkPassword {
  my ($this, $name, $password) = @_;

  my $user = $this->auth->findUser(
    id => $name,
    loginName => $name,
    wikiName => $name
  );

  return $user->checkPassword($password) if defined $user;
  return 0;
}

=begin TML

---++ ObjectMethod setPassword( $cUID, $newPassU, $oldPassU ) -> $boolean

If the $oldPassU matches matches the user's password, then it will
replace it with $newPassU.

If $oldPassU defined but incorrect, will return 0.

If $oldPassU is undefined, will force the change irrespective of
the existing password, adding the user if necessary.

Otherwise returns 1 on success, undef on failure.

Default behaviour is to fail.

=cut

sub setPassword {
  my ($this, $name, $newPassword, $oldPassword) = @_;

  my $user = $this->auth->findUser(
    id => $name,
    loginName => $name,
    wikiName => $name
  );

  return $user->setPassword($newPassword, $oldPassword) if defined $user;
  return 0;
}

### static helper

sub _writeDebug {
  print STDERR "PluggableAuthUserMapping - $_[0]\n" if TRACE;
}

1;

