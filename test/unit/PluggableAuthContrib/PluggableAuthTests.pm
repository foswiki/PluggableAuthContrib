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

package PluggableAuthTests;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub test_singleton {
  my $this = shift;

  my $auth1 = Foswiki::PluggableAuth->new();
  $this->assert($auth1->isa("Foswiki::PluggableAuth"), "Not a Foswiki::PluggableAuth");

  $this->assert_equals($this->{auth}, $auth1);
}

sub test_db {
  my $this = shift;

  my $db = $this->{auth}->db;

  $this->assert($db);
  $this->assert($db->isa("Foswiki::DBI::Database"));
  $this->assert($db->handler->isa("DBI::db"));
}

sub test_normalizeWikiName {
  my $this = shift;

  my $wikiWord = $this->{auth}->normalizeWikiName("This is a test!");
  $this->assert_equals("ThisIsATest", $wikiWord);
}

sub test_normalizeGroupName {
  my $this = shift;

  my $res;

  $Foswiki::cfg{PluggableAuth}{NormalizeGroupNames} = 1;

  $res = $this->{auth}->normalizeGroupName("This is a test!");
  $this->assert_equals("ThisIsATestGroup", $res);

  $res = $this->{auth}->normalizeGroupName("Frühstücks-Warn-System");
  $this->assert_equals("FruehstuecksWarnSystemGroup", $res);

  $res = $this->{auth}->normalizeGroupName('@tick tack Group');
  $this->assert_equals("TickTackGroup", $res);
}

sub test_transliterate {
  my $this = shift;

  my $res = Foswiki::PluggableAuth::transliterate("Frühstücksei");
  $this->assert_equals("Fruehstuecksei", $res);
}

sub test_extractInitials {
  my $this = shift;

  my $res;

  $res = Foswiki::PluggableAuth::extractInitials("Foo Bar");
  $this->assert_equals("FB", $res);

  $res = Foswiki::PluggableAuth::extractInitials("Foo Bar Baz");
  $this->assert_equals("FBB", $res);

  $res = Foswiki::PluggableAuth::extractInitials("");
  $this->assert_equals("", $res);

  $res = Foswiki::PluggableAuth::extractInitials("This is a Test");
  $this->assert_equals("TiaT", $res);

  $res = Foswiki::PluggableAuth::extractInitials("Überstunden");
  $this->assert_equals("Ue", $res);

  $res = Foswiki::PluggableAuth::extractInitials("John-Doe");
  $this->assert_equals("JD", $res);

  $res = Foswiki::PluggableAuth::extractInitials("Örtliche Ämter");
  $this->assert_equals("OeAe", $res);

  $res = Foswiki::PluggableAuth::extractInitials("Örtliche Ämter", 0);
  $this->assert_equals("ÖÄ", $res);
}

sub test_getUserByID {
  my $this = shift;

  my $user1 = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user1);
  $this->assert_equals(1, $user1->isLoaded, "user should be loaded after find");

  my $user2 = $this->{auth}->getUserByID($user1->prop("id"));
  $this->assert_user($user2);
  $this->assert_equals(1, $user2->isLoaded, "user should be loaded after getting it again");

  $this->assert_equals($user1->prop("id"), $user2->prop("id"), "users should have the same id");

  $this->assert($user1->equals($user2), "users should be equal");
  $this->assert_equals(1, $user2->isLoaded, "user should be loaded after equal");
}

sub test_getAdminGroup {
  my $this = shift;

  my $group = $this->{auth}->getAdminGroup;
  $this->assert_group($group);
  $this->assert_equals($Foswiki::cfg{SuperAdminGroup}, $group->prop("wikiName"));

  my $adminUserLogin = $Foswiki::cfg{AdminUserLogin};
  my $admin = $this->{auth}->findUser(loginName => $adminUserLogin);
  $this->assert_user($admin);
  $this->assert_equals(1, $group->hasMember($admin), "AdminGroup should have Admin as member");
}

sub test_eventHandlers {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  $this->assert_equals(0, $provider->{beforeSaveHandlerCounter});
  $this->assert_equals(0, $provider->{afterSaveHandlerCounter});

  my @users = $provider->eachUser->all;
  $this->assert_user($users[0]);

  Foswiki::Func::saveTopic($this->{test_users_web}, $users[0]->prop("wikiName"));

  $this->assert_equals(1, $provider->{beforeSaveHandlerCounter});
  $this->assert_equals(1, $provider->{afterSaveHandlerCounter});
}

sub test_getProviders {
  my $this = shift;

  foreach my $provider ($this->{auth}->getProviders) {
    $this->assert_provider($provider);

    my $id = $provider->prop("id");
    $this->assert($id);

    my $domain = $provider->prop("DomainName");
    if ($provider->isa("Foswiki::PluggableAuth::Provider::Ldap") || $provider->isa("PluggableAuthTestProvide")) {
      $this->assert($domain);
    }
   
    #print STDERR "class=$provider, provider=$id, domainName=".($domain//'undef')."\n";
  }
}

sub test_getProviderOfDomain {
  my $this = shift;

  my $provider = $this->{auth}->getProviderOfDomain("test.domain.com");
  $this->assert($provider);

  $provider = $this->{auth}->getProviderOfDomain("TEST2.DOMAIN.COM");
  $this->assert($provider);

  $provider = $this->{auth}->getProviderOfDomain("test2.domain.com");
  $this->assert($provider);

  $provider = $this->{auth}->getProviderOfDomain("TEST2.DOMAIN.COM");
  $this->assert($provider);

  $provider = $this->{auth}->getProviderOfDomain("TEST2");
  $this->assert($provider);

  $provider = $this->{auth}->getProviderOfDomain("foobar");
  $this->assert(!$provider);

  my @providers = $this->{auth}->getProviderOfDomain("test2.domain.com");
  $this->assert_equals(2, scalar(@providers), "should be 2 provider for test.domain.com");
}

1;
