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

package Foswiki::PluggableAuth::Provider::Facebook;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Facebook

This is the Dropbox provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OAuth ();
#use Data::Dump qw(dump);

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{_endpoints} = {
    authorization => "https://www.facebook.com/dialog/oauth",
    token => "https://graph.facebook.com/oauth/access_token",
    debug => "https://graph.facebook.com/debug_token",
    user => "https://graph.facebook.com",
  };

  return $this;
}

=begin TML

---++ ObjectMethod getScopes() -> 'email'

returns the string 'email' as this is the only scope required for this provider.

=cut

sub getScopes {
  #my $this = shift;

  return 'email';
}

=begin TML

---++ ObjectMethod getUserId($accessToken) -> $userID

This method fetches the =user_id= from Facebook's =debug= endpoint.
The user id is required to further fetch user data.

=cut

sub getUserId {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called getUserId");

  my $endpoint = $this->getEndpoint("debug");

  my $appToken = $this->prop("ClientID") . "|" . $this->prop("ClientSecret");

  $endpoint .= "?input_token=$accessToken&access_token=$appToken";

  $this->writeDebug("... debug endpoint = $endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->get($endpoint);

  if (!$response->is_success){
    _writeError("facebook access_token verification failed");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We couldn't verify the validity of the claims we received from your provider.");
  }

  #$this->writeDebug("... response=".$response->decoded_content);

  my $json = $this->json->decode($response->decoded_content);

  #$this->writeDebug("... data=".dump($json));

  return $json->{data}{user_id};
}

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $data

This method fetches more user information for the current user including 
his profile picture.

=cut

sub fetchUser {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called fetchUserInfo");

  my $userId = $this->getUserId($accessToken);
  return unless defined $userId;

  my $endpoint = $this->getEndpoint("user");

  $endpoint .= "/".$userId . '?access_token='.$accessToken;
  $endpoint .= "&fields=first_name,last_name,picture,middle_name,name,short_name,id,email";

  $this->writeDebug("... user endpoint = $endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->get($endpoint);

  if (!$response->is_success){
    _writeError("failed to fetch facebook user info");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We couldn't fetch the user data of the claims we received from your provider.");
  }

  $this->writeDebug("... response=".$response->decoded_content);

  my $data = $this->json->decode($response->decoded_content);

  if (ref($data->{picture})) {
    $data->{picture} = $data->{picture}{data}{url};
  }
  
  return $data;
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::Facebook - ERROR: $_[0]\n";
}

1;

