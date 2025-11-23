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

package Foswiki::PluggableAuth::Provider::Dropbox;

=begin TML

---+ package Foswiki::PluggableAuth::Provder::Dropbox

This is the Dropbox provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OAuth ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

#use Data::Dump qw(dump);

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{_endpoints} = {
    authorization => "https://www.dropbox.com/oauth2/authorize",
    token => "https://api.dropboxapi.com/oauth2/token",
    user => "https://api.dropboxapi.com/2/users/get_current_account",
  };
  
  $this->{_scopes} = '';

  return $this;
}

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $data;

This method fetches more user data from Dropbox's user endpoint.

=cut

sub fetchUser {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called fetchUser()");

  my $endpoint = $this->getEndpoint("user");

  $this->writeDebug("... endpoint=$endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->post($endpoint, 
    "Authorization" => "Bearer $accessToken",
    "Content-Type" => "application/json",
    "Content" => "null"
  );

  if (!$response->is_success){
    _writeError("failed to fetch user info");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We couldn't fetch the user data of the claims we received from your provider.");
  }

  #$this->writeDebug("... response=".$response->decoded_content);

  my $data = $this->json->decode($response->decoded_content);

  #$this->writeDebug("... user data=".dump($data));

  return $data;
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::Dropbox - ERROR: $_[0]\n";
}

1;

