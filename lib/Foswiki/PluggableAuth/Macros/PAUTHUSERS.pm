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

package Foswiki::PluggableAuth::Macros::PAUTHUSERS;

=begin TML

---+ package Foswiki::PluggableAuth::Macros::PAUTHUSERS

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Foswiki::Time ();

sub handle {
  my ($session, $params, $topic, $web, $topicObject) = @_;

  my $pauth = Foswiki::PluggableAuth->new();

  my $theHeader = $params->{header} || '';
  my $theFooter = $params->{footer} || '';
  my $theLimit = $params->{limit} || 0;
  my $theSkip = $params->{skip} || 0;
  my $theInclude = $params->{include};
  my $theExclude = $params->{exclude};
  my $theProp = $params->{property} // "wikiName";
  my $theSort = $params->{sort} // 'wikiName';
  my $thePid = $params->{pid} // $params->{provider};
  my $theCasesensitive = Foswiki::Func::isTrue($params->{casesensitive}, 1);
  my $theDateFormat = $params->{dateformat} // $Foswiki::cfg{DateManipPlugin}{DefaultDateTimeFormat} // '$day $mon $year - $hour:$min';
  my $theShowAll = Foswiki::Func::isTrue($params->{showall}, 0);

  $theProp = "wikiName" unless $theProp =~ /^(pid|id|loginName|email|wikiName|displayName|firstName|middleName|lastName|registrationDate|initials|loginDate|picture)$/;

  my $currentUser = Foswiki::Func::getCanonicalUserID();

  my $theFormat = $params->{format};
  $theFormat = '   1 $wikiName' unless defined $theFormat;

  my $theSep = $params->{separator};
  $theSep = $params->{sep} unless defined $theSep;
  $theSep = '$n' unless defined $theSep;

  $theSkip =~ s/[^\d]//g;
  $theLimit =~ s/[^\d]//g;

  my $index = 0;
  my @result = ();
  my %opts = ();
  $opts{sort} = $theSort;
  $opts{pid} = $thePid if $thePid;
  $opts{enabled} = 1 unless $theShowAll;
  my $it = $pauth->eachUser(%opts);

  while ($it->hasNext) {
    my $user = $it->next;

    my $prop = $user->prop($theProp) // "";

    if ($theCasesensitive) {
      next if $theExclude && $prop =~ /$theExclude/;
      next if $theInclude && $prop !~ /$theInclude/;
    } else {
      next if $theExclude && $prop =~ /$theExclude/i;
      next if $theInclude && $prop !~ /$theInclude/i;
    }

    $index++;
    next if $index <= $theSkip;
    my $line = $theFormat;

    my $cloak = ($Foswiki::cfg{AntiSpam}{HideUserDetails} && !$session->{context}{isadmin} && $user->prop("id") ne $currentUser) ? 1 : 0;
    while (my ($key, $val) =  each %{$user->props}) {
      $val //= '';
      $val = '' if $cloak && $key !~ /^(wikiName|loginName|id)$/;
      $line =~ s/\$$key\b/$val/g;
    }

    my $provider = $user->getProvider();
    my $domainName = $provider->prop("DomainName") // "";
    my $provName = $provider->prop("Name");
    my $twofa = $user->isTwoFactorAuthEnabled() ? "on" : "off";

    $line =~ s/\$2fa\b/$twofa/g;
    $line =~ s/\$index\b/$index/g;
    $line =~ s/\$providerName\b/$provName/g;
    $line =~ s/\$providerDomain\b/$domainName/g;
    $line =~ s/\$formatTime\((.*?)\)/$1?Foswiki::Time::formatTime($1, $theDateFormat):""/ge;
    push @result, $line;

    last if $index == $theLimit;
  }
  return "" unless @result;

  my $result = $theHeader. join($theSep, @result) . $theFooter;
  my $count = scalar(@result);
  $result =~ s/\$count\b/$count/g;

  return Foswiki::Func::decodeFormatTokens($result);
}

1;
