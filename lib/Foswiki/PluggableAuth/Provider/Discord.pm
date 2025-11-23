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

package Foswiki::PluggableAuth::Provider::Discord;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Discord

This is the Discord provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OAuth ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{_endpoints} = {
    authorization => 'https://discord.com/api/oauth2/authorize',
    token => 'https://discord.com/api/oauth2/token',
    user => 'https://discord.com/api/v8/users/@me',
  };

  $this->{_scopes} = 'identify email';

  return $this;
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
    scope => $this->getScopes,
    redirect_uri => $this->getRedirectUri($state),
    state => $state->{key},
    prompt => "none",
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

=begin TML

---++ ObjectMethod extractUserInfo($idToken) -> $userInfo

In addition to Foswiki::PluggableAuth::Provider::OAuth::extractUserInfo()
this method adds the avatar image as a picture to the =$userInfo= hash.

=cut

sub extractUserInfo {
  my ($this, $idToken) = @_;

  my $userInfo = $this->SUPER::extractUserInfo($idToken);

  if ($userInfo->{picture}) {
    $userInfo->{picture} = 'https://cdn.discordapp.com/avatars/'.$idToken->{id}.'/'.$userInfo->{picture}.'.png';

    $this->writeDebug("picture=$userInfo->{picture}");
  }

  return $userInfo;
}

1;
