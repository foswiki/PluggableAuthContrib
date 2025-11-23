# Extension for Foswiki - The Free and Open Source Wiki, https://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2023-2025 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::PluggableAuth::TwoFactorAuth;

=begin TML

---+ package Foswiki::PluggableAuth::TwoFactorAuth

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Convert::Base32 qw( encode_base32 decode_base32);
use Error qw(:try);
use JSON ();
use Bytes::Random::Secure ();

use constant TRACE => 0; # toggle me 

=begin TML

---++ ClassMethod new(%params) -> $this

=cut

sub new {
  my ($class, %params) = @_;

  #$this->writeDebug("called new()");

  my %defaults = (
    LogoUrl => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{LogoUrl} // 'https://foswiki.org/pub/System/ProjectLogos/foswiki-logo-large.png',
    Policy => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Policy} // 'optional',
    PolicyExceptions => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{PolicyExceptions} // '',
    MaxAttempts => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{MaxAttempts} // 3,
    AttemptsPeriod => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{AttemptsPeriod} // 60,
    NotifySecurityAlert => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{NotifySecurityAlert} // 0,
    Issuer => $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Issuer} || Foswiki::Func::getPreferencesValue("WIKITOOLNAME") || "Foswiki",
  );

  my %thisParams = (%defaults, %params);

  my $this = bless ({
    _props => \%thisParams
  }, $class);

  $this->{_debug} = TRACE || $Foswiki::cfg{PluggableAuth}{Debug} || $Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Debug};

  return $this;
}

sub DESTROY {
  my $this = shift;

  $this->finish();
}

sub finish {
  my $this = shift;

  undef $this->{_props};
  undef $this->{_debug};
  undef $this->{_oath};
  undef $this->{_json};
  undef $this->{_random};
}

sub auth {
  #my $this = shift;
  return Foswiki::PluggableAuth->new();
}

sub db {
  my $this = shift;

  return $this->auth->db();
}

sub oath {
  my $this = shift;

  unless ($this->{_oath}) {
    require Authen::OATH;
    $this->{_oath} = Authen::OATH->new();
  }

  return $this->{_oath};
}

sub random {
  my $this = shift;

  $this->{_random} //= Bytes::Random::Secure->new(NonBlocking => 1);
  return $this->{_random};
}

sub props {
  my ($this, $props) = @_;

  if (defined $props) {
    $this->{_props} = $props;
  }

  return $this->{_props};
}

sub prop {
  my ($this, $key, $val) = @_;

  #$this->writeDebug("called prop($key, ".($val//'undef').")");

  if (defined $val) {
    $this->{_props}{$key} = $val;
  } else {
    $val = $this->{_props}{$key};
  }

  # delayed evaluation
  if ($key eq 'Issuer' && !$val) {
    $val = Foswiki::Func::getPreferencesValue("WIKITOOLNAME");
  }

  #$this->writeDebug("... val=".($val//'undef'));

  return $val;
}

=begin TML

---++ ObjectMethod checkPolicy($user) -> $boolean 

returns 1 if 2fa is already ennabled

returns 1 of policy is optional

returns 0 if 2fa is not enabled but policy is mandatory

returns 0 if 2fa is not enabled but policy is mandatory for admins and user is admin

=cut

sub checkPolicy {
  my ($this, $user) = @_;

  # okay if 2fa is already enabled for this user
  return 1 if $user->isTwoFactorAuthEnabled();

  # okay if user is excempted
  my $wikiName = $user->prop("wikiName");
  my $exceptions = $this->prop("PolicyExceptions");
  return 1 if $exceptions =~ /\b\Q$wikiName\E\b/;

  # if 2fa isn't enabled for this user check the required policy
  my $policy = $this->prop("Policy");

  return 1 if $policy eq 'optional';
  return 0 if $policy eq 'mandatory';
  return 0 if $policy eq 'mandatory-for-admins' && $user->isAdmin;

  # check is okay by default
  return 1;
}

sub verify {
  my ($this, $code, $uid) = @_;

  $this->writeDebug("called verify()");

  return 0 unless $code;
  return 0 unless $this->checkAttempts($uid);

  my $thisCode = $this->getCode($uid);

  # normalize a bit
  $code =~ s/ //g;

  $this->writeDebug("verify($code) ... this code = $thisCode");

  my $isOk = $code eq $thisCode ? 1 : 0;

  $this->writeDebug("isOk=$isOk");
  $this->resetAttempts($uid) if $isOk;
  return $isOk;
}

sub checkAttempts {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called checkAttempts()");
  my $maxAttempts = $this->prop("MaxAttempts");
  my $attemptsPeriod = $this->prop("AttemptsPeriod");
  return 1 unless $maxAttempts && $attemptsPeriod;

  my $data = $this->getUserKey($uid);
  return 1 unless $data; #happens during activation

  my $now = time();
  $data->{attemptTime} ||= $now;
  my $since = $now - $data->{attemptTime};


  $data->{counter} ||= 0;
  $data->{counter} = 0 if $since >= $attemptsPeriod;
  $data->{counter}++;

  $this->writeDebug("maxAttempts=$maxAttempts, attemptsPeriod=$attemptsPeriod, since=$since, counter=$data->{counter}");

  if ($data->{counter} > $maxAttempts) {
    $this->writeWarning("user $uid tried more than $maxAttempts times to verify the token");

    if ($this->prop("NotifySecurityAlert")) {
      my $user = $this->auth->findUser(id => $uid);
      $user->sendEmail("mailsecurityalert") if $user;
    }

    throw Error::Simple($this->auth->maketext("Too many failures"));
  }

  $data->{attemptTime} = $now;
  $this->updateUserKey($data);

  return 1;  
}

sub resetAttempts {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called resetAttempts($uid)");

  my $data = $this->getUserKey($uid);
  return unless $data;

  $data->{counter} = 0;
  $data->{attemptTime} = 0;

  return $this->updateUserKey($data);
}

sub getCode {
  my ($this, $uid) = @_;
  
  $uid ||= Foswiki::Func::getCanonicalUserID();
  return $this->oath->totp(decode_base32($this->getSecret($uid)));
}

sub activate {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called activate($uid)");

  my $data = $this->getUserKey($uid);
  $data = $this->createUserKey($uid) unless $data && $data->{enabled};
  $data->{enabled} = 1;

  return $this->updateUserKey($data);
}

sub deactivate {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called deactivate($uid)");

  my $data = $this->getUserKey($uid);
  return unless $data;

  $data->{enabled} = 0;
  return $this->updateUserKey($data);
}

sub isEnabled {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  #$this->writeDebug("called isEnabled($uid)");

  my $data = $this->getUserKey($uid);
  return unless $data;
  return $data->{enabled} ? 1:0;
}

sub updateUserKey {
  my ($this, $data) = @_;

  my $uid = $data->{uid} // Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called updateUserKey($uid)");
  $data->{id} //= $this->auth->generateID("userkey");
  $data->{uid} //= $uid;

  my (@fields, @values, @q);
  while (my ($k, $v) = each %$data) {
    push @fields, $k;
    push @values, $v;
    push @q, "?";
  }

  my $stm = "REPLACE into PluggableAuth_user_keys (". join(", ", @fields).") VALUES (".join(", ", @q).")";
  my $res = $this->db->handler->do($stm, {}, @values);

  while (my ($k, $v) = each %$data) {
    $this->{_data}{$uid}{$k} = $v;
  }

  return $this->{_data}{$uid};
}


sub getUserKey {
  my ($this, $uid, $type) = @_;

  $type ||= 'otp';
  $uid ||= Foswiki::Func::getCanonicalUserID();
  #$this->writeDebug("called getUserKey($uid)");

  unless (defined $this->{_data}{$uid}) {
    my $stm = 'SELECT * FROM PluggableAuth_user_keys WHERE uid=? AND type=?';
    $this->{_data}{$uid} = $this->db->handler->selectrow_hashref($stm, {}, $uid, $type);
  }

  return $this->{_data}{$uid};
}

sub createUserKey {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called createUserKey($uid)");
  
  my $secret = $this->getSecretFromSession() || $this->generateSecret();
  $this->clearSecretFromSession();

  return {
    uid => $uid,
    type => 'otp',
    counter => 0,
    attemptTime => 0,
    enabled => 0,
    keyHandle => $secret,
  };
}

sub deleteUserKey {
  my ($this, $uid, $type) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $type ||= "otp";
  $this->writeDebug("called deleteUserKey($uid)");

  my $res = $this->db->handler->do("DELETE FROM PluggableAuth_user_keys WHERE uid=? AND type=?", {}, $uid, $type);
  delete $this->{_data}{$uid};

  return $res;
}

sub getSecret {
  my ($this, $uid) = @_;

  $uid ||= Foswiki::Func::getCanonicalUserID();
  $this->writeDebug("called getSecret($uid)");

  my $data = $this->getUserKey($uid);
  return $data->{keyHandle} if $data && $data->{enabled};

  # create a new one and store it into the session
  return $this->getSecretFromSession();
}

sub getSecretFromSession {
  my $this = shift;

  $this->writeDebug("called getSecretFromSession()");

  # create a new one and store it into the session
  my $cgis = $this->auth->{session}->getCGISession();
  return unless $cgis;

  my $secret = $cgis->param("_PAUTH_SECRET");
  unless ($secret) {
    $secret = $this->generateSecret();
    $cgis->param("_PAUTH_SECRET", $secret);
  }

  return $secret;
}

sub clearSecretFromSession {
  my $this = shift;

  my $cgis = $this->auth->{session}->getCGISession();
  $cgis->clear("_PAUTH_SECRET");
}

sub generateSecret {
  my ($this, $length) = @_;

  $length ||= 16;
  $this->writeDebug("called generateSecret($length)");

  my $universe = join("", ( 'A' .. 'Z', 0 .. 9 ));
  my $str = $this->random->string_from($universe, $length, '' );

  return uc(encode_base32($str));
}

sub writeDebug {
  my ($this, $msg) = @_;

  return unless $this->{_debug};

  my $class = ref($this);
  $class =~ s/^Foswiki:://;

  print STDERR "$class - $msg\n";
}

sub writeError {
  my ($this, $msg) = @_;

  my $class = ref($this);
  $class =~ s/^Foswiki:://;

  print STDERR "$class - ERROR: $msg\n";
}

sub writeWarning {
  my ($this, $msg) = @_;

  my $class = ref($this);
  $class =~ s/^Foswiki:://;

  print STDERR "$class - WARNING: $msg\n";
}

1;
