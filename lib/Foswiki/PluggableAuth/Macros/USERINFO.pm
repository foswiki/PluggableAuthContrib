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

package Foswiki::PluggableAuth::Macros::USERINFO;

=begin TML

---+ package Foswiki::PluggableAuth::Macros::USERINFO

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Foswiki::Macros::USERINFO ();

BEGIN {
  no warnings 'redefine'; ## no critic

  *Foswiki::origUSERINFO = \&Foswiki::USERINFO;
  *Foswiki::USERINFO = \&handle;

  use warnings 'redefine';
}

sub handle {
  my ($session, $params) = @_;    

  my $currentUser = Foswiki::Func::getCanonicalUserID();
  my $name = $params->{_DEFAULT};

  if ($name && $name =~ /@/) {
    my @wikiNames = Foswiki::Func::emailToWikiNames($name);
    $name = shift @wikiNames;
  }

  my $cUID = $name ? Foswiki::Func::getCanonicalUserID($name) : $currentUser;
  return Foswiki::origUSERINFO($session, $params) unless defined $cUID;

  my $pauth = Foswiki::PluggableAuth->new();
  my $user = $pauth->getObjectByID($cUID);
  return "" unless defined $user;

  $user = $user->load;
  return "" unless defined $user;

  my $showAll = Foswiki::Func::isTrue($params->{showall}, 0);
  return "" unless $showAll || $user->isEnabled();

  my $cloak = ($Foswiki::cfg{AntiSpam}{HideUserDetails} && !$session->{context}{isadmin} && $cUID ne $currentUser)?1:0;
  my $format = $params->{format} || '$username, $wikiusername, $emails';

  if ($cloak) {
    $format =~ s/\$(id|pid|loginName|wikiName|displayName|email|firstName|middleName|lastName|initials|enabled|loginDate|picture)\b/\0/g;
    $format =~ s/\$registrationDate(?:\((.*?)\))?\b/\0/g;
  } else {

    my $provider = $user->getProvider();
    my $twoFactorAuth = $provider->prop("TwoFactorAuthEnabled") // "\0";
    my $dateTimeFormat = $Foswiki::cfg{DateManipPlugin}{DefaultDateTimeFormat} // '$day $mon $year - $hour:$min';
    my $picture = $user->prop("picture") || '%PUBURLPATH%/%SYSTEMWEB%/PluggableAuthContrib/nobody.png';
    my $loginDate = $user ? $user->prop("loginDate") // "" : "";
    if ($loginDate) {
      $loginDate = Foswiki::Time::formatTime($loginDate, $dateTimeFormat);
    } else {
      $loginDate = "\0";
    }

    $format =~ s#\$(id|pid|loginName|wikiName|displayName|email|firstName|middleName|lastName|initials|enabled)\b#$user?$user->prop($1)||"\0":"\0"#ge;
    $format =~ s/\$registrationDate(?:\((.*?)\))?\b/$user?Foswiki::Time::formatTime($user->prop("registrationDate"), $1):"\0"/ge;
    $format =~ s/\$loginDate\b/$loginDate/g;
    $format =~ s/\$picture\b/$picture/g;
    $format =~ s/\$twoFactorAuth\b/$twoFactorAuth/g;
    $format =~ s/\$twoFactorAuthEnabled\b/$user?($user->isTwoFactorAuthEnabled?1:0):0/ge;
    $format =~ s/\$twoFactorAuthConfigured\b/$user?($user->isTwoFactorAuthConfigured?1:0):0/ge;
  }

  # prepare before calling origUSERINFO
  $params->{format} = $format;
  $params->{_DEFAULT} = $user->prop("wikiName"); # SMELL

  my $result = Foswiki::origUSERINFO($session, $params);
  $result =~ s/\0//g;

  return $result;
}

1;
