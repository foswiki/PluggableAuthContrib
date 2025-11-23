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

package PluggableAuthTestProvider;

use strict;
use warnings;

use Foswiki::PluggableAuth::Provider;

our @ISA = qw( Foswiki::PluggableAuth::Provider );

sub new {
  my $class = shift;

  my $this = $class->SUPER::new(@_);

  $this->{beforeSaveHandlerCounter} = 0;
  $this->{afterSaveHandlerCounter} = 0;

  return $this;
}

sub canDelete { 
  my ($this, $user) = @_;

  return 0 unless $this->handles($user);
  return 1;
};

sub canSetEmail { 
  my ($this, $user) = @_;

  return 0 unless $this->handles($user);
  return 1;
};

sub canSetPassword { 
  my ($this, $user) = @_;

  return 0 unless $this->handles($user);
  return 1;
};

sub canCheckPassword { 
  my ($this, $user) = @_;
  return $this->canSetPassword($user);
};

sub canCreateGroup {
  return 1;
}

sub canChangeMembership {
  return 1;
}

sub canChangeGroupName {
  return 1;
}

sub beforeSaveHandler {
  my ($this, $text, $topic, $web, $meta) = @_;

  #print STDERR "called beforeSaveHandler($web, $topic) for ".$this->prop("id")."\n";
  $this->{beforeSaveHandlerCounter}++;
  #print STDERR ".... $this->{beforeSaveHandlerCounter}\n";
}

sub afterSaveHandler {
  my ($this, $text, $topic, $web, $error, $meta) = @_;

  #print STDERR "called afterSaveHandler($web, $topic) for ".$this->prop("id")."\n";
  $this->{afterSaveHandlerCounter}++;
}

sub updateGroupTopic {
  #my ($this, $group) = @_;

  return 1;  
}

1;
