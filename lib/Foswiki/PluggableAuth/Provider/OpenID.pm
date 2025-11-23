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

package Foswiki::PluggableAuth::Provider::OpenID;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::OpenID

TODO

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::PluggableAuth::Provider::OAuth ();
use Crypt::JWT();
use MIME::Base64 ();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

sub finish {
  my $this = shift;

  $this->SUPER::finish;

  undef $this->{_openid_config};
}

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin");

  my $code = $request->param('code');
  my $error = $request->param('error');

  #$this->writeDebug("code=".($code//'undef').", error=".($error//'undef'));
  $this->writeDebug("error=".$error) if defined $error;
  return unless defined $code;

  $request->delete('code', 'error', 'pauth_provider', 'state');
  throw Error::Simple("ERROR: ".$error) if $error;

  $code = Foswiki::urlDecode($code);

  my $idToken = $this->retrieveTokenOfCode($code, $state);
  return unless $idToken;

  my $userInfo = $this->extractUserInfo($idToken);
  return unless defined $userInfo && defined $userInfo->{loginName};

  my $user = $this->findUser(
    loginName => $userInfo->{loginName},
  );

  my $isNewUser = 0;
  if (defined $user) {
    $user = $this->updateUser($user, $userInfo) if $this->prop("SyncOnLogin");
  } else {
    $isNewUser = 1;
    $user = $this->addUser(%$userInfo);
  }

  # track old membership
  my %oldMembership = ();

  unless ($isNewUser) {
    my $groupIt = $user->eachMembership(0);
    while ($groupIt->hasNext) {
      my $group = $groupIt->next;
      next if $group->prop("pid") ne $this->prop("id");

      $oldMembership{$group->prop("id")} = $group;
    }
  }

  # add user to groups
  my $groups = $this->extractGroupInfo($idToken);
  if ($groups) {
    foreach my $name (@$groups) {
      $name = $this->auth->normalizeGroupName($name);
      
      unless ($this->auth->isValidGroupName($name)) {
        $this->writeDebug("... $name not a valid group name, skipping");
        next;
      }

      my $group = $this->auth->findGroup(wikiName => $name);

      if ($group) {
        if ($group->prop("pid") ne $this->prop("id")) {

          $this->writeDebug("... group $name already owned by another provider ".$group->prop("pid")." ... not adding user as a member");
          # SMELL: do we want to add users to foreign groups?
          next;
        }
        $this->writeDebug("... found group $name");

      } else {
        $this->writeDebug("... creating group $name");
        $group = $this->addGroup(
          id => $name,
          wikiName => $name,
        );
      }

      delete $oldMembership{$group->prop("id")};

      $this->writeDebug("... adding user to group $name");
      $this->addMemberToGroup($user, $group) unless $group->hasMember($user, 0);
    }
  } else {
    $this->writeDebug("... no groups found in id token");
  }

  foreach my $group (values %oldMembership) {
    $this->writeDebug("... removing user from ".$group->stringify);
    $this->removeMemberFromGroup($user, $group);
  }

  # refresh topic groups ... disabled
  # $this->auth->getProvider("Topic")->cacheGroups() if $isNewUser;

  return $user;
}

sub extractGroupInfo {
  my ($this, $idToken) = @_;

  my $attr = $this->prop("GroupsAttribute"); 
  return unless $attr;

  $this->writeDebug("called extractGroupInfo");
  $this->writeDebug("... looking up groups in $attr");

  my $allowedGroups = $this->prop("AllowedGroups"); 
  my $deniedGroups = $this->prop("DeniedGroups"); 

  my $groups = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $attr);
  return unless $groups;

  # groups could be an array or a string 
  my @groups = ref($groups) ? @$groups: split(/\s*,\s*/, $groups);
  return unless @groups;

  $this->writeDebug("... found groups ".join(", ", @groups));

  # filter groups
  my @result = ();
  foreach my $name (@groups) {
    next if $allowedGroups && $name !~ /$allowedGroups/;
    next if $deniedGroups && $name =~ /$deniedGroups/;
    push @result, $name;
  }

  return \@result;
}

sub retrieveTokenOfCode {
  my ($this, $code, $state) = @_;

  $this->writeDebug("called retrieveTokenOfCode($code)");

  my $endpoint = $this->getEndpoint("token");
  $this->writeDebug("token endpoint = $endpoint");

  my $redirectUrl = $this->getRedirectUri($state);
  #$this->writeDebug("redirect_uri = $redirectUrl");
  #$this->writeDebug("code = $code");

  my $response = $this->auth->getUserAgent->post($endpoint, {
    client_id => $this->prop("ClientID"),
    client_secret => $this->prop("ClientSecret"),
    redirect_uri => $redirectUrl,
    code => $code,
    grant_type => "authorization_code"
  });

  unless ($response->is_success) {
    _writeError("Protocol error: Couldn't exchange auth code for token.");
    _writeError("response msg=" . $response->message);
    _writeError("response content=" . $response->decoded_content);
    throw Error::Simple("We encountered a protocol error while trying to redeem an authorization code with your provider.");
  } 

  #$this->writeDebug("... response=".$response->decoded_content);

  my $data = $this->json->decode($response->decoded_content);

  #$this->writeDebug("... data=".dump($data));

  return $this->verifyIdToken($data->{id_token});
}

sub verifyIdToken {
  my ($this, $idToken, $issuer) = @_;

  $this->writeDebug("called verifyIdToken");
  #$this->writeDebug("...idToken=$idToken");

  my @parts = split(/\./, $idToken);
  if (scalar(@parts) != 3) {
    _writeError("JWT ID token verification failed: wrong number of segments ".scalar(@parts));
    throw Error::Simple("We received a badly formatted answer from your provider.");
  }

  my $header = $this->json->decode(MIME::Base64::decode($parts[0]));
  #$this->writeDebug("... header=".dump($header));
  $this->writeDebug("header kid=$header->{kid}, alg=$header->{alg}");


  # This looks through all the public keys we got via the discovery document to find the one
  # that was used to sign the id token.

  my $keys = $this->retrievePublicKeys;

  foreach my $key (@$keys) {
    #$this->writeDebug("... key=".dump($key));
    $this->writeDebug("publickKey kid=".($key->{kid}//'undef').", alg=".($key->{alg}//'undef'));

    if ((!defined $header->{kid} || ($key->{kid} eq $header->{kid})) && 
        (!defined $key->{alg} || ($key->{'alg'} eq $header->{'alg'}))) {

      $this->writeDebug("... found matching key");
      my $data = $this->decodeJwt($idToken, $key);

      if ($this->prop("ClientID") ne $data->{'aud'}) {
        _writeError("JWT ID token verification failed: wrong audience");
        throw Error::Simple("We couldn't verify the validity of the claims we received from your provider.");
      }

      if ($issuer && $data->{'iss'} !~ /$issuer/) {
        _writeError("JWT ID token verification failed: wrong issuer (" . $data->{'iss'} . ")");
        throw Error::Simple("We couldn't verify the validity of the claims we received from your provider.");
      }

      #$this->writeDebug("...JWT ID token=".dump($data));

      return $data;
    }
  }

  _writeError("JWT ID token verification failed: unknown signing key");
  throw Error::Simple("We couldn't verify the validity of the claims we received from your provider.");
}

sub decodeJwt {
  my ($this, $token, $key) = @_;

  my $data;
  eval { 
    $data = Crypt::JWT::decode_jwt(
      token => $token, 
      key => $key
    ); 
  };
  if ($@) {
    _writeError("JWT ID token verification failed: " . $@);
    throw Error::Simple("We couldn't verify the validity of the claims we received from your provider.");
  }

  return $data;
}

sub retrievePublicKeys {
  my $this = shift;
  
  $this->writeDebug("called retrievePublicKeys");
  my $endpoint = $this->getConfig('jwks_uri');
  $this->writeDebug("endpoint = $endpoint");

  my $response = $this->auth->getUserAgent->get($endpoint);

  unless ($response->is_success) {
    _writeError("Could not retrieve public keys from $endpoint");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We encountered a protocol error while trying to fetch your provider's signing keys.");
  }

  my $data = $this->json->decode($response->decoded_content);

  #$this->writeDebug("... data=".dump($data));

  return $data->{keys};
}

sub getScopes {
  my $this = shift;

  my %supported_scopes = map { $_ => 1 } @{$this->getConfig("scopes_supported")};

  my @scopes = ();
  push @scopes, "user" if exists $supported_scopes{"user"};
  push @scopes, "openid" if exists $supported_scopes{"openid"};
  push @scopes, "email" if exists $supported_scopes{"email"};
  push @scopes, "profile" if exists $supported_scopes{"profile"};
  push @scopes, "groups" if exists $supported_scopes{"groups"};

  $this->writeDebug("... scopes=@scopes");

  return join(" ", @scopes);
}

sub getEndpoint {
  my ($this, $type) = @_;

  $type .= '_endpoint' unless $type =~ /_endpoint$/;

  return $this->getConfig($type);
}

sub getConfig {
  my ($this, $type) = @_;

  $this->{_openid_config} = $this->discoverConfig unless defined $this->{_openid_config};
  return defined($type) ? $this->{_openid_config}{$type} : $this->{_openid_config};
}

sub discoverConfig {
  my $this = shift;

  my $discoveryUri = $this->getDiscoveryUri;
  $this->writeDebug("discoveryUri=$discoveryUri");
  my $response = $this->auth->getUserAgent->get($discoveryUri);

  if (!$response->is_success) {
    _writeError("could not retrieve endpoint configuration at '$discoveryUri':");
    _writeError("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We encountered a protocol error while trying to fetch your provider configuration.");
  }

  #$this->writeDebug("got endpoint configuration: ".$response->decoded_content);

  return $this->json->decode($response->decoded_content);
}

sub getDiscoveryUri {
  my $this = shift;

  my $url = $this->prop("Tenant");
  $url = "https://".$url unless $url =~ /^http/;
  $url .= '/.well-known/openid-configuration';

  return $url;
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::OpenID - ERROR: $_[0]\n";
}

1;

