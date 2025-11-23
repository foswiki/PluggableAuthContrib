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

package PluggableAuthBaseProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Base ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  #$Foswiki::cfg{PluggableAuth}{Providers}{Base}{Enabled} = 1;
  $this->{provider} = $this->{auth}->getProvider("Base");
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Base"), "Not a Foswiki::PluggableAuth::Provider::Base");
}

sub test_props {
  my $this = shift;

  my $props = $this->{provider}->props;
  #print STDERR "props=".dump($props)."\n";

  $this->assert($props->{Enabled});
  $this->assert($props->{Name});
  $this->assert($props->{Module});
  $this->assert(!$props->{Visible});
}

sub test_baseProvider {
  my $this = shift;

  $this->assert("Base User Mapping", $this->{provider}->prop("Name"), "wrong name");
  $this->assert("Base", $this->{provider}->prop("id"), "wrong id");

  my $unknown;
  my $error;

  try {
    $unknown = $this->{auth}->getProvider("FooBar");
  } catch Error with {
    $error = shift;
  };

  $this->assert_equals(undef, $unknown, "unknown provider found");
}

sub test_eachUser {
  my $this = shift;

  my $count = 0;
  my $it = $this->{auth}->eachUser();
  while ($it->hasNext) {
    my $user = $it->next;
    $this->assert_user($user);
    next unless $user->prop("pid") eq 'Base';
    #print STDERR $user->stringify ."\n";
    $count++;
  }

  $this->assert_equals(5, $count, "should be 5 base users, only got $count");
}

sub test_eachUserOfBase {
  my $this = shift;

  my $count = 0;
  my $it = $this->{provider}->eachUser();
  while ($it->hasNext) {
    my $user = $it->next;
    $this->assert_user($user);
    #print STDERR $user->stringify ."\n";
    $count++;
  }

  $this->assert_equals(5, $count, "should be 5 base users, only got $count");
}

#qw(BaseUserMapping_111 BaseUserMapping_222 BaseUserMapping_333 BaseUserMapping_666 BaseUserMapping_999)) 
sub test_projectContributor {
  my $this = shift;

  my $user = $this->{auth}->getUserByID("BaseUserMapping_111");
  $this->assert_user($user);
  $this->assert_equals('ProjectContributor', $user->prop("loginName"), "wrong loginName ".($user->prop("loginName")//'undef'));
  $this->assert_equals('ProjectContributor', $user->prop("wikiName"), "wrong wikiName");
  $this->assert_equals("", $user->prop("email"), "wrong email ".($user->prop("email")//'undef'));
  $this->assert_equals("Base", $user->prop("pid"), "wrong provider");
  $this->assert_equals(1, $user->isEnabled, "not enabled");
}

sub test_registrationAgent {
  my $this = shift;

  my $user = $this->{auth}->getUserByID("BaseUserMapping_222");
  $this->assert_user($user);
  $this->assert_equals("RegistrationAgent", $user->prop("loginName"), "wrong loginName ".($user->prop("loginName")//'undef'));
  $this->assert_equals("RegistrationAgent", $user->prop("wikiName"), "wrong wikiName");
  $this->assert_equals("", $user->prop("email"), "wrong email ".($user->prop("email")//'undef'));
  $this->assert_equals("Base", $user->prop("pid"), "wrong provider");
  $this->assert_equals(1, $user->isEnabled, "not enabled");
}

sub test_adminUser {
  my $this = shift;

  my $user = $this->{auth}->getUserByID("BaseUserMapping_333");
  $this->assert_user($user);

  #print STDERR "user=".dump($user->load)."\n";

  $this->assert_equals($Foswiki::cfg{AdminUserLogin}, $user->prop("loginName"), "wrong loginName ".($user->prop("loginName")//'undef').", should be ".$Foswiki::cfg{AdminUserLogin});
  $this->assert_equals($Foswiki::cfg{AdminUserWikiName}, $user->prop("wikiName"), "wrong wikiName");
  $this->assert_equals($Foswiki::cfg{WebMasterEmail}, $user->prop("email"), "wrong email ".($user->prop("email")//'undef'));
  $this->assert_equals("Base", $user->prop("pid"), "wrong provider");
  $this->assert_equals(1, $user->isEnabled, "not enabled");
}

sub test_defaultUser {
  my $this = shift;

  my $user = $this->{auth}->getUserByID("BaseUserMapping_666");
  $this->assert_user($user);

  #print STDERR "user=".dump($user->load)."\n";

  $this->assert_equals($Foswiki::cfg{DefaultUserLogin}, $user->prop("loginName"), "wrong loginName ".($user->prop("loginName")//'undef').", should be ".$Foswiki::cfg{DefaultUserLogin});
  $this->assert_equals($Foswiki::cfg{DefaultUserWikiName}, $user->prop("wikiName"), "wrong wikiName");
  $this->assert_equals("", $user->prop("email"), "wrong email ".($user->prop("email")//'undef'));
  $this->assert_equals("Base", $user->prop("pid"), "wrong provider");
  $this->assert_equals(1, $user->isEnabled, "not enabled");
}

sub test_unknownUser {
  my $this = shift;

  my $user = $this->{auth}->getUserByID("BaseUserMapping_999");
  $this->assert_user($user);
  $this->assert_equals("unknown", $user->prop("loginName"), "wrong loginName ".($user->prop("loginName")//'undef'));
  $this->assert_equals("UnknownUser", $user->prop("wikiName"), "wrong wikiName");
  $this->assert_equals("", $user->prop("email"), "wrong email ".($user->prop("email")//'undef'));
  $this->assert_equals("Base", $user->prop("pid"), "wrong provider");
  $this->assert_equals(1, $user->isEnabled, "not enabled");
}

sub test_isDeleteable {
  my $this = shift;

  my $it = $this->{provider}->eachUser();
  while ($it->hasNext) {
    my $user = $it->next;
    $this->assert_user($user);
    $this->assert_equals(0, $user->isDeleteable, "base user ".$user->prop("id")." should not be deleteable");
    $user->delete if $user->isDeleteable;
  }
}

sub test_canCheckPassword {
  my $this = shift;

  my $it = $this->{provider}->eachUser;
  while ($it->hasNext) {
    my $user = $it->next;
    if ($user->isAdmin) {
      $this->assert_equals(1, $this->{provider}->canCheckPassword($user), "admin should be able to check password");
    } else {
      $this->assert_equals(0, $this->{provider}->canCheckPassword($user), $user->prop("wikiName")." should not be able to check password");
    }
  }
}

sub test_canRegisterUser {
  my $this = shift;

  $this->assert_equals(0, $this->{provider}->canRegisterUser(), "base cannot register any user");
}

sub test_canDeleteUser {
  my $this = shift;

  $this->assert_equals(0, $this->{provider}->canDelete(), "base cannot delete any user");
}

sub test_canSetEmail {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("Base");
  $this->assert_equals(0, $this->{provider}->canSetEmail(), "base cannot set any email");
}

sub test_canSetPassword {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("Base");
  $this->assert_equals(0, $this->{provider}->canSetPassword(), "base cannot set any password");
}

sub test_checkPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{AdminUserLogin});
  $this->assert_user($user);

  my $hash = crypt("some password", time());
  $Foswiki::cfg{Password} = $hash;

  $this->assert_equals(1, $this->{provider}->checkPassword($user, "some password"), "base should be able to check password");
  $this->assert_equals(0, $this->{provider}->checkPassword($user, "wrong password"), "base should be able to check the wrong password");
  $this->assert_equals(1, $user->checkPassword("some password"), "should be able to check password");
}

sub test_setPassword {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{AdminUserLogin});
  $this->assert_user($user);

  my $res = $user->setPassword("foobar");
  $this->assert_equals(0, $res, "should not be able to set the admin password");
}

sub test_isAdmin {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{AdminUserLogin});

  $this->assert_user($user);
  $this->assert_equals(1, $user->isAdmin, "admin user should be admin");
  $this->assert_equals(1, $this->{provider}->isAdmin($user), "base provider should rank admin as admin");

  $user = $this->{auth}->findUser(loginName => $Foswiki::cfg{DefaultUserLogin});
  $this->assert_user($user);
  $this->assert_equals(0, $user->isAdmin, "guest user should not be admin");
  $this->assert_equals(0, $this->{provider}->isAdmin($user), "base provider should not rank guest as admin");
}

1;
