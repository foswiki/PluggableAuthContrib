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

package Foswiki::PluggableAuth::Provider::Saml;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Saml

TODO

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::PluggableAuth::Provider ();
use Error qw(:try);

use Net::SAML2;
use Net::SAML2::XML::Sig;
use MIME::Base64 qw/ decode_base64 /;
use Crypt::OpenSSL::Verify;
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

clears local properties

=cut

sub finish {
  my $this = shift;

  $this->SUPER::finish;

  undef $this->{_json};
}

=begin TML

---++ ObjectMethod isInternalLogin() -> $boolean

=cut

sub isInternalLogin {
  return 0;
}

=begin TML

---++ ObjectMethod initLogin($request, $state) -> $boolean

returns true of the init was successfull

=cut

sub initLogin {
  my ($this, $request, $state) = @_;

  return 0 unless $this->handlesLogin($request, $state);
  return 0 if $this->prop("Visible");

  $this->writeDebug("called initLogin");

  my $request_uri = $this->buildAuthRequest($state);

  $this->writeDebug("... redirecting to $request_uri");

  my $session = $Foswiki::Plugins::SESSION;
  $session->{response}->redirect($request_uri);

  return 1;
}

=begin TML

---++ ObjectMethod buildAuthRequest($state)

=cut

sub buildAuthRequest {
  my ($this, $state) = @_;

  $this->writeDebug("called buildAuthRequest");

  throw Error::Simple("ERROR: no service provider key defined") unless $this->prop("ServiceProviderKey");
  throw Error::Simple("ERROR: service provider key not found ") unless -f $this->prop("ServiceProviderKey");

  throw Error::Simple("ERROR: no service provider certificate defined") unless $this->prop("ServiceProviderCertificate");
  throw Error::Simple("ERROR: service provider certificate not found") unless -f $this->prop("ServiceProviderCertificate");

  my $metadataFile = $this->prop("Metadata");
  $this->writeDebug("... reading file $metadataFile");
  my $xml = Foswiki::Func::readFile($metadataFile);
  my $idp = Net::SAML2::IdP->new_from_xml(xml => $xml, cacert => $this->prop("CACert"));

  # Important not to return as XML here as we need to track the id for later verification
  my $authnreq = Net::SAML2::Protocol::AuthnRequest->new(
    issuer => $this->prop("Issuer"),
    destination => $idp->sso_url('urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'),    # The ssl_url destination for redirect
    provider_name => $this->prop("ProviderName"),
  );

  # Store the request's id for later verification
  Foswiki::Func::setSessionValue('saml_request_id', $authnreq->id);

  my $redirect = Net::SAML2::Binding::Redirect->new(
    key => $this->prop("ServiceProviderKey"),
    cert => $this->prop("ServiceProviderCertificate"),
    param => 'SAMLRequest',
    url => $idp->sso_url('urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'),    # The ssl_url destination for redirect
  );

  return $redirect->sign($authnreq->as_xml);
}

=begin TML

---++ ObjectMethod processLogin($request, $state) -> $user

returns a user object if logged in successfully or undef otherwise

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request);
  $this->writeDebug("called processLogin");

  my $samlResponse = $request->param('SAMLResponse');
  my $error = $request->param('error');

  #$this->writeDebug("samlResponse=".($samlResponse//'undef').", error=".($error//'undef'));
  return unless defined $samlResponse;

  $request->delete('SAMLResponse', 'error', 'pauth_provider', 'state');
  throw Error::Simple("ERROR: ".$error) if $error;

  my $assertion = $this->retrieveAssertion($request, $samlResponse);
  return unless $assertion;

  my $userInfo = $this->extractUserInfo($assertion);
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

---++ ObjectMethod retrieveAssertion($request, $samlResponse) -> $assertion

=cut

sub retrieveAssertion {
  my ($this, $request, $samlResponse) = @_;

  $this->writeDebug("called retrieveAssertion");

  # create the POST binding object to get the details from the SALMResponse'
  $this->writeDebug("... getting details from SAMLResponse");
  my $post = Net::SAML2::Binding::POST->new(cacert => $this->prop("CACert"));
  my $ret = $post->handle_response(
    $samlResponse
  );

  $this->writeDebug("... ret=$ret");

  return unless $ret;
  my $assertion = Net::SAML2::Protocol::Assertion->new_from_xml(
    xml => decode_base64($samlResponse)
  );

  my $isValid = $assertion->valid($this->prop("Issuer"));
  $this->writeDebug("... isValid=$isValid");

  throw Error::Simple("ERROR: SAML request does not validate") unless $isValid;

  return $assertion;
} 

=begin TML

---++ ObjectMethod extractUserInfo($assesrtion) -> $userInfo

returns a hash of the user info available in the saml assertion

=cut

sub extractUserInfo {
  my ($this, $assertion) = @_;

  $this->writeDebug("called extractUserInfo");

  my %userInfo = ();

# if ($this->{_debug}) {
#   while (my ($k, $v) = each %{$assertion->attributes}) {
#     $this->writeDebug("... saml: $k=".dump($v));
#   }
# }

  $userInfo{loginName} = $assertion->nameid;
  throw Error::Simple("Sorry, access denied. No valid login information found.") 
    unless $this->auth->isValidLoginName($userInfo{loginName});


  $userInfo{email} = _getAttr($assertion, $this->prop("MailAttribute"));
  throw Error::Simple("Sorry, access denied. No valid email address found.") 
    unless defined $userInfo{email};

  $userInfo{firstName} = _getAttr($assertion, $this->prop("FirstNameAttribute"));
  $userInfo{middleName} = _getAttr($assertion, $this->prop("MiddleNameAttribute"));
  $userInfo{lastName} = _getAttr($assertion, $this->prop("LastNameAttribute"));
  $userInfo{initials} = _getAttr($assertion, $this->prop("InitialsAttribute"));
  $userInfo{picture} = _getAttr($assertion, $this->prop("PictureAttribute"));

  # displayName ###
  my @displayName = ();
  foreach my $key (split(/\s*,\s*/, $this->prop("DisplayNameAttributes"))) {
    my $val = _getAttr($assertion, $key);
    #$this->writeDebug("key=$key, val=" . ($val // 'undef'));
    push @displayName, $val if defined $val;
  }

  my $separator = $this->prop("DisplayNameSeparator") // "";
  $userInfo{displayName} = join($separator, @displayName) if @displayName;


  # wikiName ###
  my $wikiName = '';
  foreach my $key (split(/\s*,\s*/, $this->prop("WikiNameAttributes"))) {
    my $val = _getAttr($assertion, $key);
    #$this->writeDebug("key=$key, val=" . ($val // 'undef'));
    $wikiName .= $val if defined $val;
  }
  $userInfo{wikiName} = $wikiName if $this->auth->isValidWikiName($wikiName);
  throw Error::Simple("Sorry, access denied. No valid wikiName found.") unless defined $userInfo{wikiName};

  $userInfo{displayName} //= $userInfo{wikiName};

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

  #$this->writeDebug("... userInfo=".dump(\%userInfo));

  return \%userInfo;
}

=begin TML

---++ StaticMethod _getAttr($key)

=cut

sub _getAttr {
  my ($assertion, $key) = @_;

  return unless defined $key && $key ne "";
  my $val = $assertion->attributes->{$key};
  return unless defined $val;
  return $val unless ref($val);
  return $val->[0];
}

1;
