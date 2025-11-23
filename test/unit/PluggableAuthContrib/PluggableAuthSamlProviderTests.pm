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

package PluggableAuthSamlProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Saml ();
use Error qw(:try);

our @ISA = qw( PluggableAuthTestCase );

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  $Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Enabled} = 1;
  $this->{provider} = $this->{auth}->getProvider("SAML");
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Saml"));
}

sub test_buildAuthRequest {
  my $this = shift;

  my $url = $this->{provider}->buildAuthRequest();
  $this->assert($url);
}

1;
