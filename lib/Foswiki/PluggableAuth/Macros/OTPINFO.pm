# Extension for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2023-2025 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::PluggableAuth::Macros::OTPINFO;

=begin TML

---+ package Foswiki::PluggableAuth::Macro:;OTPINFO

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use URI::Escape qw(uri_escape);

sub handle {
  my($session, $params, $topic, $web, $topicObject) = @_;

  my $pauth = Foswiki::PluggableAuth->new();
  my $twofa = $pauth->getTwoFactorAuth();

  my $result = $params->{_DEFAULT} || $params->{format} // '$otpauth';
  my $issuer = $params->{issuer} // $twofa->prop("Issuer");
  my $keyId = $params->{keyId};

  unless (defined $keyId) {
    my $wikiName = Foswiki::Func::getWikiName();
    my $loginName = Foswiki::Func::wikiToUserName($wikiName);
    $keyId = $loginName;
  }

  my $secret = $twofa->getSecret();
  my @groups = ();
  for (my $i = 0; $i < length($secret); $i += 4) {
    push @groups, substr($secret, $i, 4);
  }
  my $group = join(" ", @groups);

  my $otpauth = 'otpauth://totp/' .
          uri_escape($issuer) . ':' . uri_escape($keyId) .
          '?secret=' . $secret . 
          '&issuer=' . uri_escape($issuer) .
          '&image=' . uri_escape($twofa->prop("LogoUrl"));
  
  $result =~ s/\$otpauth/$otpauth/g;
  $result =~ s/\$issuer/$issuer/g;
  $result =~ s/\$keyid/$keyId/g;
  $result =~ s/\$secret/$group/g;

  return Foswiki::Func::decodeFormatTokens($result);
}

1;
