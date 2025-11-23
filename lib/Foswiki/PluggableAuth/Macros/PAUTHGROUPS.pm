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

package Foswiki::PluggableAuth::Macros::PAUTHGROUPS;

=begin TML

---+ package Foswiki::PluggableAuth::Macros:;PAUTHGROUPS

TODO

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Func ();

sub handle {
  my ($session, $params, $topic, $web, $topicObject) = @_;

  my $pauth = Foswiki::PluggableAuth->new();

  my $theHeader = $params->{header} || '';
  my $theFooter = $params->{footer} || '';
  my $theLimit = $params->{limit} || 0;
  my $theSkip = $params->{skip} || 0;
  my $theInclude = $params->{include};
  my $theExclude = $params->{exclude};
  my $theSort = $params->{sort} // 'wikiName';
  my $thePid = $params->{pid} // $params->{provider};
  my $theCasesensitive = Foswiki::Func::isTrue($params->{casesensitive}, 1);
  my $theExpand = Foswiki::Func::isTrue($params->{expand}, 0);
  my $theUser = $params->{user};
  my $theGroup = $params->{group};
  my $theShowAll = Foswiki::Func::isTrue($params->{showall}, 0);

  my $theFormat = $params->{format};
  $theFormat = '   1 [[$link][$wikiName]]' unless defined $theFormat;

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
  $opts{wikiName} = $theGroup if $theGroup;

  my $it;

  if ($theUser) {
    my $cUID = Foswiki::Func::getCanonicalUserID($theUser);
    return "" unless $cUID;
    my $user = $pauth->findUser(id => $cUID, loginName => $cUID);
    return "" unless $user;
    $it = $user->eachGroup(%opts);
  } else {
    $it = $pauth->eachGroup(%opts);
  }

  my $self = $pauth->getSelf();

  while ($it->hasNext) {
    my $group = $it->next;

    if ($theCasesensitive) {
      next if $theExclude && $group->prop("wikiName") =~ /$theExclude/;
      next if $theInclude && $group->prop("wikiName") !~ /$theInclude/;
    } else {
      next if $theExclude && $group->prop("wikiName") =~ /$theExclude/i;
      next if $theInclude && $group->prop("wikiName") !~ /$theInclude/i;
    }

    $index++;
    next if $index <= $theSkip;
    my $line = $theFormat;
    while (my ($key, $val) =  each %{$group->props}) {
      $val //= '';
      $line =~ s/\$$key\b/$val/g;
    }

    my $members = "";
    if ($line =~ /\$members\b/) {
      my @members = $group->eachMember($theExpand, $theShowAll)->all;
      $members = join(", ", sort map {$_->prop("wikiName")} @members);
    }

    my $provider = $group->getProvider();
    my $providerName = $provider->prop("Name");
    my $pid = $provider->prop("id");
    my $link = $line =~ /\$link\b/ ? $group->getLink() : "";
    my $canChangeMembership = $line =~ /\$canChangeMembership\b/ ? $provider->canChangeMembership($self, $group) : "";
    my $canChangeGroupName = $line =~ /\$canChangeGroupName\b/ ? $provider->canChangeGroupName($self, $group) : "";
    my $canDeleteGroup = $line =~ /\$canDeleteGroup\b/ ? $provider->canDelete($group) : "";
    my $isEnabled = $line =~ /\$isEnabled\b/ ? ($group->isEnabled() ? 1 : 0) : "";
    my $displayName = $line =~ /\$displayName\b/ ? $group->prop("displayName") : "";

    $line =~ s/\$link\b/$link/g;
    $line =~ s/\$index\b/$index/g;
    $line =~ s/\$pid\b/$pid/g;
    $line =~ s/\$providerName\b/$providerName/g;
    $line =~ s/\$members\b/$members/g;
    $line =~ s/\$isEnabled\b/$isEnabled/g;
    $line =~ s/\$displayName\b/displayName/g;
    $line =~ s/\$canChangeGroupName\b/$canChangeGroupName/g;
    $line =~ s/\$canChangeMembership\b/$canChangeMembership/g;
    $line =~ s/\$canDeleteGroup\b/$canDeleteGroup/g;

    push @result, $line;

    last if $index == $theLimit;
  }
  return "" unless @result;

  my $result = $theHeader. join($theSep, @result) . $theFooter;
  my $total = scalar(@result);
  $result =~ s/\$total\b/$total/g;

  return Foswiki::Func::decodeFormatTokens($result);
}

1;

