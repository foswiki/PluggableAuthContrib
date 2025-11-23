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

package Foswiki::PluggableAuth::Provider::Twitter;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Twitter

This is a provider based on CPAN:Net::Twitter, that is we do not use
our own OAuth or <nop>OpenID implementation here.

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::PluggableAuth::Provider ();
use Net::Twitter ();
#use Data::Dump qw(dump);

our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  return $this;
}

=begin TML

---++ ObjectMethod finish()

destructor for this class

=cut

sub finish {
  my $this = shift;

  $this->SUPER::finish();
  undef $this->{_twitter};
}

=begin TML

---++ ObjectMethod twitter() -> $netTwitter

constructs the Net::Twitter delegate

=cut

sub twitter {
  my $this = shift;

  unless (defined($this->{_twitter})) {
    $this->{_twitter} = Net::Twitter->new(
      traits => [qw/API::RESTv1_1/],
      consumer_key => $this->prop("ClientID"),
      consumer_secret => $this->prop("ClientSecret"),
    );
  }

  return $this->{_twitter};
}

=begin TML

---++ ObjectMethod initLogin($request, $state)

This methid inittializes the login procedure for Twitter.
It builds the authentication request and redirects to it.

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
  my $authUrl = $this->buildAuthRequest($state);

  $this->writeDebug("redirecting to $authUrl");

  my $session = $Foswiki::Plugins::SESSION;
  $session->{response}->redirect($authUrl);

  return 1;
}

=begin TML

---++ ObjectMethod processLogin($request, $state)

Once the login has been performed on the Twitter side the client
is redirected back to this place so that the login can be processed further.
This method makes sure authentication succeeded and extracts user information
to be added to the user mapping.

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request);
  $this->writeDebug("called processLogin");

  my $requestToken = $request->param('oauth_token');

  my $pid = $request->param("pauth_provider");
  return unless defined $pid && $pid eq $this->prop("id") && defined $requestToken;

  my $error = $request->param('error');
  throw Error::Simple("ERROR: ".$error) if $error;

  my $verifier = $request->param('oauth_verifier');
  my $origRequestToken = Foswiki::Func::getSessionValue("twitter_request_token");
  my $requestTokenSecret = Foswiki::Func::getSessionValue("twitter_request_token");

  Foswiki::Func::clearSessionValue("twitter_request_token");
  Foswiki::Func::clearSessionValue("twitter_request_secret");

  throw Error::Simple("Something is horribly wrong: request tokens don't match")
    unless defined($origRequestToken) && $origRequestToken eq $requestToken;

  $request->delete('error', 'pauth_provider', 'state', 'oauth_token', 'oauth_verifier');

  $this->twitter->request_token($requestToken);
  $this->twitter->request_token_secret($requestTokenSecret);

  $this->writeDebug("oauth_token=$requestToken, oauth_verifier=$verifier");

  my ($accessToken, $accessSecret) = $this->twitter->request_access_token(verifier => $verifier);

  $this->writeDebug("access_token=$accessToken, access_secret=$accessSecret");

  my $userInfo = $this->extractUserInfo($accessToken, $accessSecret);
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

---++ ObjectMethod extractUserInfo($accessToken, $accessSecret) -> $userInfo

This method extracts any user information as returned by respective endpoints

=cut

sub extractUserInfo {
  my ($this, $accessToken, $accessSecret) = @_;

  my %userInfo = ();

  my $accountInfo = $this->twitter->verify_credentials({
    include_entities => 'true',
    skip_status => 'true', 
    include_email => 'true',
  });

  #$this->writeDebug("accountInfo=".dump($accountInfo));

  $userInfo{loginName} = $accountInfo->{screen_name};
  $userInfo{displayName} = $userInfo{wikiName} = $accountInfo->{name};
  $userInfo{email} = $accountInfo->{email};

  # extract firstName, middleName, lastName from displayName
  my @parts = split(/\s+/, $userInfo{displayName});
  if (@parts) {
    $userInfo{firstName} = shift @parts unless defined $userInfo{firstName};
    $userInfo{middleName} = shift @parts unless defined($userInfo{middleName}) || scalar(@parts) < 3;
    $userInfo{lastName} = shift @parts unless defined $userInfo{lastName};
  }
  $userInfo{initials} = Foswiki::PluggableAuth::extractInitials(($userInfo{firstName}||'') . " ". ($userInfo{middleName} ||'') . " " . ($userInfo{lastName}||''));
  $userInfo{picture} = $accountInfo->{profile_image_url_https};
  $userInfo{picture} =~ s/_normal\b//;

  #$this->writeDebug("... userInfo=".dump(\%userInfo));

  return \%userInfo;
}

=begin TML

---++ ObjectMethod buildAuthRequest($state) -> $url

This method returns an authentication url to redirect the client to.

=cut

sub buildAuthRequest {
  my ($this, $state) = @_;

  my $authUrl = $this->twitter->get_authentication_url(
    callback => $this->getRedirectUri($state),
  );

  Foswiki::Func::setSessionValue("twitter_request_token", $this->twitter->request_token);
  Foswiki::Func::setSessionValue("twitter_request_token_secret", $this->twitter->request_token);

  return $authUrl;
}

=begin TML

---++ ObjectMethod getRedirectUri($state) -> $url

This is the callback for the Twitter endpoint as created in buildAuthRequest().

=cut

sub getRedirectUri {
  my ($this, $state) = @_;

  my $url = Foswiki::Func::getScriptUrl(undef, undef, 'login') . '?pauth_provider='.$this->prop("id");

  #$this->writeDebug("redirectUrl=$url");

  return $url;
}

1;

