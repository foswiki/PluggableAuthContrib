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

package Foswiki::PluggableAuth::Macros::LDAP;

=begin TML

---+ package Foswiki::PluggableAuth::Macros::LDAP

TODO

=cut

use strict;
use warnings;

use Foswiki::Contrib::CacheContrib ();
use Foswiki::PluggableAuth ();
use Foswiki::Func ();
use Digest::MD5 ();
use Error qw(:try);
use Encode ();

sub handle {
  my ($session, $params, $topic, $web, $topicObject) = @_;

  my $pauth = Foswiki::PluggableAuth->new();

  _writeDebug("called handle");

  my $theWarnings = Foswiki::Func::isTrue($params->{warn}, 1);
  my $theProvider = $params->{pid};

  unless ($theProvider) {
    # find the first ldap provider which is enabled
    foreach my $pid (sort grep {/^Ldap/} keys %{$Foswiki::cfg{PluggableAuth}{Providers}}) {
      if ($Foswiki::cfg{PluggableAuth}{Providers}{$pid}{Enabled}) {
        $theProvider = $pid;
        last;
      }
    }
  }
  return ($theWarnings ? _inlineError("no ldap provider available") : "") unless $theProvider;

  my $ldap = $pauth->getProvider($theProvider);
  return ($theWarnings ? _inlineError("unknown ldap provider $theProvider") : "") unless defined $ldap && ref($ldap) eq 'Foswiki::PluggableAuth::Provider::Ldap';

  my $request = Foswiki::Func::getRequestObject();
  my $theRefresh = $request->param('refresh') || '';
  $theRefresh = 1 if $theRefresh =~ /^(on|ldap)$/;

  my $cache;
  my $fingerPrint;
  my $theCache = $params->{cache};
  $theCache = $Foswiki::cfg{PluggableAuth}{CacheExpire} // 3600 if !defined($theCache) || $theCache eq 'on';
  $theCache = 0 if $theCache eq 'off';

  if ($theCache) {
    $fingerPrint = Digest::MD5::md5_hex(Encode::encode_utf8($params->stringify()));
    _writeDebug("fingerPrint=$fingerPrint");
    $cache = Foswiki::Contrib::CacheContrib::getCache("Ldap", $theCache);
    if ($theRefresh) {
      _writeDebug("refreshing cache item");
      $cache->remove($fingerPrint);
    }
    my $data = $cache->get($fingerPrint);
    if ($data) {
      _writeDebug("found response in cache");
      return $data;
    } else {
      _writeDebug("not found in cache ... recomputing");
    }
  }

  # get args
  my $theFilter = $params->{filter} || $params->{_DEFAULT} || '';
  my $theFormat = $params->{format} || '$dn';
  my $theHeader = $params->{header} || '';
  my $theFooter = $params->{footer} || '';
  my $theSort = $params->{sort} || '';
  my $theReverse = Foswiki::Func::isTrue($params->{reverse}, 0);
  my $theLimit = $params->{limit} || 0;
  my $theSkip = $params->{skip} || 0;
  my $theHideNull = Foswiki::Func::isTrue($params->{hidenull}, 0);
  my $theNullFormat = $params->{nullformat} || '';
  my $theClear = $params->{clear} || '';
  my $theExclude = $params->{exclude} || '';
  my $theInclude = $params->{include} || '';
  my $theCasesensitive = Foswiki::Func::isTrue($params->{casesensitive}, 1);
  my $theBlobAttrs = $params->{blob} || '';
  my $theScope = $params->{scope} || 'sub';

  my %blobAttrs = map {$_ => 1} split(/\s*,\s*/, $theBlobAttrs);

  # backwards compatibility. note that you won't be able to have a jpegPhoto attribute
  # in your ldap that is _not_ to be handled as a blob 
  $blobAttrs{jpegPhoto} = 1; 

  my $theSep = $params->{separator};
  $theSep = $params->{sep} unless defined $theSep;
  $theSep = '$n' unless defined $theSep;

  my $theValueSep = $params->{value_separator};
  $theValueSep = ", " unless defined $theValueSep;


  # fix args
  $theSkip =~ s/[^\d]//g;
  $theLimit =~ s/[^\d]//g;
  my @theSort = split(/[\s,]+/, $theSort);

  _writeDebug("filter=$theFilter");
  #_writeDebug("format=$theFormat");

  my $theBase = $params->{'base'};

  # search
  my @entries = ();
  my $error;

  try {  
    my $search = $ldap->search(
      filter => $theFilter,
      base => $theBase,
      scope => $theScope,
      sizelimit => $theReverse ? 0 : $theLimit,
      callback => sub {
        push @entries, $_[1];
      }
    );

    # DISABLED: as it destroys the @entries array colleced while following references etc
    # TODO: use our own sorting or borrow from Net::LDAP::Search
    #@entries = $search->sorted(@theSort); 

  } catch Error with {
    $error = shift;
    $error =~ s/ at .*$//;
    $error =~ s/^\s+//;
    $error =~ s/\s+$//;
  };
  return ($theWarnings ? _inlineError("ERROR: $error") : "") if defined $error;


  @entries = reverse @entries if $theReverse;
  my $index = 0;
  my @results = ();
  foreach my $entry (@entries) {
    my $dn = $ldap->getDN($entry);
    if ($theCasesensitive) {
      next if $theExclude && $dn =~ /$theExclude/;
      next if $theInclude && $dn !~ /$theInclude/;
    } else {
      next if $theExclude && $dn =~ /$theExclude/i;
      next if $theInclude && $dn !~ /$theInclude/i;
    }

    $index++;
    next if $index <= $theSkip;

    my %data;
    $data{dn} = $dn;
    $data{index} = $index;
    foreach my $attr ($entry->attributes()) {
      if ($blobAttrs{$attr}) { 
        $data{$attr} = $ldap->cacheBlob($entry, $attr, $theRefresh);
      } else {
        $data{$attr} = join($theValueSep, $ldap->getValues($entry, $attr));
      }
    }
    push @results, _expandVars($theFormat, %data);
    last if $index == $theLimit;
  }

  my $count = scalar(@results);
  unless ($count) {
    return $theHideNull?"":Foswiki::Func::decodeFormatTokens($theNullFormat);
  }

  my $result = $theHeader . join($theSep, @results) . $theFooter;
  $result =~ s/\$count\b/$count/g;

  #_writeDebug("result=$result");

  if ($theClear) {
    $theClear =~ s/\$/\\\$/g;
    my $regex = join('|', split(/[\s,]+/, $theClear));
    $result =~ s/$regex//g;
  }

  $result = Foswiki::Func::decodeFormatTokens($result);

  if ($theCache) {
    $cache->set($fingerPrint, $result, $theCache);
  }

  _writeDebug("done handleLdap()");
  return $result;
}

sub _writeDebug {
  print STDERR "PluggableAuth::Macros::LDAP - $_[0]\n" if $Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Debug} || $Foswiki::cfg{PluggableAuth}{Debug};
}

sub _inlineError {
  return "<span class='foswikiAlert'>$_[0]</span>";
}

sub _expandVars {
  my ($format, %data) = @_;

  foreach my $key (keys %data) {
    my $value = $data{$key};
    next unless defined $value;
    $value = join(', ', sort @$value) if ref($data{$key}) eq 'ARRAY';

    # format list values using the '$' delimiter in multiple lines; see rfc4517
    # The only attribute I've seen so far where this rule should be used is in in postalAddress.
    # In most other cases this hurts a lot more than anything else.
    if ($key =~ /^(postalAddress)$/) { # TODO: make this rule configurable
      $value =~ s/([^\\])\$/$1<br \/>/g;
      $value =~ s/\\\$/\$/g;
      $value =~ s/\\\\/\\/g;
    }

    $format =~ s/\$$key\b/$value/gi;

    #writeDebug("$key=$value");
  }

  return $format;
}

1;
