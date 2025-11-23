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

package Foswiki::PluggableAuth::Provider::ClientCert;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::ClientCert

This provider authenticates requests using client side certificates. Note that each
client certificate will contain sufficient user information to map it onto an identity
provided by seconday provider.

=cut

use strict;
use warnings;

use Crypt::OpenSSL::X509 ();
use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ObjectMethod isInternalLogin()

returns false as this provider does not authenticate users on its own.

=cut

sub isInternalLogin {
  return 0;
}

=begin TML

---++ ObjectMethod processLogin($request, $state) -> $user

This is called by Foswiki::LoginManager::PluggableLogin to process a login request.
It returns undef if this provider is not responsible, or the provided certificate is valid.

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin");

#  if ($state->{"ClientCert_attempted"}) {
#    $this->writeDebug("... already attempted to log in using this provider");
#    return;
#  }
#  $state->{"ClientCert_attempted"} = 1;

  my $pid = $request->param("pauth_provider");
  return if $this->prop("Visible") && !(defined $pid && $pid eq $this->prop("id"));

  my $envVar = $this->prop("EnvVariable");
  return unless defined $envVar;

  my $email;
  my $user;
  my $pem = $ENV{$envVar};

  return unless $pem;

  my $cert = Crypt::OpenSSL::X509->new_from_string($pem);

  unless ($cert) {
    print STDERR "WARNING: could not decode certificate\n";
    return;
  }

  if ($this->prop("VerifyCertificates")) {
    $this->writeDebug("verifying certificate");

    my $isOk = $this->auth->getCertificateAuthority->verify($cert);
    $this->writeDebug("isOk=$isOk");
      
    unless ($isOk) {
      print STDERR "WARNING: client certificate is not valid\n";
      return;
    }

  } else {
    $this->writeDebug("not verifying certificate");
  }

  foreach my $email (split(/ /, $cert->email)) {
    $this->writeDebug("email=$email");
    $user = $this->auth->findUser(email => $email);
    return $user if $user;
  }

  $this->writeDebug("certificate doesn't contain a known user");
}

1;
