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

package Foswiki::PluggableAuth::UserAgent;

=begin TML

---+ package Foswiki::PluggableAuth::UserAgent

TODO

=cut

use strict;
use warnings;

use LWP::UserAgent();
our @ISA = qw( LWP::UserAgent );

=begin TML

---++ ClassMethod new(%params) -> $this

constructor

=cut

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  my $proxy = $Foswiki::cfg{PROXY}{HOST};
  if ($proxy) {
    $this->proxy(['http', 'https'], $proxy);

    my $noProxy = $Foswiki::cfg{PROXY}{NoProxy};
    if ($noProxy) {
      my @noProxy = split(/\s*,\s*/, $noProxy);
      $this->no_proxy(@noProxy);
    }
  }

  $this->protocols_allowed(['http', 'https']);

# $this->ssl_opts(
#   verify_hostname => 0,
# );

  $this->agent("PluggableAuth Foswiki"); # dont identify as libwww-perl as some providers reject access based on this agent string

  return $this;
}

1;
