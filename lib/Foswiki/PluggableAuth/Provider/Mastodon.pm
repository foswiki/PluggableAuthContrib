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

package Foswiki::PluggableAuth::Provider::Mastodon;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Mastodon

This is the Mastodon provider based on Foswiki::PluggableAuth::Provider::OAuth.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider::OAuth ();

our @ISA = qw(Foswiki::PluggableAuth::Provider::OAuth );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor for this package

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  my $server = $this->prop("Server");
  $server =~ s/\/+$//;

  $this->{_endpoints} = {
    authorization => "$server/oauth/authorize",
    token => "$server/oauth/token",
    user => "$server/api/v1/accounts/verify_credentials"
  };
  
  $this->{_scopes} = 'read';

  return $this;
}

1;

