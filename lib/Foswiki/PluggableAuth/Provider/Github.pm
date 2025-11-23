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

package Foswiki::PluggableAuth::Provider::Github;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Github

This is the Github provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

#use Data::Dump qw(dump);
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
    authorization => "https://github.com/login/oauth/authorize",
    token => "https://github.com/login/oauth/access_token",
    user => "https://api.github.com/user",
  };

  return $this;
}

=begin TML

---++ ObjectMethod getScopes() -> 'user'

returns the string 'user' as this is the only scope required for this provider

=cut

sub getScopes {
  my $this = shift;

  return 'user';
}

=begin TML

---++ ObjectMethod retrieveTokenOfCode($code, $state) -> $accessToken

This method retrieves an access token for the current oauth exchange

=cut

sub retrieveTokenOfCode {
  my ($this, $code, $state) = @_;

  $this->writeDebug("called retrieveTokenOfCode($code)");

  my $endpoint = $this->getEndpoint("token");

  $this->writeDebug("token endpoint = $endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->post($endpoint, {
      client_id => $this->prop("ClientID"),
      client_secret => $this->prop("ClientSecret"),
      redirect_uri => $this->getRedirectUri($state),
      code => $code,
      grant_type => "authorization_code"
    },
    Accept => "application/json",
  );

  unless ($response->is_success) {
    _writeError("Protocol error: Couldn't exchange auth code for token.");
    _writeError("response msg=" . $response->message);# . " content=" . $response->decoded_content);
    throw Error::Simple("We encountered a protocol error while trying to redeem an authorization code with your provider.");
  } 

  $this->writeDebug("... response=".$response->decoded_content);

  my $data = $this->json->decode($response->decoded_content);

  #$this->writeDebug("... data=".dump($data));

  return $data->{access_token};
}

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $data

This method fetches more user information for the current user.

=cut

sub fetchUser {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called fetchUser()");

  my $endpoint = $this->getEndpoint("user");

  #$endpoint .= "/".$userId;# . '?access_token='.$idToken;
  #$endpoint .= "&fields=first_name,last_name,picture,middle_name,name,short_name,id,email";

  $this->writeDebug("... endpoint=$endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->get($endpoint, 
    Authorization => "token $accessToken"
  );

  if (!$response->is_success){
    _writeError("failed to fetch github user info");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We couldn't fetch the user data of the claims we received from your provider.");
  }

  #$this->writeDebug("... response=".$response->decoded_content);

  return $this->json->decode($response->decoded_content);
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::Github - ERROR: $_[0]\n";
}

1;

