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

package Foswiki::PluggableAuth::Group;

=begin TML

---+ package Foswiki::PluggableAuth::Group

TODO

=cut

use strict;
use warnings;

use Foswiki::Iterator::DBIterator ();
use Foswiki::Plugins::TopicTitlePlugin ();
use Foswiki::PluggableAuth::BaseObject ();
use Error qw(:try);

use constant TABLE_PROPS => qw(pid id wikiName displayName enabled count);
use constant TABLE_NAME => "groups";

our @ISA = qw(Foswiki::PluggableAuth::BaseObject );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor

=cut

sub new {
  my ($class, %params) = @_;

  my $this = $Foswiki::PluggableAuth::SINGLETON->getCachedGroup($params{id});
  #print STDERR "found group $id in cache\n" if $this;
  return $this if defined $this;

  return $class->SUPER::new(%params); 
}

sub init {
  my ($this, $row) = @_;

  $this = $this->SUPER::init($row);
  $this->auth->cacheGroup($this);

  return $this;
}

sub find {
  my ($this, %params) = @_;

  return $this->auth->getCachedGroup($params{id}) // $this->SUPER::find(%params);
}

sub load {
  my ($this, %params) = @_;

  my $that = $this->auth->getCachedGroup($params{id});
  return $that if defined $that;

  return $this->SUPER::load(%params);
}

sub reload {
  my $this = shift;

  $this->auth->deleteCachedGroup($this);

  return $this->SUPER::reload();
}

sub stringify {
  my $this = shift;

  return 
    ($this->prop("id") // 'undef') . '/' . 
    ($this->prop("wikiName") // 'undef') . '/' . 
    ($this->prop("pid") // 'undef');
}


sub enable {
  my $this = shift;

  return $this->update(enabled => 1);
}

sub disable {
  my $this = shift;

  return $this->update(enabled => 0);
}

sub delete {
  my $this = shift;

  return $this->getProvider->deleteGroup($this);
}

sub deleteTopic {
  my $this = shift;

  $this->writeDebug("called deleteTopic() for ".$this->stringify);

  my ($web, $topic) = $this->getTopic();
  unless (Foswiki::Func::topicExists($web, $topic)) {
    $this->writeDebug("... topic not found");
    return;
  }

  my $newTopic = "$topic" . time();

  Foswiki::Func::moveTopic($web, $topic, $Foswiki::cfg{TrashWebName}, $newTopic);
}

sub deleteMembers {
  my $this = shift;

  return $this->getProvider->deleteMembers($this);
}

sub setMembers {
  my ($this, $members) = @_;

  return $this->getProvider->setMembersOfGroup($members, $this);
}

sub addMember {
  my ($this, $obj) = @_;

  return $this->getProvider->addMemberToGroup($obj, $this);
}

sub removeMember {
  my ($this, $obj) = @_;

  return $this->getProvider->removeMemberFromGroup($obj, $this);
}

sub isAdminGroup {
  my $this = shift;

  return $this->getProvider->isAdminGroup($this);
}

sub allowsView {
  my ($this, $user) = @_;

  return $this->getProvider->checkGroupAccess("VIEW", $this, $user);
}

sub allowsChange {
  my ($this, $user) = @_;

  return $this->getProvider->checkGroupAccess("CHANGE", $this, $user);
}

sub getEmailsOfMembers {
  my $this = shift;

  my %emails = ();
  my $it = $this->eachMember();
  while ($it->hasNext) {
    my $obj = $it->next;
    next unless defined $obj;

    my $email = $obj->prop("email");
    next unless defined $email;

    $emails{$email} = 1;
  }

  return keys %emails;
}

sub isEmpty {
  my $this = shift;

  #$this->writeDebug("called isEmpty()");

  return $this->prop("count") ? 0 : 1;
}

sub hasMember {
  my ($this, $obj, $expand) = @_;

  my $oid = $obj->prop("id");
  my $found = 0;

  if ($expand) {
    if (0) {
      # SMELL: this is slow ... should be done on SQL ... or members are cached otherwise
      my $it = $this->eachMember($expand);
      while ($it->hasNext) {
        my $member = $it->next;
        my $mid = $member->prop("id");
        #$this->writeDebug("... found $mid");
        if ($mid eq $oid) {
          $found = 1;
          last;
        }
      }
    } else {
      my $it = $this->eachMember($expand, 0, "id='$oid'");
      $found = $it->hasNext ? 1 : 0; 
    }
  } else {
    my $gid = $this->prop("id");
    my $stm = "SELECT COUNT(*) FROM PluggableAuth_group_members WHERE gid=? AND mid=?";
    my @res = $this->db->handler->selectrow_array($stm, {}, $gid, $oid);
    $found = (@res && $res[0]) ? 1 : 0;
  }

  return $found;
}

sub eachMember {
  my ($this, $expand, $showAll, $where) = @_;

  my $gid = $this->prop("id");
  my $stm;
  my @values = ();
  $expand //= 1;

  #$this->writeDebug("called eachMember($expand)");

  my $uEnabled = $showAll ? "" : "AND u.enabled=1";
  my $gEnabled = $showAll ? "" : "AND g.enabled=1";
  $where = $where ? "WHERE $where" : "";

  if ($expand) {
    $stm = <<"SQL";
WITH RECURSIVE
  memberOf(gid, mid) AS (
    SELECT gid, mid 
      FROM PluggableAuth_group_members AS m
      INNER JOIN PluggableAuth_groups AS g
      ON g.id=m.gid $gEnabled
      WHERE m.gid=?
    UNION
    SELECT gm2.gid as gid, gm2.mid as mid 
      FROM memberOf
      LEFT OUTER JOIN PluggableAuth_group_members AS gm2
      ON memberOf.mid = gm2.gid
      INNER JOIN PluggableAuth_groups AS g 
      ON g.id=gm2.gid $gEnabled
  )
SELECT DISTINCT mid as id 
  FROM memberOf 
  JOIN PluggableAuth_users AS u 
    ON mid=u.id $uEnabled
    $where
SQL
    push @values, $gid;
  } else {
  
    $stm = <<"SQL";
SELECT id 
  FROM PluggableAuth_users AS u
  JOIN PluggableAuth_group_members AS m
    ON (m.mid=u.id AND m.gid=? $uEnabled)
    $where

UNION 

SELECT id 
  FROM PluggableAuth_groups AS g
  JOIN PluggableAuth_group_members AS m
    ON (m.mid=g.id AND m.gid=? $gEnabled)
    $where
SQL
    push @values, $gid, $gid;
  }

  #$this->writeDebug("...stm=$stm");

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, $stm, \@values,
    sub {
      return $this->auth->getObjectByID(shift->{id});
    }
  );
}

sub getTopic {
  my $this = shift;

  return ($Foswiki::cfg{UsersWebName}, $this->prop("wikiName"));
}

sub getLink {
  my $this = shift;

  my ($web, $topic) = $this->getTopic();

  return Foswiki::Func::getScriptUrlPath($web, $topic, "view")
    if Foswiki::Func::topicExists($web, $topic);

  return Foswiki::Func::getScriptUrlPath($web, "WikiGroups", "view",
    group => $topic
  );
}

sub createTopic {
  my ($this, %params) = @_;

  return unless $this->getProvider->canCreateGroup($this);

  my ($web, $topic) = $this->getTopic();

  $this->writeDebug("called createGroup($topic)");

  if (Foswiki::Func::topicExists($web, $topic)) {
    $this->writeDebug("...already exists");
    return;
  }

  my $templateTopic = $this->getProvider->prop("NewGroupTemplate") || $Foswiki::cfg{PluggableAuth}{NewGroupTemplate} || 'System.PluggableAuthNewGroupTemplate';

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

  $this->writeDebug("... new group template=$templateWeb.$templateTopic");

  # process template
  my ($meta, $text) = Foswiki::Func::readTopic($web, $topic);

  my $members = $params{groupMembers};
  if (defined $members) {
    $members = join(", ", sort @$members);
  } else {
    $members = join(", ", sort map {$_->prop("wikiName")} $this->eachMember(0)->all);
  }

  my $wikiName = Foswiki::Func::getWikiName();
  $text = $meta->text($this->expandOnTopicCreate($templateText, 
    groupMembers => $members,
    wikiName => $wikiName,
  ));
  $meta->text($text);
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
      $field->{value} = $this->expandOnTopicCreate($field->{value}, 
        groupMembers => $members,
        wikiName => $wikiName,
      );
    }
  }

  foreach my $field ($meta->find('PREFERENCE')) {
    $field->{value} = $this->expandOnTopicCreate($field->{value}, 
      groupMembers => $members,
      wikiName => $wikiName,
    );
  }

  Foswiki::Func::setTopicTitle($web, $topic, $this->prop("displayName"), $meta, 1);

  $this->writeDebug("... creating topic $web.$topic");
  my $rev = $meta->save(ignorepermissions => 1);

  $origUser->switch() if $origUser;
  Foswiki::Func::popTopicContext();

  $this->writeDebug("... done");
  return $rev;
}

sub expandOnTopicCreate {
  my ($this, $text, %params) = @_;

  return '' unless $text;

  my ($web, $topic) = $this->getTopic();
  my $wikiUserName = $web . '.' . $topic;

  my $groupName = $this->prop("wikiName") || '';
  $text =~ s/\%CREATE:GROUPNAME\%/$groupName/g;

  foreach my $key (keys %params) {
    my $val = $params{$key} // "";
    $key = uc($key);
    $text =~ s/\%CREATE:$key\%/$val/g;
  }

  return $text;
}

sub updateCount {
  my ($this, $count) = @_;

  $this->writeDebug("called updateCount(".($count//'undef').")");

  if (defined $count) {
    $count = 0 if $count < 0;
  } else {
    $count = $this->_countMembers();
  }

  my $gid = $this->prop("id");
  my $stm = "UPDATE PluggableAuth_groups SET count=? WHERE id=?";

  my $res = $this->db->handler->do($stm, {}, $count, $gid);

  $this->prop("count", $count);

  return $res;
}

sub _countMembers {
  my $this = shift;

  my $it = $this->eachMember();

  #return $it->count();
  return scalar($it->all);
}

sub update {
  my ($this, %params) = @_;

  $this->writeDebug("called update()");

  my $res = $this->SUPER::update(%params);
  return unless $res;

  my ($oldWeb, $oldTopic) = $this->getTopic();
  return 1 unless Foswiki::Func::topicExists($oldWeb, $oldTopic);

  my $wikiName = Foswiki::Func::getWikiName();
  return unless Foswiki::Func::checkAccessPermission("CHANGE", $wikiName, undef, $oldTopic, $oldWeb);

  my ($web, $topic) = $this->getTopic();

  # move topic
  if ($oldWeb ne $web || $oldTopic ne $topic) {
    Foswiki::Func::moveTopic($oldWeb, $oldTopic, $web, $topic);

    # SMELL: update other ACLs
  }

  # update topic
  return $this->getProvider->updateGroupTopic($this, undef, 2);
}

sub indexSolr {
  my $this = shift;

  return $this->getProvider->indexGroup($this, @_);
}

1;
