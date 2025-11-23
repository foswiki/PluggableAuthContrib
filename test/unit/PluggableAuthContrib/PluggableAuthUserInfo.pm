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

package PluggableAuthUserInfo;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub new {
  $Foswiki::cfg{Register}{AllowLoginName} = 1;
  my $self = shift()->SUPER::new();

  $Foswiki::cfg{DefaultDateFormat} = '$day $month $year';

  return $self;
}

sub test_basic {
  my $this = shift;

  $Foswiki::cfg{AntiSpam}{HideUserDetails} = 0;
  my $result = $this->{test_topicObject}->expandMacros('%USERINFO%');
  $this->assert_matches(qr/^$Foswiki::cfg{AdminUserLogin}, $Foswiki::cfg{UsersWebName}.$Foswiki::cfg{AdminUserWikiName}, .*@.*$/, $result);
}

sub test_withWikiName {
  my $this = shift;

  $Foswiki::cfg{AntiSpam}{HideUserDetails} = 0;
  my $result = $this->{test_topicObject}->expandMacros('%USERINFO{"AliceWeinstein"}%');
  $this->assert_str_equals("alice, $Foswiki::cfg{UsersWebName}.AliceWeinstein, alice\@foo.bar", $result);
}

sub test_withLogin {
  my $this = shift;

  $Foswiki::cfg{AntiSpam}{HideUserDetails} = 0;
  my $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice"}%');
  $this->assert_str_equals("alice, $Foswiki::cfg{UsersWebName}.AliceWeinstein, alice\@foo.bar", $result);
}

sub test_formatted {
  my $this = shift;

  $Foswiki::cfg{AntiSpam}{HideUserDetails} = 0;
  $this->{session}{context}{isadmin} = 0;
  my $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$id"}%');
  $this->assert_matches(qr/^user\-[A-Z0-9]+\-[A-Z0-9]+\-[A-Z0-9]+\-[A-Z0-9]+\-[A-Z0-9]+$/, $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$pid"}%');
  $this->assert_str_equals("test", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$loginName"}%');
  $this->assert_str_equals("alice", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$wikiName"}%');
  $this->assert_str_equals("AliceWeinstein", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$displayName"}%');
  $this->assert_str_equals("Alice Weinstein", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$email"}%');
  $this->assert_str_equals('alice@foo.bar', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$firstName"}%');
  $this->assert_str_equals('Alice', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$middleName"}%');
  $this->assert_str_equals('', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$lastName"}%');
  $this->assert_str_equals('Weinstein', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$initials"}%');
  $this->assert_str_equals('AW', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$enabled"}%');
  $this->assert_str_equals('1', $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$picture"}%');
  $this->assert_str_equals("$Foswiki::cfg{PubUrlPath}/$Foswiki::cfg{SystemWebName}/PluggableAuthContrib/nobody.png", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$registrationDate"}%');
  my $now = Foswiki::Time::formatTime(time());
  $this->assert_str_equals($now, $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$loginDate"}%');
  $this->assert_str_equals("", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$twoFactorAuth"}%');
  $this->assert_str_equals("", $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$twoFactorAuthEnabled"}%');
  $this->assert_str_equals(0, $result);

  $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$twoFactorAuthConfigured"}%');
  $this->assert_str_equals(0, $result);
}

sub test_cloaked {
  my $this = shift;

  $Foswiki::cfg{AntiSpam}{HideUserDetails} = 1;
  $this->{session}{context}{isadmin} = 0;

  foreach my $token (qw(id pid loginName wikiName displayName email 
                        firstName middleName lastName initials enabled
                        registrationDate picture
                       )) {
    my $result = $this->{test_topicObject}->expandMacros('%USERINFO{"alice" format="$'.$token.'"}%');
    $this->assert_str_equals('', $result);
  }
}

1;
