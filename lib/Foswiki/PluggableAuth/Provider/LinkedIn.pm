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

package Foswiki::PluggableAuth::Provider::LinkedIn;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::LinkedIn

This is the <nop>LinkedIn provider based on Foswiki::PluggableAuth::Provider::OpenID.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OpenID ();
our @ISA = qw(Foswiki::PluggableAuth::Provider::OpenID );

=begin TML

---++ ObjectMethod getDiscoveryUri() -> $uri

This method returns the url of the discovery endpoint for the <nop>OpenID protocol.

=cut

sub getDiscoveryUri {
  my $this = shift;

  return "https://www.linkedin.com/oauth/.well-known/openid-configuration";
}

1;
