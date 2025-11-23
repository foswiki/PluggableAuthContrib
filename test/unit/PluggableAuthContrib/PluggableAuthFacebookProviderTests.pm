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

package PluggableAuthFacebookProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Facebook ();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( PluggableAuthTestCase );

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  $Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Enabled} = 1;
  $this->{provider} = $this->{auth}->getProvider("Facebook");
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Facebook"));
}

sub test_id {
  my $this = shift;

  my $pid = $this->{provider}->prop("id");
  $this->assert_equals("Facebook", $pid);
}

sub test_props {
  my $this = shift;

  my $props = $this->{provider}->props;
  #print STDERR "props=".dump($props)."\n";

  $this->assert($props->{Enabled});
  $this->assert($props->{Name});
  $this->assert($props->{Module});
  $this->assert($props->{Visible});
  #$this->assert($props->{ClientID});
  #$this->assert($props->{ClientSecret});
}

1;
