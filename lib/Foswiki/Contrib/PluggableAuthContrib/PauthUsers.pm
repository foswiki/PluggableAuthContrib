# Extension for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2025 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::Contrib::PluggableAuthContrib::PauthUsers;

=begin TML

---+ package Foswiki::Contrib::PluggableAuthContrib::PauthUsers

This package wraps the jQuery module =PauthUsers=.

=cut

use strict;
use warnings;

use Foswiki::Plugins ();
use Foswiki::Contrib::PluggableAuthContrib ();
use Foswiki::Plugins::JQueryPlugin::Plugin ();

our @ISA = qw( Foswiki::Plugins::JQueryPlugin::Plugin );

=begin TML

---++ ClassMethod new($session) -> $this

Constructor for this module. This will be called by Foswiki::Plugins::JQueryPlugin::createPlugin().

=cut

sub new {
  my $class = shift;
  my $session = shift || $Foswiki::Plugins::SESSION;

  my $this = bless(
    $class->SUPER::new(
      $session,
      name => 'PauthUsers',
      version => $Foswiki::Contrib::PluggableAuthContrib::VERSION,
      author => 'Michael Daum',
      homepage => 'http://foswiki.org/Extensions/PluggableAuthContrib',
      puburl => '%PUBURLPATH%/%SYSTEMWEB%/PluggableAuthContrib',
      documentation => '%SYSTEMWEB%.PluggableAuthContrib',
      javascript => ['pauthusers.js'],
      dependencies => ['ui::dialog', 'blockui', 'wikiword', 'validate', 'ajaxform', 'jsonrpc', 'pnotify', 'foswikitemplate'],
    ),
    $class
  );

  return $this;
}

1;

