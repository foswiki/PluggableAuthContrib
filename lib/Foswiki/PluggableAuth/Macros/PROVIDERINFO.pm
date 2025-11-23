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

package Foswiki::PluggableAuth::Macros::PROVIDERINFO;

=begin TML

---+ package Foswiki::PluggableAuth::Macros::PROVIDERINFO

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Error qw(:try);

sub handle {
  my($session, $params, $topic, $web, $topicObject) = @_;

  my $pauth = Foswiki::PluggableAuth->new();

  my $header = $params->{header} // '';
  my $format = $params->{format} // '$name';
  my $footer = $params->{footer} // '';
  my $separator = $params->{separator} // ', ';
  my $doVisible = $params->{showvisible};
  my $doExternal = $params->{showexternal};
  my $doInternal = $params->{showinternal};
  my $doAllowed = $params->{showallowed};
  my $doAll = $params->{showall};
  my $include = $params->{include};
  my $exclude = $params->{exclude};

  $doVisible = Foswiki::Func::isTrue($doVisible)?1:0 if defined $doVisible;
  $doExternal = Foswiki::Func::isTrue($doExternal)?1:0 if defined $doExternal;
  $doInternal = Foswiki::Func::isTrue($doInternal)?1:0 if defined $doInternal;
  $doAllowed = Foswiki::Func::isTrue($doAllowed)?1:0 if defined $doAllowed;
  $doAll = Foswiki::Func::isTrue($doAll)?1:0 if defined $doAll;

  my @result = ();
  my @providers = ();

  my $pid = $params->{_DEFAULT} || $params->{id};
  if ($pid) {

    my $provider;
    my $error;

    try {
      $provider = $pauth->getProvider($pid);
    } catch Error with {
      $error = shift;
      $error =~ s/ at .*$//s;
    };

    return _inlineError($error) if defined $error;

    push @providers, $provider;
  } else {
    @providers = $pauth->getProviders($doAll);;
  }

  my $index = 1;
  foreach my $provider (@providers) {
    next if defined $doVisible && $provider->isVisible ne $doVisible;
    next if defined $doExternal && $provider->isExternalLogin ne $doExternal;
    next if defined $doInternal && $provider->isInternalLogin ne $doInternal;
    next if defined $doAllowed && $provider->isAllowedIpAddress ne $doAllowed;
    next if defined $include && $provider->prop("Name") !~ /$include/;
    next if defined $exclude && $provider->prop("Name") =~ /$exclude/;

    my $line = $format;
    $line =~ s/\$name\b/$provider->prop("Name")/ge;
    $line =~ s/\$id\b/$provider->prop("id")/ge;
    $line =~ s/\$enabled\b/$provider->isEnabled?1:0/ge;
    $line =~ s/\$visible\b/$provider->isVisible?1:0/ge;
    $line =~ s/\$external\b/$provider->isExternalLogin?1:0/ge;
    $line =~ s/\$internal\b/$provider->isInternalLogin?1:0/ge;
    $line =~ s/\$allowed\b/$provider->isAllowedIpAddress?1:0/ge;
    $line =~ s/\$index\b/$index/g;
    push @result, $line;
    $index++;
  }

  my $count = scalar(@result);
  return "" unless $count;

  my $result = $header.join($separator, @result).$footer;
  $result =~ s/\$count\b/$count/g;

  return Foswiki::Func::decodeFormatTokens($result);
}

sub _inlineError {
  return "<span class='foswikiAlert'>$_[0]</span>";
}

1;

