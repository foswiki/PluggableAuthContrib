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

package PluggableAuthUnknownProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Base ();
use Foswiki();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  $this->{provider} = $this->{auth}->getProvider("Unknown");
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Unknown"), "Not a Foswiki::PluggableAuth::Provider::Unknown");
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

sub test_wrongProvider {
  my $this = shift;

  $this->assert("Unknown", $this->{provider}->prop("Name"), "wrong name");
  $this->assert("Unknown", $this->{provider}->prop("id"), "wrong id");

  my $provider;
  my $error;

  try {
    $provider = $this->{auth}->getProvider("FooBar");
  } catch Error with {
    $error = shift;
  };

  $this->assert($error);
}

sub test_disabledProvider {
  my $this = shift;

  my $provider = $this->{auth}->getProvider("test");
  $this->assert($provider);
  $this->assert_equals("test", $provider->prop("id"));

  $provider->disable();

  $provider = $this->{auth}->getProvider("test");
  $this->assert($provider);
  $this->assert_equals("Unknown", $provider->prop("id"));
}

1;
