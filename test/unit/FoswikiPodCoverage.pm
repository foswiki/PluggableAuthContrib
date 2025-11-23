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

package FoswikiPodCoverage;

use strict;
use warnings;

use Pod::Coverage ();
use Pod::Find qw(pod_where);

use base 'Pod::Coverage';

sub _get_pods {
  my $this = shift;

  my $package = $this->{package};

  $this->{pod_from} ||= pod_where({-inc => 1}, $package);

  my $pod_from = $this->{pod_from};
  unless ($pod_from) {
    $this->{why_unrated} = "couldn't find pod";
    return;
  }

  my $pod = FoswikiPodExtractor->new;
  $pod->{nonwhitespace} = $this->{nonwhitespace};
  $pod->parse_from_file($pod_from, '/dev/null');

  return $pod->{identifiers} || [];
}

package FoswikiPodExtractor; ## no critic

use base 'Pod::Coverage::Extractor';

use constant TRACE => 0;

sub textblock {
  my ($this, $text, $line_num, $pod_para) = @_;

  #print STDERR "called textblock($text)\n" if TRACE;

  foreach my $line (split(/\r?\n/, $text)) {
    my $pod;
    if ($line =~ /^---\+(?:!!)?\s+package\s+(\S+)/) {
      $pod = $1;
    }
    if ($line =~ /^---\++\s+\w+Method\s+(.*?)\(.+$/) {
      $pod = $1;
    }

    unless ($pod) {
      print STDERR "... ignoring $line\n" if TRACE;
      next;
    }

    print STDERR "... adding '$pod'\n" if TRACE;

    my $section = $this->{nonwhitespace} ? "recent" : "identifiers";
    push @{$this->{$section}}, $pod;
  }
}

1;
