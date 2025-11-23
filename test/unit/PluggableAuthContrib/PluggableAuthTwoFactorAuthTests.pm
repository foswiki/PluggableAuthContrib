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

package PluggableAuthTwoFactorAuthTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth::TwoFactorAuth ();
use Foswiki();
use Foswiki::Func();
use JSON;
use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub countKeys {
  my $this = shift;

  my $res = $this->{auth}->db->handler->selectrow_hashref("SELECT count(*) as count from PluggableAuth_user_keys");
  return $res->{count};
}

sub test_self {}

sub test_getTwoFactorAuth {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  $this->assert_equals("Foswiki::PluggableAuth::TwoFactorAuth", ref($twofa));
}

sub test_props {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $props = $twofa->props();

  $this->assert_equals(7, scalar(keys %$props));
  $this->assert($props->{"AttemptsPeriod"});
  $this->assert($props->{"Issuer"});
  $this->assert($props->{"LogoUrl"});
  $this->assert($props->{"MaxAttempts"});
  $this->assert($props->{"NotifySecurityAlert"});
  $this->assert($props->{"Policy"});
}

sub test_prop {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  foreach my $key (qw(AttemptsPeriod Issuer LogoUrl MaxAttempts)) {
    my $val = $twofa->prop($key);
    $this->assert($val);
  }
}

sub test_oath {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  $this->assert_equals("Authen::OATH", ref($twofa->oath));
}

sub test_random {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  $this->assert_equals("Bytes::Random::Secure", ref($twofa->random));
}

sub test_getUserKey {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $data = $twofa->getUserKey();
  $this->assert(!defined($data));

  $this->assert_equals(0, $this->countKeys);

  $data = $twofa->createUserKey();
  $this->assert(defined($data));
  $this->assert(!defined($data->{id}));

  $data = $twofa->updateUserKey($data);
  $this->assert(defined($data));
  $this->assert(defined($data->{id}));

  $this->assert_equals(1, $this->countKeys);
}

sub test_deleteUserKey {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  $this->assert_equals(0, $this->countKeys); 

  my $data = $twofa->updateUserKey($twofa->createUserKey());
  $this->assert(defined($data));
  $this->assert_equals(1, $this->countKeys); 

  my $res = $twofa->deleteUserKey();
  $this->assert_equals(1, $res);

  $this->assert_equals(0, $this->countKeys);
}

sub test_generateSecret {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $secret = $twofa->generateSecret();

  $this->assert($secret =~ /^[A-Z0-9]+$/);
  $this->assert_equals(26, length($secret));
}

sub test_getSecret {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $secret = $twofa->getSecret();

  $this->assert($secret =~ /^[A-Z0-9]+$/);
  $this->assert_equals(26, length($secret));
}

sub test_activate {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $uid = Foswiki::Func::getCanonicalUserID();
  my $data = $twofa->activate();

  $this->assert($data);
  $this->assert($data->{enabled});
  $this->assert($data->{keyHandle});
  $this->assert($data->{id} =~ /^userkey\-/);
  $this->assert_equals("otp", $data->{type});
  $this->assert_equals($uid, $data->{uid});

  $this->assert_equals(1, $this->countKeys);

  my $data2 = $twofa->activate();
  $this->assert($data2);

  $this->assert_equals(1, $this->countKeys);
}

sub test_deactivate {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  my $data = $twofa->deactivate();
  $this->assert(!defined($data));

  $data = $twofa->updateUserKey($twofa->createUserKey());
  $this->assert(defined($data));

  $data = $twofa->deactivate();
  $this->assert($data);
  $this->assert(!$data->{enabled});

  $this->assert_equals(1, $this->countKeys);
}

sub test_isEnabled {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  my $res = $twofa->isEnabled();
  $this->assert(!defined($res));

  $twofa->activate();
  $this->assert($twofa->isEnabled());

  $twofa->deactivate();
  $this->assert(!$twofa->isEnabled());
}

sub test_getCode {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();
  my $code = $twofa->getCode();

  $this->assert($code);
  $this->assert($code =~ /^\d\d\d\d\d\d$/);
}

sub test_verify {
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  my $code = $twofa->getCode();
  my $res = $twofa->verify($code);
  $this->assert($res); 

  my $data = $twofa->createUserKey();
  $data->{enabled} = 1;
  $data = $twofa->updateUserKey($data);

  $this->assert($data);
  $this->assert_equals(0, $data->{counter});
  $this->assert_equals(0, $data->{attemptTime});

  $res = $twofa->verify("123456");
  $this->assert(!$res);

  $data = $twofa->getUserKey();
  $this->assert_equals(1, $data->{counter});
  $this->assert_equals(time(), $data->{attemptTime});

  $res = $twofa->verify("123456");
  $this->assert(!$res);

  $data = $twofa->getUserKey();
  $this->assert_equals(2, $data->{counter});
  $this->assert_equals(time(), $data->{attemptTime});

  $res = $twofa->verify($code);
  $data = $twofa->getUserKey();
  $this->assert_equals(0, $data->{counter});
  $this->assert_equals(0, $data->{attemptTime});
}

sub test_resetAttempts { 
  my $this = shift;

  my $twofa = $this->{auth}->getTwoFactorAuth();

  my $data = $twofa->updateUserKey($twofa->createUserKey());
  $this->assert($data);

  my $res = $twofa->verify("1234");
  $this->assert(!$res);

  $this->assert_equals(1, $data->{counter});
  $twofa->resetAttempts();

  $this->assert_equals(0, $data->{counter});
  $this->assert_equals(0, $data->{attemptTime});
}

1;
