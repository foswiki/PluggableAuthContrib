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

package Foswiki::PluggableAuth::BaseObject;

=begin TML

---+ package Foswiki::PluggableAuth::BaseObject

This is the base class for Foswiki::PluggableAuth::User and
Foswiki::PluggableAuth::Group objects. It implements the
database interface to initialize these objects accesing
the respective tables. There are two class constants
that are set by the deriving classes:

   * TABLE_NAME: the name of the table that holds the object data
   * TABLE_PROPS: column names that are loaded into the object and made 
     accessible using the =Foswiki::PluggableAuth::BaseObject::prop()= method

Each object is owned by a provider. Some of the object's methods are delegating
work to the provider as objects may be handled differently based on the type
of provider.

Each object can be "enabled" or "disabled". Some operations may be filtering
the state of the object. For example, a user might not log in if the user object is disabled.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth ();
use Foswiki::Iterator::DBIterator ();
#use Data::Dump qw(dump);

use constant TRACE => 0;
use constant TABLE_PROPS => qw();
use constant TABLE_NAME => "";

=begin TML

---++ ClassMethod new(%params) -> $this

constructor 

=cut

sub new {
  my ($class, %params) = @_;

  #$this->writeDebug("called new(). params=".dump(\%params));

  my $this = bless ({
    _props => \%params
  }, $class);

  $this->{_isLoaded} = 0;

  #print STDERR "creating new base object id=".($params{id}//'undef')."\n";

  return $this;
}

=begin TML

---++ ObjectMethod DESTROY()

destructor for this object

=cut

sub DESTROY {
  my $this = shift;

  undef $this->{_props};
}

=begin TML

---++ ObjectMethod auth() -> $auth

returns the Foswiki::PluggableAuth singleton method

=cut

sub auth {
  #my $this = shift;
  return $Foswiki::PluggableAuth::SINGLETON;
}

=begin TML

---++ ObjectMethod db() -> $db

returns the Foswiki::DBI::Database handle of <nop>PluggableAuth.

=cut

sub db {
  my $this = shift;

  return $this->auth->db();
}

=begin TML

---++ ObjectMethod load(%params) -> $object

Loads the object properties from the database. This method
can safely be called multiple times. Properties are only loaded
once and cached within the =_props= hash of the object.

The method returns a reference to =$this= or undefined if no
properties for the current object exist in the database.

=cut

sub load {
  my ($this, %params) = @_;

  #$this->writeDebug("called load()");

  return $this if $this->{_isLoaded};
  %params = %{$this->{_props}} unless keys %params;

  #$this->writeDebug("loading");
  #$this->writeDebug("...params=".dump(\%params));

  return $this->_load("AND", %params);
}

sub find {
  my ($this, %params) = @_;

  return $this->_load("OR", %params);
}

sub _load {
  my ($this, $oper, %params) = @_;

  my $class = ref($this);
  my $stm = "SELECT * FROM PluggableAuth_".$class->TABLE_NAME." WHERE ";

  my @query = ();
  my @values = ();
  my $pid = delete $params{pid};

  foreach my $prop ($class->TABLE_PROPS) {
    my $val = $params{$prop};
    next unless defined $val && $val ne "";

    my $vals;
    if (ref($val)) {
      $vals = $val;
    } else {
      push @$vals, $val;
    }

    my @thisQuery = ();
    foreach my $v (@$vals) {
      next unless defined $v && $v ne "";
      if ($prop eq 'email') { # compare emails case insensitive
        $v = lc($v);
        push @thisQuery, "lower($prop) = ?";
      } else {
        push @thisQuery, "$prop = ?";
      }
      push @values, $v;
    }
    push @query, "(" . join(" OR ", @thisQuery) . ")" if @thisQuery;
  }

  return unless @query && @values;

  $stm .= "(" . join(" $oper ", @query) . ")";

  if (defined $pid) {
    $stm .= " AND pid = ?";
    push @values, $pid;
  }

  #$this->writeDebug("... stm = $stm");
  #$this->writeDebug("... values = ". join(", ", @values));

  #print STDERR "stm=$stm,values=".join(", ", @values)."\n";

  my $sth = $this->db->handler->prepare_cached($stm);
  $sth->execute(@values);

  my @result = ();

  my $obj = $this;
  while (my $row = $sth->fetchrow_hashref()) {
    push @result, $obj->init($row);
    $obj = $this->clone;
  }
  $sth->finish();

  #$this->writeDebug("... result=".dump(\@result));
  #$this->writeDebug("props=".dump($this->{_props}));

  if (@result) {
    #$this->writeDebug("... object(s) found");
    return wantarray ? @result : $result[0];
  }

  #$this->writeDebug("... no objects found");

  return;
}

=begin TML

---++ ObjectMethod reload() -> $object

reloads an object with information from the database.
note that this method might return undefined if the object
of the given id has vanished in the database.

=cut

sub reload {
  my $this = shift;

  $this->{_isLoaded} = 0;

  return $this->load(id => $this->prop("id"));
}

=begin TML

---++ ObjectMethod clone() -> $object

Creates a copy of this object. Any property already
loaded will be copied as well.

=cut

sub clone {
  my $this = shift;

  my $class = ref($this);
  my $that = $class->new();
  %{$that->{_props}} = %{$this->{_props}};

  return $that;
}

=begin TML

---++ ObjectMethod equals($that) -> $boolean

Returns true if =$this= object equals =$that= object.
It loads both objects and the compares all properties.
It will only return true of all properties in both
objects are equal.

=cut

sub equals {
  my ($this, $that) = @_;

  my $thisClass = ref($this);
  my $thatClass = ref($that);
  return 0 unless $thisClass eq $thatClass;

  if ($this->isLoaded || $that->isLoaded) {
    $this->load;
    $that->load;
  }

  foreach my $prop ($thisClass->TABLE_PROPS) {
    my $thisVal = $this->prop($prop);
    my $thatVal = $that->prop($prop);
    return 0 if defined($thisVal) && !defined($thatVal);
    return 0 if !defined($thisVal) && defined($thatVal);
    next unless defined($thisVal) && defined($thatVal);
    return 0 if $thisVal ne $thatVal;
  }

  return 1;
}

=begin TML

---++ ObjectMethod init($row) -> $object

Initializes =$this= object using the given database row.
In addition it will call the provider's Foswiki::PluggableAuth::Provider::initObject()
method in case the object needs further initialization on behalf of the provider
responsible for this object.

=cut

sub init {
  my ($this, $row) = @_;

  #$this->writeDebug("called init()");
  #$this->writeDebug("row=".dump($row));

  return unless defined $row;
  $this->props($row);
  $this->{_isLoaded} = 1;

  return $this;
}

=begin TML

---++ ObjectMethod enable()

enables the current object

=cut

sub enable {
  my $this = shift;

  return $this->update(enabled => 1);
}

=begin TML

---++ ObjectMethod disable()

disables the current object

=cut

sub disable {
  my $this = shift;

  return $this->update(enabled => 0);
}

=begin TML

---++ ObjectMethod isLoaded() -> $boolean

returns true if this object has already been initialized
reading its database properties. See Foswiki::PluggableAuth::BaseObject::load()

=cut

sub isLoaded {
  my $this = shift;

  return $this->{_isLoaded};
}

=begin TML

---++ ObjectMethod isDeleteable() -> $boolean

returns true if the provider for this object can delete it.
Some objects cannot be deleted such as objects provided by
the Foswiki::PluggableAuth::Provider::Base provider

SMELL: duplicate API - see canBeDeleted

=cut

sub isDeleteable {
  my $this = shift;
  
  return $this->getProvider->canDelete($this);
}

=begin TML

---++ ObjectMethod canBeDeleted() -> $boolean

returns true if this object can be deleted by its provider

SMELL: duplicate API - see isDeleteable

=cut

sub canBeDeleted {
  my $this = shift;

  return $this->getProvider->canDelete($this);
}

=begin TML

---++ ObjectMethod isGroup() -> $boolean

returns true if this object is a Foswiki::PluggableAuth::Group object.

=cut

sub isGroup {
  my $this = shift;

  return $this->isa("Foswiki::PluggableAuth::Group") ? 1: 0;
}

=begin TML

---++ ObjectMethod isUser() -> $boolean

returns true if this object is a Foswiki::PluggableAuth::User object.

=cut

sub isUser {
  my $this = shift;

  return $this->isa("Foswiki::PluggableAuth::User") ? 1: 0;
}

=begin TML

---++ ObjectMethod isEnabled() -> $boolean

returns true if this object is enabled. 

=cut

sub isEnabled {
  return shift->prop("enabled");
}

=begin TML

---++ ObjectMethod isUpdateAllowed($prop, $val) -> $boolean

returns true the given property can be updated.

=cut

sub isUpdateAllowed {
  my ($this, $prop, $val) = @_;

  return 0 if $prop eq 'groups';
  return 0 if $prop =~ /^_/;;
  return 1; # may be implemented by sub classes, e.g. is changing the email of a user permitted
}

=begin TML

---++ ObjectMethod readTopic() -> $meta

returns a Foswiki::Meta object for a topic representing this object.

=cut

sub readTopic {
  my $this = shift;

  my ($web, $topic) = $this->getTopic();
  my ($meta) = Foswiki::Func::readTopic($web, $topic);
  return $meta;
}

=begin TML

---++ ObjectMethod update(%params) -> $boolean

stores the object properties into the database and returns
true on success. For example the following code will
update the =displayName= and the =wikiName=:

<verbatim>
$this->update(
  displayName => "Foo Bar",
  wikiName => "FooBar"
);
</verbatim>

=cut

sub update {
  my ($this, %params) = @_;

  $this->writeDebug("called update()");
  #$this->writeDebug("...params=".dump(\%params));

  my $id = $this->prop("id");

  if (!$this->isLoaded && !defined($id)) {
    $this->load();
    $id = $this->prop("id");

    throw Error::Simple("could not update unknown object") unless defined $id && $this->isLoaded;
  }

  #$this->writeDebug("... id=$id");

  my (@fields, @values);
  while (my ($k, $v) = each %params) {
    next unless $this->isUpdateAllowed($k, $v);
    push @fields, "$k=?";
    push @values, $v;
  }
  push @values, $id;
  return 0 unless @fields;

  my $class = ref($this);
  my $stm = "UPDATE PluggableAuth_".$class->TABLE_NAME." SET ". join(", ", @fields)." WHERE id=?";

  #$this->writeDebug("... stm=$stm");

  my $res = $this->db->handler->do($stm, {}, @values);

  while (my ($k, $v) = each %params) {
    $this->prop($k, $v);
  }

  return $res;
}

=begin TML

---++ ObjectMethod getProvider() -> $provider

returns a Foswiki::PluggableAuth::Provider object that is responsible for this object.

=cut

sub getProvider {
  my $this = shift;

  return $this->auth->getProvider($this->prop("pid"));
}

=begin TML

---++ ObjectMethod props($props) -> $props

setter/getter for all props. It takes a =$props= hash
reference and sets the internal object properties.
Note that these may not reflect whats in the database.

Without a =$props= argument will the current object be loaded
and a hash reference to its properties will be returned.

=cut

sub props {
  my ($this, $props) = @_;

  if (defined $props) {
    $this->{_props} = $props;
  } else {
    $this->load();
  }

  return $this->{_props};
}

=begin TML

---++ ObjectMethod prop($key, $val) -> $val

setter/getter for properties of this object. If =$val= 
is provided the property =$key= will be set. Note that
this method does not update the database. Only the object's
internal property is being set. Use Foswiki::PluggableAuth::update()
to actually write those properties into the database. This getter/setter
may be used to access any arbitrary properties to the object. Only
those listed in =TABLE_PROPS= will be written to the database.

=cut

sub prop {
  my ($this, $key, $val) = @_;

  #$this->writeDebug("called prop($key, ".($val//'undef').")");

  if (defined $val) {
    $this->{_props}{$key} = $val;
  } else {
    $val = $this->{_props}{$key};
    $this->load unless defined $val;
  }

  $val = $this->{_props}{$key};

  #$this->writeDebug("... val=".($val//'undef'));

  return $val;
}

=begin TML

---++ ObjectMethod stringify() -> $string

returns a text representation of this object. Note that user and group
classes have a more specific version of this method.

=cut

sub stringify {
  return shift->prop("id");
}

=begin TML

---++ ObjectMethod delete() -> $boolean

deletes this object from the database and returns true on success

=cut

sub delete {
  my $this = shift;

  #$this->writeDebug("called delete");

  throw Error::Simple("cannot delete ".$this->prop("id")) unless $this->isDeleteable;

  my $id = $this->prop("id");

  if (!$this->isLoaded && !defined($id)) {
    $this->load();
    $id = $this->prop("id");

    throw Error::Simple("could not update unknown object") unless defined $id && $this->isLoaded;
  }

  $id = $this->prop("id");
  $this->writeDebug("... id=$id");

  my $class = ref($this);
  my $res = $this->db->handler->do("DELETE FROM PluggableAuth_".$class->TABLE_NAME." WHERE id=?", {}, $id);

  $this->{_isLoaded} = 0;

  $this->writeDebug("... res=$res");

  return $res;
}

=begin TML

---++ ObjectMethod eachMembership($expand) -> $it

TODO

=cut

sub eachMembership {
  my ($this, $expand) = @_;

  $this->writeDebug("called eachMembership");

  my $uid = $this->prop("id");
  my $stm;
  $expand //= 1;

  if ($expand) {
    $stm = <<"SQL";
WITH RECURSIVE
  memberShip(gid, mid) AS (
    SELECT gid, mid FROM PluggableAuth_group_members 
      INNER JOIN PluggableAuth_groups ON PluggableAuth_groups.id=gid AND PluggableAuth_groups.enabled=1
      WHERE mid=?
    UNION
    SELECT gm2.gid as gid, gm2.mid as mid FROM memberShip
      LEFT OUTER JOIN PluggableAuth_group_members gm2
      ON memberShip.gid = gm2.mid
      INNER JOIN PluggableAuth_groups ON PluggableAuth_groups.id=gm2.gid AND PluggableAuth_groups.enabled=1
  )
SELECT DISTINCT gid as id FROM memberShip 
  JOIN PluggableAuth_groups ON gid=id AND enabled=1
SQL

  } else {
  
    $stm = <<"SQL";
SELECT id FROM PluggableAuth_groups 
  INNER JOIN PluggableAuth_group_members
    ON gid=id 
    WHERE mid=? AND enabled=1
SQL
  }

  $this->writeDebug("stm=$stm");

  return Foswiki::Iterator::DBIterator->new(
    $this->db->handler, $stm, [$uid],
    sub {
      return $this->auth->getObjectByID(shift->{id});
    }
  );
}

sub isMemberOf {
  my ($this, $group, $expand) = @_;

  return $group->hasMember($this, $expand);
}

sub writeDebug {
  my ($this, $msg) = @_;

  return unless $this->{_debug} || $Foswiki::cfg{PluggableAuth}{Debug};

  my $class = ref($this);
  $class =~ s/^Foswiki:://;

  print STDERR "$class - $msg\n";
}

sub indexSolr {
  #my ($this, $indexer, $doc, $meta, $text) = @_;
}

1;

