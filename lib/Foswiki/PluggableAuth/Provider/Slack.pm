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

package Foswiki::PluggableAuth::Provider::Slack;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Slack

This is the Slack provider based on Foswiki::PluggableAuth::Provider::OAuth.

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
    authorization => "https://slack.com/oauth/v2/authorize",
    token => "https://slack.com/api/oauth.v2.access",
    user => "https://slack.com/api/users.identity",
  };

  $this->{_scopes} = 'identity.basic identity.email identity.avatar';

  return $this;
}

=begin TML

---++ ObjectMethod buildAuthRequest($state) -> $url

This method constructs the authentication endpoint.

=cut

sub buildAuthRequest {
  my ($this, $state) = @_;

  $this->writeDebug("called buildAuthRequest");

  my %params = (
    client_id => $this->prop("ClientID"),
    response_type => "code",
    user_scope => $this->getScopes,
    redirect_uri => $this->getRedirectUri($state),
    state => $state->{key},
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

---++ ObjectMethod extractAccessToken($data) -> $accessToken

This method extracts the =access_token= from the data returned at this
stage of the protocol as this is stored a little bit differently compared to
Foswiki::PluggableAuth::Provider::OAuth::extractAccessToken().

=cut

sub extractAccessToken {
  my ($this, $data) = @_;

  return $data->{authed_user}{access_token};
}

1;
