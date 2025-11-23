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

package Foswiki::PluggableAuth;

=begin TML

---+ package Foswiki::PluggableAuth

This is the base class for all auth services.

=cut

use strict;
use warnings;

use DBI;
use Foswiki::Func ();
use Foswiki::Plugins ();
use Foswiki::Validation ();
use Foswiki::Plugins::JQueryPlugin ();
use Foswiki::ListIterator ();
use Foswiki::LoginManager ();
use Foswiki::Contrib::JsonRpcContrib ();
use Foswiki::DBI ();
use Foswiki::Iterator::DBIterator ();
use Foswiki::PluggableAuth::User();
use Foswiki::PluggableAuth::Group();
use Foswiki::PluggableAuth::Provider();
use Foswiki::PluggableAuth::Macros::USERINFO ();
use Text::Unidecode;
use File::Spec ();
use Error qw(:try);

use constant TRACE => 0;

#use Data::Dump qw(dump);
#use Carp qw(confess); 

our $SINGLETON;

our %INTERNALPROVIDERS = (
  Unknown => {
    Enabled => 1,
    Name => "Unknown",
    Module => 'Foswiki::PluggableAuth::Provider::Unknown',
    Visible => 0,
  },
  Base => {
    Enabled => 1,
    Name => "Base",
    Module => 'Foswiki::PluggableAuth::Provider::Base',
    Visible => 0,
  }
);

# monkey-patch Func API
BEGIN {
  unless (defined Foswiki::Func->can("findUser")) {
    no warnings 'redefine'; ## no critic
    *Foswiki::Func::findUser = sub {
      return Foswiki::PluggableAuth::findUser(undef, @_);
    };
    use warnings 'redefine';
  } else {
  }
}

=begin TML

---++ ClassMethod new(%params) -> $this

constructor for the singleton Foswiki::PluggableAuth class. 

=cut

sub new {
  my $class = shift;

  unless (defined $SINGLETON) {
    $SINGLETON = bless({
        session => $Foswiki::Plugins::SESSION,
        name => "PluggableAuth", # to make Foswiki::Plugins happy during registerEventHandler
        _usersCache => {},
        _groupsCache => {},
        @_
      },
      $class
    );
    #writeDebug("new singleton $SINGLETON");


    $SINGLETON->init();
  }

  return $SINGLETON;
}

=betin TML

--++ ObjectMethod DESTROY()

calls the finish method whenever this instance goes out of order

=cut

sub DESTROY {
  my $this = shift;

  #writeDebug("called destroy");
  $this->finish();
}

=begin TML

---++ ObjectMethod init()

read the config and initialize the database

=cut

sub init {
  my $this = shift;

  return if $this->{_doneInit};
  $this->{_doneInit} = 1;

  $this->{_blockedEvents} = {
    'beforeSaveHandler' => 0,
    'afterSaveHandler' => 0,
    'afterRenameHandler' => 0,
  };
  $this->{_providers} = ();
  $this->{_schemaVersions} = {};

  # load all providers
  $this->loadProviders();

  Foswiki::Plugins::JQueryPlugin::registerPlugin(
    'pauthusers', 
    'Foswiki::Contrib::PluggableAuthContrib::PauthUsers'
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'validateEmail',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcValidateEmail(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'validatePassword',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcValidatePassword(@_);
    }
  );

  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'checkEmail',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcCheckEmail(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'refresh',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcRefresh(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'addUser',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcAddUser(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'deleteUser',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcDeleteUser(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'enableUser',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcEnableUser(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'updateUser',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcUpdateUser(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'membership',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcMembership(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'addGroup',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcAddGroup(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'updateGroup',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcUpdateGroup(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'deleteGroup',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcDeleteGroup(@_);
    }
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'deleteProvider',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcDeleteProvider(@_);
    },
  );

  # admins only
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'deleteTwoFactorAuth', 
    sub { 
      return Foswiki::PluggableAuth->new->jsonRpcDeleteTwoFactorAuth(@_);
    }
  );

  # users
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'changePassword',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcChangePassword(@_);
    }
  );

  # users
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'changeEmail',
    sub {
      return Foswiki::PluggableAuth->new->jsonRpcChangeEmail(@_);
    }
  );

  # users
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'activateTwoFactorAuth', 
    sub { 
      return Foswiki::PluggableAuth->new->jsonRpcActivateTwoFactorAuth(@_);
    }
  );

  # users
  Foswiki::Contrib::JsonRpcContrib::registerMethod(
    'PluggableAuth',
    'deactivateTwoFactorAuth', 
    sub { 
      return Foswiki::PluggableAuth->new->jsonRpcDeactivateTwoFactorAuth(@_);
    }
  );

  # only for testing
  # Foswiki::Contrib::JsonRpcContrib::registerMethod(
  #   'PluggableAuth',
  #   'verify2fa', 
  #   sub { 
  #     return Foswiki::PluggableAuth->new->jsonRpcVerifyTwoFactorAuth(@_);
  #   }
  # );

  $this->registerEventHandler("beforeSaveHandler");
  $this->registerEventHandler("afterSaveHandler");
  $this->registerEventHandler("afterRenameHandler");
  $this->registerEventHandler("validateRegistrationHandler");

  Foswiki::Func::registerTagHandler('PROVIDERINFO', sub {
    require Foswiki::PluggableAuth::Macros::PROVIDERINFO;
    return Foswiki::PluggableAuth::Macros::PROVIDERINFO::handle(@_);
  });

  Foswiki::Func::registerTagHandler('PAUTHUSERS', sub {
    require Foswiki::PluggableAuth::Macros::PAUTHUSERS;
    return Foswiki::PluggableAuth::Macros::PAUTHUSERS::handle(@_);
  });

  Foswiki::Func::registerTagHandler('PAUTHGROUPS', sub {
    require Foswiki::PluggableAuth::Macros::PAUTHGROUPS;
    return Foswiki::PluggableAuth::Macros::PAUTHGROUPS::handle(@_);
  });

  Foswiki::Func::registerTagHandler('OTPINFO', sub { 
    require Foswiki::PluggableAuth::Macros::OTPINFO;
    return Foswiki::PluggableAuth::Macros::OTPINFO::handle(@_);
  });

  unless (exists $Foswiki::cfg{Plugins}{LdapNgPlugin} && $Foswiki::cfg{Plugins}{LdapNgPlugin}{Enabled}) {
    Foswiki::Func::registerTagHandler('LDAP', sub {
      require Foswiki::PluggableAuth::Macros::LDAP;
      return Foswiki::PluggableAuth::Macros::LDAP::handle(@_);
    });
  }

  if (exists $Foswiki::cfg{Plugins}{SolrPlugin} && $Foswiki::cfg{Plugins}{SolrPlugin}{Enabled}) {
    require Foswiki::Plugins::SolrPlugin;
    Foswiki::Plugins::SolrPlugin::registerIndexTopicHandler(sub {
        $this->indexTopicHandler(@_);
    });
  }

  if (exists $Foswiki::cfg{Plugins}{JQDataTablesPlugin} && $Foswiki::cfg{Plugins}{JQDataTablesPlugin}{Enabled}) {
    require Foswiki::Plugins::JQDataTablesPlugin;
    Foswiki::Plugins::JQDataTablesPlugin::registerConnector("users", "Foswiki::PluggableAuth::UsersConnector");
    #Foswiki::Plugins::JQDataTablesPlugin::registerConnector("groups", "Foswiki::PluggableAuth::GroupsConnector");
  }

  # create exclude maps
  $this->{_excludeWikiNames} = {map { $_ => 1 } split(/\s*,\s*/, $Foswiki::cfg{PluggableAuth}{ExcludeWikiNames} // '')};
  $this->{_excludeLoginNames} = {map { $_ => 1 } split(/\s*,\s*/, $Foswiki::cfg{PluggableAuth}{ExcludeLoginNames} // '')};
  $this->{_excludeGroupNames} = {map { $_ => 1 } split(/\s*,\s*/, $Foswiki::cfg{PluggableAuth}{ExcludeGroupNames} // '')};

  my $it = $this->eachUser(pid => 'Base');
  while ($it->hasNext) {
    my $user = $it->next;
    $this->{_excludeWikiNames}{$user->prop("wikiName")} = 1;
    $this->{_excludeLoginNames}{$user->prop("loginName")} = 1;
  }

  $it = $this->eachGroup(pid => 'Base');
  while ($it->hasNext) {
    my $group = $it->next;
    $this->{_excludeGroupNames}{$group->prop("wikiName")} = 1;
  }

  # flag pauth to wiki apps
  Foswiki::Func::getContext()->{PluggableAuthEnabled} = 1;

  # init database if required
  #$this->refresh() unless $this->countUsers();
}

=begin TML

---++ ObjectMethod finish()

this detroys the singleton object created in the constructor after
having disconnected from the database

=cut

sub finish {
  my $this = shift;

  #writeDebug("called finish");
  return if $this->{_doneFinish};
  $this->{_doneFinish} = 1;

  foreach my $id (keys %{$this->{_providers}}) {
    $this->{_providers}{$id}->finish if defined $this->{_providers}{$id};
    undef $this->{_providers}{$id};
  }

  $this->{_ca}->finish() if $this->{_ca};
  undef $this->{_ca};

  $this->{_2fa}->finish() if $this->{_2fa};
  undef $this->{_2fa};

  $this->{_db}->finish() if $this->{_db};
  undef $this->{_db};

  undef $this->{_providers};
  undef $this->{_excludeWikiNames};
  undef $this->{_excludeLoginNames};
  undef $this->{_excludeGroupNames};
  undef $this->{_usersCache};
  undef $this->{_groupsCache};
  undef $this->{_userAgent};
  undef $this->{_doneInit};
  undef $this->{_providersTimeStamp};

  undef $SINGLETON;

  return;
}

=begin TML

---++ ObjectMethod db() -> $database

loads, creates and connects to the database, returns a Foswiki::DBI::Database object.

=cut

sub db {
  my $this = shift;

  $this->{_db} //= Foswiki::DBI::loadSchema("Foswiki::PluggableAuth::Schema");
  return $this->{_db};
}

=begin TML

---++ ObjectMethod registerEventHandler($event, $handler)

this method allows to hook into internal events such as "afterSaveHandler"
that normally only plugins may have access to. 

=cut

sub registerEventHandler {
  my ($this, $event, $handler) = @_;

  $handler ||= $this;

  $this->{session}{plugins}->addListener($event, $handler);
}

=begin TML

---++ ObjectMethod invoke($event, ...)

forward Foswiki events to all active providers.

known events are:

   * afterRenameHandler
   * afterSaveHandler
   * beforeSaveHandler

Any further parameter (...) are forwared to the respective
event handlers.

=cut

sub invoke {
  my $this = shift;
  my $event = shift;

  return if $this->isBlockedEvent($event);

  if ($event eq 'validateRegistrationHandler') {
    my $data = shift;
    my $provider = $this->getRegistrationProvider();

    throw Error::Simple($this->maketext("Invalid email address")) 
      unless $provider->isValidEmail($data->{Email});

    throw Error::Simple($this->maketext("Invalid password")) 
      unless $provider->isValidPassword($data->{Password});

    return;
  } 

  my $topic = $_[1];
  my $web = $_[2];

  #my ($package, $file, $line) = caller;
  writeDebug("event $event has been invoked for $web.$topic");


  my $obj = $this->findUser(wikiName => $topic) || $this->findGroup(wikiName => $topic);
  my $provider;
  if ($obj) {
    $provider = $obj->getProvider();
  } else {
    if ($web eq $Foswiki::cfg{UsersWebName} && $topic =~ /Group$/) {
      $provider = $this->getProvider("Topic");
    }
  }

  return unless $provider;

  return $provider->beforeSaveHandler(@_) 
    if $event eq 'beforeSaveHandler';

  return $provider->afterSaveHandler(@_)
    if $event eq 'afterSaveHandler';

  return $provider->afterRenameHandler(@_)
    if $event eq 'afterRenameHandler';

  throw Error::Simple($this->maketext("Unknown event [_1]", $event));
}

=begin TML

---++ ObjectMethod blockEvent($vent)

blocks the event from being processed during invoke().
This comes in handy to prevent useless event loops. Each
call to blockEvent($even) should be followed by a call
to unblockEvent($even) later on.

=cut

sub blockEvent {
  my ($this, $event) = @_;
  
  $this->{_blockedEvents}{$event} = 1 if defined $event;
}

=begin TML

---++ ObjectMethod unblockEvent($event)

unblocks a previously blocked event of the same name

=cut

sub unblockEvent {
  my ($this, $event) = @_;

  $this->{_blockedEvents}{$event} = 0 if defined $event;
}

=begin TML

---++ ObjectMethod blockAllEvents()

blocks all known events. see invoke() for a list of known events.

=cut

sub blockAllEvents {
  my $this = shift;

  $this->blockEvent($_) foreach keys %{$this->{_blockedEvents}};
}

=begin TML

---++ ObjectMethod unblockAllEvents()

unblocks all known events.

=cut


sub unblockAllEvents {
  my $this = shift;

  $this->unblockEvent($_) foreach keys %{$this->{_blockedEvents}};
}

=begin TML

---++ ObjectMethod isBlockedEvent($event) -> $boolean

tests whether the named event is currently blocked.

=cut

sub isBlockedEvent {
  my ($this, $event) = @_;

  return defined $event ? $this->{_blockedEvents}{$event} : undef;
}

=begin TML

---++ ObjectMethod indexTopicHandler($indexer, $doc, $web, $topic, $meta, $text) 

this handler is registered to SolrPlugin to be called whenever a topic is indexed.
When the indexed topic is a known user or group will the provider of this object
be calling its indexSolr() method. Each provider can then process the object
on its behalf by enriching the Solr document with extra information.

=cut

sub indexTopicHandler {
  my ($this, $indexer, $doc, $web, $topic, $meta, $text) = @_;

  return unless $web eq $Foswiki::cfg{UsersWebName};

  my $obj = $this->findUser(wikiName => $topic) || $this->findGroup(wikiName => $topic);
  return unless $obj;

  return $obj->indexSolr($indexer, $doc, $meta, $text);
}

=begin TML

---++ ObjectMethod refresh($pid, $debug)

refresh internal data of each provider, i.e. for those that perform an internal caching of user data.
if $pid is defined will refresh this specific provider, otherwise refresh all active providers.

=cut

sub refresh {
  my ($this, $pid, $debug) = @_;

  writeDebug("called refresh()");
  # delay computation until the very end
  $this->{_suppressRecompute} = 1;

  # one provider
  if (defined $pid) {
    if ($pid ne "Topic") {
      my $provider = $this->getProvider($pid);
      throw Error::Simple($this->maketext("Unknown provider")) unless $provider;
      $provider->refresh($debug);
    }
  } else {

    # first base 
    $this->getProvider("Base")->refresh($debug);

    # then all other providers except topic 
    foreach my $provider ($this->getProviders) {
      my $id = $provider->prop("id");
      next if $id =~ /^(Topic|Base|Unknown)$/;

      writeDebug(".. refreshing $id");
      $provider->refresh($debug);
    }
  }

  # we need to compute the topic provider last as it is the only one that
  # allows to integrage ids from other providers into groups; other providers
  # are more self-contained as they don't allow use of foreign ids
  $this->getProvider("Topic")->refresh($debug);

  # recompute tables
  $this->{_suppressRecompute} = 0;

  $this->updateCountOfAllGroups();
}

sub updateCountOfAllGroups {
  my $this = shift;

  return if $this->{_suppressRecompute};

  my $it = $this->eachGroup();
  while ($it->hasNext) {
    my $group = $it->next();
    $this->deleteCachedGroup($group);
    $group->updateCount();
    $group->reload();
  }
}

sub addMemberToGroup {
  my ($this, $obj, $group) = @_;

  my $mid = $obj->prop("id");
  my $gid = $group->prop("id");

  $this->writeDebug("called addMemberToGroup(mid=$mid, gid=$gid)");

  throw Error::Simple($this->maketext("Not adding myself as a member: [_1]", $mid)) if $mid eq $gid;

  #return if $group->hasMember($obj);
  return $this->db->handler->do("REPLACE INTO PluggableAuth_group_members (gid, mid) VALUES(?, ?)", {}, $gid, $mid);
}

sub removeMemberFromGroup {
  my ($this, $obj, $group) = @_;

  my $mid = $obj->prop("id");
  my $gid = $group->prop("id");

  $this->writeDebug("called removeMemberFromGroup(mid=$mid, gid=$gid)");

  #return unless $group->hasMember($obj);
  return $this->db->handler->do("DELETE from PluggableAuth_group_members WHERE gid=? AND mid=?", {}, $gid, $mid);
}

=begin TML

---++ ObjectMethod validateJsonRpc($session, $request)

validates the strikeone validation key part of a jsonrpc call.
throws an exception if the request is invalid.

=cut

sub validateJsonRpc {
  my ($this, $session, $request) = @_;

  return unless $Foswiki::cfg{Validation}{Method} eq 'strikeone';

  my $nonce = $request->param('validation_key');
  my $cgiSession = $session->getCGISession();

  return unless defined $cgiSession;

  throw Error::Simple($this->maketext("Invalid API invocation"))
    unless Foswiki::Validation::isValidNonce($cgiSession, $nonce);
}

=begin TML

---++ ObjectMethod jsonRpcRefresh($session, $request)

JSON-RPC handler for the refresh method. This method is only
allowed to be called by an admin.

parameters:

   * pid: provider id to be refreshed (optional), all providers
     will be refreshed if left undefined

=cut

sub jsonRpcRefresh {
  my ($this, $session, $request) = @_;

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  writeDebug("called refresh");

  my $pid = $request->param("pid");
  my $debug = Foswiki::Func::isTrue($request->param("debug"));

  $this->refresh($pid, $debug);

  return $this->maketext("OK");
}

=begin TML

---++ ObjectMethod jsonRpcValidateEmail($session, $request) 

JSON-RPC handler for the validate email method.

=cut

sub jsonRpcValidateEmail {
  my ($this, $session, $request) = @_;

  throw Error::Simple($this->maketext("Access to API denied"))
    unless Foswiki::Func::getContext()->{command_line} &&
      Foswiki::Func::getContext()->{isadmin};

  my $email = $request->param("email");
  throw Error::Simple($this->maketext("Email parameter missing")) unless $email;

  my $provider = $this->getRegistrationProvider();
  return $provider->isValidEmail($email);
}

=begin TML

---++ ObjectMethod jsonRpcValidatePassword($session, $request) 

JSON-RPC handler for the validatePassword method.

=cut

sub jsonRpcValidatePassword {
  my ($this, $session, $request) = @_;

  throw Error::Simple($this->maketext("Access to API denied"))
    unless Foswiki::Func::getContext()->{command_line} &&
      Foswiki::Func::getContext()->{isadmin};

  my $password = $request->param("password");
  throw Error::Simple($this->maketext("Password parameter missing")) unless $password;

  my $provider = $this->getRegistrationProvider();
  return $provider->isValidPassword($password);
}

=begin TML

---++ ObjectMethod jsonRpcCheckEmail($session, $request) 

JSON-RPC handler for the checkEmail method.

=cut

sub jsonRpcCheckEmail {
  my ($this, $session, $request) = @_;

  throw Error::Simple($this->maketext("Access to API denied"))
    unless Foswiki::Func::getContext()->{command_line} &&
      Foswiki::Func::getContext()->{isadmin};

  my $id = $request->param("uid");
  if ($id) {
    my $user = $this->findUser(
      id => $id,
      loginName => $id,
      wikiName => $id
    );
    throw Error::Simple($this->maketext("Unknown user")) unless defined $user;
    return $user->getProvider->isValidEmail($user->prop("email")) ? "valid":"invalid";
  }

  my $email = $request->param("email");
  if ($email) {
    return $this->getProvider("Base")->isValidEmail($email) ? "valid":"invalid";
  }

  throw Error::Simple($this->maketext("no uid or email parameter"));

}

=begin TML

---++ ObjectMethod jsonRpcAddGroup($session, $request)

JSON-RPC handler for the addGroup method. This method is only
allowed to be called by an admin.

This creates a new group using the Topic provider.

parameters:

   * wikiName: name of the group to be added (mandatory)
   * enabled: boolean flag indicating whether the group is active or not
   * displayName: title of the group (topic title), defaults to wikiName
   * members: list of initial members of this group

=cut

sub jsonRpcAddGroup {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcAddGroup");

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();
  $this->validateJsonRpc($session, $request); 

  my $wikiName = $request->param("wikiName");

  throw Error::Simple($this->maketext("No wikiName parameter")) unless defined $wikiName;

  my $group = $this->findGroup(
    id => $wikiName,
    wikiName => $wikiName
  );

  throw Error::Simple($this->maketext("Group already exists")) if defined $group;

  my $enabled = $request->param("enabled") // 1;
  $enabled = $enabled->[0] if ref($enabled);

  my $displayName = $request->param("displayName") // $wikiName;

  my $provider = $this->getProvider("Topic");
  $group = $provider->addGroup(
    id => $wikiName,
    wikiName => $wikiName,
    displayName => $displayName,
    enabled => $enabled
  );

  my $members = $request->param("members");
  if ($members) {
    $members = [split(/\s*,\s*/, $members)] unless ref($members);
    $members = [map {my $tmp = $_; $tmp =~ s/^.*\.//; $tmp} @$members];
  } else {
    $members = [];
  }

  return $group->createTopic(groupMembers => $members) ? "Group has been created" : "No group created";
}

=begin TML

---++ ObjectMethod jsonRpcDeleteGroup($session, $request)

JSON-RPC handler for the deleteGroup method. This method is only
allowed to be called by an admin.

parameters:

   * gid: group id (mandatory)

=cut

sub jsonRpcDeleteGroup {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcDeleteGroup");

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();
  $this->validateJsonRpc($session, $request); 

  my $id = $request->param("gid");

  throw Error::Simple($this->maketext("No gid parameter")) unless defined $id;

  my $group = $this->findGroup(
    id =>$id,
    wikiName => $id
  );

  throw Error::Simple($this->maketext("Unknown group")) unless defined $group;
  throw Error::Simple($this->maketext("Cannot delete group")) unless $group->canBeDeleted();

  $group->delete;

  return $this->maketext("Group has been deleted");
}

=begin TML

---++ ObjectMethod jsonRpcDeleteProvider($session, $request)

JSON-RPC handler for the deleteProvider method. This method is only
allowed to be called by an admin.

CAUTION: this deletes all objects associated with the given provider.

parameters:

   * pid: provider id (mandatory)

=cut

sub jsonRpcDeleteProvider {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcDeleteProvider");

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();
  $this->validateJsonRpc($session, $request); 

  my $pid = $request->param("pid");
  throw Error::Simple($this->maketext("No pid defined")) unless defined $pid;

  my $provider = $this->getProvider($pid);
  throw Error::Simple($this->maketext("Unknown provider")) unless $provider;
  $provider->deleteAll();

  return $this->maketext("Provider has been deleted");
}

=begin TML 

---++ ObjectMethod jsonRpcVerifyTwoFactorAuth($session, $request)

JSON-RPC handler to verfy2fa method. 
This handler is current disabled and only used for testing.

parameters:

   * code: 6 digits

=cut

sub jsonRpcVerifyTwoFactorAuth {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcVerifyTwoFactorAuth");

  $this->validateJsonRpc($session, $request); 

  my $code = $request->param("code");
  my $uid = Foswiki::Func::getCanonicalUserID();

  return $this->getTwoFactorAuth->verify($code, $uid) ? "true": "false";
}

=begin TML

---++ ObjectMethod jsonRpcActivateTwoFactorAuth($session, $request)

JSON-RPC handler for the activateTwoFactorAuth method. This handler
is used by a user to initiate a two factor key. if the given
code validates will the 2fa key be activated in the database.

parameters:

   * code: 6 digits

=cut

sub jsonRpcActivateTwoFactorAuth {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcActivateTwoFactorAuth");

  $this->validateJsonRpc($session, $request); 

  my $code = $request->param("code");
  my $isOk = $this->getTwoFactorAuth->verify($code);

  $this->getTwoFactorAuth->activate() if $isOk;

  return $isOk?"true":"false";;
}

=begin TML

---++ ObjectMethod jsonRpcDeactivateTwoFactorAuth($session, $request)

JSON-RPC handler for the deactivateTwoFactorAuth method. This handler
is used by a user to deactivate a two factor key. 

=cut

sub jsonRpcDeactivateTwoFactorAuth {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcDeactivateTwoFactorAuth");

  $this->validateJsonRpc($session, $request); 

  my $isOk = $this->getTwoFactorAuth->deactivate();

  return $isOk?"true":"false";;
}

=begin TML

---++ ObjectMethod jsonRpcDeleteTwoFactorAuth($session, $request)

JSON-RPC handler for the deleteTwoFactorAuth method. 

=cut

sub jsonRpcDeleteTwoFactorAuth {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcDeleteTwoFactorAuth");

  $this->validateJsonRpc($session, $request); 
  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  my $id = $request->param("uid");
  my $user;

  if ($id) {
    $user = $this->findUser(
      id => $id,
      loginName => $id,
      wikiName => $id
    );
  } else {
    $user = $this->getSelf();
  }

  throw Error::Simple($this->maketext("Unknown user")) unless defined $user;
  throw Error::Simple($this->maketext("No two-factor authentication enabled")) unless $user->isTwoFactorAuthConfigured;

  my $isOk = $user->deleteUserKey();

  return $isOk?"true":"false";;
}

=begin TML

---++ ObjectMethod jsonRpcAddUser($session, $request)

JSON-RPC handler for the addUser method. This method is only
allowed to be called by an admin. It lets you add a new user using 
the Topic provider. A new record is added to the user mapping and
a new user profile page is created filling it with the provided
user information. Note that the {NewUserTemplate} setting is being used as
a template for user profiles.

parameters:

   * loginName: mandatory
   * firstName: mandatory
   * middleName: optional
   * lastName: mandatory
   * wikiName: optional, will be generated from the first, middle and lastName if undefined
   * email: optional, however note that the user can't be contacted if undefined
   * initials: optional, will use first, middle, lastName first letters to generate a sensible default
   * displayName: optional, will use first, middle, lastName for a sensible default
   * password: optional, note that the user wont be able to login if left undefined
   * sendmail: boolean value, the user will be contacted via email if true. note that an email value is required

A user may defined without emails and password. These values may be provided later on using the =updateUser=
and =changePassword= JSON-RPC handlers later.

=cut

sub jsonRpcAddUser {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcAddUser");

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();
  $this->validateJsonRpc($session, $request); 

  my $loginName = $request->param("loginName");
  my $wikiName = $request->param("wikiName");
  my $firstName = $request->param("firstName");
  my $middleName = $request->param("middleName");
  my $lastName = $request->param("lastName");
  my $email = $request->param("email");
  my $initials = $request->param("initials");
  my $displayName = $request->param("displayName");
  my $password = $request->param("password");

  throw Error::Simple($this->maketext("LoginName required")) unless $loginName;
  throw Error::Simple($this->maketext("FirstName required")) unless $firstName;
  throw Error::Simple($this->maketext("LastName required")) unless $lastName;

  my @parts = ();
  push @parts, $firstName;
  push @parts, $middleName if defined $middleName;
  push @parts, $lastName;
  $wikiName = join(" ", @parts) unless defined $wikiName;

  $wikiName = $this->normalizeWikiName($wikiName);
  throw Error::Simple($this->maketext("Invalid wikiName")) unless defined $wikiName && $wikiName ne "";

  my $provider = $this->getRegistrationProvider();

  throw Error::Simple($this->maketext("User already exists"))
    if $this->userExists(
          loginName => $loginName, 
          wikiName => $wikiName, 
          pid => $provider->prop("id")
       );

  my %userInfo = (
    loginName => $loginName,
    wikiName => $wikiName,
    firstName => $firstName,
    middleName => $middleName,
    lastName => $lastName,
    email => $email,
    initials => $initials,
    displayName => $displayName
  );

  my $user = $provider->addUser(%userInfo);
  throw Error::Simple($this->maketext("Failed to create user")) unless defined $user;

  $user->setPassword($password) if defined $password && $password ne "";

  if (defined $email && $email ne "") {
    $user->setEmail($email);
    if (Foswiki::Func::isTrue($request->param("sendmail"), 0)) {
      my $errors = $user->sendEmail("mailaddaccount", password => $password);
      throw Error::Simple($errors) if $errors;
    }
  }

  return $this->maketext("User has been added");
}

=begin TML

---++ ObjectMethod jsonRpcChangePassword($session, $request)

JSON-RPC handler for the changePassword method. 

parameters:

   * uid: user identifier, only used in admin context  
   * password: new password
   * password_confirm: repeated new password
   * sendmail: boolean value if true will trigger an email notification to the user
     informing him/her about the new password

=cut

sub jsonRpcChangePassword {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcChangePassword");

  $this->validateJsonRpc($session, $request); 

  my $currentUser = $this->getSelf();
  my $isAdmin = $currentUser->isAdmin();
  my $user;

  if ($isAdmin) {
    my $id = $request->param("uid");

    if (defined $id) {
      $user = $this->findUser(
        id => $id,
        loginName => $id,
        wikiName => $id
      );
      throw Error::Simple($this->maketext("Unknown user"))
        unless defined $user && $user->isEnabled();
    }
  }

  $user //= $currentUser;
  throw Error::Simple($this->maketext("Cannot change password"))
    unless $user->canSetPassword($user);

  my $isCommandLine = Foswiki::Func::getContext()->{command_line};

  my $password = $request->param("password");
  throw Error::Simple($this->maketext("Password required")) unless defined $password;

  my $confirmedPassword = $request->param("password_confirm") // $request->param("passwordA");
  unless ($isCommandLine) {
    throw Error::Simple($this->maketext("Confirmed password required")) unless defined $confirmedPassword;
    throw Error::Simple($this->maketext("Passwords don't match")) unless $password eq $confirmedPassword;
  }

  throw Error::Simple($this->maketext("Invalid password"))
    unless $user->getProvider->isValidPassword($password);

  my $doSendEmail = Foswiki::Func::isTrue($request->param("sendmail"), 0);
  throw Error::Simple($this->maketext("Cannot notify user via email. Not changing the password"))
    if $doSendEmail && !$user->canSendEmail();

  my $loginManager = $session->getLoginManager();
  my $resetActive = $loginManager->getSessionValue('FOSWIKI_PASSWORDRESET');

  my $oldPassword;
  unless ($isAdmin || $resetActive) {
    $oldPassword = $request->param("password_old") // $request->param("oldpassword");
    throw Error::Simple($this->maketext("Old password required")) 
      unless $isCommandLine || defined($oldPassword);
    throw Error::Simple($this->maketext("Permission denied"))
      unless $user->checkPassword($oldPassword);
  }

  if ($user->setPassword($password, $oldPassword)) {
    if ($doSendEmail) {
      my $errors = $user->sendEmail("mailpasswordreset", password => $password);
      throw Error::Simple($errors) if $errors;
    }

    # since foswiki-2.2
    $loginManager->clearSessionValue('FOSWIKI_PASSWORDRESET');
    $loginManager->clearSessionValue('FOSWIKI_TOPICRESTRICTION');

    return $this->maketext("Password has been changed");
  }

  throw Error::Simple($this->maketext("Password was not changed"));
}

=begin TML

---++ ObjectMethod jsonRpcChangeEmail($session, $request)

JSON-RPC handler for the changeEmail method. 

parameters:

   * uid: user identifier, only used in admin context  
   * password: password if user is not an admin (oldpassword for legacy reasons)
   * email: new email address

=cut

sub jsonRpcChangeEmail {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcChangeEmail");

  $this->validateJsonRpc($session, $request); 

  my $currentUser = $this->getSelf();
  my $isAdmin = $currentUser->isAdmin();
  my $user;

  if ($isAdmin) {
    my $id = $request->param("uid");

    if (defined $id) {
      $user = $this->findUser(
        id => $id,
        loginName => $id,
        wikiName => $id
      );
      throw Error::Simple($this->maketext("Unknown user")) 
        unless defined $user && $user->isEnabled();
    }
  }

  $user //= $currentUser;

  throw Error::Simple($this->maketext("Cannot change email"))
    unless $user->canSetEmail($user);
  
  my $isCommandLine = Foswiki::Func::getContext()->{command_line};

  if (!$isCommandLine && !$isAdmin) {
    my $password = $request->param("password") // $request->param("oldpassword");
    throw Error::Simple($this->maketext("Password required")) unless defined $password;

    throw Error::Simple($this->maketext("Permission denied"))
      unless $user->checkPassword($password);
  }

  my $email = $request->param("email");
    throw Error::Simple($this->maketext("Email required")) unless $email;

  if ($user->setEmail($email)) {
    return $this->maketext("Email has been changed");
  }

  throw Error::Simple($this->maketext("Email was not changed"));
}

=begin TML

---++ ObjectMethod jsonRpcDeleteUser($session, $request)

JSON-RPC handler for the deleteUser method. This method is only
allowed to be called by an admin. This method will remove a user 
from the system as well as delete (move to Trash) the user profile

parameters:

   * uid: user identifier (mandatory)

=cut

sub jsonRpcDeleteUser {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcDeleteUser");

  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();
  $this->validateJsonRpc($session, $request); 

  my $ids = $request->param("uid");

  throw Error::Simple($this->maketext("No uid parameter")) unless defined $ids;

  my @ids = split(/\s*,\s*/, $ids);
  my $total = scalar(@ids);

  my $index = 0;
  foreach my $id (@ids) {
    $index++;
    writeDebug("$index/$total - id=$id");
    #print STDERR "$index/$total - id=$id\n";

    my $user = $this->findUser(
      id => $id,
      loginName => $id,
      wikiName => $id
    );

    throw Error::Simple($this->maketext("Unknown user")) unless defined $user;
    throw Error::Simple($this->maketext("Cannot delete user")) unless $user->canBeDeleted();

    # delete the user
    $user->delete;
  }

  return $this->maketext("User has been deleted");
}

=begin TML

---++ ObjectMethod jsonRpcEnableUser()

JSON-RPC handler for the enableUser method. This method is only
allowed to be called by an admin. This method may be used to 
enable as well as disable a user account. User won't be able
to log in if disabled. Yet his/her account information is still
part of the system.

parameters:

   * uid: user identifier (mandatory)
   * enabled: boolean value to control the enabled/disabled status of a user

=cut

sub jsonRpcEnableUser {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcEnableUser");

  $this->validateJsonRpc($session, $request); 
  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  my $ids = $request->param("uid");
  my $enabled = Foswiki::Func::isTrue($request->param("enabled"), 1);

  throw Error::Simple($this->maketext("No uid parameter")) unless defined $ids;

  foreach my $id (split(/\s*,\s*/, $ids)) {
    writeDebug("id=$id");

    my $user = $this->findUser(
      id => $id,
      loginName => $id,
      wikiName => $id
    );

    throw Error::Simple($this->maketext("Unknown user")) unless defined $user;

    if ($enabled) {
      $user->enable;
    } else {
      $user->disable;
    }
  }

  return $enabled ? $this->maketext("User has been enabled") : $this->maketext("User has been disabled");
}

=begin TML

---++ ObjectMethod jsonRpcMembership($session, $request)

JSON-RPC handler for the membership method. This method is only
allowed to be called by an admin. This method may be used to 
manage the groups a user is a member of. Note that only Topic groups
are modified. Any external group is not affected by this handle.

There are three modes that this method will be performed

   1 set membership to the given set of groups, that is any previous
     membership will be revoked
   2 join groups in addition to the current membership
   3 leave groups a user is currently a member of

parameters:

   * uid: user indentifier (mandatory)
   * groups: list of groups the user is a member of (mode 1)
   * join: list of additional groups the user is added to (mode 2)
   * leave: list of groups the user is removed from (mode 3)

Note that modes 2 and 3 can be combined by providing join and leave 
values.

=cut

sub jsonRpcMembership {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcMembership");

  $this->validateJsonRpc($session, $request); 
  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  my $id = $request->param("uid");

  throw Error::Simple($this->maketext("No uid parameter")) unless defined $id;

  my $user = $this->findUser(
    id => $id,
    loginName => $id,
    wikiName => $id
  );

  throw Error::Simple($this->maketext("Unknown user")) unless defined $user;

  my $groups = $request->param("groups");

  # change membership
  if (defined $groups) {
    my %groupNames = ();
    $groupNames{$_} = 1 foreach ref($groups) ? @$groups : split(/\s*,\s*/, $groups);

    # leave all groups Topic groups
    my $it = $user->eachGroup();
    while ($it->hasNext) {
      my $group = $it->next;
      next unless $group->prop("pid") eq 'Topic'; # only null Topic group membership

      if ($user->leaveGroup($group)) {
        writeDebug("... leaving group ".$group->prop("id"));
      }
    }

    # join new set of groups
    foreach my $groupName (keys %groupNames) {
      my $group = $this->findGroup(wikiName => $groupName);
      unless ($group) {
        writeDebug("... unknown group '$groupName'");
        next;
      }
      if ($user->joinGroup($group)) {
        writeDebug("... joining group ".$group->prop("id"));
      }
    }
  }

  my $join = $request->param("join");
  if (defined $join) {
    my %groupNames = ();
    $groupNames{$_} = 1 foreach ref($join) ? @$join : split(/\s*,\s*/, $join);
    
    foreach my $groupName (keys %groupNames) {
      my $group = $this->findGroup(wikiName => $groupName);
      unless ($group) {
        writeDebug("... unknown group '$groupName'");
        next;
      }
      if ($user->joinGroup($group)) {
        writeDebug("... joining group ".$group->prop("id"));
      }
    }
  }

  my $leave = $request->param("leave");
  if (defined $leave) {
    my %groupNames = ();
    $groupNames{$_} = 1 foreach ref($leave) ? @$leave : split(/\s*,\s*/, $leave);

    foreach my $groupName (keys %groupNames) {
      my $group = $this->findGroup(wikiName => $groupName);
      unless ($group) {
        writeDebug("... unknown group '$groupName'");
        next;
      }
      if ($user->leaveGroup($group)) {
        writeDebug("... leaving group ".$group->prop("id"));
      }
    }
  }

  return $this->maketext("Membership has been updated");
}

=begin TML

---++ ObjectMethod jsonRpcUpdateGroup($session, $request)

JSON-RPC handler for the membership method. This method is only
allowed to be called by an admin. This method may be used to 
change the properties of a group.

parameters:

   * gid: group identifier (mandatory)
   * wikiName: wiki name of the group, note that the topic will be renamed when changing this value
   * displayName: title of this group (aka topic title)
   * members: list of users member of this group
   * enabled: boolean letting you enable/disable a group while still leaving its record in the system

A disabled group is removed from the mapping, that is any ACL checks using this group are disabled.

=cut

sub jsonRpcUpdateGroup {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcUpdateGroup");

  $this->validateJsonRpc($session, $request); 
  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  my $id = $request->param("gid");

  throw Error::Simple($this->maketext("No gid parameter")) unless defined $id;

  throw Error::Simple($this->maketext("Unknown group")) unless 
    $this->groupExists( id => $id) ||
    $this->groupExists( wikiName => $id);

  my $group = $this->findGroup(
    id => $id,
    wikiName => $id
  );

  throw Error::Simple($this->maketext("Unknown group")) unless defined $group;

  writeDebug("updating group ".$group->stringify);
  my %params = ();
  foreach my $key (qw(wikiName displayName enabled)) {
    my $val = $request->param($key);
    if (defined $val) {
      if ($key eq "newid") {
        $params{"id"} = $val;
      } elsif ($key eq 'enabled') {
        $val = $val->[0] if ref($val);
        $params{$key} = Foswiki::Func::isTrue($val);
      } else {
        $params{$key} = $val;
      }
      writeDebug("... $key=$val");
    }
  }

  my $members = $request->param("members");
  throw Error::Simple($this->maketext("Please specify the attribute(s) to change")) unless scalar(keys %params) || defined($members);

  my $error;
  try {
    $group->update(%params);

    if (defined $members) {
      $members = [map { my $tmp = $_; $tmp =~ s/^.*\.//; $tmp } split(/\s*,\s*/, $members)] if defined($members) && !ref($members);
      $group->setMembers($members);
    } else {
    }

  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    writeDebug("ERROR: $error");
    throw Error::Simple($this->maketext("Error updating group: [_1]", $error));
  }

  return $this->maketext("Group has been updated");
}

=begin TML

---++ ObjectMethod jsonRpcUpdateUser($session, $request)

JSON-RPC handler for the membership method. This method is only
allowed to be called by an admin. This method may be used to 
change the properties of a user.

parameters:

   * uid: user identifier (mandatory)
   * loginName 
   * newid 
   * wikiName: note that changing the wikiName will rename the user profile page
   * displayName 
   * email 
   * firstName 
   * middleName 
   * lastName 
   * initials 
   * enabled: boolean
   * two_factor_auth_enabled: boolean value to temporarily disable or re-enable 2fa of a user; 
     instead of deaktivating a users 2fa key will 2fa be temporarily deactivated

=cut

sub jsonRpcUpdateUser {
  my ($this, $session, $request) = @_;

  writeDebug("called jsonRpcUpdateUser");

  $this->validateJsonRpc($session, $request); 
  throw Error::Simple($this->maketext("Access to API denied")) unless Foswiki::Func::isAnAdmin();

  my $id = $request->param("uid");

  throw Error::Simple($this->maketext("No uid parameter")) unless defined $id;

  my $user = $this->findUser(
    id => $id,
    loginName => $id,
    wikiName => $id
  );

  throw Error::Simple($this->maketext("Unknown user")) unless defined $user;

  writeDebug("updating user ".$user->stringify);
  my %params = ();
  foreach my $key (qw(loginName newid wikiName displayName email firstName middleName lastName initials enabled)) {
    my $val = $request->param($key);
    if (defined $val) {
      if ($key eq "newid") {
        $params{"id"} = $val;
      } elsif ($key eq 'enabled') {
        $val = $val->[0] if ref($val);
        $params{$key} = Foswiki::Func::isTrue($val);
      } else {
        $params{$key} = $val;
      }
      writeDebug("... $key=$val");
    }
  }

  my $twoFactorAuth = $request->param("two_factor_auth_enabled");

  throw Error::Simple($this->maketext("Please specify the attribute(s) to change")) 
    unless scalar(keys %params) ||
      defined $twoFactorAuth;
      
  my $error;
  try {
    $user->update(%params);
    $user->setEmail($params{email}) if defined $params{email};
  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    writeDebug("ERROR: $error");
    throw Error::Simple($this->maketext("Error updating user: [_1]", $error));
  }

  if (defined $params{enabled} && !$params{enabled}) {
    $user->removeSessions();
  }

  if (defined $twoFactorAuth && $user->isTwoFactorAuthConfigured()) {
    if (Foswiki::Func::isTrue($twoFactorAuth)) {
      $user->activateTwoFactorAuth();
    } else {
      $user->deactivateTwoFactorAuth();
    }
  }

  return $this->maketext("User has been updated");
}

sub cacheUser {
  my ($this, $obj) = @_;

  my $id = $obj->prop("id");
  $this->{_usersCache}{$id} = $obj;

  return $obj;
}

sub deleteCachedUser {
  my ($this, $obj) = @_;

  my $id = $obj->prop("id");
  undef $this->{_usersCache}{$id};
}

sub getCachedUser {
  my ($this, $id) = @_;

  return unless defined $id && !ref($id) && $id ne "";
  return $this->{_usersCache}{$id};
}

sub cacheGroup {
  my ($this, $obj) = @_;

  my $id = $obj->prop("id");
  $this->{_groupsCache}{$id} = $obj;

  return $obj;
}

sub deleteCachedGroup {
  my ($this, $obj) = @_;

  my $id = $obj->prop("id");
  undef $this->{_groupsCache}{$id};
}

sub getCachedGroup {
  my ($this, $id) = @_;

  return unless defined $id && !ref($id) && $id ne "";
  return $this->{_groupsCache}{$id};
}

=begin TML

---++ ObjectMethod getObjectByID($id, $pid) -> $userOrGroup

creates a user or group object for the given id. 

=cut

sub getObjectByID {
  my ($this, $id, $pid) = @_;

  return $this->getUserByID($id, $pid) if $this->userExists(id => $id, pid => $pid);
  return $this->getGroupByID($id, $pid) if $this->groupExists(id => $id, pid => $pid);
  return;
}

=begin TML

---++ ObjectMethod getUserByID(id, pid) -> $user

creates a user object for the given id. note this object isn't loaded yet.
note that this will even return a user object if there is no object
in the database for the given id. Use =load()=, =findUser()= or =findGroup()= 
instead.

=cut

sub getUserByID {
  my ($this, $id, $pid) = @_;

  die "no id trying to get a user" unless defined $id;

  return Foswiki::PluggableAuth::User->new(
    id => $id,
    pid => $pid,
  );
}

=begin TML

---++ ObjectMethod getGroupByID(id, pid) -> $group

creates a group object for the given id. note this object isn't loaded yet.
note that this will even return a group object if there is no object
in the database for the given id. Use =load()= to find out.

=cut

sub getGroupByID {
  my ($this, $id, $pid) = @_;

  return Foswiki::PluggableAuth::Group->new(
    id => $id,
    pid => $pid
  );
}

=begin TML

---++ ObjectMethod switchToRegistrationAgent() -> $origUser

This method switches the current session user to the registration agent.
This is used temporarily when a new user registers to the system and certain
initialization steps are required such as updating his/her user profile or
membership. These steps are carried out using the registration agent instead.
The original user object is being returned to which the session is switched
back to using =$origUser->switch()= after these operations have been finished.

=cut

sub switchToRegistrationAgent {
  my $this = shift;

  my $registrationAgent = $this->getUserByID(Foswiki::Func::getCanonicalUserID($Foswiki::cfg{Register}{RegistrationAgentWikiName}));
  return $registrationAgent->switch();
}

=begin TML

---++ ObjectMethod getSelf() -> $user

returns a Foswiki::PluggableAuth::User object for the current session user

=cut

sub getSelf {
  my $this = shift;

  my $id = Foswiki::Func::getCanonicalUserID();
  return unless defined $id;
  return $this->getUserByID($id);
}

=begin TML

---++ ObjectMethod providerExists($id) -> $boolean

returns if the provider =$id= exists and is enabled.

=cut

sub providerExists {
  my ($this, $id) = @_;

  return 0 unless defined $id;
  my $cfg = $Foswiki::cfg{PluggableAuth}{Providers}{$id} || $INTERNALPROVIDERS{$id};
  return (defined($cfg) && $cfg->{Enabled}) ? 1 :0;
}

=begin TML

---++ ObjectMethod getProvider($id) -> $provider

returns a Foswiki::PluggableAuth::Provider object for the given =$id=.
An exception will be thrown if the provider is unknown or failed to compile.

=cut

sub getProvider {
  my ($this, $id) = @_;

  #confess("no id") unless defined $id;
  throw Error::Simple($this->maketext("No id trying to get a provider")) unless $id;

  my $provider = $this->{_providers}{$id};

  unless (defined $provider) {
    my $cfg = $Foswiki::cfg{PluggableAuth}{Providers}{$id} || $INTERNALPROVIDERS{$id};
    #confess("unknown provider $id") unless defined $cfg;
    throw Error::Simple($this->maketext("Unknown provider")) unless defined $cfg;
    return $this->{_providers}{Unknown} unless $cfg->{Enabled};

    my $package = $cfg->{Module} || 'Foswiki::PluggableAuth::Provider';
    eval "use $package;"; 
    if ($@ ne '') {
        #confess("Failed loading auth: $id with $@");
        throw Error::Simple($this->maketext("Failed loading auth provider: [_1]", "$@"));
    }

    $provider = $package->new($id, $cfg);
    if ($provider->init()) {
      $this->{_providers}{$id} = $provider;
    } else {
      $provider = undef;
    }
  }

  return $provider if $provider && $provider->isEnabled();
  return $this->{_providers}{Unknown};
}

=begin TML

---++ ObjectMethod getProviderOfDomain($domain) -> $provider(s)

returns a (list of) Foswiki::PluggableAuth::Provider object(s) that are configured
to handle a given =$domain=. Mostly Ldap identitiy providers may be covering objects
coming from a specific domain. An authentication provider such as Kerberos may
request the providers that may handle the user that just recently logged in via
this domain.

In list context all matching providers will be returned. In scalar context,
the first provider found will be returned.

=cut

sub getProviderOfDomain {
  my ($this, $domain) = @_;

  return unless $domain;
  $domain = lc($domain);

  my @providers = ();

  foreach my $provider ($this->getProviders) {
    my $provDomain = lc($provider->prop("DomainName") // "");
    push @providers, $provider if $provDomain =~ /\b\Q$domain\E\b/;
  }

  return wantarray ? @providers : $providers[0];
}

=begin TML

---++ ObjectMethod getRegistrationProvider() -> $provider

returns a Foswiki::PluggableAuth::Provider that is able to handle new user registrations.
Most of the time this is configured to be the Topic provider.

=cut

sub getRegistrationProvider {
  my $this = shift;

  return $this->getProvider($Foswiki::cfg{PluggableAuth}{RegistrationProvider});
}

=begin TML

---++ ObjectMethod getAdminGroup() -> $group

returns the admin group as per base provider

=cut


sub getAdminGroup {
  my $this = shift;

  return $this->getProvider("Base")->getAdminGroup();
}

=begin TML

---++ ObjectMethod findUser(%params) -> $user

fetches a user object for the given parameters from the database. Params maybe 
any combination of the user's properties (id, loginName, wikiName, email).
For example

<verbatim>
my $user $this->findUser(email=>'foo@bar.com');
</verbatim>

will retrun the user with the given email address.

Multiple parameters may be specified to query for either match:

<verbatim>
my $user $this->findUser(email=>'foo@bar.com', loginName => 'foo');
</verbatim>

will return the user which either matches the given email _or_ loginName.

If no matching user was found undef will be returned.

=cut

sub findUser {
  my ($this, %params) = @_;

  return Foswiki::PluggableAuth::User->new->find(%params);
}

=begin TML

---++ ObjectMethod findGroup(%params) -> $group

fetches a group object for the given parameters from the database. Params maybe 
any combination of the group's properties (id, wikiName, ...).
For example

<verbatim>
my $group $this->findGroup(wikiName=>'Group1');
</verbatim>

will retrun the group with the given name.

If no matching group was found undef will be returned.

=cut

sub findGroup {
  my ($this, %params) = @_;

  return Foswiki::PluggableAuth::Group->new->find(%params);
}

=begin TML

---++ ObjectMethod addUser(%params) -> $user

add a user to the database. %params describes the user:

   * id - optional, generates a uuid by default
   * pid - optional, defaults to 'provider-unknown' 
   * loginName - required
   * email - optional
   * wikiName - if undefined either displayName, firstName, middleNam, or lastName are required
   * displayName - optional
   * firstName - optional
   * middleName - optional
   * lastName - optional
   * initials - optional
   * picture - optional
   * registrationDate - optional, set to now by default

TODO:

   * telephoneNumber
   * mobileNumber
   * telefaxNumber

returns a Foswiki::PluggableAuth::User object for the newly created user

=cut

sub addUser {
  my ($this, %params) = @_;

  writeDebug("called addUser()");
  #writeDebug("params=".dump(\%params));

  throw Error::Simple($this->maketext("Unknown provider")) 
    unless $this->providerExists($params{pid});

  $params{id} //= $this->generateID('user');
  $params{registrationDate} //= time();

  writeDebug("... loginName=$params{loginName}, email=".($params{email}//'undef').", pid=$params{pid}");

  # process wikiName
  my $wikiName;
  if ($params{wikiName}) {
    $wikiName = $params{wikiName};
  } elsif (defined $params{displayName}) {
    $wikiName = $params{displayName};
  } else {
    my @parts = ();
    push @parts, $params{firstName} if defined $params{firstName};
    push @parts, $params{middleName} if defined $params{middleName};
    push @parts, $params{lastName} if defined $params{lastName};
    $wikiName = join(" ", @parts);
  }

  $wikiName = $this->normalizeWikiName($wikiName);
  throw Error::Simple($this->maketext("Sorry, access denied. No source for a wikiName.")) 
    unless defined $wikiName && $wikiName ne "";

  my ($firstName, $lastName) = extractNames($wikiName);
  $params{firstName} ||= $firstName;
  $params{lastName} ||= $lastName;
  $params{initials} ||= Foswiki::PluggableAuth::extractInitials(($params{firstName}||'') . " ". ($params{middleName} ||'') . " " . ($params{lastName}||''));
  $params{initials} ||= Foswiki::PluggableAuth::extractInitials(Foswiki::Func::spaceOutWikiWord($wikiName));

  unless (defined $params{displayName} && $params{displayName} ne "") {
    my @parts = ();
    foreach my $part (qw(firstName middleName lastName)) {
      push @parts, $params{$part} if defined $params{$part};
    }
    $params{displayName} = join(" ", @parts);
  }

  $wikiName = $this->getUniqueWikiName($wikiName);
  $params{wikiName} = $wikiName;

  my (@fields, @values, @q);
  while (my ($k, $v) = each %params) {
    next if $k =~ /^_/;
    push @fields, $k;
    push @values, $v;
    push @q, '?';
  }

  my $stm = "INSERT INTO PluggableAuth_users (".join(", ", @fields).") VALUES(".join(", ", @q).")";
  $this->db->handler->do($stm, {}, @values);

  my $user = $this->getUserByID($params{id}, $params{pid});

  $this->blockAllEvents;
  $user->createTopic;
  $this->unblockAllEvents;

  return $user;
}

=begin TML

---++ ObjectMethod addGroup(%params)

TODO

=cut

sub addGroup {
  my ($this, %params) = @_;

  writeDebug("called addGroup()");

  throw Error::Simple($this->maketext("Unknown provider")) unless $this->providerExists($params{pid});

  $params{id} ||= $this->generateID('group');

  my $groupName = $params{wikiName};
  throw Error::Simple($this->maketext("No group name specified")) unless defined $groupName;
  $params{displayName} //= $groupName;
  $params{wikiName} = $this->normalizeGroupName($groupName);

  my (@fields, @values, @q);
  while (my ($k, $v) = each %params) {
    next if $k =~ /^_/;
    push @fields, $k;
    push @values, $v;
    push @q, '?';
  }

  my $stm = "INSERT INTO PluggableAuth_groups (".join(", ", @fields).") VALUES(".join(", ", @q).")";
  $this->db->handler->do($stm, {}, @values);

  return $this->getGroupByID($params{id}, $params{pid});
}

=begin TML

---++ ObjectMethod userExists(%params) -> $boolean

TODO

=cut

sub userExists {
  my ($this, %params) = @_;

  return defined $this->findUser(%params) ? 1 : 0;
}

=begin TML

---++ ObjectMethod groupExists(%params) -> $boolean

=cut

sub groupExists {
  my ($this, %params) = @_;

  return defined $this->findGroup(%params) ? 1 : 0;
}

=begin TML

---++ ObjectMethod countUsers($pid) -> $boolean

returns the number of users of the given provider, or all users if pid is undefined

=cut

sub countUsers {
  my ($this, $pid) = @_;

  my $stm = "SELECT COUNT(*) FROM PluggableAuth_users";

  my @values = ();
  if ($pid) {
    $stm .= "WHERE pid=?" ;
    push @values, $pid;
  }

  #writeDebug("... stm = $stm");

  my @res = $this->db->handler->selectrow_array($stm, {}, @values);

  return $res[0];
}


=begin TML

---++ ObjectMethod eachUser(%params) -> $iterator

TODO

=cut

sub eachUser {
  my ($this, %params) = @_;

  #writeDebug("called eachUser");

  my @order = ();
  my @where = ();
  my @values = ();

  while (my ($k, $v) = each %params) {
    next unless defined $v && $v ne "";
    if ($k eq 'sort') {
      push @order, $v;
    } else {
      push @where, "$k=?";
      push @values, $v;
    }
  }

  my $where = @where ? " WHERE " . join(" AND ", @where) : "";
  my $order = @order ? " ORDER BY " . join(" AND ", @order) : "";
  
  my $stm = "SELECT * FROM PluggableAuth_users". $where . $order;
  #writeDebug("... stm=$stm");

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    $stm,
    \@values,
    sub {
      return Foswiki::PluggableAuth::User->new->init(shift);
    }
  );
}

=begin TML

---++ ObjectMethod eachUserIDs(%params) -> $iterator

TODO

=cut

sub eachUserIDs {
  my ($this, %params) = @_;

  #writeDebug("called eachUserIDs");

  my @order = ();
  my @where = ();
  my @values = ();

  while (my ($k, $v) = each %params) {
    next unless defined $v && $v ne "";
    if ($k eq 'sort') {
      push @order, $v;
    } else {
      push @where, "$k=?";
      push @values, $v;
    }
  }

  my $stm = "SELECT * FROM PluggableAuth_users WHERE ". join(" AND ", @where) . (@order?" ORDER BY ".join(", ", @order):"");

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    $stm,
    \@values,
    sub {
      my $row = shift;
      return $row->{id};
    }
  );
}

=begin TML

---++ ObjectMethod eachGroup(%params) -> $iterator

TODO

=cut

sub eachGroup {
  my ($this, %params) = @_;

  #writeDebug("called eachGroup");

  my @order = ();
  my @where = ();
  my @values = ();

  while (my ($k, $v) = each %params) {
    if ($k eq 'sort') {
      push @order, $v if $k eq 'sort';
    } else {
      push @where, "$k=?";
      push @values, $v;
    }
  }
  my $where = @where ? "WHERE ".join(" AND ", @where) : "";
  my $order = @order ? "ORDER BY ".join(", ", @order) : "";

  my $stm = "SELECT * FROM PluggableAuth_groups ".$where." ".$order;

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    $stm,
    \@values,
    sub {
      return Foswiki::PluggableAuth::Group->new->init(shift);
    }
  );
}

=begin TML

---++ ObjectMethod getProviders($all) -> $list

returns a list of all Foswiki::PluggableAuth::Provider objects.
If =$all= is true will even disabled providers be returned. Otherwise
only currently active providers will be returned.

=cut

sub getProviders {
  my ($this, $all) = @_;

  my $it = $this->eachProvider($all);
  my @providers = sort { $a->prop("Name") cmp $b->prop("Name") } $it->all;

  return @providers;
}

=begin TML

---++ ObjectMethod loadProviders()

loads all active providers. This is part of the initialization of this object.

=cut

sub loadProviders {
  my $this = shift;

  return if defined $this->{_providersTimeStamp};

  #writeDebug("called loadProviders()");
  $this->eachProvider();

  # update provider table if required
  my $timeStampFile = $this->getWorkArea("localSiteCfg.time");
  my $providersTimeStamp = _getModificationTime($timeStampFile);

  #writeDebug("timeStampFile=$timeStampFile");

  my $localSiteCfg = $INC{'LocalSite.cfg'};
  my $lastModified = _getModificationTime($localSiteCfg);

  if (!$lastModified || !$providersTimeStamp || $lastModified > $providersTimeStamp) {
    writeDebug("... updating providers table");
    # SMELL: only MySQL, MariaDB???
    my $stm = "REPLACE into PluggableAuth_providers (id, name, enabled) VALUES (?, ?, ?)";
    my $sth = $this->db->handler->prepare_cached($stm);
    my $it = $this->eachProvider(1);

    my $error;
    try {
      while ($it->hasNext) {
        my $provider = $it->next();
        my @values = (
          $provider->prop("id"), 
          $provider->prop("Name"),
          Foswiki::Func::isTrue($provider->prop("Enabled")) ? 1:0,
        );
        $sth->execute(@values);
      }
    } catch Error with {
      $error = shift;
    };
    $sth->finish();

    if (defined $error) {
      writeDebug("ERROR: $error");
      throw Error::Simple($this->maketext("Error during updateUser(): [_1]", $error));
    }

    Foswiki::Func::saveFile($timeStampFile, $lastModified);
  }

  $this->{_providersTimeStamp} = $lastModified;
}

=begin TML

---++ ObjectMethod eachProvider($all) -> $iterator

returns an iterator for all Foswiki::PluggableAut::Provider objects.
If =$all= is true even disabled providers will be returned.

=cut

sub eachProvider {
  my ($this, $all) = @_;

  #writeDebug("called eachProvider");

  my @providers = ();

  foreach my $id (keys %INTERNALPROVIDERS) {
    if ($all || $INTERNALPROVIDERS{$id}{Enabled}) {
      push @providers, $this->getProvider($id);
    }
  }

  foreach my $id (keys %{$Foswiki::cfg{PluggableAuth}{Providers}}) {
    if (($all || $Foswiki::cfg{PluggableAuth}{Providers}{$id}{Enabled}) && 
        defined $Foswiki::cfg{PluggableAuth}{Providers}{$id}{Module} &&
        defined $Foswiki::cfg{PluggableAuth}{Providers}{$id}{Name}) {

      my $provider;

      try {
        $provider = $this->getProvider($id);
      } catch Error with {
        my $error = shift;
        writeError("couldn't load provider '$id': $error") unless $all;
      };

      push @providers, $provider if defined $provider;
    }
  }

  return Foswiki::ListIterator->new(\@providers);
}

=begin TML

---++ ObjectMethod getUserAgent() -> $ua

returns a Foswiki::PluggableAuth::UserAgent object. 
This is a singleton object part of the Foswiki::PluggableAuth object

=cut

sub getUserAgent {
  my $this = shift;

  writeDebug("called getUserAgent");

  unless (defined $this->{_userAgent}) {
    writeDebug("... creating a userAgent");
    require Foswiki::PluggableAuth::UserAgent;
    $this->{_userAgent} = Foswiki::PluggableAuth::UserAgent->new();

    # DISABLE in production envs
    #$ua->ssl_opts(verify_hostname => 0);
  }

  return $this->{_userAgent};
}

=begin TML

---++ ObjectMethod getCertificateAuthority() -> $ca

returns a Foswiki::PluggableAuth::CertificateAuthority object.
This is a singleton object part of Foswiki::PluggableAuth object

=cut

sub getCertificateAuthority {
  my $this = shift;

  writeDebug("called getCertificateAuthority");

  unless (defined $this->{_ca}) {
    require Foswiki::PluggableAuth::CertificateAuthority;
    $this->{_ca} = Foswiki::PluggableAuth::CertificateAuthority->new();

  }
  return $this->{_ca};
}

=begin TML

---++ ObjectMethod getTwoFactorAuth()

returns a Foswiki::PluggableAuth::TwoFactorAuth object. 
This is a singleton object part of the Foswiki::PluggableAuth object

=cut

sub getTwoFactorAuth {
  my $this = shift;

  #writeDebug("called getTwoFactorAuth");

  unless (defined $this->{_2fa}) {
    #writeDebug("... creating 2fa");
    require Foswiki::PluggableAuth::TwoFactorAuth;
    $this->{_2fa} = Foswiki::PluggableAuth::TwoFactorAuth->new();
  }

  return $this->{_2fa};
}

=begin TML

---++ ObjectMethod getUniqueWikiName($wikiName) -> $uniqueWikiName

returns a wikiName that is guaranteed to be unique within the pluggable auth
user mapping.

=cut

sub getUniqueWikiName {
  my ($this, $wikiName) = @_;

  writeDebug("called getUniqueWikiName($wikiName)");

  my $serial = 1;
  my $newWikiName = $wikiName;
  while ($this->wikiNameExists($newWikiName)) {
    writeDebug("already found user $newWikiName ... renaming");
    $newWikiName = $wikiName . $serial++;
  }

  return $newWikiName;
}

=begin TML

---++ ObjectMethod wikiNameExists($wikiName) -> $boolean

returns true if the given =$wikiName= is already being used.

=cut

sub wikiNameExists {
  my ($this, $wikiName) = @_;

  my $res = $this->db->handler->selectcol_arrayref("SELECT id FROM PluggableAuth_users WHERE wikiName=?", {}, $wikiName);
  return (defined $res && scalar(@$res)) ? 1: 0;
}

=begin TML

---++ ObjectMethod generateID($prefix) -> $string

generates a unique id with an optional prefix. An optional
=$prefix= may be specified to be prepended to the result. This method
is used to generate ids when creating new user and group objects stored
into the database.

=cut

sub generateID {
  my ($this, $prefix) = @_;

  if (defined $prefix) {
    $prefix .= '-';
  } else {
    $prefix = '';
  }

  # secure enuf
  my $uuid = sprintf("%08X-%04X-%04X-%04X-%08X", 
    rand(0xFFFFFFFF) & 0xFFFFFFFF, 
    rand(0xFFFF) & 0xFFFF, 
    rand(0xFFFF) & 0xFFFF, 
    rand(0xFFFF) & 0xFFFF, 
    rand(0xFFFFFFFF) & 0xFFFFFFFF
  );

  return $prefix . $uuid;
}

=begin TML 

---++ ObjectMethod normalizeWikiName($name) -> $string

normalizes a string to form a proper <nop>WikiName

=cut

sub normalizeWikiName {
  my ($this, $name) = @_;

  return wikify($this->rewriteName($name, $Foswiki::cfg{PluggableAuth}{RewriteWikiNames}));
}

=begin TML 

---++ ObjectMethod normalizeGroupName($name) -> $string

create a proper group name by wikifying it and appending Group to it

=cut

sub normalizeGroupName {
  my ($this, $name) = @_;

  my $groupName = $this->rewriteName($name, $Foswiki::cfg{PluggableAuth}{RewriteGroupNames});

  if ($Foswiki::cfg{PluggableAuth}{NormalizeGroupNames}) {
    $groupName = wikify($name);
    $groupName =~ s/Group$//;
    $groupName .= "Group";
  } else {
    # at least filter some bad chars
    $groupName =~ s/[,@\(\)\s\-'"&\/]+/_/g;
    $groupName =~ s/__/_/g;
    $groupName =~ s/^_+//g;
    $groupName =~ s/_+$//g;
  }

  return $groupName;
}

=begin TML

---++ ObjectMethod isValidWikiName($name) -> $boolean

returns true if the given =$name= is a valid wikiName, i.e.
it is not prohibited by the {ExcludeWikiNames} setting

=cut

sub isValidWikiName {
  my ($this, $name) = @_;

  return $this->{_excludeWikiNames}{$name} ? 0 : 1;
}

=begin TML

---++ ObjectMethod isValidGroupName($name) -> $boolean

returns true if the given =$name= is a valid groupName, i.e.
it is not prohibited by the {ExcludeGroupNames} setting

=cut

sub isValidGroupName {
  my ($this, $name) = @_;

  return $this->{_excludeGroupNames}{$name} ? 0 : 1;
}

=begin TML

---++ ObjectMethod isValidLoginName($name) -> $boolean

returns true if the given =$name= is a valid loginName, i.e.
it is not prohibited by the {ExcludeLoginNames} setting

=cut

sub isValidLoginName {
  my ($this, $name) = @_;

  return $this->{_excludeLoginNames}{$name} ? 0 : 1;
}

=begin TML

---++ ObjectMethod rewriteName($in, $rules) -> $out

rewrites a name based on a set of rewrite rules

=cut

sub rewriteName {
  my ($this, $in, $rules) = @_;

  return $in unless $rules;

  my $out = $in;

  foreach my $pattern (keys %$rules) {
    my $subst = $rules->{$pattern};
    if ($out =~ /^(?:$pattern)$/) {
      my $arg1 = $1;
      my $arg2 = $2;
      my $arg3 = $3;
      my $arg4 = $4;
      my $arg5 = $5;
      $arg1 = '' unless defined $arg1;
      $arg2 = '' unless defined $arg2;
      $arg3 = '' unless defined $arg3;
      $arg4 = '' unless defined $arg4;
      $subst =~ s/\$1/$arg1/g;
      $subst =~ s/\$2/$arg2/g;
      $subst =~ s/\$3/$arg3/g;
      $subst =~ s/\$4/$arg4/g;
      $subst =~ s/\$5/$arg5/g;
      $out = $subst;
      writeDebug("rewriting '$in' to '$out' using rule $pattern");
    }
  }

  return $out;
}

=begin TML

---++ ObjectMethod getWorkArea()

returns a worki_area directory for PluggableAuthContrib. See Foswiki::Func::getWorkArea().

=cut

sub getWorkArea {
  my ($this, @path) = @_;

  return File::Spec->catfile(Foswiki::Func::getWorkArea("PluggableAuthContrib"), @path);
}

=begin TML

---++ ObjectMethod maketext($text, @args) -> $translation

deletages translation of =$text= to Foswiki::I18N::maketext().

=cut

sub maketext {
  my $this = shift;

  return $this->{session}->i18n->maketext(@_);
}

=begin TML

---++ StaticMethod extractInitials($string, $doTransliterate) -> $initials

TODO

=cut

sub extractInitials {
  my ($string, $doTransliterate) = @_;

  return unless defined $string;

  $doTransliterate //= 1;
  my $initials = "";

  while ($string =~ s/^(\w+)\W*//g) {
    my $char = substr($1, 0, 1);
    $initials .= $doTransliterate ? transliterate($char) : $char;
  }
  return $initials;
}

=begin TML

---++ StaticMethod extractNames($wikiName) -> ($firstName, $lastNAme)

extracts a first and last name from a wikiName

=cut

sub extractNames {
  my $wikiName = shift;

  my $initials = "";
  my $string = Foswiki::Func::spaceOutWikiWord($wikiName);
  my @parts = ();

  push @parts, $_ foreach split(/\s/, $string);

  my $firstName = shift @parts;
  my $lastName = join("", @parts);

  return ($firstName, $lastName);
}

=begin TML

---++ StaticMethod wikify($string) -> $wikiWord

takes an arbitrary string and constructs a wikiWord from it.
All non-ascii characters will be replaced by their nearby ascii counterparts
using Foswiki::PluggableAuth::transliterate.

=cut

sub wikify {
  my $name = shift;

  $name = transliterate($name);

  my $wikiName = '';

  # first, try without forcing each part to be lowercase
  foreach my $part (split(/[^$Foswiki::regex{mixedAlphaNum}]/, $name)) {
    $wikiName .= ucfirst($part);
  }

  return $wikiName;
}

=begin TML

---++ StaticMethod transliterate($string) -> $transString

returns a string where all unicode chars in =$string= have been rewritten
using similar ascii chars. In addition to Text::Unidecode common umlaut chars
are transliterated, such as a-umlaut to ae, u-umlaut to ue etc.

=cut

sub transliterate {
  my $string = shift;

  # custom ones
  $string =~ s/\xc4/Ae/go;    # A uml
  $string =~ s/\xe4/ae/go;    # a uml
  $string =~ s/\xe6/ae/go;    # ae
  $string =~ s/\xc6/AE/go;    # AE

  $string =~ s/\xd6/Oe/go;    # O uml
  $string =~ s/\xf6/oe/go;    # o uml
  $string =~ s/\xf8/oe/go;    # o stroke

  $string =~ s/\xdc/Ue/go;    # U uml
  $string =~ s/\xfc/ue/go;    # u uml

  # now go for Text::Unidecode
  return unidecode($string);
}

=begin TML

---++ StaticMethod writeDebug($string)

prints the given string to STDERR if in debug mode.

=cut

sub writeDebug {
  print STDERR "PluggableAuth - $_[0]\n" if TRACE || $Foswiki::cfg{PluggableAuth}{Debug};
  #Foswiki::Func::writeDebug("PluggableAuth - $_[0]") if $Foswiki::cfg{PluggableAuth}{Debug};
}

=begin TML

---++ StaticMethod writeError($string)

prints the given string to STDERR 

=cut

sub writeError {
  print STDERR 'PluggableAuth - ERROR: '.$_[0]."\n";
}

### testing helpers

sub _dumpUsers {
  my $this = shift;

  my $it = Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    "SELECT * from PluggableAuth_users",
    []
  );

  while($it->hasNext) {
    _dumpRow($it->next);
  }
}

sub _dumpGroups {
  my $this = shift;

  my $it = Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    "SELECT * from PluggableAuth_groups",
    []
  );

  while($it->hasNext) {
    _dumpRow($it->next);
  }
}

sub _dumpMembers {
  my $this = shift;

  my $it = Foswiki::Iterator::DBIterator->new(
    $this->db->handler, 
    "SELECT * from PluggableAuth_group_members",
    []
  );

  while($it->hasNext) {
    _dumpRow($it->next);
  }
}

### static helpers

sub _dumpRow {
  my $row = shift;
  print STDERR "| " . join(" | ", map {$row->{$_} // ''} sort keys %$row) . " |\n";
}

sub _inlineError {
  return "<span class='foswikiAlert'>$_[0]</span>";
}

sub _getModificationTime {
  my $path = shift;

  return 0 unless $path;

  my @stat = stat($path);

  return $stat[9] || $stat[10] || 0;
}

1;
