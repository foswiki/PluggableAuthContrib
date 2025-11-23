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

package Foswiki::PluggableAuth::Provider::OAuth;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::OAuth

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider ();
use JSON();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ObjectMethod new(%params) -> $this

constructor

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{_endpoints} = {
    authorization => "",
    token => "",
    user => "",
  };

  $this->{_scopes} = 'email profile';

  return $this;
}

=begin TML

---++ ObjectMethod finish()

clears local properties

=cut

sub finish {
  my $this = shift;

  $this->SUPER::finish;

  undef $this->{_endpoints};
  undef $this->{_scopes};
}

=begin TML

---++ ObjectMethod initLogin($request, $state) -> $boolean

returns true if the login was initialized successfully

=cut

sub initLogin {
  my ($this, $request, $state) = @_;

  my $pid = $request->param("pauth_provider");
  if (defined $pid) {
    return 0 if $pid ne $this->prop("id");
  } else {
    return 0 if $this->prop("Visible");
  }

  return 0 unless $this->isAllowedIpAddress;

  $this->writeDebug("called initLogin");
  my $request_uri = $this->buildAuthRequest($state);

  $this->writeDebug("redirecting to $request_uri");

  my $session = $Foswiki::Plugins::SESSION;
  $session->{response}->redirect($request_uri);

  return 1;
}

=begin TML

---++ ObjectMethod buildAuthRequest($state) -> $endpoint

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

---++ ObjectMethod processLogin($request, $state) -> $user

returns the user object on success or undef otherwise

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request);
  $this->writeDebug("called processLogin");

  my $code = $request->param('code');
  my $error = $request->param('error');

  $this->writeDebug("code=".($code//'undef').", error=".($error//'undef'));
  return unless defined $code;

  $request->delete('code', 'error', 'pauth_provider', 'state');
  throw Error::Simple("ERROR: ".$error) if $error;

  $code = Foswiki::urlDecode($code);

  my $authToken = $this->retrieveTokenOfCode($code, $state);
  $this->writeDebug("no authToken") unless defined $authToken;
  return unless $authToken;

  my $data = $this->fetchUser($authToken);
  return unless defined $data;

  my $userInfo = $this->extractUserInfo($data, $authToken);
  return unless defined $userInfo && defined $userInfo->{loginName};

  my $user = $this->findUser(loginName => $userInfo->{loginName});

  if (defined $user) {
    $user = $this->updateUser($user, $userInfo) if $this->prop("SyncOnLogin");
  } else {
    $user = $this->addUser(%$userInfo);
  }

  return $user;
}

=begin TML

---++ ObjectMethod extractUserInfo($idToken) -> $userInfo

returns a hash of the user info contained in the idToken

=cut

sub extractUserInfo {
  my ($this, $idToken) = @_;

  $this->writeDebug("called extractUserInfo");
  #$this->writeDebug("... idToken: " . dump($idToken));

  my %userInfo = ();

  # email ###
  foreach my $key (split(/\s*,\s*/, $this->prop("MailAttributes"))) {
    my $val = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $key);
    $this->writeDebug("key=$key, val=" . ($val // 'undef'));
    if (defined $val) {
      $userInfo{email} = $val;
      last;
    }
  }

  if (defined $userInfo{email}) {
    my $configKey = $this->prop("MailVerifiedAttribute");
    if ($configKey) {
      my $emailVerified = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $configKey);
      unless ($emailVerified) {
        $this->writeDebug("...emailVerified=$emailVerified");
        undef $userInfo{email};
        _writeError("Email not verified");
        throw Error::Simple("Sorry, access denied. Your email address isn't verified yet.");
      }
    }
  } else {
    _writeError("No email data found in token searching for " . $this->prop("MailAttributes"));
    throw Error::Simple("Sorry, access denied. No valid email address found.");
  }
  

  # loginName ###
  my $loginName = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $this->prop("LoginNameAttribute"));
  if (defined $loginName) {
    $loginName =~ s/@.*$//;
    $userInfo{loginName} = $loginName if $this->auth->isValidLoginName($loginName);
  }

  throw Error::Simple("Sorry, access denied. No valid login information found.") unless defined $userInfo{loginName};

  # displayName ###
  my @displayName = ();
  foreach my $key (split(/\s*,\s*/, $this->prop("DisplayNameAttributes"))) {
    my $val = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $key);
    $this->writeDebug("key=$key, val=" . ($val // 'undef'));
    push @displayName, $val if defined $val;
  }

  my $separator = $this->prop("DisplayNameSeparator") // "";
  $userInfo{displayName} = join($separator, @displayName) if @displayName;

  # wikiName ###
  my $wikiName = '';
  foreach my $key (split(/\s*,\s*/, $this->prop("WikiNameAttributes"))) {
    my $val = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $key);
    $this->writeDebug("key=$key, val=" . ($val // 'undef'));
    $wikiName .= $val if defined $val;
  }
  $userInfo{wikiName} = $wikiName if $this->auth->isValidWikiName($wikiName);
  throw Error::Simple("Sorry, access denied. No valid wikiName found.") unless defined $userInfo{wikiName};

  $userInfo{displayName} //= $userInfo{wikiName};

  # firstName, lastName, ...
  foreach my $key (qw(firstName middleName lastName picture initials)) {
    my $mappedKey = $Foswiki::cfg{PluggableAuth}{Providers}{$this->prop("id")}{ucfirst($key)."Attribute"};
    $mappedKey ||= $key;
    my $val = Foswiki::PluggableAuth::Provider::getAttribute($idToken, $mappedKey);
    $this->writeDebug("key=$key, val=" . ($val // 'undef'));
    next unless defined $val;

    # SMELL
    #if ($key eq 'picture') {
    #  $userInfo{"_".$key} = $val;
    #  next;
    #} 
    $userInfo{$key} = $val;
  }

  # if required, extract firstName, middleName, lastName from displayName
  my @parts = split(/\s+/, $userInfo{displayName});
  if (@parts) {
    $userInfo{firstName} = shift @parts unless defined $userInfo{firstName};
    $userInfo{middleName} = shift @parts unless defined($userInfo{middleName}) || scalar(@parts) < 3;
    $userInfo{lastName} = shift @parts unless defined $userInfo{lastName};
  }

  unless ($userInfo{initials}) {
    $userInfo{initials} = Foswiki::PluggableAuth::extractInitials(($userInfo{firstName}||'') . " ". ($userInfo{middleName} ||'') . " " . ($userInfo{lastName}||''));
  }

  #$this->writeDebug("... userInfo: " . dump(\%userInfo));

  return \%userInfo;
}

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $data

returns infos about the user available through this provider

=cut

sub fetchUser {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called fetchUser()");

  my $endpoint = $this->getEndpoint("user");
  $this->writeDebug("... endpoint=$endpoint");

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->get($endpoint, 
    Authorization => "Bearer $accessToken"
  );

  if (!$response->is_success){
    _writeError("failed to fetch user info");
    $this->writeDebug("response status=" . $response->message . " content=" . $response->decoded_content);
    throw Error::Simple("We couldn't fetch the user data of the claims we received from your provider.");
  }

  #$this->writeDebug("... response=".$response->decoded_content);

  return $this->decodeUserData($response->decoded_content);
}

=begin TML

---++ ObjectMethod decodeUserData($string) -> $data

decodes the json object encoded in the string, returns it as a hash ref

=cut

sub decodeUserData {
  my ($this, $string) = @_;

  my $data = $this->json->decode($string);

  #$this->writeDebug("... user data=".dump($data));

  return $data;
}

=begin TML

---++ ObjectMethod retrieveTokenOfCode($code, $state) -> $accessToken

gets an access token to further process the login information

=cut

sub retrieveTokenOfCode {
  my ($this, $code, $state) = @_;

  $this->writeDebug("called retrieveTokenOfCode()");

  my $endpoint = $this->getEndpoint("token");

  my $params = {
    client_id => $this->prop("ClientID"),
    client_secret => $this->prop("ClientSecret"),
    grant_type => "authorization_code",
    redirect_uri => $this->getRedirectUri($state),
    code => $code,
  };

  $this->writeDebug("token endpoint = $endpoint");
  #$this->writeDebug("... posting data=".dump($params));

  my $ua = $this->auth->getUserAgent();
  my $response = $ua->post($endpoint, $params);

  unless ($response->is_success) {
    _writeError("Protocol error: Couldn't exchange auth code for token.");
    _writeError("response msg=" . $response->message .", content=" . $response->decoded_content);
    throw Error::Simple("We encountered a protocol error while trying to redeem an authorization code with your provider.");
  } 

  my $data = $this->json->decode($response->decoded_content);
  #$this->writeDebug("... data=".dump($data));

  return $this->extractAccessToken($data);
}

=begin TML

---++ ObjectMethod extractAccessToken($data) -> $accessToken

extracts the accessToken from the retrieved token

=cut

sub extractAccessToken {
  my ($this, $data) = @_;

  #$this->writeDebug("extractAccessToken from data=".dump($data));
  return $data->{access_token};
}

=begin TML

---++ ObjectMethod getScopes() -> $scopes

returns available scopes for this provider

=cut

sub getScopes {
  my $this = shift;

  return $this->{_scopes}
}

=begin TML

---++ ObjectMethod getRedirectUri($state) -> $url

returns the url the user is redirected to after granting access

=cut

sub getRedirectUri {
  my ($this, $state) = @_;

  my $url = Foswiki::Func::getScriptUrl(undef, undef, 'login') . '?pauth_provider='.$this->prop("id");

  #$this->writeDebug("redirectUrl=$url");

  return $url;
}

=begin TML

---++ ObjectMethod getEndpoint($type) -> $url

returns endpoint information of a specific type

=cut

sub getEndpoint {
  my ($this, $type) = @_;

  return defined $type ? $this->{_endpoints}{$type} : $this->{_endpoints};
}

=begin TML

---++ ObjectMethod isInternalLogin() -> $boolean

=cut

sub isInternalLogin {
  return 0;
}

=begin TML

---++ ObjectMethod checkGroupAccess($type, $group, $user) -> $boolean

=cut

sub checkGroupAccess {
  my ($this, $type, $group, $user) = @_;

  return 1 if $type =~ /^VIEW$/i;
  return 0;
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::OAuth - ERROR: $_[0]\n";
}

1;


