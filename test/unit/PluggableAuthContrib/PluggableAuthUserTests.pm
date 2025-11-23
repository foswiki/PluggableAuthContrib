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

package PluggableAuthUserTests;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Foswiki();
use Error qw ( :try );
#use Data::Dump qw(dump); 

our @ISA = qw( PluggableAuthTestCase );

sub test_self {
  my $this = shift;
  return;

  print STDERR "### groups\n";
  $this->{auth}->_dumpGroups();
  print STDERR "### members\n";
  $this->{auth}->_dumpMembers();
  print STDERR "### members flat\n";
  $this->{auth}->_dumpMembersFlat();
}

sub test_addUser {
  my $this = shift;

  my $user;
  my $error;

  try {
    $user = $this->{auth}->addUser(
      pid => "test",
      loginName => 'frank',
      firstName => 'Foo',
      lastName => 'Frank',
      email => 'frank@foo.bar',
    );
  } catch Error with {
    $error = shift->text();
  };

  $this->assert(defined($error), "There should be an error adding the same user again.");
  $this->assert($error =~ m/UNIQUE constraint failed/?1:0, "Wrong error message '$error'");
  $this->assert(!defined($user), "It should not add another user");
}

sub test_addUserUniqueLoginName {
  my $this = shift;

  my $user;
  my $error;

  try {
    $user = $this->{auth}->addUser(
      pid => "test",
      loginName => 'frank',
      firstName => 'Some',
      lastName => 'User',
      email => 'yo.lo@foo.bar',
    );
  } catch Error with {
    $error = shift->text();
    #print "error=$error\n";
  };

  $this->assert($error, "no error message");
  $this->assert($error =~ /UNIQUE constraint failed/, "unexpected error message");

  my $it = $this->{auth}->eachUser();
  my $count = scalar($it->all);

  $this->assert_equals(undef, $user, "user with same loginName has been created");
}

# sub test_addUserUniqueEmail {
#   my $this = shift;
#
#   my $user;
#   my $error;
#
#   try {
#     $user = $this->{auth}->addUser(
#       pid => "test",
#       loginName => 'somebody',
#       firstName => 'Some',
#       lastName => 'User',
#       email => 'frank.n.stein@foo.bar',
#     );
#   } catch Error with {
#     $error = shift->text();
#     #print "error=$error\n";
#   };
#
#   $this->assert($error, "no error message");
#   $this->assert($error =~ /UNIQUE constraint failed/, "unexpected error message");
#   $this->assert_equals(undef, $user, "user with same email has been created");
#
#   my $it = $this->{auth}->eachUser();
#   my $count = scalar($it->all);
# }

sub test_stringify_user {
  my $this = shift;

  my $user = $this->{auth}->findUser(wikiName => "FrankNStein");
  my $str = $user->stringify();

  $this->assert_matches(qr#user\-[A-F0-9]{8}\-[A-F0-9]{4}\-[A-F0-9]{4}\-[A-F0-9]{4}\-[A-F0-9]{8}/frank/FrankNStein/test/frank.n.stein\@foo.bar#, $str);
}

sub test_getUserByWikiName {
  my $this = shift;

  my $user = $this->{auth}->findUser(wikiName => "FrankNStein");

  $this->assert_user($user);
  $this->assert_equals("Frank", $user->prop("firstName"));
  $this->assert_equals("Stein", $user->prop("lastName"));
  $this->assert_equals("N", $user->prop("middleName"));
  $this->assert_equals("FrankNStein", $user->prop("wikiName"));
  $this->assert_equals("frank", $user->prop("loginName"));
  $this->assert_equals('frank.n.stein@foo.bar', $user->prop("email"));
}

sub test_getUserByLoginName {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");

  $this->assert_user($user);
  $this->assert_equals("FrankNStein", $user->prop("wikiName"));
  $this->assert_equals("frank", $user->prop("loginName"));
  $this->assert_equals('frank.n.stein@foo.bar', $user->prop("email"));
}

sub test_getUserByEmail {
  my $this = shift;

  my $user = $this->{auth}->findUser(email => 'frank.n.stein@foo.bar');

  $this->assert_user($user);
  $this->assert_equals("FrankNStein", $user->prop("wikiName"));
  $this->assert_equals("frank", $user->prop("loginName"));
  $this->assert_equals('frank.n.stein@foo.bar', $user->prop("email"));
}

sub test_findUser {
  my $this = shift;

  my $user1 = $this->{auth}->findUser(email => 'frank.n.stein@foo.bar');
  my $user2 = $this->{auth}->findUser(wikiName => 'FrankNStein');
  $this->assert($user1->equals($user2));

  my $user3 = $this->{auth}->findUser(
    loginName => 'frank',
    wikiName => 'FrankNStein'
  );
  $this->assert($user1->equals($user3));

  my $user4 = $this->{auth}->findUser(
    pid => 'foobar',
    loginName => 'frank',
    wikiName => 'FrankNStein'
  );

  $this->assert(!$user4);
}

sub test_getUnknownUser {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => 'lala');
  $this->assert_equals(undef, $user, "found unknown user");
}

sub test_userExists {
  my $this = shift;

  my $res = $this->{auth}->userExists(loginName => "frank");
  $this->assert_equals(1, $res, "User should exist");

  $res = $this->{auth}->userExists(loginName => "lila");
  $this->assert_equals(0, $res, "User must not exist");
}

sub test_wikiNameExists {
  my $this = shift;

  my $res = $this->{auth}->wikiNameExists("FrankNStein");
  $this->assert_equals(1, $res, "WikiName should exist");

  $res = $this->{auth}->wikiNameExists("YoLo");
  $this->assert_equals(0, $res, "WikiName must not exist");
}

sub test_eachUser {
  my $this = shift;

  my $it = $this->{auth}->eachUser();

  $this->assert($it);
  $this->assert(ref($it));
  $this->assert($it->isa("Foswiki::Iterator::DBIterator"), "Not a DBIterator");

  my $count = 0;
  while ($it->hasNext()) {
    my $user = $it->next();

    $this->assert_user($user);
    #print STDERR dump($user)."\n";
    #print STDERR $user->stringify."\n";
    $count++;
  }

  $this->assert_equals(7, $count, "Wrong number of users count=$count");
}

sub test_enableDisableUser {
  my $this = shift;

  my $it = $this->{auth}->eachUser(enabled => 1);

  my $count1 = scalar($it->all);
  $this->assert_equals(7, $count1, "1 - Wrong number of users: $count1");

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $res = $user->disable;
  $this->assert_equals(1, $res);

  $it->reset;
  my $count2 = scalar($it->all);
  $this->assert_equals($count1-1, $count2, "2 - Wrong number of users: $count2");

  $res = $user->enable();
  $this->assert_equals(1, $res);

  $it->reset;
  my $count3 = scalar($it->all);
  $this->assert_equals($count1, $count3, "3 - Wrong number of users: $count3");
}

sub test_deleteUser {
  my $this = shift;

  my $it = $this->{auth}->eachUser();

  my @allUsers = $it->all;
  #print STDERR "allUsers:\n".join("\n", map{$_->prop("id")} @allUsers)."\n";

  my $count1 = scalar(@allUsers);
  $this->assert_equals(7, $count1, "1 - Wrong number of users: $count1");

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $res = $user->delete();
  $this->assert_equals(1, $res, "one user should have been deleted, but got res=$res");
  $this->assert_equals(0, $user->isLoaded, "user should be unloaded after delete");

  $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_equals(undef, $user, "user should not be found anymore");

  $it->reset();
  my $count2 = scalar($it->all);
  $this->assert_equals(6, $count2, "2 - Wrong number of users: $count2");

  $res = $this->{auth}->findUser(loginName => "alice")->delete();
  $this->assert(1, $res, "one user should should have been deleted");

  $it->reset();
  my $count3 = scalar($it->all);
  $this->assert_equals(5, $count3, "3 - Wrong number of users: $count3");
}

sub test_getUniqueWikiName {
  my $this = shift;

  my $wikiName = $this->{auth}->getUniqueWikiName("FrankNStein");
  $this->assert_equals("FrankNStein1", $wikiName);

  $wikiName = $this->{auth}->getUniqueWikiName("YoLo");
  $this->assert_equals("YoLo", $wikiName);
}

sub test_cloneUser {
  my $this = shift;

  my $frank = $this->{auth}->findUser(loginName => "frank");
  $this->assert($frank);
  #print STDERR "1 - frank=".dump($frank)."\n";

  my $clone = $frank->clone();
  $this->assert($clone);
  #print STDERR "1 - clone=".dump($clone)."\n";

  $this->assert($frank->equals($clone), "frank's clone is not identical");
}

sub test_loginDifferentProviders {
  my $this = shift;

  my $frank1 = $this->{auth}->findUser(loginName => "frank");

  $this->assert_user($frank1);
  $this->assert_equals("test", $frank1->prop("pid"), "frank1 is not provided by correctly");

  #print STDERR "frank1=".$frank1->prop("loginName")."/".$frank1->prop("pid")."\n";

  my $frank2;
  my $error;

  try {
    $frank2 = $this->{auth}->addUser(
      pid => "test2",
      id => "frank_test2",
      loginName => 'frank',
      firstName => 'Foo',
      lastName => 'Frank',
      email => 'frank@foo.bar',
    );
  } catch Error with {
    $error = shift;
  };

  $this->assert_equals($error, undef, "There was an errror: ".($error//''));
  $this->assert_user($frank2);
  $this->assert_equals("test2", $frank2->prop("pid"), "frank2's provider should be test2");

  #print STDERR "frank2=".$frank2->prop("loginName")."/".$frank2->prop("pid")."\n";

  my @users = $this->{auth}->findUser(loginName => "frank");
  #print STDERR "users=".dump(\@users)."\n";
  $this->assert_equals(2, scalar(@users), "should be two franks from different providers, but got ".scalar(@users));
  $this->assert($users[0]->prop("pid") ne $users[1]->prop("pid"), "providers should differ");

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);
}

sub test_registrationDate {
  my $this = shift;

  my $now = time();
  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user, "where's frank");

  #print STDERR "now=$now\n";
  #print STDERR "registrationDate=".$user->prop("registrationDate")."\n";

  $this->assert($user->prop("registrationDate") - $now <= 100, "invalid registration date");

  $this->assert_equals(undef, $user->prop("loginDate"), "frank never logged in");

  my $res = $user->updateLoginDate();
  $this->assert(1, $res, "updating login date failed");
  $this->assert($user->prop("loginDate") - $now <= 100, "invalid login date");

  my $regDateStr = Foswiki::Func::formatTime($user->prop("registrationDate"), '$day $mon $year - $hour:$min');
  my $loginDateStr = Foswiki::Func::formatTime($user->prop("loginDate"), '$day $mon $year - $hour:$min');

  $this->assert_equals($regDateStr, $loginDateStr, "frank should have logged in the minute he registered");
}

sub test_eachMembership {
  my $this = shift;

  my $alice = $this->{auth}->findUser(loginName => "alice");
  $this->assert_user($alice);

  my $group1 = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_group($group1);

  my $group2 = $this->{auth}->findGroup(wikiName => "Group2");
  $this->assert_group($group2);

  #print STDERR "### members\n";
  #$this->{auth}->_dumpMembers();
  #print STDERR "### members flat\n";
  #$this->{auth}->_dumpMembersFlat();


  $this->assert($group1->hasMember($group2, 0), "Group1 should have Group2 as a member");
  $this->assert($group2->isMemberOf($group1, 0), "Group2 should be member of Group1");
  $this->assert(!$alice->isMemberOf($group1, 0), "Alice is not a direct member of Group1");
  $this->assert($alice->isMemberOf($group1, 1), "Alice should be indirect member of Group1");
  $this->assert($alice->isMemberOf($group2), "Alice should be member of Group2");

  my @groups = map {$_->load} $alice->eachMembership(1)->all;
  $this->assert_equals(2, scalar(@groups), "Alice is member of two groups");

  foreach my $group (@groups) {
    $this->assert_group($group);
    $this->assert($group->prop("wikiName") =~ /^Group(1|2)$/, "Alice is in Group1 and Group2");  
  }
}

sub test_checkTwoFactorPolicy {
  my $this = shift;

  my $alice = $this->{auth}->findUser(loginName => "alice");
  $this->assert_user($alice);

  $this->assert_null($alice->getProvider->prop("TwoFactorAuthEnabled"));
  $this->assert_equals(0, $alice->isTwoFactorAuthEnabled);
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa isn't enabled for provider");

  $alice->getProvider->prop("TwoFactorAuthEnabled", 1);
  $this->assert_equals(1, $alice->getProvider->prop("TwoFactorAuthEnabled"));
  $this->assert_equals(0, $alice->isTwoFactorAuthEnabled);
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa isn't enabled for user");

  my $twofa = $this->{auth}->getTwoFactorAuth();

  $twofa->prop("Policy", "optional");
  $this->assert_equals("optional", $twofa->prop("Policy"));
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa is optional");

  $twofa->prop("Policy", "mandatory");
  $this->assert_equals("mandatory", $twofa->prop("Policy"));
  $this->assert_equals(0, $alice->checkTwoFactorPolicy, "2fa is mandatory");

  $this->assert_equals(0, $alice->isAdmin, "alice isn't an admin");
  $twofa->prop("Policy", "mandatory-for-admins");
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa only for admins");

  my $key = $alice->activateTwoFactorAuth();
  $this->assert(defined $key);
  $this->assert_equals(1, $alice->isTwoFactorAuthEnabled, "2fa is enabled for user");
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa still only for admins");

  $twofa->prop("Policy", "mandatory");
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "2fa enabled as it is mandatory");

  my $key2 = $alice->deactivateTwoFactorAuth();
  $this->assert(defined $key2);
  $this->assert_equals($key->{id}, $key2->{id});

  $this->assert_equals(0, $alice->checkTwoFactorPolicy, "2fa disabled but it is mandatory");

  $twofa->prop("PolicyExceptions", "AliceWeinstein");
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "alice is excempted");

  $twofa->prop("PolicyExceptions", "AliceWeinstein, FooBar");
  $this->assert_equals(1, $alice->checkTwoFactorPolicy, "alice is excempted");

  $twofa->prop("PolicyExceptions", "FooBar");
  $this->assert_equals(0, $alice->checkTwoFactorPolicy, "alice not is excempted");

  $twofa->prop("PolicyExceptions", "Alice");
  $this->assert_equals(0, $alice->checkTwoFactorPolicy, "alice not is excempted");

  $twofa->prop("PolicyExceptions", "");
  $this->assert_equals(0, $alice->checkTwoFactorPolicy, "alice not is excempted");
}

1;
