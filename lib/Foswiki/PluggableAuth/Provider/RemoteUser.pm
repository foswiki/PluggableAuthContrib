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

package Foswiki::PluggableAuth::Provider::RemoteUser;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::RemoteUser

This provider extracts the user from the HTTP request
itself. Authentication itself is handled externally, for example by the web server itself.
Note that the remote user must be known to the system otherwise using one of the other
identity providers (Topic, Ldap, ...)

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

=begin TML

---++ ObjectMethod isInternalLogin() -> $boolean

Returns false as this provider cannot authenticate a user itself.

=cut

sub isInternalLogin {
  return 0;
}

=begin TML

---++ ObjectMethod processLogin()

This method processes the login by extracting the remote_user from the HTTP request

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  return unless $this->handlesLogin($request, $state);
  $this->writeDebug("called processLogin");

  my $authName = $request->remote_user;
  unless (defined $authName && $authName ne "") {
    $this->writeDebug("REMOTE_USER not set");
    return;
  }
  $this->writeDebug("loginName=$authName");

  my $user = $this->auth->findUser(email => $authName, loginName => $authName);
  return $user if defined $user && $user->isEnabled;
  return;
}

1;

