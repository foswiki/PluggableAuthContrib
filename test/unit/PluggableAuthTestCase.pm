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

package PluggableAuthTestCase;

use strict;
use warnings;
use utf8;

use Foswiki ();
use FoswikiTestCase;
use Foswiki::PluggableAuth ();
use File::Temp;
use Foswiki();
use Unit::Request();
use Unit::Response();
use Foswiki::Plugins::DBIPlugin();
use Foswiki::Plugins::TopicTitlePlugin();

our @ISA = qw( FoswikiTestCase );

sub new {
  my $this = shift()->SUPER::new(@_);

  $this->{test_web}   = 'TemporaryPluggableAuth';
  $this->{test_topic} = 'TestTopic';
  $this->{test_users_web} = $this->{test_web};
  $this->{test_users_topic} = 'WikiUsers';
  $this->{workingDir} = File::Temp::tempdir(CLEANUP => 1);
  $this->{fileName} = $this->{workingDir} . '/pluggableAuth.db';

  $Foswiki::cfg{DBI}{Implementation} = 'Foswiki::DBI::Database::SQLite';
  $Foswiki::cfg{DBI}{SQLite}{Filename} = $this->{fileName};
  $Foswiki::cfg{Cache}{Enabled} = 0;
  $Foswiki::cfg{PluggableAuth}{EnableGravatarFallback} = 0;

  $Foswiki::cfg{UsersWebName} = $this->{test_users_web};
  $Foswiki::cfg{UsersTopicName} = $this->{test_users_topic};

  return $this;
}

sub createRequest {
  my $this = shift;

  $this->{request} = new Unit::Request("") unless defined $this->{request};
  $this->{request}->path_info("/$this->{test_web}/$this->{test_topic}");

  return $this->{request};
}

sub createSession {
  my $this = shift;

  unless (defined($this->{session})) {

    $this->createRequest();
    $this->createNewFoswikiSession($Foswiki::cfg{AdminUserLogin}, $this->{request});
  }

  return $this->{session};
}

sub createWebs {
  my $this = shift;

  #print STDERR "### createWebs\n";
  #print STDERR "... creating web '$this->{test_users_web}'\n";
  Foswiki::Func::createWeb($this->{test_users_web});
}

sub createWikiUsers {
  my $this = shift;

  #print STDERR "called createWikiUsers\n";

  my $text = <<'TEXT';
   * A - <a name="A">- - - -</a>
   * AliceWeinstein - alice_t - 17 Jun 2020
   * B - <a name="B">- - - -</a>
   * C - <a name="C">- - - -</a>
   * D - <a name="D">- - - -</a>
   * E - <a name="E">- - - -</a>
   * F - <a name="F">- - - -</a>
   * FrankNStein - frank_t - 16 Jun 2020
   * G - <a name="G">- - - -</a>
   * H - <a name="H">- - - -</a>
   * I - <a name="I">- - - -</a>
   * J - <a name="J">- - - -</a>
   * K - <a name="K">- - - -</a>
   * L - <a name="L">- - - -</a>
   * M - <a name="M">- - - -</a>
   * N - <a name="N">- - - -</a>
   * O - <a name="O">- - - -</a>
   * P - <a name="P">- - - -</a>
   * ProjectContributor - 1 Jan 2005
   * Q - <a name="Q">- - - -</a>
   * R - <a name="R">- - - -</a>
   * RegistrationAgent - 1 Jan 2005
   * S - <a name="S">- - - -</a>
   * T - <a name="T">- - - -</a>
   * U - <a name="U">- - - -</a>
   * UnknownUser - 1 Jan 2005
   * V - <a name="V">- - - -</a>
   * W - <a name="W">- - - -</a>
   * WikiGuest - guest - 10 Feb 1999
   * X - <a name="X">- - - -</a>
   * Y - <a name="Y">- - - -</a>
   * Z - <a name="Z">- - - -</a>
TEXT

  Foswiki::Func::saveTopic($this->{test_users_web}, $this->{test_users_topic}, undef, $text);

  open(my $fh, '>:encoding(utf-8)', $this->{htPasswd})
    || die "Unable to open \n $! \n\n ";
  print $fh <<'DONE';
alligator:njQ4t57Dts41s
bat:$apr1$9/PfK37z$HrNORnyJefA2ex4nWLOoR1
budgie:{SHA}1pqeQCvCHCfCrnFA8mTGYna/DV0=
dodo:$1$pUXqkX97$zqxdNSnpusVmoB.B.aUhB/:dodo@extinct
frank_t:MyNewRealmm:3e60f5f16dc3b8658879d316882a3f00:frank@foo.bar
mole:plainpasswordx:mole@hill
alice_t:$2a$08$STPELUTxMRf2Y0v1J1nWaOXH1mdWf9VzPlGQ9NgIFU.9B/GCGpC8G:alice@foo.bar
DONE

  close($fh);
}

sub createLotsOfUsers {
  my $this = shift;

  #print STDERR "called createLotsOfUsers\n";
  $this->{auth}->blockAllEvents;

  my @wikiUsers = ();
  my @mapping = ();
  my @logins = ();
  for my $i (1 .. 100) {
    my $wikiName = "TestUser$i";
    my $loginName = "testUser$i";
    my $email = "test$i\@foo.bar";

    my $salt = Foswiki::generateRandomChars(2, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./');
    my $hash = crypt($email, substr($salt, 0, 2));

    push @wikiUsers, $wikiName;
    Foswiki::Func::saveTopic($this->{test_users_web}, $wikiName, undef, "");

    push @mapping, "   * $wikiName - $loginName - 16 Jun 2020";
    push @logins, "$loginName:$hash:$email";
  }

  my ($meta, $text) = Foswiki::Func::readTopic($this->{test_users_web}, $this->{test_users_topic});

  $text =~ s/^(   \* T.*\n)/$1.join("\n", @mapping)."\n"/me;

  $meta->text($text);  
  $meta->save();

  my $content = Foswiki::Func::readFile($this->{htPasswd});
  $content =~ s/\n+$//g;
  $content .= "\n".join("\n", @logins);

  $this->{wikiUsers} = \@wikiUsers;

  #print STDERR "... created ".scalar(@wikiUsers)." user(s)\n";

  Foswiki::Func::saveFile($this->{htPasswd}, $content);

  $this->{auth}->unblockAllEvents;
}

sub createLotsOfGroups {
  my $this = shift;

  $this->{auth}->blockAllEvents;

  my @groups = ();
  $this->{wikiUsers} //= [];
  my $nrWikiUsers = scalar(@{$this->{wikiUsers}});
  for my $i (1..100) {
    my $groupName = "Test".$i."Group";

    my @members = ();
    for my $j (1..10) {
      my $member = $this->{wikiUsers}->[int(rand($nrWikiUsers))];
      push @members, $member if defined $member;
    }
    for my $j (1..2) {
      my $member = $groups[int(rand(scalar(@groups)))];
      push @members, $member if defined $member;
    }
    
    my $members = join(", ", @members);

    my $text = <<"TEXT";
%META:PREFERENCE{name="GROUP" title="GROUP" type="Set" value="$members"}%
TEXT

    push @groups, $groupName;
    Foswiki::Func::saveTopic($this->{test_users_web}, $groupName, undef, $text);
  }

  $this->{groups} = \@groups;

  #print STDERR "... created ".scalar(@groups)." group(s)\n";
  $this->{auth}->unblockAllEvents;
}

sub populateDatabase {
  my $this = shift;

  #print STDERR "### populateDatabase\n";
  $this->{auth}->refresh("Base");

  #print STDERR "### dumpUsers()\n";
  #$this->{auth}->_dumpUsers();

  #print STDERR "### dumpMembers()\n";
  #$this->{auth}->_dumpMembers();

  $Foswiki::PluggableAuth::INTERNALPROVIDERS{test} = {
    Enabled => 1,
    Name => "Test Mapping",
    DomainName => "test.domain.com",
    Visible => 1,
    Module => "PluggableAuthTestProvider",
  };

  $Foswiki::PluggableAuth::INTERNALPROVIDERS{test2} = {
    Enabled => 1,
    Name => "Test Mapping 2",
    DomainName => "test2.domain.com",
    Visible => 1,
    Module => "PluggableAuthTestProvider",
  };

  $Foswiki::PluggableAuth::INTERNALPROVIDERS{test3} = {
    Enabled => 1,
    Name => "Test Mapping 3",
    DomainName => "test2.domain.com",
    Visible => 1,
    Module => "PluggableAuthTestProvider",
  };

  my %groups = ();
  foreach my $name (qw(Group1 Group2 Group3)) {
    my $group = $groups{$name} = $this->{auth}->addGroup(
      pid => "test",
      wikiName => $name,
      #id => $name, # just enable for testing the tests. except test_stringify_group as it will fail if commented out
    );
    $group->createTopic();
  }

  my %users = ();
  $users{user1} = $this->{auth}->addUser(
    pid => "test",
    loginName => "frank",
    firstName => "Frank",
    middleName => "N",
    lastName => "Stein",
    email => 'frank.n.stein@foo.bar',
  );

  $users{user2} = $this->{auth}->addUser(
    pid => "test",
    loginName => "alice",
    wikiName => "Alice Weinstein",
    email => 'alice@foo.bar',
  );

  $groups{Group1}->setMembers([$users{user1}, $groups{Group2}]);
  $groups{Group2}->setMembers([$users{user2}]);

  # same as ...
  #$groups{Group1}->addMember($users{user1});
  #$groups{Group1}->addMember($groups{Group2});
  #$groups{Group2}->addMember($users{user2});

  if (0) {
    print STDERR "\n###\n";
    foreach my $user (values %users) {
      print STDERR $user->prop("wikiName") ." = ".$user->prop("id")."\n";
    }

    print STDERR "### dumpGroups()\n";
    $this->{auth}->_dumpGroups();

    print STDERR "### dumpMembers()\n";
    $this->{auth}->_dumpMembers();

    print STDERR "###\n\n";
  }
}

sub set_up {
  my $this = shift;

  #print STDERR "### set_up\n";
  $Foswiki::cfg{AdminUserLogin} = 'root'; # SMELL: make sure this is set early enuf

  $this->SUPER::set_up(@_);

  # config settings
  Foswiki::Plugins::DBIPlugin::finishPlugin();

  $Foswiki::cfg{Htpasswd}{FileName} = $this->{htPasswd} = "$Foswiki::cfg{TempfileDir}/junkpasswd";
  $Foswiki::cfg{DBI}{Implementation} = 'Foswiki::DBI::Database::SQLite'; # only testing sqlite
  $Foswiki::cfg{DBI}{SQLite}{Filename} = $this->{pauthDB} = "$Foswiki::cfg{TempfileDir}/pauthDB";

  $this->createSession();
  $this->{auth} = Foswiki::PluggableAuth->new();

  $this->createWebs();
  $this->populateDatabase();
  $this->createWikiUsers();

  $this->{auth}->getProvider("test")->{beforeSaveHandlerCounter} = 0;
  $this->{auth}->getProvider("test2")->{beforeSaveHandlerCounter} = 0;
  $this->{auth}->getProvider("test")->{afterSaveHandlerCounter} = 0;
  $this->{auth}->getProvider("test2")->{afterSaveHandlerCounter} = 0;

}

sub tear_down {
  my $this = shift;

  #print STDERR "### tear_down\n";
  if (defined $this->{session}) {
    $this->removeWebFixture( $this->{session}, $this->{test_users_web});
    undef $this->{request};
    undef $this->{session};
    unlink $this->{htPasswd} if -e $this->{htPasswd};
  }

  $this->{auth}->db->handler->do("delete from db_meta where type='PluggableAuth'");
  $this->{auth}->db->handler->do("drop table PluggableAuth_group_members");
  $this->{auth}->db->handler->do("drop table PluggableAuth_groups");
  $this->{auth}->db->handler->do("drop table PluggableAuth_users");

  Foswiki::Plugins::DBIPlugin::finishPlugin();

  $this->{auth}->finish;

  undef $this->{auth};
  unlink $this->{pauthDB} if -e $this->{pauthDB};

  $this->SUPER::tear_down();
}

sub assert_user {
  my ($this, $user) = @_;

  $this->assert($user, "Must not be NULL");
  $this->assert(ref($user), "Not a reference");
  $this->assert($user->isa("Foswiki::PluggableAuth::User"), "Not a Foswiki::PluggableAuth::User");
}

sub assert_group {
  my ($this, $group) = @_;

  $this->assert($group, "Must not be NULL");
  $this->assert(ref($group), "Not a reference");
  $this->assert($group->isa("Foswiki::PluggableAuth::Group"), "Not a Foswiki::PluggableAuth::Group");
}

sub assert_provider {
  my ($this, $provider) = @_;

  $this->assert($provider, "Must not be NULL");
  $this->assert(ref($provider), "Not a reference");
  $this->assert($provider->isa("Foswiki::PluggableAuth::Provider"), "Not a Foswiki::PluggableAuth::Provider");
}

1;
