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

package PluggableAuthHtPasswdTests;

use strict;
use warnings;
use utf8;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth::HtPasswd ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub tear_down {
  my $this = shift;

  $this->SUPER::tear_down();
  undef $this->{_htpasswd};
}

sub test_self {}

sub htPasswd {
  my $this = shift;

  unless (defined $this->{_htpasswd}) {
    require Foswiki::PluggableAuth::HtPasswd;
    $this->{_htpasswd} = Foswiki::PluggableAuth::HtPasswd->new();
  }

  return $this->{_htpasswd};
}

sub test_readPasswords {
  my $this = shift;

  my $data = $this->htPasswd->read;
  $this->assert_equals(7, scalar(keys %$data), "should be 7 passwd entries");
}

sub test_getPassword {
  my $this = shift;

  my ($pw, $entry) = $this->htPasswd->getPassword("alice_t");
  $this->assert($pw);
  $this->assert($entry);
  $this->assert_equals('alice@foo.bar', $entry->{emails});
}

sub test_eachEntry {
  my $this = shift;

  my $it = $this->htPasswd->eachEntry();
  while ($it->hasNext) {
    my $entry = $it->next;
    #print STDERR "entry=".dump($entry)."\n";
    $this->assert($entry);
    $this->assert($entry->{login});
    $this->assert($entry->{enc});
    $this->assert(defined($entry->{emails}));
    $this->assert($entry->{pass});
  }
}

sub test_dumpPasswords {
  my $this = shift;

  $this->htPasswd->read;
  my $content = $this->htPasswd->dumpPasswords();
  $this->assert($content);

  $content =~ s/:.*:/:x:/g;

  my $shouldBe = <<'HERE';
alice_t:x:alice@foo.bar
alligator:x:
bat:x:
budgie:x:
dodo:x:dodo@extinct
frank_t:x:frank@foo.bar
mole:x:mole@hill
HERE

  $this->assert_equals($shouldBe, $content);
}

sub test_savePassword {
  my $this = shift;

  $this->htPasswd->savePassword(
    uid => "alice",
    encoding => "plain",
    password => "foobar"
  );

  my $passwd = $this->htPasswd->getPassword("alice");
  $this->assert_equals("foobar", $passwd);
}

1;
