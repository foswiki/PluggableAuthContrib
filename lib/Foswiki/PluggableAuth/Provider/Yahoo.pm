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

package Foswiki::PluggableAuth::Provider::Yahoo;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Yahoo

This is the Yahoo provider based on Foswiki::PluggableAuth::Provider::OpenID.

FIX: This provider is still experimental as we weren't able to authenticate
successfully and fetch user information.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OpenID ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OpenID );

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $userInfo

FIX: not implemented yet as Yahoo doesn't seem to follow <nop>OpenID here

=cut

sub fetchUser {
  my ($this, $accessToken) = @_;

  $this->writeDebug("called fetchUser()");
}

=begin TML

---++ ObjectMethod getSupportedScopes() -> $scopes

returns an array of supported scopes: 'openid', 'profile' and 'email'

=cut

sub getSupportedScopes {
  my $this = shift;

  return ['openid', 'profile', 'email'];
}

### static helper

sub _writeError {
  print STDERR "PluggableAuth::Provider::Yahoo - ERROR: $_[0]\n";
}

1;
