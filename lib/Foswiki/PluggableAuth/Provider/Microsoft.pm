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

package Foswiki::PluggableAuth::Provider::Microsoft;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Microsoft

This is the Microsoft/Azure provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OpenID ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OpenID );

=begin TML

---++ ObjectMethod getDiscoveryUri() -> $uri

This method returns the url of the discovery endpoint for the <nop>OpenID protocol.

=cut

sub getDiscoveryUri {
  my $this = shift;

  return 'https://login.microsoftonline.com/'.$this->prop("Tenant").'/v2.0/.well-known/openid-configuration';
}

=begin TML

---++ ObjectMethod discovery() -> $config

adds an extra =appid= parameter to the jwks_uri as micrsoft doesnt do so by default.
only then will the public keys be discovered as required to decrypt the user id token.

=cut

sub discoverConfig {
  my $this = shift;

  my $config = $this->SUPER::discoverConfig();

  if ($this->prop("DiscoveryHack")) {
    my $endpoint = $config->{'jwks_uri'};
    if ($endpoint && !($endpoint =~ /appid=/)) {
      $endpoint .= "?appid=".$this->prop("ClientID");
      $config->{jwks_uri} = $endpoint;
    }
  }

  return $config;
}

1;
