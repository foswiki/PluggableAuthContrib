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

package Foswiki::PluggableAuth::Provider::Topic;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Topic

TODO

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::Time ();
use Foswiki::Plugins ();
use Foswiki::Plugins::TopicTitlePlugin();
use Error qw(:try);

#use Data::Dump qw(dump);

use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

sub finish {
  my $this = shift;

  $this->SUPER::finish;

  undef $this->{_htpasswd};
  undef $this->{_passwordManager};
}

sub refresh {
  my ($this, $debug) = @_;

  $this->{_debug} = $debug;
  $this->writeDebug("called refresh");
  $this->cacheUsers;
  $this->cacheGroups;

  # finally 
  return $this->SUPER::refresh();
}

sub deleteUser {
  my ($this, $user) = @_;

  $this->SUPER::deleteUser($user);
  $this->htPasswd->deletePassword($user->prop("id"));
}

sub deleteAll {
  my $this = shift;

  my $res = $this->SUPER::deleteAll;
  undef $this->{_usersCached};
  undef $this->{_groupsCached};

  return $res;
}

sub afterSaveHandler {
  my ($this, $text, $topic, $web, $error, $meta) = @_;

  return if $web ne $Foswiki::cfg{UsersWebName};

  $this->SUPER::afterSaveHandler($text, $topic, $web, $error, $meta);

  try {
    my $group = $this->auth->findGroup(wikiName => $topic);

    if ($group && ($group->prop("pid") eq $this->prop("id") || $topic eq $Foswiki::cfg{SuperAdminGroup})) {
      # check for old group
      $this->writeDebug("... updating group (pid=".$group->prop("pid").")");
      my $groupInfo = $this->extractGroupInfo($web, $topic, $meta);
      $this->cacheGroupMembers($group, $groupInfo);
      $this->updateGroup($group, $groupInfo);
    } else {

      # check for a new group
      if ($topic =~ /Group$/ && $meta->get("PREFERENCE", "GROUP")) {
        $this->writeDebug("... found a new group");
        my $groupInfo = $this->extractGroupInfo($web, $topic, $meta);
        my $group = $this->cacheGroup($groupInfo);
        $this->cacheGroupMembers($group, $groupInfo);
      } else {
        $this->writeDebug("... not a group");
      }
    }
  } catch Error with {
    my $error = shift;
    throw Error::Simple($error);
  };

  return;
}

sub afterRenameHandler {
  my ($this, $oldWeb, $oldTopic, $oldAttachment, $newWeb, $newTopic, $newAttachment) = @_;

  return if $oldWeb ne $Foswiki::cfg{UsersWebName};
  $this->SUPER::afterRenameHandler($oldWeb, $oldTopic, $oldAttachment, $newWeb, $newTopic, $newAttachment);

  try {
    my $group = $this->auth->findGroup(wikiName => $oldTopic);

    if ($group && $group->prop("pid") eq $this->prop("id")) {
      if ($newWeb eq $Foswiki::cfg{TrashWebName}) {
        $group->delete();
      } elsif ($newWeb eq $Foswiki::cfg{UsersWebName}) {
        $group->update("wikiName" => $newTopic);
      }
    }
  } catch Error with {
    my $error = shift;
    throw Error::Simple($error);
  };

  return;
}

sub extractGroupInfo {
  my ($this, $web, $topic, $meta) = @_;

  ($meta) = Foswiki::Func::readTopic($web, $topic) unless defined $meta;

  my $topicTitle = Foswiki::Func::getTopicTitle($web, $topic, undef, $meta);
  my $members = $meta->get("PREFERENCE", "GROUP");

  $members = defined $members ? $members->{value} : '';
  my %members = map {$_ => 1} split(/\s*,\s*/, $members);

  my %groupInfo = ();

  $groupInfo{id} = $this->generateID($topic);
  $groupInfo{wikiName} = $topic;
  $groupInfo{displayName} = $topicTitle;
  $groupInfo{web} = $web;
  $groupInfo{_members} = [keys %members];

  return \%groupInfo;
}

sub extractUserInfo {
  my ($this, $wikiName, $loginName, $meta) = @_;

  my $userInfo = $this->extractUserInfoFromTopic(
    wikiName => $wikiName, 
    loginName => $loginName, 
    meta => $meta
  );

  $userInfo->{email} =  $this->getEmailFromSource($wikiName, $loginName);

  return $userInfo;
}

sub cacheUsers {
  my ($this, $forced) = @_;

  return $this->{_usersCached} if !$forced && $this->{_usersCached};

  $this->writeDebug("called cacheUsers()");

  my $usersWeb = $Foswiki::cfg{UsersWebName};
  my $usersTopic = $Foswiki::cfg{UsersTopicName};

  $this->writeDebug("... usersWeb=$usersWeb, usersTopic=$usersTopic");

  my $count = 0;
  my %seen = ();

  if (Foswiki::Func::topicExists($usersWeb, $usersTopic)) {
  
    my ($meta, $text) = Foswiki::Func::readTopic($usersWeb, $usersTopic);
    #$this->writeDebug("usersText=$text");

    while ($text =~ /^\s*\* (?:$Foswiki::regex{webNameRegex}\.)?($Foswiki::regex{wikiWordRegex})\s*(?:-\s*(\S+)\s*)?-\s*(.*?)\s*$/gm) {
      $seen{$1} = 1;
      $count ++ if $this->cacheUser($1, $2, $3);
    }
  } else {
    #print STDERR "cannot find users topic at $usersWeb.$usersTopic\n";
  }

  $this->writeDebug("$count user(s) cached");

  $this->{_usersCached} = $count;;
  return $count;
}

sub cacheUser {
  my ($this, $wikiName, $loginName, $date) = @_;

  $loginName ||= $wikiName;
  $this->writeDebug("called cacheUser($wikiName, $loginName)");

  unless ($this->auth->isValidWikiName($wikiName)) {
    $this->writeDebug("... not a valid wikiName");
    return;
  }

  unless ($this->auth->isValidLoginName($loginName)) {
    $this->writeDebug("... not a valid loginName");
    return;
  }

  my $userInfo = $this->extractUserInfo($wikiName, $loginName);
  $this->writeDebug("... wikiName=$wikiName, loginName=$loginName, date=".($date//'undef').", email=".($userInfo->{email}//'undef'));

  my $user = $this->auth->findUser(loginName => $loginName);

  if (defined $user) {
    my $provider = $user->getProvider();
    if ($provider->prop("id") ne $this->prop("id")) {
      $this->writeDebug("... not updating user from different provider ".$provider->prop("id"));
      return;
    }

    $this->writeDebug("... updating user $loginName");
    $this->updateUser($user, $userInfo);
    return $user;
  }

  unless (defined $userInfo->{email}) {
    $this->writeDebug("... couldn't get email for user $wikiName/$loginName");
    return; 
  }

  $this->writeDebug("... adding user $loginName");

  $userInfo->{registrationDate} = Foswiki::Time::parseTime($date) if $date && $date !~ /^\d+$/;
  $user = $this->addUser(%$userInfo);

  my ($hash, $encoding) = $this->getPasswordFromSource($loginName);
  #print STDERR "... caching hash=$hash, encoding=$encoding for $wikiName\n";

  $user->getProvider->savePassword(
    uid => $user->prop("id"),
    password => $hash, 
    encoding => $encoding,
    realm => "",
  ) if defined $hash;

  return $user,
}

sub getEmailFromSource {
  my ($this, $wikiName, $loginName, $emailSource) = @_;

  $emailSource ||= $this->prop("EmailSource");
  $emailSource ||= 'htpasswd';

  $this->writeDebug("called getEmailFromSource $emailSource");

  if ($emailSource eq 'htpasswd') {
    my (undef, $entry) = $this->htPasswd->getPassword($loginName);
    return $entry->{emails};
  }

  if ($emailSource eq 'topic') {
    my ($meta) = Foswiki::Func::readTopic($Foswiki::cfg{UsersWebName}, $wikiName);
    my $email = $meta->get('FIELD', $this->prop("EmailAttribute"));
    $email = $email->{value} if defined $email;
    return $email if defined $email && $email ne '';
    return $this->getEmailFromSource($wikiName, $loginName, 'htpasswd'); # fallback
  }

  if ($emailSource eq 'password manager') {
    my @emails = $this->getPasswordManager->getEmails($loginName);
    return join("; ", @emails);
  }

  return;
}

sub getPasswordFromSource {
  my ($this, $loginName) = @_;

  my (undef, $entry) = $this->htPasswd->getPassword($loginName);
  return ($entry->{pass}, $entry->{enc}) if defined $entry;
  return (undef, undef);
}

sub htPasswd {
  my $this = shift;

  unless (defined $this->{_htpasswd}) {
    require Foswiki::PluggableAuth::HtPasswd;
    $this->{_htpasswd} = Foswiki::PluggableAuth::HtPasswd->new();
  }

  return $this->{_htpasswd};
}

sub getPasswordManager {
  my $this = shift;

  unless (defined $this->{_passwordManager}) {

    my $implPasswordManager = $Foswiki::cfg{PasswordManager};
    $implPasswordManager = 'Foswiki::Users::Password'
      if ($implPasswordManager eq 'none');

    eval "require $implPasswordManager";
    die $@ if $@;

    $this->{_passwordManager} = $implPasswordManager->new($Foswiki::Plugins::SESSION);
  }

  return $this->{_passwordManager};
}

sub setEmail {
  my ($this, $user, $email) = @_;

  $this->SUPER::setEmail($user, $email);
  $this->htPasswd->setEmail($user, $email);

  return 1;
}

sub savePassword {
  my ($this, %params) = @_;

  return 0 unless $this->SUPER::savePassword(%params);
  $this->htPasswd->savePassword(%params);

  return 1;
}

sub cacheGroups {
  my ($this, $forced) = @_;

  return $this->{_groupsCached} if !$forced && $this->{_groupsCached};

  $this->writeDebug("called cacheGroups()");
  my $origUser = $this->auth->switchToRegistrationAgent();

  # collect all topic groups 
  my $groupInfos = $this->findGroups();
  throw Error::Simple("no groups found there should be at least one") unless scalar(keys %$groupInfos);
  #print STDERR "groupsInfo=".dump($groupInfos)."\n";

  # first, delete database groups unless they still exist
  my $groupIt = $this->auth->eachGroup(pid => $this->prop("id"));
  while ($groupIt->hasNext) {
    my $group = $groupIt->next;
    $this->writeDebug("checking group ".$group->prop("id"));

    my $groupInfo = $groupInfos->{$group->prop("id")};
    if ($groupInfo) {
      $this->writeDebug("... group $groupInfo->{id} still exists: ".$group->stringify);
    } else {
      $this->writeDebug("... old group found ... deleting ".$group->prop("id"));
      $group->delete;
    }
  }

  my @groups = ();

  # second, create all groups
  foreach my $groupInfo (values %$groupInfos) {
    my $group = $this->cacheGroup($groupInfo);
    next unless $group;
    $this->updateGroup($group, $groupInfo) if $group->prop("pid") eq $this->prop("id");
    push @groups, $group;
  }

  # then, cache all members
  foreach my $group (@groups) {
    $this->cacheGroupMembers($group, $groupInfos->{$group->prop("id")});
  }

  # special case for AdminGroup
  my $baseProvider = $this->auth->getProvider("Base");
  my $adminGroup = $baseProvider->getAdminGroup;
  my $groupInfo = $groupInfos->{$adminGroup->prop("id")};
  $this->cacheGroupMembers($adminGroup, $groupInfo);

  my $adminUser = $baseProvider->getAdminUser;
  $adminGroup->addMember($adminUser);

  $origUser->switch();

  return $this->{_groupsCached} = scalar(@groups);
}

sub cacheGroup {
  my ($this, $groupInfo) = @_;

  $this->writeDebug("called cacheGroup($groupInfo->{wikiName})");

  my $group = $this->auth->findGroup(id => $groupInfo->{id});

  if (defined $group) {
    # skip groups that this provider doesn't manage
    return unless $this->prop("id") eq $group->prop("pid");

    $this->writeDebug("... alreay exists, skipping");
  } else {

    $this->writeDebug("... caching id=$groupInfo->{id}");

    $group = $this->addGroup(
      wikiName => $groupInfo->{wikiName},
      displayName => $groupInfo->{displayName},
      id => $groupInfo->{id},
    );
  }

  return $group;
}

sub cacheGroupMembers {
  my ($this, $group, $groupInfo) = @_;

  return $this->setMembersOfGroup($groupInfo->{_members}, $group);
}

sub findGroups {
  my ($this, $web, $groupInfos) = @_;

  $this->writeDebug("called findGroups()");
  $web //= $Foswiki::cfg{UsersWebName};

  my $matches = Foswiki::Func::query(
    "name=~'.*Group\$' AND preferences[name='GROUP']",
    undef,
    {
      web => $web,
      files_without_match => 1
    }
  );

  $groupInfos //= {};

  while ($matches->hasNext) {
    my $topic;
    ($web, $topic) = Foswiki::Func::normalizeWebTopicName($web, $matches->next);
   
    my $groupInfo = $this->extractGroupInfo($web, $topic);
    $groupInfos->{$groupInfo->{id}} = $groupInfo if $groupInfo;
  }

  return $groupInfos;
}

sub handlesLogin {
  my ($this, $request, $state) = @_;
  
  return 0 unless $this->SUPER::handlesLogin($request, $state);

  $this->writeDebug("called handlesLogin");

  my $authName = $request->param("username");
  return 0 unless defined $authName;

  $this->writeDebug("... authName=$authName");

  my $user = $this->findAuthName($authName);

  return 0 unless defined $user;
  return 0 unless $user->isEnabled;
  
  return $this->handles($user);
}

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called handlesLogin");

  my $authName = $request->param("username");
  my $password = $request->param("password");
  return unless defined $authName && $password;

  my $user = $this->findAuthName($authName);
  return unless defined $user;

  throw Error::Simple($this->auth->maketext("Sorry, account is disabled (3)")) unless $user->isEnabled;

  if ($this->checkPassword($user, $password)) {

    # sync user topic on login
    if ($this->prop("SyncOnLogin")) {
      my $userInfo = $this->extractUserInfo($user->prop("wikiName"), $user->prop("loginName"));
      $user = $this->updateUser($user, $userInfo) if $userInfo;
    }

    return $user;
  }

  $this->writeDebug("... failed");
  return;
}

sub checkGroupAccess {
  my ($this, $type, $group, $user) = @_;

  return Foswiki::Func::checkAccessPermission($type, $user->prop("id"), undef, $group->prop("wikiName"), $Foswiki::cfg{UsersWebName});
}

sub generateID {
  my ($this, $name) = @_;

  my $id = $name;

  # use bytes to ignore character encoding
  use bytes;
  $id =~ s/([^a-zA-Z0-9_])/'_'.sprintf('%02x', ord($1))/ge;
  no bytes;

  return $id;
}

sub canChangeMembership {
  my ($this, $user, $group) = @_;

  return 0 if $group->prop("id") eq $this->getProviderGroupName();
  return 1;
}

sub canChangeGroupName {
  my ($this, $user, $group) = @_;

  return Foswiki::Func::checkAccessPermission("CHANGE", $user->prop("id"), undef, $group->prop("wikiName"), $Foswiki::cfg{UsersWebName});
}

sub canRegisterUser {
  # SMELL: bulk registration is done via manage, still this sux
  return $Foswiki::cfg{Register}{EnableNewUserRegistration} || Foswiki::Func::getContext()->{manage};
}

sub canCreateGroup {
  return 1;
}

sub canSetEmail {
  my ($this, $user) = @_;

  return 0 if !defined($user) || !$this->handles($user);
  return 1;
}

sub canSetPassword {
  my ($this, $user) = @_;

  return 0 if defined($user) && !$this->handles($user);
  return 1;
}

sub removeMemberFromGroup {
  my ($this, $obj, $group) = @_;

  my $res = $this->SUPER::removeMemberFromGroup($obj, $group);
  return unless $res;

  return $this->updateGroupTopic($group, [$obj], 0);
}

sub addMemberToGroup {
  my ($this, $obj, $group) = @_;

  my $res = $this->SUPER::addMemberToGroup($obj, $group);
  return unless $res;

  return $this->updateGroupTopic($group, [$obj], 1);
}

sub setMembersOfGroup {
  my ($this, $members, $group) = @_;

  my $res = $this->SUPER::setMembersOfGroup($members, $group);
  return unless $res;

  return $this->updateGroupTopic($group, $members, 2);
}

sub updateGroupTopic {
  my ($this, $group, $members, $mode) = @_;

  my ($web, $topic) = $group->getTopic();
  return if $this->getProviderGroupName() eq $topic;

  #throw Error::Simple("topic $web.$topic for Group $topic does not exist") unless Foswiki::Func::topicExists($web, $topic);

  $this->auth->blockAllEvents();

  my $meta = $group->readTopic();
  my $origUser = $this->auth->switchToRegistrationAgent();

  Foswiki::Func::setTopicTitle($web, $topic, $group->prop("displayName"), $meta);

  if ($members) {

    my $field = $meta->get('PREFERENCE', 'GROUP') // {
      type  => 'Set',
      name  => 'GROUP',
      title => 'GROUP',
      value => ''
    };

    my $oldVal = $field->{value};

    my %members = $mode == 2 ? () : map {my $tmp = $_; $tmp =~ s/^.\.//; $tmp => 1;} split (/\s*,\s/, $field->{value});

    foreach my $item (@$members) {
      my $name = ref($item) ? $item->prop("wikiName") : $item;
      $name =~ s/^.*?\.//;

      if ($mode > 0) {
        $members{$name} = 1;
      } else {
        delete $members{$name};
      }
    }

    my $newVal = join(", ", sort keys %members);

    if ($oldVal ne $newVal) {
      $field->{value} = $newVal;
      $meta->putKeyed("PREFERENCE", $field);
      $meta->save();
    }
  }

  $origUser->switch();

  $this->auth->unblockAllEvents();

  #throw Error::Simple("topic $web.$topic for Group $topic does not exist after updating it") unless Foswiki::Func::topicExists($web, $topic);

  return 1;
}

1;
