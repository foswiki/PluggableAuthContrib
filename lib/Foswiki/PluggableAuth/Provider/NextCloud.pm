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

package Foswiki::PluggableAuth::Provider::NextCloud;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::NextCloud

This is the Microsoft/Azure provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OAuth ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  my $url = $this->prop("DomainUrl") // "";

  $this->{_endpoints} = {
    authorization => "$url/apps/oauth2/authorize",
    token => "$url/apps/oauth2/api/v1/token",
    user => "$url/ocs/v1.php/cloud/user?format=json",
  };

  #$this->{_scopes} = 'identity.basic identity.email identity.avatar';

  return $this;
}

=begin TML

---++ ObjectMethod fetchUser($accessToken) -> $data

This method extracts the user data from the right spot as returned
by the standard Foswiki::PluggableAuth::Provider::OAuth::fetchUser() method.

=cut

sub fetchUser {
  my $this = shift;

  my $userInfo = $this->SUPER::fetchUser(@_);
  return $userInfo->{ocs}{data} if defined $userInfo;
}

1;
