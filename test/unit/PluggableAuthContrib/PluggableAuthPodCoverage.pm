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

package PluggableAuthPodCoverage;

use strict;
use warnings;

use File::Basename;
use FoswikiTestCase;
use FoswikiPodCoverage ();
use Foswiki::Plugins::TopicTitlePlugin();

our @ISA = qw( FoswikiTestCase );

BEGIN {

  no strict 'refs';

  my $file = __FILE__;
  my $dir = dirname($file);
  my $extDir = $dir =~ /Plugin$/ ? "Plugins" : "Contrib";
  
  my $manifest = "$ENV{FOSWIKI_ROOT}/lib/Foswiki/$extDir/$dir/MANIFEST";
  die "MANIFEST not found at $manifest" unless -e $manifest;

  my $FH;
  open($FH, '<', $manifest) or die "cannot open MANIFEST file at $manifest";

  while (my $line = <$FH>) {
    next unless $line =~ /^lib\/(Foswiki.*)\.pm/;

    my $pkg = $1;
    $pkg =~ s/\//::/g;

    next if $pkg =~ /^Foswiki::Configure/;

    my $sub = "test_$pkg";
    $sub =~ s/::/_/g;
    $sub = "PluggableAuthPodCoverage::".$sub;
 
    *$sub = sub {
      shift->pod_coverage($pkg);
    }
  }

  close $FH;

  use strict 'refs';
}

sub pod_coverage {
  my ($this, $pkg) = @_;

  my $pc = FoswikiPodCoverage->new(package => $pkg);

  my $coverage = $pc->coverage;

  if (defined $coverage) {
    $coverage = int($coverage * 100);
    my $msg = "$pkg is not fully documented. Pod coverage currently is $coverage%. Uncovered functions:\n   ". join("\n   ", sort $pc->uncovered)."\n";
    #print STDERR "### coverage=$coverage\n";
    $this->assert_equals(100, $coverage, $msg);
  } else {
    my $why = $pc->why_unrated;

    $this->assert($why =~ /^no public symbols defined/, "Pod of $pkg is unrated: ". $why);
  }
}

1;
