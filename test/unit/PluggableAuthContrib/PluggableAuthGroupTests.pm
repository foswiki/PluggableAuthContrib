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

package PluggableAuthGroupTests;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub test_self {}

sub test_addGroup {
  my $this = shift;

  my $group;
  my $error;

  try {
    $group = $this->{auth}->addGroup(
      pid => "test",
      wikiName => "Group1"
    );
  } catch Error with {
    $error = shift->text();
  };

  $this->assert(defined($error), "There should be an error adding the same group again.");
  $this->assert($error =~ m/UNIQUE constraint failed/?1:0, "Wrong error message '$error'");
  $this->assert(!defined($group), "It should not add another group");
}

sub test_stringify_group {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "Group1");
  my $str = $group->stringify();

  my $res = ($str =~ m/^group\-([0-9A-F]+\-[0-9A-F]+\-[0-9A-F]+\-[0-9A-F]+\-[0-9A-F]+)\/Group1\/test$/)?1:0;
  $this->assert($res, "Unexpected stringifier result $str");
}

sub test_getUnknownGroup {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => 'lala');
  $this->assert_equals(undef, $group, "found unknown group");
}

sub test_groupExists {
  my $this = shift;

  my $res = $this->{auth}->groupExists(wikiName => "Group1");
  $this->assert_equals(1, $res, "Group should exist");

  $res = $this->{auth}->groupExists(wikiName => "lila");
  $this->assert_equals(0, $res, "Group must not exist");
}

sub test_eachGroup {
  my $this = shift;

  my $it = $this->{auth}->eachGroup();

  $this->assert($it);
  $this->assert(ref($it));
  $this->assert($it->isa("Foswiki::Iterator::DBIterator"), "Not a DBIterator");

  my $count = 0;
  while ($it->hasNext()) {
    my $group = $it->next();

    $this->assert_group($group);
    #print STDERR dump($group)."\n";
    $count++;
  }

  $this->assert_equals(6, $count, "Wrong number of groups $count, expected 6");
}

sub test_enableDisableGroup {
  my $this = shift;

  my $it = $this->{auth}->eachGroup(enabled => 1);

  my $count1 = scalar($it->all);
  $this->assert_equals(6, $count1, "1 - Wrong number of groups $count1, expected 6");

  my $group = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_group($group);

  my $res = $group->disable();
  $this->assert_equals(1, $res, "group->disable() should return 1 on success");

  $it->reset;
  my $count2 = scalar($it->all);
  $this->assert_equals($count1-1, $count2, "2 - Wrong number of groups $count2, expected ".($count1-1));

  $res = $group->enable();
  $this->assert_equals(1, $res);

  $it->reset;
  my $count3 = scalar($it->all);
  $this->assert_equals($count1, $count3, "3 - Wrong number of groups $count3, expected $count1");
}

sub test_deleteGroup {
  my $this = shift;

  my $it = $this->{auth}->eachGroup();

  my @groups = $it->all();
  my $count1 = scalar(@groups);
  #print STDERR "groups=".join(", ", map{$_->prop("wikiName")} @groups)."\n";
  $this->assert_equals(6, $count1, "1 - Wrong number of groups $count1, expected 6");

  my $group = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_group($group);

  my $res = $group->delete();
  $this->assert_equals(1, $res, "1 - one group should have been deleted");
  $this->assert_equals(0, $group->isLoaded, "group should be unloaded after delete");

  $group = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_equals(undef, $group, "group should not be found anymore");

  $it->reset();
  my $count2 = scalar($it->all);
  $this->assert_equals($count1-1, $count2, "2 - Wrong number of groups");

  $res = $this->{auth}->findGroup(wikiName => "Group2")->delete();
  $this->assert(1, $res, "2 - one group should should have been deleted");

  $it->reset();
  my $count3 = scalar($it->all);
  $this->assert_equals($count1-2, $count3, "3 - Wrong number of groups $count3, expected ".($count1-2));
}

sub test_deleteAllGroups {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");

  my $it = $provider->eachGroup();

  my @groups = $it->all();
  my $count = scalar(@groups);
  $this->assert_equals(3, $count, "1 - Wrong number of groups $count, expected 3");

  my $res = $provider->deleteAllGroups();
  $this->assert_equals($count, $res, "2 - Wrong number of groups $res, expected $count");

  $it->reset();
  $count = scalar($it->all);
  $this->assert_equals(0, $count, "3 - Wrong number of groups $count, expected 0");
}

sub test_addMember {
  my $this = shift;

  my $user = $this->{auth}->findUser(loginName => "frank");

  $this->assert($user, "frank not found");
  $this->assert($user->isa("Foswiki::PluggableAuth::User"));

  my $group = $this->{auth}->findGroup(wikiName => "Group1");

  $this->assert($group, "Group1 not found");
  $this->assert($group->isa("Foswiki::PluggableAuth::Group"));

  my $res = $group->hasMember($user);
  $this->assert_equals(1, $res, "1 - user should be member of group");

  $group->removeMember($user);

  $res = $group->hasMember($user);
  $this->assert_equals(0, $res, "1 - user should not be member of group anymore");

  $res = $group->addMember($user);
  $this->assert_equals(1, $res, "2 - should have added one member");

  $user->delete;

  $res = $group->hasMember($user);
  $this->assert_equals(0, $res, "2 - user should not be member of group anymore");
}

sub test_setMembers {
  my $this = shift;

  my $group1 = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert($group1);

  my $group2 = $this->{auth}->findGroup(wikiName => "Group2");
  $this->assert($group2);

  my $user1 = $this->{auth}->findUser(loginName => "frank");
  my $user2 = $this->{auth}->findUser(loginName => "alice");

  $group1->deleteMembers();
  $group2->deleteMembers();

  $group1->setMembers([$user1, $group2]);
  $group2->setMembers([$user2]);

  $group1->reload(); # need to reload as group2 had a sideeffect on group1
  
  my $res;
  $res = $group1->hasMember($user1);
  $this->assert_equals(1, $res, $user1->prop("id")." should be member of group1");

  $res = $group1->hasMember($user2);
  $this->assert_equals(0, $res, $user2->prop("id")." should not be a direct member of group1");

  $res = $group1->hasMember($user2, 1);
  $this->assert_equals(1, $res, $user2->prop("id")." should be member of group1");

  my $count = $group1->prop("count");
  $this->assert_equals(2, $count, "group1 should have 2 members, found $count");
}

sub test_deleteMembers {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_group($group);

  my $count = $group->prop("count");
  $this->assert_equals(2, $count, "group1 should have 2 members, but found $count");

  my $res = $group->deleteMembers();
  $count = $group->prop("count");

  $this->assert_equals(0, $count, "group1 should have no member, but found $count");
}

sub test_directMembers {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "Group1");

  #print STDERR "### Group1:\n";

  my $it = $group->eachMember(0);
  while ($it->hasNext) {
    my $m = $it->next();
    my $name;
    if ($m->isa("Foswiki::PluggableAuth::User")) {
      my $wikiName = $m->prop("wikiName");
      #print STDERR "   wikiName: $wikiName\n";
      $this->assert_equals("FrankNStein", $wikiName, "member of Group1 must be FrankNStein but found ".$wikiName);
    } else {
      my $name = $m->prop("wikiName");
      #print STDERR "   groupName: $name\n";
      $this->assert_equals("Group2", $name, "member of Group1 must be Group2 but found ".$name);
    }
  }

  $group = $this->{auth}->findGroup(wikiName => "Group2");

  #print STDERR "### Group2:\n";

  $it = $group->eachMember();
  while ($it->hasNext) {
    my $m = $it->next();
    my $name;
    if ($m->isa("Foswiki::PluggableAuth::User")) {
      my $wikiName = $m->prop("wikiName");
      $this->assert_equals("AliceWeinstein", $wikiName, "member of Group1 must be AliceWeinstein but found ".$wikiName);
    } else {
      $this->assert(0, "Group2 must not have any sub-groups but found ".$m->prop("wikiName"));
    }
  }
}

sub test_allMembers {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "Group1");

  #print STDERR "### Group1:\n";

  my $it = $group->eachMember();
  while ($it->hasNext) {
    my $m = $it->next();
    my $name;
    if ($m->isa("Foswiki::PluggableAuth::User")) {
      my $wikiName = $m->prop("wikiName");
      #print STDERR "   wikiName: $wikiName\n";
      $this->assert($wikiName =~ /^(AliceWeinstein|FrankNStein)$/, "member of Group1 must be FrankNStein and AliceWeinstein but found ".$wikiName);
    } else {
      $this->assert(0, "should return users only");
    }
  }

  $group = $this->{auth}->findGroup(wikiName => "Group2");

  #print STDERR "### Group2:\n";

  $it = $group->eachMember();
  while ($it->hasNext) {
    my $m = $it->next();
    my $name;
    if ($m->isa("Foswiki::PluggableAuth::User")) {
      my $wikiName = $m->prop("wikiName");
      #print STDERR "   wikiName: $wikiName\n";
      $this->assert_equals("AliceWeinstein", $wikiName, "member of Group2 must be AliceWeinstein but found ".$wikiName);
    } else {
      $this->assert(0, "should return users only");
    }
  }
}

sub test_eachMember_disabled {
  my $this = shift;

  my $group1 = $this->{auth}->findGroup(wikiName => "Group1");
  my $group2 = $this->{auth}->findGroup(wikiName => "Group2");

  #print STDERR "membership\n";
  #$this->{auth}->_dumpMembers();

  #print STDERR "membership flat\n";
  #$this->{auth}->_dumpMembersFlat();

  my $it = $group1->eachMember();
  my @members = $it->all;

  #print STDERR "before members=".join(", ", sort map {$_->prop("id")} @members)."\n";
  $this->assert_equals(2, scalar(@members), "Group1 should have two members");

  #print STDERR "... disabling group2\n";
  $group2->disable;

  #print STDERR "after membership flat\n";
  #$this->{auth}->_dumpMembersFlat();

  $it->reset;
  @members = $it->all;

  #print STDERR "after members=".join(", ", sort map {$_->prop("id")} @members)."\n";
  $this->assert_equals(1, scalar(@members), "Group1 should only have one member after Group2 has been disabled");

  $group2->enable;
  my $user = $this->{auth}->findUser(wikiName => "FrankNStein");
  $this->assert($user, "user not found");

  $it->reset;
  @members = $it->all;
  $this->assert_equals(2, scalar(@members), "Group1 should have two members again");

  $user->disable;
  $it->reset;
  @members = $it->all;
  $this->assert_equals(1, scalar(@members), "Group1 should have only one member left after one user was disabled");

  $user->enable;
}

sub test_isMemberOf {
  my $this = shift;

  my $group1 = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert($group1, "Group1 not found");

  my $group2 = $this->{auth}->findGroup(wikiName => "Group2");
  $this->assert($group2, "Group2 not found");

  my $user1 = $this->{auth}->findUser(loginName => "frank");
  $this->assert($user1, "frank not found");

  my $user2 = $this->{auth}->findUser(loginName => "alice");
  $this->assert($user2, "alice not found");

  # print STDERR "### members\n";
  # $this->{auth}->_dumpMembers();
  #
  # print STDERR "### members (flat)\n";
  # $this->{auth}->_dumpMembersFlat();

  $this->assert_equals(1, $user1->isMemberOf($group1), "frank not a member of Group1?");
  $this->assert_equals(0, $user1->isMemberOf($group2), "frank is a member of Group2?");

  $this->assert_equals(0, $user2->isMemberOf($group1, 0), "alice not a direct member of Group1?");
  $this->assert_equals(1, $user2->isMemberOf($group1, 1), "alice not an indirect member of Group1?");
  $this->assert_equals(1, $user2->isMemberOf($group2), "alice not a member of Group2?");
}

sub test_cloneGroup {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "Group1");
  $this->assert_group($group);
  #print STDERR "orig - ".dump($group)."\n";

  my $clone = $group->clone();
  $this->assert_group($clone);
  #print STDERR "clone=".dump($clone)."\n";

  $this->assert($group->equals($clone), "group clone is not identical");
}

sub test_isEmpty {
  my $this = shift;

  my $group = $this->{auth}->findGroup(wikiName => "NobodyGroup");
  $this->assert_group($group);
  $this->assert_equals(1, $group->isEmpty, "NobodyGroup should be empty");

  $group = $this->{auth}->findGroup(wikiName => "BaseGroup");
  $this->assert_group($group);

  $this->assert_equals(0, $group->isEmpty, "BaseGroup should NOT be empty");
}

1;
