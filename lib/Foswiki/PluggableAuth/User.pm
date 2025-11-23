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

package Foswiki::PluggableAuth::User;

=begin TML

---+ package Foswiki::PluggableAuth::User

A User object bundles all information available for a specific user, i.e. its id, loginName and wikiName.
It serves as an interface to manipulate a user object.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::BaseObject ();
use Foswiki::Func ();
use Foswiki::Plugins::ImageGeneratorPlugin ();
use Foswiki::Form ();
use Foswiki::Plugins ();
use File::Temp ();
use Digest::MD5 ();
use Encode ();
use Error qw(:try);

use constant TABLE_PROPS => qw(pid id loginName email wikiName displayName firstName middleName lastName registrationDate initials loginDate picture);
use constant TABLE_NAME => "users";

our $IMAGEMAGICK_ENABLED;

BEGIN {
  eval 'use Image::Magick()';
  $IMAGEMAGICK_ENABLED = $@ ? 0 : 1;
}

our @ISA = qw(Foswiki::PluggableAuth::BaseObject );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor

=cut

sub new {
  my ($class, %params) = @_;

  my $this = $Foswiki::PluggableAuth::SINGLETON->getCachedUser($params{id});
  return $this if defined $this;

  return $class->SUPER::new(%params); 
}

sub init {
  my ($this, $row) = @_;

  $this = $this->SUPER::init($row);
  $this->auth->cacheUser($this);

  return $this;
}

sub find {
  my ($this, %params) = @_;

  return $this->auth->getCachedUser($params{id}) // $this->SUPER::find(%params);
}

sub load {
  my ($this, %params) = @_;

  my $that = $this->auth->getCachedUser($params{id});
  return $that if defined $that;

  return $this->SUPER::load(%params);
}

sub reload {
  my $this = shift;

  $this->auth->deleteCachedUser($this);

  return $this->SUPER::reload();
}

sub stringify {
  my $this = shift;

  return 
    ($this->prop("id")//'undef') . '/' . 
    ($this->prop("loginName")//'undef') . '/' . 
    ($this->prop("wikiName")//'undef') . '/' .
    ($this->prop("pid")//'undef') . '/' . 
    ($this->prop("email")//'undef');
}

sub updateLoginDate {
  my $this = shift;

  return $this->update(loginDate => time());
}

sub enable {
  my $this = shift;

  my $res = $this->SUPER::enable();

  my $it = $this->eachGroup();
  while ($it->hasNext) {
    my $group = $it->next();
    $group->updateCount($group->prop("count") + 1);
  }

  return $res;
}

sub disable {
  my $this = shift;

  my $res = $this->SUPER::disable();

  my $it = $this->eachGroup();
  while ($it->hasNext) {
    my $group = $it->next();
    $group->updateCount($group->prop("count") - 1);
  }

  $this->removeSessions();

  return $res;
}

sub removeSessions {
  my $this = shift;

  return $this->getProvider->removeUserSessions($this);
}

sub update {
  my ($this, %params) = @_;

  $this->writeDebug("called update()");

  if (defined $params{wikiName} && $params{wikiName} eq "") {
    $params{wikiName} = $this->auth->normalizeWikiName($params{displayName});
  }

  my ($oldWeb, $oldTopic) = $this->getTopic();

  my $res = $this->SUPER::update(%params);
  return unless $res;

  if ($params{id}) {

    # update passwords table
    my $stm = "UPDATE PluggableAuth_passwords SET uid=? where uid=?";
    #$this->writeDebug("... stm=$stm");
    $this->db->handler->do($stm, {}, $params{id}, $this->prop("id"));

    # update keys table
    $stm = "UPDATE PluggableAuth_user_keys SET uid=? where uid=?";
    $this->db->handler->do($stm, {}, $params{id}, $this->prop("id"));
  }

  my ($web, $topic) = $this->getTopic();
  return unless Foswiki::Func::topicExists($oldWeb, $oldTopic);

  my $wikiName = Foswiki::Func::getWikiName();
  my $mustIndex = 1;
  if (Foswiki::Func::checkAccessPermission("CHANGE", $wikiName, undef, $oldTopic, $oldWeb)) {

    # move topic
    if ($oldWeb ne $web || $oldTopic ne $topic) {
      if (Foswiki::Func::topicExists($oldWeb, $oldTopic) && !Foswiki::Func::topicExists($web, $topic)) {
        Foswiki::Func::moveTopic($oldWeb, $oldTopic, $web, $topic);
        $mustIndex = 0;
      }
    }

    # update topic
    $mustIndex = 0 if $this->getProvider->updateUserTopic($this);
  }

  # SMELL: We are working around broken browsers massively hitting the feed links on a page repeatedly.
  #
  # These links occur in the html header such as 
  #
  #     <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="/SomeWeb/WebRss">
  #     <link rel="alternate" type="application/atom+xml" title="Atom Feed" href="/SomeWeb/WebAtom">
  #
  # The Brave browser loads both links a dozen times each within a short period of time for no good reason
  # causing a high server load within a short period of time. To mitigate this load we cut off
  # below update call to spare the database access happening here. Especially when using PluggableAuthContrib
  # together with SolrPlugin will the user's profile page - and all of its attachment - be indexed a few dozen times
  # visiting pages with these rss and atom links.

  my $session = $Foswiki::Plugins::SESSION;
  my $baseTopic = $session->{topicName};
  $mustIndex = 0 if $baseTopic =~ /^(WebAtom|WebRss)$/;

  # force reindex
  if ($mustIndex && Foswiki::Func::getContext()->{SolrPluginEnabled}) {
    require Foswiki::Plugins::SolrPlugin;
 
    my $indexer = Foswiki::Plugins::SolrPlugin::getIndexer();
    $indexer->indexTopic($web, $topic);
  }

  return $res;
}

sub checkPassword {
  my ($this, $password) = @_;

  return $this->getProvider->checkPassword($this, $password);
}

sub setPassword {
  my ($this, $newPassword, $oldPassword, $encoding) = @_;

  return $this->getProvider->setPassword($this, $newPassword, $oldPassword, $encoding);
}

sub getPassword {
  my $this = shift;

  return $this->getProvider->getPassword($this);
}

sub setEmail {
  my ($this, $email) = @_;

  return $this->getProvider->setEmail($this, $email);
}

sub joinGroup {
  my ($this, $group) = @_;

  return $group->getProvider->addMemberToGroup($this, $group);
}

sub leaveGroup {
  my ($this, $group) = @_;

  return $group->getProvider->removeMemberFromGroup($this, $group);
}

sub eachGroup {
  my ($this, %params) = @_;

  # TODO create filter based on %params

  # only returns direct membership, compare eachMember
  my $stm = <<"SQL";
SELECT gid 
  FROM PluggableAuth_groups AS g
  JOIN PluggableAuth_group_members AS m
    ON (m.gid=g.id AND m.mid=? AND g.enabled=1)
SQL

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, $stm, [$this->prop("id")],
    sub {
      return $this->auth->getGroupByID(shift->{gid});
    }
  );
}

sub twofa {
  my $this = shift;
  return $this->auth->getTwoFactorAuth();
}

sub isAdmin {
  my $this = shift;
  return $this->getProvider->isAdmin($this);
}

sub isUnknown {
  my $this = shift;
  return $this->prop("id") eq 'BaseUserMapping_999';
}

sub isTwoFactorAuthEnabled {
  my $this = shift;

  return 0 unless $this->getProvider->prop("TwoFactorAuthEnabled");
  return $this->twofa->isEnabled($this->prop("id")) ? 1:0;
}

=begin TML

---++ ObjectMethod checkTwoFactorPolicy() -> $boolean

returns 1 if current provider doesn't have 2fa enabled

more at Foswiki::PluggableAuth::TwoFactorAut::checkPolicy()

=cut

sub checkTwoFactorPolicy {
  my $this = shift;

  # it's okay as 2fa isn't enabled for this user's provider anyway
  return 1 unless $this->getProvider->prop("TwoFactorAuthEnabled");
  return $this->twofa->checkPolicy($this);
}

sub isTwoFactorAuthConfigured {
  my $this = shift;

  return 0 unless $this->getProvider->prop("TwoFactorAuthEnabled");
  return defined $this->twofa->getUserKey($this->prop("id"), "otp") ? 1 : 0;
}

sub activateTwoFactorAuth {
  my $this = shift;

  return $this->twofa->activate($this->prop("id"));
}

sub deactivateTwoFactorAuth {
  my $this = shift;

  return $this->twofa->deactivate($this->prop("id"));
}

sub deleteUserKey {
  my ($this, $type) = @_;

  return $this->twofa->deleteUserKey($this->prop("id"), $type);
}

sub verifySecondFactor {
  my ($this, $code) = @_;

  $this->writeDebug("called verifySecondFactor()");
  return unless $this->isTwoFactorAuthEnabled();

  return $this->twofa->verify($code, $this->prop("id"));
  return 0;
}

sub logout {
  my $this = shift;

  return $this->getProvider->processLogout($this);
}

sub delete {
  my $this = shift;

  $this->writeDebug("called delete");

  my $provider = $this->getProvider;
  return unless defined $provider;

  $this->removeSessions();
  return $provider->deleteUser($this);
}

sub canSendEmail {
  my $this = shift;

  my $provider = $this->getProvider;
  return unless defined $provider;

  return $provider->canSendEmail($this);
}

sub canCheckPassword {
  my $this = shift;

  my $provider = $this->getProvider;
  return unless defined $provider;

  return $provider->canCheckPassword($this);
}

sub canSetPassword {
  my $this = shift;

  my $provider = $this->getProvider;
  return unless defined $provider;

  return $provider->canSetPassword($this);
}

sub canSetEmail {
  my $this = shift;

  my $provider = $this->getProvider;
  return unless defined $provider;

  return $provider->canSetEmail($this);
}

sub deleteTopic {
  my $this = shift;

  return unless $Foswiki::cfg{PluggableAuth}{CreateUserTopics}; 

  $this->writeDebug("called deleteTopic() for ".$this->stringify);

  my ($web, $topic) = $this->getTopic();
  unless (Foswiki::Func::topicExists($web, $topic)) {
    $this->writeDebug("... topic not found");
    return;
  }

  my $newTopic = "$topic" . time();

  Foswiki::Func::moveTopic($web, $topic, $Foswiki::cfg{TrashWebName}, $newTopic);
}

sub createTopic {
  my $this = shift;

  return unless $Foswiki::cfg{PluggableAuth}{CreateUserTopics}; 

  $this->writeDebug("called createTopic() for ".$this->stringify);

  my ($web, $topic) = $this->getTopic();
  if (Foswiki::Func::topicExists($web, $topic)) {
    $this->writeDebug("...already exists");
    return;
  }

  my $templateTopic = $this->getProvider->prop("NewUserTemplate") || $Foswiki::cfg{PluggableAuth}{NewUserTemplate} || 'System.PluggableAuthNewUserTemplate';

  my $templateWeb;
  ($templateWeb, $templateTopic) = Foswiki::Func::normalizeWebTopicName($web, $templateTopic);
  unless (Foswiki::Func::topicExists($templateWeb, $templateTopic)) {
    $this->writeDebug("... template topic not found: $templateWeb.$templateTopic");
    return;
  }

  my ($templateMeta, $templateText) = Foswiki::Func::readTopic($templateWeb, $templateTopic);
  unless ($templateMeta) {
    _writeError("can't read $templateWeb.$templateWeb");
    return;
  }

  Foswiki::Func::pushTopicContext($web, $topic);
  my $origUser = $this->auth->switchToRegistrationAgent();

  $this->writeDebug("... new user template=$templateWeb.$templateTopic");

  # process template
  my ($meta, $text) = Foswiki::Func::readTopic($web, $topic);

  $text = $this->expandOnTopicCreate($templateText);
  $meta->text($templateText);
  $meta->copyFrom($templateMeta);

  my $formDef = $meta->get('FORM');
  $formDef = $formDef->{name} if defined $formDef;

  if ($formDef) {
    my $form = Foswiki::Form->new($Foswiki::Plugins::SESSION, undef, $formDef);
    foreach my $field ($meta->find('FIELD')) {
      unless (defined($field->{value}) && $field->{value} ne "") {
        my $fieldDef = $form->getField($field->{name});
        $field->{value} = $fieldDef->getDefaultValue() if defined $fieldDef;
      }
      $field->{value} = $this->expandOnTopicCreate($field->{value});
    }
  }

  foreach my $field ($meta->find('PREFERENCE')) {
    $field->{value} = $this->expandOnTopicCreate($field->{value});
  }

  Foswiki::Func::setTopicTitle($web, $topic, $this->prop("displayName"), $meta, 1);

  $this->writeDebug("... creating topic $web.$topic");
  my $rev = $meta->save();

  $origUser->switch() if $origUser;
  Foswiki::Func::popTopicContext();

  $this->writeDebug("... done");
  return $rev;
}

sub expandOnTopicCreate {
  my ($this, $text) = @_;

  return '' unless $text;

  my ($web, $topic) = $this->getTopic();
  my $wikiUserName = $web . '.' . $topic;

  my $loginName = $this->prop("loginName");
  my $firstName = $this->prop("firstName") || '';
  my $middleName = $this->prop("middleName") || '';
  my $lastName = $this->prop("lastName") || '';
  my $initials = $this->prop("initials") || '';
  my $email = $this->prop("email") || '';
  my $displayName = $this->prop("displayName") || '';

  $text =~ s/\%CREATE:DISPLAYNAME\%/$displayName/g;
  $text =~ s/\%CREATE:FIRSTNAME\%/$firstName/g;
  $text =~ s/\%CREATE:MIDDLENAME\%/$middleName/g;
  $text =~ s/\%CREATE:LASTNAME\%/$lastName/g;
  $text =~ s/\%CREATE:INITIALS\%/$initials/g;
  $text =~ s/\%CREATE:EMAIL\%/$email/g;
  $text =~ s/\%CREATE:USERNAME\%/$loginName/g;
  $text =~ s/\%CREATE:WIKINAME\%/$topic/g;
  $text =~ s/\%CREATE:WIKIUSERNAME\%/$wikiUserName/g;
  $text =~ s/\%SPLIT%.*\%SPLIT%\n*//gms; # legacy cruft

  return $text;
}

=begin TML

---++ sendEmail($template, %data) -> $errors

send an email notification to this user

=cut

sub sendEmail {
  my ($this, $template, %data) = @_;

  unless ($this->{_doneTemplate}{$template}) {
    $this->{_doneTemplate}{$template} = 1;
    Foswiki::Func::readTemplate($template);
  }

  unless (defined $data{firstLastName}) {
    my @parts = ();
    foreach my $key (qw(firstName middleName lastName)) {
      my $val = $this->prop($key);
      push @parts , $val if $val;
    }
    $data{firstLastName} = join(" ", @parts)
  }

  $data{firstName} //= $this->prop("firstName");
  $data{middleName} //= $this->prop("middleName");
  $data{lastName} //= $this->prop("lastName");
  $data{displayName} //= $this->prop("displayName");
  $data{wikiName} //= $this->prop("wikiName");
  $data{loginName} //= $this->prop("loginName");
  $data{emailAddress} //= $this->prop("email");
  $data{introduction} //= "";

  my ($web, $topic) = $this->getTopic();
  my $meta = $this->readTopic();

  Foswiki::Func::pushTopicContext($web, $topic);

  foreach my $key (keys %data) {
    my $val = $data{$key};
    next unless defined $val;
    $key = uc($key);
    Foswiki::Func::setPreferencesValue($key, $val);
  }

  my $text = Foswiki::Func::expandTemplate("pauth::mail");
  $text = $meta->expandMacros($text);
  Foswiki::Func::popTopicContext();

  $text =~ s/^\s+//;
  $text =~ s/\s+$//;

  #print STDERR "email:\n$text\n";
  Foswiki::Func::writeEvent("sendmail", "to=".$this->prop("wikiName")." subject=$template");
  return Foswiki::Func::sendEmail($text, 3);
}

=begin TML

---++ ObjectMethod getTopic() -> ($web, $topic)

returns the location of the user's profile page, either a (web, topic) array
in array context or a "web.topic" string in scalar context;

=cut

sub getTopic {
  my $this = shift;

  return wantarray ? ($Foswiki::cfg{UsersWebName}, $this->prop("wikiName")) : $Foswiki::cfg{UsersWebName} . "." . $this->prop("wikiName");
}

=begin TML

---++ ObjectMethod getLink() -> $url

returns the view url for the user's profile page.

returns an empty string if the profile page doesn't exist;

=cut

sub getLink {
  my $this = shift;

  my ($web, $topic) = $this->getTopic();

  return "" unless Foswiki::Func::topicExists($web, $topic);

  return Foswiki::Func::getViewUrl($web, $topic);
}

sub getDefaultImage {
  my $this = shift;

  if ($IMAGEMAGICK_ENABLED && $Foswiki::cfg{PluggableAuth}{EnableGravatarFallback}) {
    my $emailAddress = $this->prop("email");
    if ($emailAddress) {
      $emailAddress = lc($emailAddress);
      $emailAddress =~ s/^\s+//;
      $emailAddress =~ s/\s+$//;

      $this->writeDebug("trying to fetch gravatar for $emailAddress");

      my $md5 = Digest::MD5::md5_hex($emailAddress);
      my $url = "https://www.gravatar.com/avatar/$md5.jpeg?size=300&d=404";
      $this->writeDebug("url=$url");

      my $response = $this->auth->getUserAgent->get($url);
      if ($response->is_success) {
        $this->writeDebug("... found");

        my $image = Image::Magick->new();
        $image->BlobToImage($response->content);
        return $image;

      } else {
        $this->writeDebug("... not found");
      }
    } else {
      #$this->writeDebug("... no email addr for ".$this->stringify);
    }
  }

  my @names = ();
  foreach my $key (qw(firstName middleName lastName)) {
    my $val = $this->prop($key);
    push @names, $val if $val;
  }
  my $text = join(" ", @names);

  my $label = $this->prop("initials");
  if ($label eq "") {
    $label .= uc(substr($_, 0, 1)) foreach split(/[^\w]+/, $text);
  }

  return Foswiki::Plugins::ImageGeneratorPlugin::getCore()->render({
    label => $label, 
    text => $text, 
    width => 150, 
    height => 150
  });
}

sub indexSolr {
  my $this = shift;

  return $this->getProvider->indexUser($this, @_);
}

sub switch {
  my $this = shift;

  my $origUser = $this->auth->getSelf();
  return unless $origUser;

  my $session = $Foswiki::Plugins::SESSION;
  $session->{user} = $this->prop("id");
  $session->{forms} = undef; 

  return $origUser;
}

### static helper
sub _writeError {
  print STDERR 'PluggableAuth::Users - ERROR: '.$_[0]."\n";
}

1;
