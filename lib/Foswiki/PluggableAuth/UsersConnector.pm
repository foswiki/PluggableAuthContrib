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

package Foswiki::PluggableAuth::UsersConnector;

=begin TML

---+ package Foswiki::PluggableAuth::UsersConnector

implements the grid connector interface to access the user database

=cut


use strict;
use warnings;

use Foswiki::Plugins::JQDataTablesPlugin::Connector ();
use Foswiki::PluggableAuth ();
use Error qw(:try);
#use Data::Dump qw(dump);

our @ISA = qw( Foswiki::Plugins::JQDataTablesPlugin::Connector );

use constant TRACE => 0;    # toggle me

=begin TML

---++ ClassMethod new($session) -> $this

constructor

=cut

sub new {
  my ($class, $session) = @_;

  my $this = $class->SUPER::new($session);

  $this->{columnDescription} = {
    'id' => {
      type => 'default',
      data => 'u.id',
      search => 'u.id',
      sort => 'u.id',
    },
    'pid' => {
      type => 'pid',
      data => 'pid',
      search => 'pid',
      sort => 'pid',
    },
    'providerName' => {
      type => 'string',
      data => 'providerName',
      search => 'LOWER(p.name)',
      sort => 'LOWER(p.name)',
      column => 'p.name as providerName',
    },
    'email' => {
      type => 'email',
      data => 'email',
      search => 'email',
      sort => 'email',
    },
    'registrationDate' => {
      type => 'date',
      data => 'registrationDate',
      search => 'registrationDate',
      sort => 'registrationDate',
    },
    'loginDate' => {
      type => 'date',
      data => 'loginDate',
      search => 'loginDate',
      sort => 'loginDate',
    },
    'wikiName' => {
      type => 'user',
      data => 'wikiName',
      search => 'LOWER(displayName)', 
      sort => 'LOWER(displayName)', 
     },
    'displayName' => {
      type => 'default',
      data => 'displayName',
      search => 'LOWER(displayName)', 
      sort => 'LOWER(displayName)', 
     },
    'loginName' => {
      type => 'default',
      data => 'loginName',
      search => 'LOWER(loginName)', 
      sort => 'LOWER(loginName)', 
     },
    'firstName' => {
      type => 'default',
      data => 'firstName',
      search => 'LOWER(firstName)', 
      sort => 'LOWER(firstName)', 
     },
    'middleName' => {
      type => 'default',
      data => 'middleName',
      search => 'LOWER(middleName)', 
      sort => 'LOWER(middleName)', 
     },
    'lastName' => {
      type => 'default',
      data => 'lastName',
      search => 'LOWER(lastName)', 
      sort => 'LOWER(lastName)', 
     },
    'initials' => {
      type => 'default',
      data => 'initials',
      search => 'LOWER(initials)', 
      sort => 'LOWER(initials)', 
     },
    'enabled' => {
      type => 'boolean',
      data => 'u.enabled',
      search => 'u.enabled', 
      sort => 'u.enabled', 
    },
    'picture' => {
      type => 'image',
      data => 'picture',
      search => 'LOWER(picture)',
      sort => 'LOWER(picture)',
    }
  };

  return $this;
}

=begin TML

---++ ObjectMethod DESTROY

undef local properties

=cut

sub DESTROY {
  my $this = shift;

  undef $this->{_auth};
}

=begin TML

---++ ObjectMethod auth() -> $pauthObject

access Foswiki::PluggableAuth service

=cut


sub auth {
  my $this = shift;

  $this->{_auth} = Foswiki::PluggableAuth->new() unless defined $this->{_auth};

  return $this->{_auth};
}

=begin TML

---++ ObjectMethod restHandleSave($request, $response)

this is called by the gridconnector REST handler based on the "oper"
url parameter as provided by the GRID widget.

=cut

sub restHandleSave {
  die "not implemented";
}

=begin TML

---++ ObjectMethod buildQuery($request) -> $string

creates a query based on the current request

=cut

sub buildQuery {
  my ($this, $request) = @_;

  my @query = ();

  my @columns = $this->getColumnsFromRequest($request);
  my $globalFilter = $request->param('search[value]');

  if (defined($globalFilter) && $globalFilter ne "") {
    my $regexFlag = ($request->param("search[regex]") || 'false') eq 'true' ? 1 : 0;

    foreach my $part (split(/\s+/, $globalFilter)) {
      $part =~ s/^\s+//;
      $part =~ s/\s+$//g;
      my $neg = 0;
      if ($part =~ /^-(.*)$/) {
        $part = $1;
        $neg = 1;
      }
      $part = lc($part);

      my @includeFilter = ();
      my @excludeFilter = ();

      foreach my $column (@columns) {
        next unless $column->{searchable};
        my $desc = $this->getColumnDescription($column->{data});
	my $expr;
	if ($regexFlag) {
	  $expr = "$desc->{search} =* '"._sanitizeString($part)."'";
	} else {
	  $expr = "$desc->{search} LIKE '%"._sanitizeString($part)."%'";
	}

        if ($neg) {
          push @excludeFilter, $expr;
        } else {
          push @includeFilter, $expr;
        }
      }

      push @query, "(" . join(" OR ", @includeFilter) . ")"
        if @includeFilter;
      push @query, "NOT (" . join(" OR ", @excludeFilter) . ")"
        if @excludeFilter;
    }
  }

  # build column filter
  foreach my $column (@columns) {
    next unless $column->{searchable};

    my $filter = $column->{search_value};
    next if !defined($filter) || $filter eq "";

    my $regexFlag = $column->{search_regex} eq 'true' ? 1 : 0;

    $filter = Foswiki::Plugins::JQDataTablesPlugin::Connector::urlDecode($filter);

    my $desc = $this->getColumnDescription($column->{data});
    my @includeFilter = ();
    my @excludeFilter = ();

    foreach my $part (split(/\s+/, $filter)) {
      $part =~ s/^\s+//;
      $part =~ s/\s+$//g;

      my $neg = 0;
      if ($part =~ /^-(.*)$/) {
        $part = $1;
        $neg = 1;
      }
      $part = lc($part);

      my $expr;
      if ($regexFlag) {
	$expr = "$desc->{search} =* '"._sanitizeString($part)."'";
      } else {
	$expr = "$desc->{search} LIKE '%"._sanitizeString($part)."%'";
      }

      if ($neg) {
        push @excludeFilter, $expr;
      } else {
        push @includeFilter, $expr;
      }
    }

    push @query, "(" . join(" AND ", @includeFilter) . ")"
      if @includeFilter;
    push @query, "NOT (" . join(" AND ", @excludeFilter) . ")"
      if @excludeFilter;
  }

  push @query, $request->param("query") if $request->param("query");

  my $query = "";
  $query = join(' AND ', @query) if @query;

  writeDebug("query=$query");

  return $query;
}

=begin TML

---++ ObjectMethod getValueOfResult( $doc, $property, $fieldDef ) -> $value

get a property of a result document

=cut

sub getValueOfResult {
  my ($this, $result, $property, $fieldDef) = @_;

  $property =~ s/^[\/#]//;
  my $val = $result->{$property};
  return $val // '';
}

=begin TML

---++ ObjectMethod convertResult( %params ) -> \%row

convert a result to a rows for datatable.

This implementation may be shared among all connectors that deal with foswiki data.

=cut

sub convertResult {
  my ($this, %params) = @_;

  my %row = ();
  my $count = 0;

  foreach my $fieldName (@{$params{fields}}) {
    my $isEscaped = substr($fieldName, 0, 1) eq '/' ? 1 : 0;
    #my $isLinked = substr($fieldName, 0, 1) eq '#' ? 1 : 0; # unused by now

    my $desc = $this->getColumnDescription($fieldName);
    next if !$desc || $desc->{data} eq '#';

    my $fieldValue = $this->getValueOfResult($params{result}, $fieldName);
    
    # generate cell based on column type
    my $cell;

    if ($this->isProtected($fieldName)) {
      $cell = {
	"display" => '***',
	"raw" => '***',
      };
    } elsif ($fieldName eq 'index' || $desc->{type} eq 'index') {
      $cell = {
        "display" => "<span class='rowNumber'>$params{index}</span>",
        "raw" => $params{index},
      };
    } elsif (!$isEscaped && $desc->{type} eq 'date') {
      my $time = "";
      my $html = "";
      my $epoch;
      if ($fieldValue) {
        $epoch = ($fieldValue =~ /^\-?\d+$/) ? $fieldValue : Foswiki::Time::parseTime($fieldValue);

	my $format = $Foswiki::cfg{DateManipPlugin}{DefaultDateTimeFormat} || $Foswiki::cfg{DefaultDateFormat} . ' - $hour:$min';
	$time = Foswiki::Time::formatTime($epoch, $format);

        $html = "<span style='white-space:nowrap'>$time</span>";
      }
      $epoch ||= 0;
      $cell = {
        "display" => $html,
        "epoch" => $epoch,
        "raw" => $time
      };
    } elsif (!$isEscaped && $desc->{type} eq 'user') {
      my @html = ();
      foreach my $item (split(/\s*,\s*/, $fieldValue)) {
        if (Foswiki::Func::topicExists($Foswiki::cfg{UsersWebName}, $item)) {
          my $topicTitle = Foswiki::Func::getTopicTitle($Foswiki::cfg{UsersWebName}, $item);
          push @html, "<a href='" . Foswiki::Func::getViewUrl($Foswiki::cfg{UsersWebName}, $item) . "' style='white-space:nowrap'>$topicTitle</a>";
        } else {
          push @html, $item;
        }
      }
      $cell = {
        "display" => join(", ", @html),
        "raw" => $fieldValue // "",
      };
    } elsif (!$isEscaped && $desc->{type} eq 'email') {
      my $html = $fieldValue ? "<a href='mailto:$fieldValue'>$fieldValue</a>" : "";
      $cell = {
        "display" => $html,
        "raw" => $fieldValue || "",
      };
    } elsif (!$isEscaped && $desc->{type} eq 'boolean') {
      $cell = {
        "display" => $fieldValue ? '<i class="fa-fw fa fa-check" style="color:#4CAF50"></i>' : '<i class="fa-fw fa fa-times" style="color:#FF5722"></i>',
        "raw" => $fieldValue,
      };
    } elsif (!$isEscaped && $desc->{type} eq 'image') {
      $fieldValue //= "";
      $fieldValue = "" if $fieldValue =~ /\bnobody\.png$/;
      my $url = $fieldValue || '';

      $cell = {
        "display" => $url ? "<img src='$url' class='pauthUserPicture' />" : "",
        "raw" => $fieldValue || "",
      };
    } else {
      $fieldValue //= "";

      $cell = {
        "display" => $fieldValue,
        "raw" => $fieldValue,
      };
    }

    if ($cell) {
      $row{$fieldName} = $cell;
      $count++;
    }
  }
  return unless $count;

  return \%row;
}

=begin TML

---++ ObjectMethod search( %params ) -> ($total, $totalFiltered, $data)

perform the actual search and fetch result 

=cut

sub search {
  my ($this, %params) = @_;
  
  my %sort;

  foreach my $s (split(/\s*,\s*/, $params{sort})) {
    next if $s eq 'index';
    my $desc = $this->getColumnDescription($s);
    next unless defined $desc;
    $sort{$s} = {
      column => $desc->{sort},
      direction => "ASC",
    };
  }

  foreach my $r (split(/\s*,\s*/, $params{reverse})) {
    my $desc = $this->getColumnDescription($r);
    next unless defined $desc;

    my $rec = $sort{$r};
    next unless defined $rec;

    $sort{$r}{direction} = "DESC";
  }

  my $orderBy = "";
  if (keys %sort) {
    $orderBy = "ORDER BY " . join(", ", map { $_->{column} . " " . $_->{direction}} values %sort);
  }
  writeDebug("orderBy=$orderBy");

  my %columns;
  foreach my $field (@{$params{fields}}) {
    my $column = $this->getSQLColumnOfField($field);
    next unless $column;
    next if $column eq 'null'; # SMELL SMELL
    $columns{"$column"} = 1;
  }
  $columns{wikiName} = 1;
  #$columns{"group_concat(distinct gid) as gid"} = 1;
  my $columns = join(", ", keys %columns);

  writeDebug("columns=$columns");

  my $where = "";
  $where = "WHERE $params{query}" if $params{query}; # sanitized in buildQuery

  my $limit = "";
  $limit = "LIMIT $params{skip},18446744073709551615" if $params{skip};

  my $baseStm = <<"SQL";
SELECT $columns FROM PluggableAuth_users AS u 
  LEFT JOIN PluggableAuth_providers AS p ON u.pid = p.id 
  LEFT JOIN PluggableAuth_group_members AS m ON u.id = m.mid
  $where 
  GROUP BY u.id
SQL

  writeDebug("... baseStm=$baseStm");

#print STDERR "baseStm=$baseStm\n";

  my $error;
  my $it;
  my $dbh = $this->auth->db->handler;
  try {

    my $stm = $baseStm . " $orderBy $limit";
    writeDebug("... stm=$stm");

    $it = Foswiki::Iterator::DBIterator->new($dbh, $stm, []);

  } catch Error with {
    $error = shift->stringify();
    print STDERR "UsersConnector: ERROR - $error\n";
  };

  return (0, 0, []) unless $it;

  my @data = ();

  my $index = $params{skip} || 0;
  my $totalFiltered = 0;
  my $wikiName = Foswiki::Func::getWikiName();
  my $web = $Foswiki::cfg{UsersWebName};
  my $context = Foswiki::Func::getContext();

  while ($it->hasNext) {
    my $hit = $it->next();

    next if !$context->{isadmin} && !Foswiki::Func::checkAccessPermission('VIEW', $wikiName, undef, $hit->{wikiName}, $web);

    $index++;
    $totalFiltered++;

    my $row = $this->convertResult(
      fields => $params{fields},
      result => $hit,
      index => $index, 
    );

    push @data, $row if $row;
    last if $params{limit} > 0 && $index >= $params{skip} + $params{limit};
  }

  my $total = $dbh->do($baseStm);
  writeDebug("totalFiltered=$totalFiltered, total=$total");

  return ($totalFiltered, $total, \@data);
}

sub getSQLColumnOfField {
  my ($this, $field) = @_;

  return unless $field;
  return if $field =~ /^(topic|index)$/;

  my $desc = $this->getColumnDescription($field);
  return unless $desc;

  return $desc->{column} || $desc->{data} || $field;
}

sub writeDebug {
  return unless TRACE;

  #Foswiki::Func::writeDebug("UsersConnector - $_[0]");
  print STDERR "UsersConnector - $_[0]\n";
}

sub _sanitizeString {
  my $str = shift;

  return unless defined $str;

  $str =~ s/[^\w\s\.\/\%_]//g;

  return $str;
}

sub _sanitizeStringList {
  my $str = shift;

  return unless defined $str;
  return map {_sanitizeString($_)} split(/\s*,\s*/, $str);
}

sub _sanitizeInteger {
  my $str = shift;

  return unless defined $str;

  $str =~ s/[^\-\+\d]//g;

  return $str;
}

sub _sanitizeFloat {
  my $str = shift;

  return unless defined $str;

  $str =~ s/[^\-\+\.\d]//g;

  return $str;
}

1;
