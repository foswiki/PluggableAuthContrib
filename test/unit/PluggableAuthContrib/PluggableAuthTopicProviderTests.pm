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

package PluggableAuthTopicProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::Meta();
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Topic ();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  $Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Enabled} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Topic}{EmailSource} = 'htpasswd';

  # TODO: create tests for EmailSource = topic and passwordmanager

  $this->{provider} = $this->{auth}->getProvider("Topic");
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Topic"));
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

sub test_cacheUsers {
  my $this = shift;

  $this->createLotsOfUsers();

  my $count = $this->{provider}->cacheUsers();
  $this->assert_equals(102, $count, "should be 102 users in cache, but found ".($count//'undef'));

  my $count2 = $this->{provider}->cacheUsers();
  $this->assert_equals($count, $count2, "should be 102 users again, but found ".($count2//'undef'));

  my $it = $this->{provider}->eachUser();
  my @all = $it->all;
  $this->assert_equals(102, $count, "should be 102 iterating users, but found ".scalar(@all));

  foreach my $user (@all) {
    $this->assert(Foswiki::Func::topicExists($this->{test_users_web}, $user->prop("wikiName")), "no topic found for user ".$user->stringify);

    my $email = $user->prop("email");
    $this->assert($email, "no email");
    next unless $email =~ /^test\d+\@foo.bar$/;

    my $res = $user->checkPassword($email);
    $this->assert($res);
  }
}

sub test_cacheGroups {
  my $this = shift;

  $this->{provider}->deleteAll;
  $this->{auth}->{_suppressRecompute} = 1;
  $this->createLotsOfUsers();
  $this->createLotsOfGroups();

  my $res;

  $this->{provider}->cacheUsers();
  $res = $this->{provider}->cacheGroups();
  $this->assert($res);

  $this->{auth}->{_suppressRecompute} = 0;
  $this->{auth}->refresh("Topic");
  
  my @groups = $this->{provider}->eachGroup->all;
  my $count = scalar(@groups);
  $this->assert_equals(100, $count, "should be 100 groups in cache, but found $count");

  $res = $this->{provider}->cacheGroups();
  $this->assert($res);

  @groups = $this->{provider}->eachGroup->all;
  $count = scalar(@groups);

  $this->assert_equals(100, $count, "should still be 100 groups in cache, but found $count");
}

sub test_createGroupTopic {
  my $this = shift;

  my $web = $Foswiki::cfg{UsersWebName};
  my $topic = "TestGroup";

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $meta = Foswiki::Meta->new($this->{session}, $web, $topic, "");
  $meta->putKeyed("PREFERENCE", { 
    name => 'GROUP', 
    title => 'GROUP', 
    value => $user->prop("wikiName")
  });

  $meta->save();

  my $group = $this->{auth}->findGroup(wikiName => $topic);
  $this->assert_group($group);
  $this->assert_equals("TestGroup", $group->prop("wikiName"));

  my @members = $group->eachMember->all;
  $this->assert_equals(1, scalar(@members));

  my @groups = $user->eachGroup->all();
  $this->assert_equals(2, scalar(@groups));

  my $found = 0;
  foreach my $group (@groups) {
    #print STDERR "### group=".$group->prop("wikiName")."\n\n";
    $found = 1 if $group->prop("wikiName") eq 'TestGroup';
  }

  $this->assert($found, "TestGroup not found");
}

sub test_renameGroupTopic {
  my $this = shift;

  my $web = $Foswiki::cfg{UsersWebName};
  my $topic = "TestGroup";

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $meta = Foswiki::Meta->new($this->{session}, $web, $topic, "");
  $meta->putKeyed("PREFERENCE", { 
    name => 'GROUP', 
    title => 'GROUP', 
    value => $user->prop("wikiName")
  });

  $meta->save();

  my $group = $this->{auth}->findGroup(wikiName => "TestGroup");
  $this->assert_group($group);
  $this->assert_equals("TestGroup", $group->prop("wikiName"));

  Foswiki::Func::moveTopic($web, $topic, $web, "NewTestGroup");

  $group = $this->{auth}->findGroup(wikiName => "NewTestGroup");
  $this->assert_group($group);
  $this->assert_equals("NewTestGroup", $group->prop("wikiName"));

  my @members = $group->eachMember->all;
  $this->assert_equals(1, scalar(@members));

  my @groups = $user->eachGroup->all();
  $this->assert_equals(2, scalar(@groups));

  my $found = 0;
  foreach my $group (@groups) {
    #print STDERR "### group=".$group->prop("wikiName")."\n\n";
    $found = 1 if $group->prop("wikiName") eq 'NewTestGroup';
  }

  $this->assert($found, "NewTestGroup not found");
}

sub test_deleteGroupTopic {
  my $this = shift;

  my $web = $Foswiki::cfg{UsersWebName};
  my $topic = "TestGroup";

  my $user = $this->{auth}->findUser(loginName => "frank");
  $this->assert_user($user);

  my $meta = Foswiki::Meta->new($this->{session}, $web, $topic, "");
  $meta->putKeyed("PREFERENCE", { 
    name => 'GROUP', 
    title => 'GROUP', 
    value => $user->prop("wikiName")
  });

  $meta->save();

  Foswiki::Func::moveTopic($web, $topic, $Foswiki::cfg{TrashWebName}, $topic.time());
  my $group = $this->{auth}->findGroup(wikiName => $topic);
  $this->assert_null($group);

  my @groups = $user->eachGroup->all();
  $this->assert_equals(1, scalar(@groups));
}

sub test_setEmail {
  my $this = shift;

  # disable in case you enabled it
  $Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled} = 0;

  $this->createLotsOfUsers;
  my $count = $this->{provider}->cacheUsers();

  my $user = $this->{auth}->findUser(wikiName => "TestUser1");
  $this->assert_user($user);

  my $email = $user->prop("email");
  $this->assert($email);

  #print STDERR "email=$email\n";

  my $res = $user->setEmail('test1@bar.baz');
  $this->assert($res);

  $email = $user->prop("email");
  $this->assert_equals($email, 'test1@bar.baz');
}

sub test_setPassword {
  my $this = shift;

  $this->createLotsOfUsers;
  my $count = $this->{provider}->cacheUsers();

  my $user = $this->{auth}->findUser(wikiName => "TestUser1");
  $this->assert_user($user);

  my $res = $user->setPassword("random_password"); 
  $this->assert($res);

  $res = $user->setPassword("random_password2"); 
  $this->assert($res);

  $res = $user->setPassword("random_password3", "random_password2"); 
  $this->assert($res);

  $res = $user->setPassword("random_password4", "wrong password"); 
  $this->assert(!$res);

  my $hash = $this->{provider}->hashPassword($user, "secret");
  $this->assert($hash);

  $hash = $this->{provider}->hashPassword($user, "random_password");
  $this->assert($hash);
}

sub test_refresh {
  my $this = shift;

  $this->{auth}->{_suppressRecompute} = 1;
  $this->createLotsOfUsers;
  $this->createLotsOfGroups();
  $this->{auth}->{_suppressRecompute} = 0;

  $this->{auth}->refresh("Topic");

  my $provider = $this->{auth}->getProvider("Topic");
  my @users = $provider->eachUser->all;
  #print STDERR "users=".join(", ", sort map {$_->prop("id")} @users)."\n";
  $this->assert_equals(102, scalar(@users), "should have refreshed 100 users but got ".scalar(@users));
}

sub test_deleteAll {
  my $this = shift;

  $this->{auth}->{_suppressRecompute} = 1;
  $this->createLotsOfUsers;
  $this->createLotsOfGroups();
  $this->{auth}->{_suppressRecompute} = 0;

  $this->{auth}->refresh("Topic");

  my $provider = $this->{auth}->getProvider("Topic");
  my @allUsers = $provider->eachUser->all;
  my $count = scalar(@allUsers);
  $this->assert_equals(102, $count, "should be 102 users in provider, but found $count");

  my @allGroups = $provider->eachGroup->all;
  $count = scalar(@allGroups);
  $this->assert_equals(100, $count, "should be 100 groups in provider, but found $count");

  my $res = $provider->deleteAll;
  $this->assert_equals(102, $res, "should have deleted 102 users from provider, but found ".($res//'undef'));

  my $count2 = scalar($provider->eachUser->all);
  $this->assert_equals(0, $count2, "should be no users left in provider, but found $count2");

  my $count3 = scalar($provider->eachGroup->all);
  $this->assert_equals(0, $count3, "should be no group left in provider, but found $count3");

  my @res = $this->{auth}->db->handler->selectrow_array("SELECT COUNT(*) from PluggableAuth_users WHERE pid='Topic'");
  $this->assert_equals(0, $res[0]);

  @res = $this->{auth}->db->handler->selectrow_array("SELECT COUNT(*) from PluggableAuth_groups WHERE pid='Topic'");
  $this->assert_equals(0, $res[0]);

  @res = $this->{auth}->db->handler->selectrow_array("SELECT COUNT(*) from PluggableAuth_group_members INNER JOIN PluggableAuth_users ON PluggableAuth_group_members.mid=PluggableAuth_users.id WHERE PluggableAuth_users.pid='Topic'");
  $this->assert_equals(0, $res[0]);

  @res = $this->{auth}->db->handler->selectrow_array("SELECT COUNT(*) from PluggableAuth_group_members INNER JOIN PluggableAuth_groups ON PluggableAuth_group_members.mid=PluggableAuth_groups.id WHERE PluggableAuth_groups.pid='Topic'");
  $this->assert_equals(0, $res[0]);

  my $stm = "SELECT COUNT(*) from PluggableAuth_group_members WHERE gid IN (".join(", ", map {"'".$_->prop("id")."'"} @allGroups).")";
  @res = $this->{auth}->db->handler->selectrow_array($stm);
  $this->assert_equals(0, $res[0], "should be no group_members left, but got $res[0]");
}

sub test_canSetPassword {
  my $this = shift;

  $this->createLotsOfUsers;
  my $count = $this->{provider}->cacheUsers();

  my $user = $this->{auth}->findUser(wikiName => "TestUser1");

  $this->assert_equals(1, $this->{provider}->canSetPassword($user), "provider cannot set any password");
}

1;
