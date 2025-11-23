# Extension for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2021-2025 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::PluggableAuth::Provider::Egroupware;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Egroupware

This is the Egroupware provider based on Foswiki::PluggableAuth::Provider::OpenID.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OpenID ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OpenID );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);
  my $tenant = $this->prop("Tenant") // "";

  $this->{_openid_config} = {
    "authorization_endpoint" => "$tenant/authorize",
    "token_endpoint" => "$tenant/access_token",
    "user_endpoint" => "$tenant/userinfo",
    "jwks_uri" => "$tenant/jwks",
    "scopes_supported" => [
      "address", 
      "basic",
      "email",
      "openid",
      "phone",
      "profile", 
    ]
  };

  return $this;
}

=begin TML

---++ ObjectMethod getConfig($type) -> $config

returns the <nop>OpenID configuration of the given type.
Config items are declared in the constructor. Types can be :

   * authorization_endpoint
   * token_endpoint
   * user_endpoint
   * jwks_uri
   * scopes_supported

=cut

sub getConfig {
  my ($this, $type) = @_;

  return defined($type) ? $this->{_openid_config}{$type} : $this->{_openid_config};
}

1;
