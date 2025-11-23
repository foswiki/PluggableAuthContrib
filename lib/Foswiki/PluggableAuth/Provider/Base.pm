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

package Foswiki::PluggableAuth::Provider::Base;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Base

This is the provider base provider for all built-in default users and groups part of every Foswiki:

   * <nop>AdminUser
   * <nop>ProjectContributor
   * <nop>RegistrationAgent
   * <nop>WikiGuest
   * <nop>UnknownUser
   * <nop>NobodyGroup
   * <nop>BaseGroup
   * <nop>AdminGroup

Note that the <nop>AdminGroup - being based on topic information - is further managed by Foswiki::PluggableAuth::Provider::Topic.
Any other user and group in this provider remains static in comparison.

=cut

use strict;
use warnings;

use Encode ();
use Digest::MD5 ();
use Crypt::PasswdMD5 ();

use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ObjectMethod refresh($debug)

makes sure all objects managed by this provider are available in the database

=cut

sub refresh {
  my ($this, $debug) = @_;

  $this->{_debug} = $debug;
  $this->writeDebug("called refresh");
  $this->cacheUsers;
  $this->cacheGroups;
}

=begin TML

---++ ObjectMethod cacheUsers()

creates all user objects of this provider

=cut

sub cacheUsers {
  my $this = shift;

  $this->writeDebug("called cacheUsers");

  my $userIt = $this->eachUser();
  while ($userIt->hasNext) {
    my $user = $userIt->next;

    my $oldPic = $user->prop("picture");
    my $newPic = $this->updatePictureOfUser($user);

    if (!$oldPic || $oldPic ne $newPic) {
      $user->update(
        picture => $newPic
      );
    }
  }
}

=begin TML

---++ ObjectMethod cacheGroups()

creates all group objects of this provider

=cut

sub cacheGroups {
  my $this = shift;

  $this->writeDebug("called cacheGroups");

  my $count = 0;

  my $baseGroup = $this->auth->getGroupByID('BaseGroup');
  $this->_deleteMembers($baseGroup);
  foreach my $id (qw(BaseUserMapping_111 BaseUserMapping_222 BaseUserMapping_333 BaseUserMapping_666 BaseUserMapping_999)) {
    my $user = $this->auth->getUserByID($id);
    $this->addMemberToGroup($user, $baseGroup); 
  }

  # Note, AdminGroup is further managed by topic provider
  $this->addMemberToGroup($this->getAdminUser, $this->getAdminGroup);
}

=begin TML

---++ ObjectMethod cacheGroup()

caches an individual group part of this provider

=cut

sub cacheGroup {
  my ($this, %groupInfo) = @_;

  $this->writeDebug("called cacheGroup($groupInfo{id})");
  my $group = $this->auth->findGroup(id => $groupInfo{id});

  if (defined $group) {
    $this->writeDebug("... already exists, skipping");
  } else {
    $group = $this->addGroup(%groupInfo);
  }

  # make sure the topic exists
  $group->createTopic();

  return $group
}

=begin TML

---++ ObjectMethod isAdminGroup($group) -> $boolean

returns true if =$group= is the (one and only) admin group as defined in =$Foswiki::cfg{SuperAdminGroup}=

=cut

sub isAdminGroup {
  my ($this, $group) = @_;

  return $group->prop("id") eq $Foswiki::cfg{SuperAdminGroup} ? 1:0;
}

=begin TML

---++ ObjectMethod getAdminGroup() -> $group

returns the admin group object of type Foswiki::PluggableAuth::Group

=cut

sub getAdminGroup {
  my $this = shift;
 
  return $this->auth->getGroupByID($Foswiki::cfg{SuperAdminGroup});
}

=begin TML

---++ ObjectMethod getAdminUser() -> $user

returns the admin user object of type Foswiki::PluggableAuth::User

=cut

sub getAdminUser {
  my $this = shift;
  
  return $this->auth->getUserByID('BaseUserMapping_333') 
}

=begin TML

---++ ObjectMethod getUnknownUser() -> $user

returns the unknown user object of type Foswiki::PluggableAuth::User

=cut

sub getUnknownUser {
  my $this = shift;
  
  return $this->auth->getUserByID('BaseUserMapping_999') 
}

=begin TML

---++ ObjectMethod canChangeMembership() -> $boolean

returns false for any but the admin group

=cut

sub canChangeMembership {
  my ($this, $user, $group) = @_;

  return 1 if $group->prop("id") eq $Foswiki::cfg{SuperAdminGroup};
  return 0;
}

sub canCreateGroup {
  my ($this, $group) = @_;

  my $id = $group->prop("id");
  return 1 if $id =~ /^(BaseGroup|NobodyGroup|$Foswiki::cfg{SuperAdminGroup})$/;
  return 0;
}


=begin TML

---++ ObjectMethod canCheckPassword($user) -> $boolean

returns false for any but the admin user

=cut

sub canCheckPassword {
  my ($this, $user) = @_;

  return $user->prop("loginName") eq $Foswiki::cfg{AdminUserLogin} ? 1:0;
}

=begin TML

---++ ObjectMethod canSetPassword() -> $boolean

always returns false as none of the users' password can be changed by this provider

=cut

sub canSetPassword {
  return 0;
}

=begin TML

---++ ObjectMethod canSetEmail() -> $boolean

always returns false as none of the users' email can be changed by this provider

=cut

sub canSetEmail {
  return 0;
}

=begin TML

---++ ObjectMethod canDelete() -> $boolean

always returns false as none of the usersemail can be deleted

=cut

sub canDelete {
  return 0;
}

=begin TML

---++ ObjectMethod canRegisterUser() -> $boolean

returns false as this provider cannot register new users

=cut

sub canRegisterUser {
  return 0;
}

=begin TML

---++ ObjectMethod handlesLogin($request, $state) -> $boolean

This method is called by Foswiki::LoginManager::PluggableLogin for any provider
for them to test whether they are responsible for the current login attempt.

request parameters processed by this method:

   * username

=cut

sub handlesLogin {
  my ($this, $request, $state) = @_;

  return 0 unless $this->SUPER::handlesLogin($request, $state);

  $this->writeDebug("called handlesLogin");

  my $authName = $request->param("username");
  return 0 unless defined $authName;

  my $user = $this->findAuthName($authName);

  return 0 unless defined $user;
  return 0 unless $user->isEnabled;
  
  return $this->handles($user);
}

=begin TML

---++ ObjectMethod processLogin($request, $state) -> $user

This is called by Foswiki::LoginManager::PluggableLogin to process a login request.
It returns undef if this provider is not responsible, or the provided password is correct.

request parameters processed by this method:

   * username
   * password

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called handlesLogin");

  my $authName = $request->param("username");
  my $password = $request->param("password");
  return unless defined $authName && $password;

  my $user = $this->findAuthName($authName);

  return $user if $user->isEnabled && $this->checkPassword($user, $password);
  return;
}

=begin TML

---++ ObjectMethod checkGroupAccess($type, $group, $user) -> $boolean

returns true if =$user= may perform an action of the given =$type= on the =$group=.

=cut

sub checkGroupAccess {
  my ($this, $type, $group, $user) = @_;

  return 1 if $type eq 'VIEW';
  return 0 unless $user->isAdmin;
}

=begin TML

---++ ObjectMethod checkPassword($user, $password) -> $boolean

returns true if the =$password= for the given =$user= is correct.
Note that this provider can only check the password of the admin user
as stored in =$Foswiki::cfg{Password}=. Further note that the admin user
should actually be deactivated for security reasons when using Foswiki in
production mode.

=cut

sub checkPassword {
  my ($this, $user, $password) = @_;

  return 0 unless $this->canCheckPassword($user);

  $password = Encode::encode_utf8($password);
  my $hash = $Foswiki::cfg{Password};

  if (length($hash) == 13) {
    return 1 if crypt($password, $hash) eq $hash;
  } elsif (length($hash) == 42) {
    my $salt = substr($hash, 0, 10);
    return 1
      if ($salt . Digest::MD5::md5_hex($salt . $password) eq $hash);
  } else {
    my $salt = substr($hash, 0, 14);
    return 1
      if (Crypt::PasswdMD5::apache_md5_crypt($password, $salt) eq $hash);
  }

  return 0;
}

=begin TML

---++ ObjectMethod removeMemberFromGroup($obj, $group) -> $boolean

deletages group maintenance to Topic provider for AdminGroup

=cut

sub removeMemberFromGroup {
  my ($this, $obj, $group) = @_;

  return $this->auth->getProvider("Topic")->removeMemberFromGroup($obj, $group)
    if $group->prop("id") eq $Foswiki::cfg{SuperAdminGroup};

  return $this->SUPER::removeMemberFromGroup($obj, $group);
}

=begin TML

---++ ObjectMethod setMembersOfGroup($members, $group) -> $boolean

deletages group maintenance to Topic provider for AdminGroup

=cut

sub setMembersOfGroup {
  my ($this, $members, $group) = @_;

  return $this->auth->getProvider("Topic")->setMembersOfGroup($members, $group)
    if $group->prop("id") eq $Foswiki::cfg{SuperAdminGroup};

  return $this->SUPER::setMembersOfGroup($members, $group);
}

=begin TML

---++ ObjectMethod addMemberToGroup($obj, $group) -> $boolean

deletages group maintenance to Topic provider for AdminGroup

=cut

sub addMemberToGroup {
  my ($this, $obj, $group) = @_;

  return $this->auth->getProvider("Topic")->addMemberToGroup($obj, $group)
    if $group->prop("id") eq $Foswiki::cfg{SuperAdminGroup};

  return $this->SUPER::addMemberToGroup($obj, $group);
}

=begin TML

---++ ObjectMethod afterSaveHandler($text, $topic, $web, $error, $meta) 

deletages group maintenance to Topic provider for AdminGroup

=cut

sub afterSaveHandler {
  my ($this, $text, $topic, $web, $error, $meta) = @_;

  return if $web ne $Foswiki::cfg{UsersWebName};

  return $this->auth->getProvider("Topic")->afterSaveHandler($text, $topic, $web, $error, $meta)
    if $topic eq $Foswiki::cfg{SuperAdminGroup};

  return $this->SUPER::afterSaveHandler($text, $topic, $web, $error, $meta);
}

1;
