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

package Foswiki::PluggableAuth::Provider;

=begin TML

---+ package Foswiki::PluggableAuth::Provider

TODO

=cut

use strict;
use warnings;

use Foswiki ();
use Foswiki::LoginManager ();
use Foswiki::Contrib::CacheContrib ();
use Encode ();
use Foswiki::Func ();
use Error qw(:try);
use Net::CIDR ();
use Email::Valid ();
use Fcntl qw(SEEK_END );
#use Data::Dump qw(dump);

BEGIN {
    # Backwards compatibility for Foswiki 2.1.x
    unless ( Foswiki->can('generateRandomChars') ) {
        no warnings 'redefine'; ## no critic
        *Foswiki::generateRandomChars = \&_generateRandomChars;
        use warnings 'redefine';
    }
}

=begin TML

---++ ClassMethod new($id, $props) -> $this

constructor

=cut

sub new {
  my ($class, $id, $props) = @_;

  #$this->writeDebug("called new(). params=".dump(\%params));

  my $this = bless ({
    _id => $id,
    _props => $props,
  }, $class);

  return $this;
}

sub DESTROY {
  my $this = shift;

  $this->finish;
}

sub finish {
  my $this = shift;

  undef $this->{_id};
  undef $this->{_props};
  undef $this->{_debug};
  undef $this->{_json};
}

sub init {
  my $this = shift;

  $this->{_debug} = $this->prop("Debug") || $Foswiki::cfg{PluggableAuth}{Debug};

  return 1;
}

=begin TML

---++ ObjectMethod json() -> $json

retunrs a JSON object

=cut

sub json {
  my $this = shift;

  $this->{_json} = JSON->new() unless $this->{_json};
  return $this->{_json};
}

sub auth {
  #my $this = shift;
  return Foswiki::PluggableAuth->new();
}

sub db {
  my $this = shift;

  return $this->auth->db();
}

sub prop {
  my ($this, $key, $val) = @_;

  #$this->writeDebug("called prop($key, ".($val//'undef').")");

  return $this->{_id} if $key eq 'id';

  $this->{_props}{$key} = $val if defined $val;
  return $this->{_props}{$key};
}

sub props {
  my ($this, $props) = @_;

  $this->{_props} = $props if defined $props;
  return $this->{_props};
}

sub stringify {
  return shift->prop("id");
}

sub failure {
  my ($this, $state, $val) = @_;

  my $key = "_".$this->prop("id")."_failed";
  $state->{$key} = $val if defined $val;
  return $state->{$key};
}

sub beforeSaveHandler {
  # my ($this, $text, $topic, $web, $meta) = @_;
}

sub afterRenameHandler {
  my ($this, $oldWeb, $oldTopic, $oldAttachment, $newWeb, $newTopic, $newAttachment) = @_;

  $this->writeDebug("afterRenameHandler triggered by oldTopic=$oldWeb.$oldTopic, newTopic=$newWeb.$newTopic, oldAttachment=".($oldAttachment//'undef').", newAttachment=".($newAttachment//'undef'));

  return if $oldWeb ne $Foswiki::cfg{UsersWebName};

  # TODO: deal with rename user topic -> rewrite wikiName
  my $user = $this->findUser(wikiName => $oldTopic);
  return unless defined $user;

  unless ($user->isEnabled) {
    $this->writeDebug("user is disabled");
    return;
  }

  $this->writeDebug("... updating user (pid=".$user->prop("pid").")");

  my $userInfo = $this->extractUserInfoFromTopic(user => $user);
  $this->updateUser($user, $userInfo, 1) if defined $userInfo;


  return;
}

sub afterSaveHandler {
  my ($this, $text, $topic, $web, $error, $meta) = @_;

  return if $web ne $Foswiki::cfg{UsersWebName};

  $this->writeDebug("afterSaveHandler triggered by $web.$topic");

  my $user = $this->findUser(wikiName => $topic);
  unless (defined $user) {
    $this->writeDebug("user $topic not found in ".$this->prop("id"));
    return;
  }

  unless ($user->isEnabled) {
    $this->writeDebug("user is disabled");
    return;
  }

  $this->writeDebug("... updating a user of pid=".$user->prop("pid"));

  my $userInfo = $this->extractUserInfoFromTopic(meta => $meta, user => $user);
  $this->updateUser($user, $userInfo, 1) if defined $userInfo;

  return;
}

sub extractUserInfoFromTopic {
  my ($this, %params) = @_;

  my $user = $params{user};

  my %userInfo = ();

  $userInfo{wikiName} = $params{wikiName} if $params{wikiName};
  $userInfo{wikiName} = $user->prop("wikiName") if !$userInfo{wikiName} && $user;

  $userInfo{loginName} = $params{loginName} if $params{loginName};
  $userInfo{loginName} = $user->prop("loginName") if !$userInfo{loginName} && $user;

  $userInfo{pid} = $user->prop("pid") if $user;
  $userInfo{pid} = $this->prop("id") unless $userInfo{pid};

  #$this->writeDebug("called extractUserInfoFromTopic($userInfo{wikiName}, $userInfo{loginName})");

  my $meta = $params{meta};
  ($meta) = Foswiki::Func::readTopic($Foswiki::cfg{UsersWebName}, $userInfo{wikiName}) unless defined $meta;

  if (defined $meta) {
    my $topicProvider = $this->auth->getProvider("Topic");
    foreach my $key (qw(firstName middleName lastName displayName initials)) {  # not email
      my $name = $topicProvider->prop(ucfirst($key).'Attribute');
      my $field = $meta->get('FIELD', $name);
      my $val = defined $field ? $field->{value} : undef;
      $userInfo{$key} = $val if defined $val;
    }

    if (Foswiki::Func::getContext()->{TopicTitlePluginEnabled}) {
      $userInfo{displayName} ||= Foswiki::Func::getTopicTitle($Foswiki::cfg{UsersWebName}, $userInfo{wikiName}, undef, $meta);
    }

    $userInfo{initials} ||= $user->prop("initials") if $user;
    $userInfo{initials} ||= Foswiki::PluggableAuth::extractInitials($userInfo{displayName}) if defined $userInfo{displayName};
    $userInfo{initials} ||= Foswiki::PluggableAuth::extractInitials(($userInfo{firstName}||'') . " ". ($userInfo{middleName} ||'') . " " . ($userInfo{lastName}||''));
    $userInfo{initials} ||= Foswiki::PluggableAuth::extractInitials(Foswiki::Func::spaceOutWikiWord($userInfo{wikiName}));
  }

  my ($firstName, $lastName) = Foswiki::PluggableAuth::extractNames($userInfo{wikiName});
  $userInfo{firstName} ||= $user->prop("firstName") if $user;
  $userInfo{firstName} ||= $firstName;
  $userInfo{lastName} ||= $user->prop("lastName") if $user;
  $userInfo{lastName} ||= $lastName;

  #print STDERR "userInfo=".dump(\%userInfo)."\n";
  return \%userInfo;
}

sub updateUserTopic {
  my ($this, $user) = @_;

  $this->writeDebug("called updateUserTopic");

  my ($web, $topic) = $user->getTopic();
  my $meta = $user->readTopic();

  my $mustSave = 0;
  my $topicProvider = $this->auth->getProvider("Topic");
  foreach my $key (qw(displayName firstName middleName lastName initials)) { # not email
    my $name = $topicProvider->prop(ucfirst($key).'Attribute');
    my $field = $meta->get('FIELD', $name);
    next unless $field;

    my $fieldVal = $field->{value};
    my $propVal = $user->prop($key);

    next unless defined $propVal;
    next if $fieldVal eq $propVal;

    $field->{value}  = $propVal;
    $mustSave = 1;
  }

  if ($mustSave) {
    $this->auth->blockAllEvents;
    $meta->save(
      dontlog => 1,
      minor => 1,
    );
    $this->auth->unblockAllEvents;
  }

  return $mustSave;
}

sub updateGroupTopic {
  #my ($this, $group) = @_;

  return 0;  
}

sub eachGroup {
  my $this = shift;

  return $this->auth->eachGroup(pid => $this->prop("id"), enabled => 1);
}

sub eachUser {
  my $this = shift;

  return $this->auth->eachUser(pid => $this->prop("id"), enabled => 1);
}

sub handles {
  my ($this, $obj) = @_;

  return 0 unless defined $obj;
  my $pid = $obj->prop("pid") // '';
  return ($pid eq $this->prop("id")) ? 1:0;
}

sub updateUser {
  my ($this, $user, $userInfo, $forceUpdate) = @_;

  $this->writeDebug("called updateUser ".($user?$user->stringify:'undef'));
  $forceUpdate //= 0;

  #$this->writeDebug("forceUpdate=$forceUpdate");
  #$this->writeDebug("userInfo=".dump($userInfo));

  return unless defined $user;
  # just to make extra sure
  if ($user->prop("pid") ne $this->prop("id")) { 
    $this->writeDebug("... not updating user provided by ".$user->prop("pid")." with provider ".$this->prop("id"));
    return;
  }

  $userInfo->{picture} = $this->updatePictureOfUser($user, $userInfo->{picture});

  my %updates = ();

  foreach my $key (qw(email firstName middleName lastName displayName initials picture enabled)) {
    my $newVal = $userInfo->{$key};
    my $oldVal = $user->prop($key);

    next unless defined $newVal;

    #$this->writeDebug("... key=$key, oldVal='".($oldVal//'undef')."', newVal='".($newVal//'undef')."'");

    my $doUpdate = $forceUpdate;
    $doUpdate = 1 if !defined($oldVal) || $oldVal ne $newVal;

    if ($doUpdate) {
      $this->writeDebug("... updating $key=$newVal");
      $updates{$key} = $newVal;
    }
  }

  $this->auth->blockAllEvents;
  $user->createTopic;
  $this->auth->unblockAllEvents;

  $user->update(%updates) if scalar(keys %updates);

  return $user;
}

sub updatePictureOfUser {
  my ($this, $user, $url) = @_;

  #$this->writeDebug("called updatePictureOfUser(".($url//'undef').")");
  return unless $Foswiki::cfg{PluggableAuth}{CreateUserTopics};

  my $meta = $user->readTopic();
  my ($web, $topic) = $user->getTopic();
  return _getNobodyLink() unless $meta;

  my $baseFilename;
  my $tempFile;

  if ($url) {
    $url = URI->new($url) unless ref($url);

    my $res = $this->auth->getUserAgent->get($url);
    if ($res->is_success) {
      $this->writeDebug("... found");
      my $contentType = $res->header('Content-Type');

      foreach my $segment (reverse $url->path_segments) {
        if ($segment ne '') {
          $baseFilename = $segment;
          $baseFilename =~ s/%([\da-f]{2})/chr(hex($1))/gei;

          # SMELL: just covering a few
          $baseFilename .= ".jpeg" if $baseFilename !~ /\.jpe?g$/ && $contentType eq 'image/jpeg';
          $baseFilename .= ".gif" if $baseFilename !~ /\.gif$/ && $contentType eq 'image/gif';
          $baseFilename .= ".svg" if $baseFilename !~ /\.svg$/ && $contentType eq 'image/svg+xml';
          $baseFilename .= ".png" if $baseFilename !~ /\.png$/ && $contentType eq 'image/png';
          $baseFilename .= ".tiff" if $baseFilename !~ /\.tiff$/ && $contentType eq 'image/tiff';
          $baseFilename .= ".bmp" if $baseFilename !~ /\.bmp$/ && $contentType eq 'image/bmp';
          $baseFilename .= ".webp" if $baseFilename !~ /\.webp$/ && $contentType eq 'image/webp';
          last;
        }
      }
    } else {
      $this->writeDebug("... not found");
    }

    if ($baseFilename) {
      $this->writeDebug("... wasn't able to detect basefile from $url");

      ($baseFilename) = Foswiki::Sandbox::sanitizeAttachmentName($baseFilename);
      if ($meta->hasAttachment($baseFilename)) {
        $this->writeDebug("... picture already exists at $baseFilename");
        return _getAttachmentLink($web, $topic, $baseFilename);
      }

      my $content = $res->decoded_content();
      $tempFile = File::Temp->new(UNLINK => $Foswiki::cfg{PluggableAuth}{Debug}?0:1);
      print $tempFile $content;
      $tempFile->seek(0, SEEK_END);
    }
  } 

  if (!$url || !$baseFilename) {

    # find other image with a t attribute
    foreach my $otherAttachment ($meta->find("FILEATTACHMENT")) {
      next unless $meta->hasAttachment($otherAttachment->{name});
      if($otherAttachment->{attr} && $otherAttachment->{attr} =~ /t/) {
        #$this->writeDebug("... found other attachment flagged as a thumbnail");
        return _getAttachmentLink($web, $topic, $otherAttachment->{name});
      }
    }

    my $image = $user->getDefaultImage();
    my $hex = Digest::MD5::md5_hex(Encode::encode_utf8($user->prop("firstName") . " " . $user->prop("lastName")));
    my $ext = $Foswiki::cfg{ImageGeneratorPlugin}{ImageType} // "png";
    $baseFilename = "picture-$hex.$ext";

    $tempFile = File::Temp->new(UNLINK => $Foswiki::cfg{PluggableAuth}{Debug}?0:1, SUFFIX => ".$ext");
    $image->Write($tempFile->filename);
    $tempFile->seek(0, SEEK_END);
  }

  my $fileSize = -s $tempFile;
  $this->writeDebug("... file=$baseFilename, fileSize=$fileSize, tmpfile=$tempFile");

  my $origUser = $user->switch();

  $meta->attach( 
    name => $baseFilename,
    comment => "auto-attached by pluggable auth",
    file => $tempFile,
    filesize => $fileSize,
    hide => 1,
    dontlog => 1,
  );

  # add t flag for new picture, disable t flag from previous ones
  foreach my $attachment ($meta->find("FILEATTACHMENT")) {
    if ($attachment->{name} eq $baseFilename) {
      $attachment->{attr} = "ht";
    } else {
      $attachment->{attr} =~ s/t//g
    }
  }

  $this->auth->blockEvent("afterSaveHandler");
  $meta->save();
  $this->auth->unblockEvent("afterSaveHandler");

  $origUser->switch();

  close $tempFile;

  return _getAttachmentLink($web, $topic, $baseFilename);
}

sub updateGroup {
  my ($this, $group, $groupInfo) = @_;

  return unless defined $group;

  # just to make extra sure we don't override foreign groups
  my $pid = $group->prop("pid");
  $this->writeDebug("called updateGroup(".$group->stringify.")");

  if ($pid ne $this->prop("id") && $pid ne 'Base') {
    throw Error::Simple("... woops, refused to update group ".$group->stringify." via provider ".$this->prop("id"));
  }

  my %updates = ();

  foreach my $key (qw(wikiName displayName)) {
    my $newVal = $groupInfo->{$key};
    my $oldVal = $group->prop($key);

    #$this->writeDebug("... key=$key, oldVal=".($oldVal//'undef').", newVal=".($newVal//'undef'));

    if (defined $newVal && (!defined $oldVal || $newVal ne $oldVal)) {
      $this->writeDebug("... updating $key");
      $updates{$key} = $newVal;
    }
  }

  $group->update(%updates) if scalar(keys %updates);

  return $group;
}

sub indexGroup {
  my ($this, $group, $indexer, $doc, $meta, $text) = @_;

  #$this->writeDebug("indexing group ".$group->stringify);
}

sub indexUser {
  my ($this, $user, $indexer, $doc, $meta, $text) = @_;

  $this->writeDebug("indexing user ".$user->stringify);

  my $email = $user->prop("email");
  if ($email) {
    $this->indexSolrField($doc, 'field_Email_s', $email);
    $this->indexSolrField($doc, 'field_Email_search', $email);
  }

  foreach my $key (qw(loginName initials wikiName firstName middleName lastName displayName picture)) {
    my $label = ucfirst($key);
    my $value = $user->prop($key);
    next unless defined $value;

    if ($label eq 'LastName' && $value ne "") {
      $this->indexSolrField($doc, 'LastName_first_letter', $value);
    }
    if ($label eq 'Picture') {
      $this->indexSolrField($doc, 'thumbnail', $value);
    } else {
      $this->writeDebug("... adding $label=$value");

      $this->indexSolrField($doc, 'field_' . $label . '_s', $value);
      $this->indexSolrField($doc, 'field_' . $label . '_search', $value);
    }
  }

  my $providerName = $user->getProvider->prop("Name");
  $this->indexSolrField($doc, 'field_Provider_s', $providerName);
  $this->indexSolrField($doc, 'field_Provider_search', $providerName);

  if ($user->isEnabled) {
    $this->writeDebug("... enabling user in solr");
    $this->indexSolrField($doc, 'state', 'enabled');
  } else {
    $this->writeDebug("... disabling user in solr");
    $this->indexSolrField($doc, 'state', 'disabled');
  }
}

sub indexSolrField {
  my ($this, $doc, $name, $val) = @_;

  foreach my $field ($doc->fields) {
    if ($field->{name} eq $name && ref($field->{value}) eq ref($val)) {
      $field->{value} = $val;
      return;
    }
  }

  $doc->add_fields($name => $val);
}

sub getProviderGroupName {
  my $this = shift;

  return $this->auth->normalizeGroupName($this->prop("Name") . "_Group");
}

sub getProviderGroup {
  my $this = shift;

  return unless $Foswiki::cfg{PluggableAuth}{CreateProviderGroups};
  return $this->auth->findGroup(
    pid => $this->prop("id"),
    wikiName => $this->getProviderGroupName(),
  );
}

sub refresh {
  my ($this, $debug) = @_;

  $this->{_debug} = $debug;
  $this->writeDebug("called refresh for '".$this->prop("Name")."'");

  if ($Foswiki::cfg{PluggableAuth}{CreateProviderGroups}) {

    my $group = $this->getProviderGroup();

    if ($group) {
      $this->writeDebug("... found it");
    } else {
      my $groupName = $this->getProviderGroupName();
      $this->writeDebug("... creating provider group $groupName");
      $group = $this->addGroup(
         wikiName => $groupName, 
         id => $groupName, 
      );
    }

    #$this->writeDebug("group = ".$group->stringify);
    $this->_deleteMembers($group);

    my $userIt = $this->auth->eachUser(pid => $this->prop("id"));
    while ($userIt->hasNext) {
      my $user = $userIt->next;
      $this->auth->addMemberToGroup($user, $group);
    }
  } 

  my $userIt = $this->auth->eachUser(pid => $this->prop("id"));
  while ($userIt->hasNext) {
    my $user = $userIt->next;
    my $userInfo = $this->extractUserInfoFromTopic(user => $user);
    $this->updateUser($user, $userInfo) if defined $userInfo;
  }
}

# must be implemented by sub classes
sub checkGroupAccess {
  #my ($this, $type, $group, $user) = @_;
  return 0;
}

sub handlesLogin {
  my ($this, $request) = @_;

  my $pid = $request->param("pauth_provider");
  if (defined $pid) {
    if ($pid eq 'internal') {
      return 0 unless $this->isInternalLogin();
    } else {
      return 0 if $pid ne $this->prop("id");
    }
  }

  return 0 unless $this->isAllowedIpAddress;
  return 1;
}

sub initLogin {
  #my ($this, $request, $state) = @_;

  return 0;
}

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  return;
}

sub processLogout {
  #my ($this, $user) = @_;

  return;
}

sub isAdmin {
  my ($this, $user) = @_;;

  return $this->getAdminGroup->hasMember($user);
}

sub isAdminGroup {
  #my ($this, $user) = @_;;
  return 0;
}

sub getAdminGroup {
  my $this = shift;

  return $this->auth->getProvider("Base")->getAdminGroup;
}

sub getAdminUser {
  my $this = shift;

  return $this->auth->getProvider("Base")->getAdminUser;
}

sub getUnknownUser {
  my $this = shift;

  return $this->auth->getProvider("Base")->getUnknownUser;
}

sub enable {
  my $this = shift;

  $this->prop("Enabled", 1);
}

sub disable {
  my $this = shift;

  $this->prop("Enabled", 0);
}

sub isVisible {
  return shift->prop("Visible");
}

sub isEnabled {
  return shift->prop("Enabled");
}

sub isInternalLogin {
  return 1;
}

sub isExternalLogin {
  return !shift->isInternalLogin();
}

sub isAllowedIpAddress {
  my ($this, $addr) = @_;

  my $denyList = $this->prop("DeniedIPAddresses");
  my $allowList = $this->prop("AllowedIPAddresses");
  
  return 1 unless $denyList || $allowList;

  $addr = Foswiki::Func::getRequestObject->remote_addr unless defined $addr;

  return 0 if $denyList && _lookupAddr($addr, $denyList);
  return 0 if $allowList && !_lookupAddr($addr, $allowList);

  return 1;
}

sub canSendEmail {
  my ($this, $user) = @_;

  # Foswiki::Net::sendEmail can still fail

  return 0 unless $Foswiki::cfg{EnableEmail};
  my $email = $user->prop("email");
  return 0 unless $email;
  return 1;
}

sub canCheckPassword {
  my ($this, $user) = @_;

  return 0 unless $this->handles($user);
  return 1;
}

sub canSetPassword {
#  my ($this, $user) = @_;
#
#  return 0 if defined($user) && !$this->handles($user);
  return 0;
}

sub canSetEmail {
#  my ($this, $user) = @_;
#
#  return 0 if defined($user) && !$this->handles($user);
  return 0;
}

sub canDelete {
  my ($this, $obj) = @_;

  return $this->handles($obj) ? 1 : 0;
}

sub canRegisterUser {
  # my $this = shift;
  return 0;
}

sub canCreateGroup {
  # my ($this,$group) = @_;
  return 0;
}

sub canChangeMembership {
  # my ($this, $user, $group) = @_;
  return 0;
}

sub canChangeGroupName {
  # my ($this, $user, $group) = @_;
  return 0;
}

sub deleteUser {
  my ($this, $user) = @_;

  my $id = $user->prop("id");
  my $res;
  my $error;

  $this->writeDebug("called deleteUser ".$user->stringify);

  my @groups = ();
  my $it = $user->eachGroup();
  while ($it->hasNext) {
    push @groups, $it->next;
  }
  $this->db->handler->begin_work;

  try {
    my $tmp = $this->db->handler->do("DELETE FROM PluggableAuth_passwords WHERE uid=?", {}, $id);
    $this->writeDebug("... deleted $tmp from passwords");

    $tmp = $this->db->handler->do("DELETE FROM PluggableAuth_group_members WHERE mid=?", {}, $id);

    $this->writeDebug("... deleted $tmp rows from group_members");

    $tmp = $this->db->handler->do("DELETE FROM PluggableAuth_user_keys WHERE uid=?", {}, $id);
    $this->writeDebug("... deleted $tmp rows from user_keys");

    $res = $this->db->handler->do("DELETE FROM PluggableAuth_users WHERE id=?", {}, $id);
    $this->writeDebug("... deleted $res from users");

  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    $this->db->handler->rollback;
    throw Error::Simple("$error");
  } else {

    $this->db->handler->commit;

    foreach my $group (@groups) {
      $group->updateCount($group->prop("count") - 1);
    }

    $user->deleteTopic();
    $user->{_isLoaded} = 0;
    $this->auth->deleteCachedUser($user);
  }

  return $res;
}

sub deleteAllGroups {
  my $this = shift;

  $this->writeDebug("called deleteAllGroups");

  my $res;
  my $error;
  my $pid = $this->prop("id");

  $this->db->handler->begin_work;

  try {
    $res = $this->db->handler->do("DELETE FROM PluggableAuth_group_members WHERE mid IN (SELECT id FROM PluggableAuth_groups WHERE pid=?)", undef, $pid);
    $this->writeDebug("... deleted $res rows from group_members");

    $res = $this->db->handler->do("DELETE FROM PluggableAuth_group_members WHERE gid IN (SELECT id FROM PluggableAuth_groups WHERE pid=?)", undef, $pid);
    $this->writeDebug("... deleted $res rows from group_members");

    $res = $this->db->handler->do("DELETE FROM PluggableAuth_groups WHERE pid=?", undef, $pid);
    $this->writeDebug("... deleted $res rows from groups");

  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    $this->db->handler->rollback;
    throw Error::Simple("$error");
  } else {
    $this->db->handler->commit;
  }

  return $res;
}

sub deleteGroup {
  my ($this, $group) = @_;

  my $gid = $group->prop("id");
  my $res;
  my $error;

  $this->writeDebug("called deleteGroup ".$group->stringify);
  $this->db->handler->begin_work;

  try {
    $res = $this->deleteMembers($group);
    $this->writeDebug("... deleted $res member(s) from group_members");

    $res = $this->deleteMembership($group);
    $this->writeDebug("... deleted $res membership from group_members");

    $res = $this->db->handler->do("DELETE FROM PluggableAuth_groups WHERE id=?", {}, $gid);
    $this->writeDebug("... deleted $res from groups");

  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    $this->db->handler->rollback;
    throw Error::Simple("$error");
  } else {
    $this->db->handler->commit;
    $group->deleteTopic();
    $group->{_isLoaded} = 0;
    $this->auth->deleteCachedGroup($group);
  }

  return $res;
}

sub deleteMembers {
  my ($this, $group) = @_;

  my $res = $this->_deleteMembers($group);

  # need to recount _all_ groups
  if ($res) {
    $this->auth->updateCountOfAllGroups();
    $group->reload();
  }
  
  return $res;
}

sub _deleteMembers {
  my ($this, $group) = @_;

  my $gid = $group->prop("id");

  return $this->db->handler->do("DELETE from PluggableAuth_group_members WHERE gid=?", {}, $gid);
}

sub deleteAll {
  my $this = shift;

  my $res;
  my $error;

  $this->db->handler->begin_work;

  try {
    $res = $this->_deleteAll;
  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    $this->db->handler->rollback;
    throw Error($error);
  } else {
    $this->db->handler->commit;
  }

  return $res;
}

# same as above but without transactions
sub _deleteAll {
  my $this = shift;

  $this->writeDebug("called deleteAll");
  my $pid = $this->prop("id");

  $this->writeDebug("... pid=$pid");

  my $res;

  $res = $this->db->handler->do("DELETE FROM PluggableAuth_group_members WHERE mid IN (SELECT id FROM PluggableAuth_groups WHERE pid=?)", undef, $pid);
  $this->writeDebug("... deleted $res rows from group_members");

  $res = $this->db->handler->do("DELETE FROM PluggableAuth_group_members WHERE gid IN (SELECT id FROM PluggableAuth_groups WHERE pid=?)", undef, $pid);
  $this->writeDebug("... deleted $res rows from group_members");

  $res = $this->db->handler->do("DELETE FROM PluggableAuth_passwords WHERE uid IN (SELECT id FROM PluggableAuth_users WHERE pid=?)", undef, $pid);
  $this->writeDebug("... deleted $res rows from passwords");

  $res = $this->db->handler->do("DELETE FROM PluggableAuth_groups WHERE pid=?", undef, $pid);
  $this->writeDebug("... deleted $res rows from groups");

  $res = $this->db->handler->do("DELETE FROM PluggableAuth_users WHERE pid=?", undef, $pid);
  $this->writeDebug("... deleted $res rows from users");

  return $res;
}

# params holds keys
# - loginName
# - wikiName
# - email
# - password
sub registerUser {
  my ($this, %params) = @_;
 
  return unless $this->canRegisterUser;
  return if $params{email} && !$this->isValidEmail($params{email});

  my $password = $params{password};
  delete $params{password};
  return if $password && !$this->isValidPassword($password);

  $params{pid} = $this->prop("id");
  my $user = $this->addUser(%params);
  return unless $user;

  $user->setPassword($password) if defined $password;

  return $user;
}

sub createGroup {
  my ($this, %params) = @_;
 
  return unless $this->canCreateGroup;
}

sub loadUser {
  my ($this, %userInfo) = @_;

  my $user = Foswiki::PluggableAuth::User->new->load(%userInfo);
  return $user if defined $user && !$user->isUnknown;
}

sub findUser {
  my ($this, %userInfo) = @_;

  my %params = ( pid => $this->prop("id") , %userInfo);
  return $this->auth->findUser(%params);
}

sub findAuthName {
  my ($this, $authName) = @_;

  return $this->findUser(email => $authName, loginName => $authName)
    if $Foswiki::cfg{PluggableAuth}{AllowLoginUsingEmailAddress};

  return $this->findUser(loginName => $authName);
}

sub addUser {
  my ($this, %userInfo) = @_;

  #$this->writeDebug("... userInfo=".dump(\%userInfo));

  my $user;
  if (defined $userInfo{wikiName} && defined $userInfo{loginName}) {
    $this->writeDebug("... adding new user loginName=$userInfo{loginName}, email=".($userInfo{email}//'undef'));

    $userInfo{pid} = $this->prop("id");
    $user = $this->auth->addUser(%userInfo);

    if (defined $user) {
      my $picture = $this->updatePictureOfUser($user, $userInfo{'picture'});
      $user->update(picture => $picture) if defined $picture;

      if ($Foswiki::cfg{PluggableAuth}{CreateProviderGroups}) {
        my $group = $this->getProviderGroup();
        if ($group) {
          $this->auth->addMemberToGroup($user, $group);
          $group->updateCount($group->prop("count") + 1);
        }
      }
    }
  } else {
    $this->writeDebug("woops, not adding user: not enough infos");
  }

  return $user;
}

sub addGroup {
  my ($this, %groupInfo) = @_;

  $groupInfo{pid} = $this->prop("id");

  #$this->writeDebug("... groupInfo=".dump(\%groupInfo));

  return $this->auth->addGroup(%groupInfo);
}

sub setMembersOfGroup {
  my ($this, $members, $group) = @_;

  my $res = $this->_setMembersOfGroup($members, $group);

  if ($res) {
    $this->auth->updateCountOfAllGroups();
    $group->reload();
  }

  return $res;
}

sub _setMembersOfGroup {
  my ($this, $members, $group) = @_;

  my $gid = $group->prop("id");

  $this->writeDebug("called _setMembersOfGroup($gid)");
 
  my $res = $this->db->handler->do("DELETE from PluggableAuth_group_members WHERE gid=?", {}, $gid);

  if ($members) {
    foreach my $item (@$members) {
      next unless defined $item && $item ne "";
      my $obj; 
      if (ref($item)) {
        $obj = $item
      } else {
        $obj = $this->auth->getObjectByID($item) ||
               $this->auth->findUser(wikiName => $item);
      }
      unless ($obj) {
        #$this->writeDebug("hm, cannot find obj for $item");
        next;
      }
      $this->auth->addMemberToGroup($obj, $group);
    }
  }

  return $res;
}

sub addMemberToGroup {
  my ($this, $obj, $group) = @_;

  my $res = $this->auth->addMemberToGroup($obj, $group);

  if ($res) {
    if ($obj->isGroup) {
      $this->auth->updateCountOfAllGroups();
      $group->reload();
    } else {
      $group->updateCount(($group->prop("count")//0) + 1);
    }
  }

  return $res;
}

sub removeMemberFromGroup {
  my ($this, $obj, $group) = @_;

  my $res = $this->auth->removeMemberFromGroup($obj, $group);

  if ($res) {
    if ($obj->isGroup) {
      $this->auth->updateCountOfAllGroups();
      $group->reload();
    } else {
      $group->updateCount(($group->prop("count")//0) - 1);
    }
  }

  return $res;
}

sub deleteMembership {
  my ($this, $group) = @_;

  my $gid = $group->prop("id");

  $this->writeDebug("deleting membership for $gid");

  my $res = $this->db->handler->do("DELETE from PluggableAuth_group_members WHERE mid=? OR gid=?", {}, $gid, $gid);

  # need to recount _all_ groups
  $this->auth->updateCountOfAllGroups();
  $group->reload();

  return $res;
}

sub removeUserSessions {
  my ($this, $user) = @_;

  $this->writeDebug("called removeUserSessions(".$user->stringify().")");

  # delete any cgi session of this user
  my $msg = Foswiki::LoginManager::removeUserSessions($user->prop("id"));
  $msg .= Foswiki::LoginManager::removeUserSessions($user->prop("loginName"));

  return $msg;
}

sub setEmail {
  my ($this, $user, $email) = @_;

  $this->writeDebug("called setEmails()");
  return 0 unless $this->canSetEmail($user);
  return 0 unless $this->isValidEmail($email);

  return $user->update("email" => $email);
}

sub setPassword {
  my ($this, $user, $newPassword, $oldPassword, $encoding) = @_;

  $this->writeDebug("called setPassword()");
  return 0 unless $this->canSetPassword($user);
  return 0 unless $this->isValidPassword($newPassword);

  unless (defined $encoding) {
    (undef, $encoding) = $this->getPassword($user);
  }
  $encoding ||= $Foswiki::cfg{Htpasswd}{Encoding} // 'apache-md5';

  $this->writeDebug("encoding=$encoding");

  if (defined($oldPassword)) {
    $this->writeDebug("... checking old password");
    return 0 unless $this->checkPassword($user, $oldPassword);
  }

  my $hash = $this->hashPassword($user, $newPassword, $encoding);
  $this->writeDebug("... newPassword=$newPassword, hash=$hash");

  return $this->savePassword(
    uid => $user->prop("id"),
    password => $hash,
    encoding => $encoding,
    realm => "",
  );
}

sub savePassword {
  my ($this, %params) = @_;

  my (@fields, @values, @q);
  while (my ($k, $v) = each %params) {
    push @fields, $k;
    push @values, $v;
    push @q, '?';
  }
  return 0 unless @fields;

  my $stm = "REPLACE INTO PluggableAuth_passwords (".join(", ", @fields).") VALUES(".join(", ", @q).")";

  return $this->db->handler->do($stm, {}, @values);
}

sub getPassword {
  my ($this, $user) = @_;

  my @res = $this->db->handler->selectrow_array("SELECT password, encoding FROM PluggableAuth_passwords WHERE uid=?", {}, $user->prop("id"));
  return wantarray ? @res: $res[0];
}

sub checkPassword {
  my ($this, $user, $password) = @_;

  $this->writeDebug("called checkPassword($password)");
  return 0 unless defined $user && defined $password;
  return 0 unless $this->canCheckPassword($user);
  
  my ($orig, $encoding) = $this->getPassword($user);
  return 0 unless defined $orig;

  $encoding ||= $Foswiki::cfg{Htpasswd}{Encoding} // 'apache-md5';
  $this->writeDebug("... orig=$orig, encoding=$encoding");

  if ($encoding eq 'PBKDF2') {
    require Crypt::PBKDF2;
    my $pbkdf2 = Crypt::PBKDF2->new();
    return $pbkdf2->validate($orig, Encode::encode_utf8($password));
  } 

  if ($encoding eq 'argon2') {
    require Crypt::Argon2;
    return Crypt::Argon2::argon2i_verify($orig, Encode::encode_utf8($password));
  }

  my $hash = $this->hashPassword($user, $password, $encoding, 0);
  #print STDERR "hashPassword($password),\nhash    =$hash\norig    =$orig\n";
  #$this->writeDebug("... hash=$hash");

  return $hash eq $orig;
}

sub isValidEmail {
  my ($this, $addr) = @_;

  $this->writeDebug("called isValidEmail($addr)");

  return 0 unless Email::Valid->address($addr);

  $this->writeDebug("... valid format");

  my $emailFilter;
  $emailFilter = qr/$Foswiki::cfg{Register}{EmailFilter}/ix if $Foswiki::cfg{Register}{EmailFilter};
  return 0 if defined $emailFilter && $addr =~ $emailFilter;

  $this->writeDebug("... passes email filter");

  if ($Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled} && $Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{APIKey}) {

    $this->writeDebug("... calling block-temporary-email.com");

    my $expire = $Foswiki::cfg{PluggableAuth}{CacheExpire} // 3600;
    my $ua = Foswiki::Contrib::CacheContrib::getUserAgent("PluggableAuth Foswiki", expire => $expire);
    my $endpoint = $Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{EmailEndpoint} || "https://block-temporary-email.com/check/email";

    $endpoint .= "/" . $addr;

    $this->writeDebug("... endpoint=$endpoint");

    my $response = $ua->get($endpoint, 
      "x-api-key" => $Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{APIKey}
    );

    unless ($response->is_success) {
      $this->writeError("response msg=" . $response->message);# . " content=" . $response->decoded_content);
      throw Error::Simple("We encountered a protocol error while validating your email.");
    } 

    #$this->writeDebug("... response=".$response->decoded_content);

    my $data = $this->json->decode($response->decoded_content);

    return 0 if $data->{temporary};
    return 0 unless $data->{dns};
  }

  $this->writeDebug("... email is valid");
  
  return 1;
}

sub isValidPassword {
  my ($this, $password) = @_;

  $password //= "";
  $this->writeDebug("called isValidPassword($password)");
  return 0 unless $password;

  return 0 if $Foswiki::cfg{MinPasswordLength} && length($password) < $Foswiki::cfg{MinPasswordLength};

  # block common passwords
  my $isValid = 1;

  my $commonPasswords = $Foswiki::cfg{PluggableAuth}{CommonPasswordsFile};
  if ($commonPasswords && -e $commonPasswords) {
    $this->writeDebug("... reading commonPasswords from $commonPasswords");

    my $fh;

    if (open($fh, $commonPasswords)) {
      while (my $line = <$fh>) {
        chomp $line;
        if ($line eq $password) {
          $this->writeDebug("... found");
          $isValid = 0;
          last;
        }
      }
      close $fh;
    }
  }
  $this->writeDebug("... isValid=$isValid");

  return $isValid;
}

sub hashPassword {
  my ($this, $user, $password, $encoding, $fresh) = @_;

  $encoding ||= $Foswiki::cfg{Htpasswd}{Encoding} // 'apache-md5';

  $fresh //= 0;

  my $login = $user->prop("loginName");
  if ($encoding eq 'PBKDF2') {
    require Crypt::PBKDF2;
    my $pbkdf2 = Crypt::PBKDF2->new();
    return $pbkdf2->generate(Encode::encode_utf8($password));
  }

  if ($encoding eq 'sha1') {
    require Digest::SHA;

    my $encodedPassword = '{SHA}' . Digest::SHA::sha1_base64(Encode::encode_utf8($password)) . '=';

    # don't use chomp, it relies on $/
    $encodedPassword =~ s/\s+$//;
    return $encodedPassword;
  }

  my $salt;
  my $prevEncoding;
  unless ($fresh) {
    ($salt, $prevEncoding) = $this->getPassword($user);
    $salt = undef if $prevEncoding && $encoding ne $prevEncoding;
  }

  if ($encoding eq 'crypt') {
    $salt //= Foswiki::generateRandomChars(2, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./');
    #print STDERR "password=$password, salt=$salt, user=".$user->stringify."\n";
    return crypt(Encode::encode_utf8($password), Encode::encode_utf8(substr($salt, 0, 2)));
  }

  if ($encoding eq 'md5' || $encoding eq 'htdigest-md5') {

    my $realm = $Foswiki::cfg{AuthRealm};
    my $toEncode = "$login:$realm:$password";
    return Digest::MD5::md5_hex(Encode::encode_utf8($toEncode));
  }

  if ($encoding eq 'apache-md5') {
    require Crypt::PasswdMD5;

    $salt //= '$apr1$'. Foswiki::generateRandomChars(8);
    return Crypt::PasswdMD5::apache_md5_crypt(Encode::encode_utf8($password), Encode::encode_utf8(substr($salt, 0, 14)));
  }

  if ($encoding eq 'crypt-md5') {
    require Crypt::PasswdMD5;

    $salt //= '$1$' . Foswiki::generateRandomChars(8);
    return Crypt::PasswdMD5::unix_md5_crypt(Encode::encode_utf8($password), Encode::encode_utf8(substr($salt, 0, 11)));
  } 

  if ($encoding eq 'plain') {
    return Encode::encode_utf8($password);
  }

  if ($encoding eq 'bcrypt') {
    require Crypt::Eksblowfish::Bcrypt;

    my $cost = $Foswiki::cfg{Htpasswd}{BCryptCost};
    $cost = 8 unless defined $cost;
    $cost = sprintf("%02d", $cost);

    if ($fresh || !$salt) {
      $salt = Foswiki::generateRandomChars(16);
      $salt = Crypt::Eksblowfish::Bcrypt::en_base64(Encode::encode_utf8($salt));
      $salt = '$2a$' . $cost . '$' . $salt;
    }

    return Crypt::Eksblowfish::Bcrypt::bcrypt($password, $salt);
  } 

  if ($encoding eq 'argon2') {
    require Crypt::Argon2;

    my $cost = $Foswiki::cfg{Htpasswd}{Argon2Timecost};
    $cost = 8 unless defined $cost;

    my $threads = $Foswiki::cfg{Htpasswd}{Argon2Threads};
    $threads = 2 unless defined $threads;

    my $mem = $Foswiki::cfg{Htpasswd}{Argon2Memcost};
    $mem = '512k' unless defined $mem;

    $salt = Foswiki::generateRandomChars(16);
    return Crypt::Argon2::argon2i_pass(Encode::encode_utf8($password), $salt, $cost, $mem, $threads, 16);
  }

  throw Error::Simple('Unsupported password encoding ' . $encoding);
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

# class function
sub getAttribute {
  my ($data, $path) = @_;

  return $data if !defined($path) || !defined($data) || !ref($data);

  #$this->writeDebug("called getAttribute($data, $path)");

  if ($path =~ /^\.(.*)$/) {
    return getAttribute($data, $1);
  }
  if ($path =~ /^\[(\d+)\](.*)$/ && ref($data) eq 'ARRAY') {
    return getAttribute($data->[$1], $2);
  }
  if ($path =~ /^(.*?[^\\])([\.\[].*)?$/ && ref($data) eq 'HASH') {
    my $key = $1;
    $key =~ s/\\//g;
    return getAttribute($data->{$key}, $2);
  }

  return;
}

### static helper

sub _lookupAddr {
  my ($addr, $list) = @_;

  return unless $list;

  my @list;
  foreach my $ip (split(/\s*,\s*/, $list)) {
    # SMELL: cache this?
    push @list, Net::CIDR::range2cidr($ip);
  }

  return Net::CIDR::cidrlookup($addr, @list);
}

# backport for Foswiki-2.1.x
my $CSPRNG;
sub _generateRandomChars {

    my $length   = shift;
    my $universe = shift;

    # Provide a default if undefined
    # $ and : illegal in htpasswd file, <># significant in URLs
    $universe ||=
'_./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#%{}[]|';

    unless ( defined $CSPRNG ) {
        $CSPRNG = 0;
        eval 'use Bytes::Random::Secure'; 
        unless ($@) {
            $CSPRNG = Bytes::Random::Secure->new(
                NonBlocking => 1,     # Use non-blocking source of randomness
                Bits        => 256    # This is the default entropy
            );
        }
    }

    if ($CSPRNG) {

        # Use Secure::Random::Bytes
        return $CSPRNG->string_from( $universe, $length, '' );

    }
    else {
        # This is the original Foswiki / TWiki Salt algorithm.
        # It mixes in the Login which is no longer recommended.
        my @chars = split( //, $universe );
        my $random;

        foreach ( 1 .. $length ) {
            $random .= $chars[ rand @chars ];
        }
        return $random;
    }
}

sub _getNobodyLink {
  return _getAttachmentLink($Foswiki::cfg{SystemWebName}, "PluggableAuthContrib", "nobody.png");
}

sub _getAttachmentLink {
  my ($web, $topic, $name) = @_;

  my $session = $Foswiki::Plugins::SESSION;
  $web =~ s/\./\//g;
  return "$Foswiki::cfg{PubUrlPath}/$web/$topic/$name";
}


1;

