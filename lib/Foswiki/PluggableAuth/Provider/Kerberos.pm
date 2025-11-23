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

package Foswiki::PluggableAuth::Provider::Kerberos;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Kerberos

TODO

=cut

use strict;
use warnings;

use GSSAPI;
use MIME::Base64;
use Encode ();
use Error qw(:try);
use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

#use Data::Dump qw(dump);

sub isInternalLogin {
  return 0;
}

sub init {
  my $this = shift;

  $this->SUPER::init();

  $ENV{KRB5_KTNAME} = "FILE:" . $this->prop("KeyTab"); 
  #$this->writeDebug("... keytab=$ENV{KRB5_KTNAME}");

  my $ccache = "DIR:" . $this->auth->getWorkArea("ccache");
  $ENV{KRB5CCNAME} = $ccache; 

  #$this->writeDebug("... ccache=$ccache");

  return 1;
}

sub initLogin {
  my ($this, $request, $state) = @_;

  $this->writeDebug("called initLogin");
  return 0 unless $this->prop("AutoLogin");
  return 0 unless $this->isAllowedIpAddress;

  my $pid = $request->param("pauth_provider");
  if (defined $pid) {
    return 0 if $pid ne $this->prop("id");
  } else {
    return 0 if $this->prop("Visible");
  }

  if ($this->failure($state)) {
    $this->writeDebug("... already failed before");
    return 0;
  }

  $this->writeDebug("... redirecting with negotiate header");

  my $session = $Foswiki::Plugins::SESSION;
  $session->{response}->header(
    -status => 401, 
    'WWW-Authenticate' => 'Negotiate'
  );

  # TODO: should throw an extension to bail out of further processing

  return 0;
}

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin");

  my $pid = $request->param("pauth_provider");
  return if $this->prop("Visible") && !(defined $pid && $pid eq $this->prop("id"));

  my $token;
  foreach my $val ($request->header("Authorization")) {
    if ($val =~ /^Negotiate (.+)$/) {
      $token = $1;
      last unless $token =~ /^TlRMT/;
    }
  }
  unless (defined $token) {
    $this->writeDebug("... no token found (yet)");
    return;
  }

  $this->writeDebug("... token found");

  if ($token =~ /^TlRMT/) {
    $this->writeDebug("... but it is an NTLM token, setting failure state");
    $this->failure($state, 1);
    return;
  }

  $token = decode_base64($token);
  my $context;
  my $client;
  my $status = GSSAPI::Context::accept($context, GSS_C_NO_CREDENTIAL, $token, GSS_C_NO_CHANNEL_BINDINGS, $client, undef, undef, undef, undef, undef);

  if (GSSAPI::Status::GSS_ERROR($status->major)) {
    $this->writeError(_getStatusMessage($status));
    throw Error::Simple("Unable to accept security context");
  }

  my $upn;
  $status = $client->display($upn);

  if (GSSAPI::Status::GSS_ERROR($status->major)) {
    $this->writeError(_getStatusMessage($status));
    throw Error::Simple("Unable to display client name");
  }

  throw Error::Simple("Invalid login token") unless defined $upn;

  $upn = Encode::decode_utf8($upn);

  my $domain;
  my $loginName;

  if ($upn =~ /^(.*)@(.*)$/) {
    $loginName = $1;
    $domain = $2;
  } else {
    $loginName = $upn;
  }
  $domain //= "";
  $loginName = lc($loginName) unless $this->prop("CaseSensitiveLogin");

  $this->writeDebug("... loginName=" . ($loginName // '') . ", domain=" . ($domain // ''));

  foreach my $provider ($this->auth->getProviderOfDomain($domain)) {

    my $user = $provider->findUser(loginName => $loginName);

    if (defined $user) {
      if ($user->isEnabled) {
        $this->writeDebug("... user $upn found in domain $domain");
        return $user;
      } else {
        $this->writeDebug("... user $upn is disabled in domain $domain");
      }
    }
  }

  $this->writeError("... no provider found for upn '$upn' or unknown user '$loginName'");
  $this->writeDebug("... login failed, setting failure state");
  $this->failure($state, 1);

  return;
}

sub _getStatusMessage {
  my $status = shift;

  my $text = "MAJOR: ". join(", ", $status->generic_message());
  $text .= " - MINOR: ".join(", ", $status->specific_message());

  return $text;
}

1;
