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

package PluggableAuthProviderTests;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki();
use JSON;
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub test_self {}

sub test_stringify_provider {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  my $str = $provider->stringify();
  $this->assert_equals("test", $str, "Unexpected stringifier result $str");
}

sub test_getUnknownProvider {
  my $this = shift;

  my $provider;
  my $error;

  try {
    $provider = $this->{auth}->getProvider('lala');
  } catch Error with {
    $error = shift;
  };

  $this->assert_equals(undef, $provider, "found unknown provider");
}

sub test_providerExists {
  my $this = shift;

  my $res = $this->{auth}->providerExists("Base");
  $this->assert_equals(1, $res, "Provider should exist");

  $res = $this->{auth}->providerExists("Topic");
  $this->assert_equals(1, $res, "Provider should exist");

  $res = $this->{auth}->providerExists("FooBar");
  $this->assert_equals(0, $res, "Provider must not exist");
}

sub test_eachProvider {
  my $this = shift;

  my $it = $this->{auth}->eachProvider();

  $this->assert($it);
  $this->assert(ref($it));
  $this->assert($it->isa("Foswiki::ListIterator"), "Not a ListIterator");

  my $count = 0;
  while ($it->hasNext()) {
    my $provider = $it->next();
    #print STDERR dump($provider)."\n";
    $this->assert_provider($provider);

    my $pid = $provider->prop("id");
    $this->assert($pid, "provider without a proper id");

    my $name = $provider->prop("Name");
    $this->assert($name, "provider without a proper Name");

    #print STDERR "found provider id=$pid, name=$name\n";
    $count++;
  }

  #$this->assert_equals(4, $count, "Wrong number of provider count=$count");
  #$it->reset;
  #my @all = $it->all;
  #$this->assert_equals(4, scalar(@all), "Wrong number of provider fetching all");
}

sub test_eachUserOfProvider {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  my $it = $provider->eachUser();
  $this->assert($it);
  $this->assert(ref($it));
  $this->assert($it->isa("Foswiki::Iterator::DBIterator"), "Not a DBIterator");
 
  my $count = 0;
  while ($it->hasNext) {
    my $user = $it->next;
    $this->assert_user($user);
    #print STDERR dump($user)."\n";
    $count++;
  }
  $this->assert_equals(2, $count, "should be two users for provider");
}

sub test_eachGroupOfProvider {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  my $it = $provider->eachGroup();
  $this->assert($it);
  $this->assert(ref($it));
  $this->assert($it->isa("Foswiki::Iterator::DBIterator"), "Not a DBIterator");
 
  my $count = 0;
  while ($it->hasNext) {
    my $group = $it->next;
    $this->assert_group($group);
    #print STDERR dump($group)."\n";
    $count++;
  }
  $this->assert_equals(3, $count, "should be three group for provider");
}

sub test_handles {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $provider = $this->{auth}->getProvider("test");
  $this->assert($provider->handles($user), "test provider should handle frank object");

  $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{AdminUserLogin});
  $this->assert_user($user);
  $this->assert(!$provider->handles($user), "test provider should not handle admin object");
}

sub test_canDelete {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $provider = $this->{auth}->getProvider("test");

  $this->assert($provider->canDelete($user), "test provider should be able to delete frank");

  $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{AdminUserLogin});
  $this->assert_user($user);

  $this->assert(!$provider->canDelete($user), "test provider should not be able to delete admin");

  $provider = $user->getProvider();
  $this->assert(!$provider->canDelete($user), "base provider should not be able to delete admin");
}

sub test_canSetEmail {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->getProvider->canSetEmail($user); 
  $this->assert($res);
}

sub test_setEmail {
  my $this = shift;

  # disable in case you enabled it
  $Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled} = 0;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $email = $user->prop("email");
  $this->assert_equals($email, 'frank.n.stein@foo.bar');

  my $res = $user->setEmail('frank.n.stein@bar.baz');
  $this->assert($res);

  $email = $user->prop("email");
  $this->assert_equals($email, 'frank.n.stein@bar.baz');
}

sub test_hashPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $provider = $user->getProvider();

  my $hash = $provider->hashPassword($user, "foo", "sha1");
  $this->assert($hash);
  $this->assert($hash =~ /^{SHA}/ ? 1:0, 'hash should start with {SHA}');

  $hash = $provider->hashPassword($user, "foo", "crypt");
  $this->assert($hash);
  $this->assert($hash =~ /^[^{]/ ? 1:0);

  $hash = $provider->hashPassword($user, "foo", "md5");
  $this->assert($hash);
  $this->assert($hash =~ /^[^{]/ ? 1:0);

  $hash = $provider->hashPassword($user, "foo", "apache-md5");
  $this->assert($hash);
  $this->assert($hash =~ /^\$apr1/ ? 1:0, 'hash should start with $apr1');

  $hash = $provider->hashPassword($user, "foo", "crypt-md5");
  $this->assert($hash);

  $hash = $provider->hashPassword($user, "foo", "plain");
  $this->assert_equals($hash, "foo");

  $hash = $provider->hashPassword($user, "foo", "bcrypt");
  $this->assert($hash);

  $hash = $provider->hashPassword($user, "foo", "argon2");
  $this->assert($hash =~ /^\$argon2/ ? 1:0, 'hash should start with $argon2');

  eval {
    $hash = $provider->hashPassword($user, "foo", "foobar");
  };
  my $e = $@;

  $this->assert($e, "Unsupported password encoding foobar");
}

sub test_canSetPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->getProvider->canSetPassword($user); 
  $this->assert($res);
}

sub test_checkPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_sha1 {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "sha1"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_crypt {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "crypt"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_md5 {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "md5"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_apache_md5 {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "apache-md5"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res, "password does not match");

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_crypt_md5 {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "crypt-md5"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_plain {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "plain"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_bcrypt {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "bcrypt"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_checkPassword_argon2 {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  my $res = $user->setPassword("frühstück", undef, "argon2"); 
  $this->assert($res);

  $res = $user->checkPassword("frühstück"); 
  $this->assert($res);

  $res = $user->checkPassword("wrong secret"); 
  $this->assert(!$res);
}

sub test_deleteAll {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("Base");

  my $count = scalar($provider->eachUser->all);
  $this->assert_equals(5, $count, "should be 5 users in provider");

  my $res = $provider->deleteAll;
  $this->assert_equals(5, $res, "should have deleted 5 users from provider");

  my $count2 = scalar($provider->eachUser->all);
  $this->assert_equals(0, $count2, "should be no users left in provider");
}

sub test_lookupAddr {
  my $this = shift;

  my $res;
  my $addr = "1.2.3.4";
  $res = Foswiki::PluggableAuth::Provider::_lookupAddr($addr, "1.2.3.4");
  $this->assert($res);

  $res = Foswiki::PluggableAuth::Provider::_lookupAddr($addr, "1.0.0.0-2.0.0.0");
  $this->assert($res);

  $res = Foswiki::PluggableAuth::Provider::_lookupAddr($addr, "1.2.3.0 - 1.2.3.255");
  $this->assert($res);

  $res = Foswiki::PluggableAuth::Provider::_lookupAddr($addr, "1.2.3.0/14, 123.123.123.123");
  $this->assert($res);
}

sub test_isAllowedIpAddress {
  my $this = shift;

  my $res;
  my $addr = "1.2.3.4";
  my $provider = $this->{auth}->getProvider("Base");

  $res = $provider->isAllowedIpAddress($addr);
  $this->assert($res);

  $provider->prop("DeniedIPAddresses", $addr);
  $res = $provider->isAllowedIpAddress($addr);
  $this->assert(!$res);

  $provider->prop("DeniedIPAddresses", "");
  $provider->prop("AllowedIPAddresses", $addr);
  $res = $provider->isAllowedIpAddress($addr);
  $this->assert($res);

  $provider->prop("DeniedIPAddresses", $addr);
  $provider->prop("AllowedIPAddresses", $addr);
  $res = $provider->isAllowedIpAddress($addr);
  $this->assert(!$res);
}

sub test_getAttribute {
  my $this = shift;

  my $res;
  my $json;

  $json = decode_json('{"foo":"bar"}');
  $this->assert($json);

  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "foo");
  $this->assert_equals("bar", $res);
 
  $json = decode_json('{"foo": {"foo": "bar"}}');
  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "foo.foo");
  $this->assert_equals("bar", $res);
 
  $json = decode_json('{"foo": [{"foo": "bar"}]}');
  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "foo[0].foo");
  $this->assert_equals("bar", $res);
 
  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "foo[1].foo");
  $this->assert_equals(undef, $res);
 
  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "foo.foo");
  $this->assert_equals(undef, $res);
 
  $json = decode_json('{"https://mdc": {"authorization": { "groups": ["foo", "bar"]}}}');
  $res = Foswiki::PluggableAuth::Provider::getAttribute($json, "https://mdc.authorization.groups");
  $this->assert($res);
  $this->assert_equals("ARRAY", ref($res));
  $this->assert_equals(2, scalar(@$res));
  $this->assert_equals("foo", $res->[0]);
  $this->assert_equals("bar", $res->[1]);
 
}

sub test_isValidEmail {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");
  if ($Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled}) {
    $this->assert(!$provider->isValidEmail('foo@bar.com'));
  }
  $this->assert($provider->isValidEmail('foswiki@foswiki.org'));
  $this->assert($provider->isValidEmail('root@foswiki.org'));
}

sub test_isValidPassword {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  $this->assert(!$provider->isValidPassword());
  $this->assert(!$provider->isValidPassword(''));
  $this->assert(!$provider->isValidPassword('123'));
  $this->assert(!$provider->isValidPassword('123456789'));
  $this->assert(!$provider->isValidPassword('ZZZZZZ'));
}

sub test_setPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  $this->assert($user->setPassword("foobar123"));
  $this->assert(!$user->setPassword());
  $this->assert(!$user->setPassword(""));
  $this->assert(!$user->setPassword("123"));
  $this->assert(!$user->setPassword("123456789"));
  $this->assert(!$user->setPassword("ZZZZZZ"));
}

1;
