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

package Foswiki::PluggableAuth::Provider::BasicAuth;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::BasicAuth

This is an provider to authenticate users using basic authentication. Note
that only the remote user name will be provided by this class which needs to
be mapped onto another provider's identity with the same name.

=cut

use strict;
use warnings;

use MIME::Base64 ();
use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ObjectMethod isInternalLogin() -> $boolean

returns false as this provider is not an "interal" provider. authentication is performed
externally.

=cut

sub isInternalLogin {
  return 0;
}

=begin TML

---++ ObjectMethod initLogin($request, $state)

This is called by Foswiki::LoginManager::PluggableLogin to init a login request, i.e. 
it sends a 401 response in case the current session isn't authenticated yet.

=cut

sub initLogin {
  my ($this, $request, $state) = @_;

  return 0 unless $this->isAllowedIpAddress;

  $this->writeDebug("called initLogin");

  my $pid = $request->param("pauth_provider");
  if (defined $pid) {
    if ($pid ne $this->prop("id")) {
      $this->writeDebug("... not my pid");
      return 0;
    }
    $this->writeDebug("... found my pid");
  } else {
    return 0 unless $this->prop("AutoLogin");
    return 0 if $this->prop("Visible");
  }

  my $session = $Foswiki::Plugins::SESSION;
  my $response = $session->{response};

  $this->writeDebug("... sending authentication header");
  $response->header(
    -status => 401,
    'WWW-Authenticate' => 'Basic realm="' . ( $this->prop("Realm") || $Foswiki::cfg{AuthRealm} || "" ) . '"'
  );

  $request->param(
    -name => 'foswiki_origin',
    -value => $state->{key}
  );

  return 1;
}

=begin TML

---++ ObjectMethod processLogin($request, $state) -> $user

This is called by Foswiki::LoginManager::PluggableLogin to process a login request.
It returns undef if this provider is not responsible, or the provided password is correct.

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin");

  my $authHeader = $request->header("Authorization");
  unless (defined $authHeader) {
    $this->writeDebug("... no basic auth header found");
    return;
  }

  my ($scheme, $cred) = $authHeader =~ /^(.*) (.*)$/;
  
  if (!defined($scheme) || !defined($cred) || $scheme ne "Basic") {
    $this->writeDebug("... not basic scheme");
    return;
  }

  $cred = MIME::Base64::decode_base64($cred);
  my ($authName, $password) = $cred =~ /^(.*):(.*)$/;

  unless (defined $authName) {
    $this->writeDebug("no authName found");
    return;
  }
  
  $this->writeDebug("authName=$authName");

  my $user = $this->findAuthName($authName);

  unless (defined($user)) {
    $this->writeDebug("... user not found");
    return;
  }

  unless ($user->isEnabled) {
    $this->writeDebug("... user is disabled");
    return;
  }

  $this->writeDebug("... checking password");
  if ($user->checkPassword($password)) {
    $this->writeDebug("... correct");
    return $user;
  } 

  $this->writeDebug("... wrong");
  return;
}

sub findAuthName {
  my ($this, $authName) = @_;

  return $this->auth->findUser(email => $authName, loginName => $authName)
    if $Foswiki::cfg{PluggableAuth}{AllowLoginUsingEmailAddress};

  return $this->auth->findUser(loginName => $authName);
}

1;
