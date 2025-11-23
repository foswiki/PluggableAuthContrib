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

package PluggableAuthLdapProviderTests;

use strict;
use warnings;

use PluggableAuthTestCase;
use Foswiki::PluggableAuth ();
use Foswiki::PluggableAuth::Provider::Ldap ();
use Error qw(:try);

our @ISA = qw( PluggableAuthTestCase );

sub loadExtraConfig {
  my $this = shift;

  $this->SUPER::loadExtraConfig(@_);
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Enabled} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrefetchUsers} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportGroups} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportUsers} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IgnorePrivateGroups} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{SyncOnLogin} = 1;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Visible} = 0;
  $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LogoutURL} = '/';
}

sub set_up {
  my $this = shift;

  $this->SUPER::set_up;

  $this->{provider} = $this->{auth}->getProvider("Ldap1");
  $this->{isConfigured} = ($this->{provider}->prop("Host")) ? 1:0;
}

sub tear_down {
  my $this = shift;

  undef $this->{provider};
  $this->SUPER::tear_down();
}

sub test_self {
  my $this = shift;

  $this->assert_provider($this->{provider});
  $this->assert($this->{provider}->isa("Foswiki::PluggableAuth::Provider::Ldap"));
}

sub test_id {
  my $this = shift;

  my $pid = $this->{provider}->prop("id");
  $this->assert_equals("Ldap1", $pid);
}

sub test_props {
  my $this = shift;

  my $props = $this->{provider}->props;

  $this->assert_equals(54, scalar(keys %$props));
  $this->assert($props->{Enabled});
  $this->assert($props->{PrefetchUsers});
  $this->assert($props->{ImportUsers});
  $this->assert($props->{ImportGroups});
  $this->assert($props->{SyncOnLogin});
  $this->assert($props->{IgnorePrivateGroups});
  $this->assert($props->{Name});
  $this->assert($props->{Module});
  $this->assert(!$props->{Visible});
  $this->assert_equals('/', $props->{LogoutURL});
}

sub test_connect {
  my $this = shift;

  return unless $this->{isConfigured};

  $this->{provider}->connect;
}

sub test_deleteAll {
  my $this = shift;

  $this->{provider}->deleteAll;
}

sub test_refresh {
  my $this = shift;

  $this->{provider}->refresh;
}

1;
