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

package Foswiki::PluggableAuth::Provider::Unknown;

=begin TML

---+ package Foswiki::PluggableAuth::Provider::Unknown

This provider is a fallback for any user or group that lost their initial provider,
i.e. when it has been disabled

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider ();
our @ISA = qw(Foswiki::PluggableAuth::Provider );

sub refersh {}

sub canCheckPassword {
  return 0;
}

sub canSetPassword {
  return 0;
}

sub canSetEmail {
  return 0;
}

sub canDelete {
  my ($this, $obj) = @_;

  return $this->handles($obj) ? 1 : 0;
}

sub canRegisterUser {
  return 0;
}

sub canCreateGroup {
  return 0;
}

sub canChangeMembership {
  return 0;
}

sub handles {
  my ($this, $obj) = @_;

  return 0 unless defined $obj;

  my $provider = $obj->getProvider();
  my $pid = defined $provider ? $provider->prop("id") : 'Unknown';

  return $pid eq 'Unknown';
}

1;
