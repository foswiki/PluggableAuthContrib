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

package Foswiki::PluggableAuth::Provider::Twitch;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Twitch

This is the Twitch provider based on Foswiki::PluggableAuth::Provider::OAuth.

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

  return "https://id.twitch.tv/oauth2/.well-known/openid-configuration";
}

=begin TML

---++ ObjectMethod buildAuthRequest($state)

This is a slightly different implementation compared to the sueper class' one
catering to the specifics of Discord.

=cut


sub buildAuthRequest {
  my ($this, $state) = @_;

  $this->writeDebug("called buildAuthRequest");

  my %params = (
    client_id => $this->prop("ClientID"),
    response_type => "code",
    scope => "openid user:read:email",
    redirect_uri => $this->getRedirectUri($state),
    state => $state->{key},
    claims => '{"id_token":{"email":null,"email_verified":null, "picture":null, "preferred_username": null}}',
  );

  my @query = ();
  foreach my $key (keys %params) {
    my $val = $params{$key};
    push @query, $key . "=" . Foswiki::urlEncode($val) if defined $val;
  }

  my $endpoint = $this->getEndpoint("authorization");
  $this->writeDebug("... auth endpoint=".($endpoint//'undef'));
  $endpoint .= "?" . join("&", @query);

  return $endpoint;
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::OpenID - ERROR: $_[0]\n";
}

1;


