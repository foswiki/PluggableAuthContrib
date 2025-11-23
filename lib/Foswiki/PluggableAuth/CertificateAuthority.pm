# Extension for Foswiki - The Free and Open Source Wiki, https://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2024-2025 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::PluggableAuth::CertificateAuthority;

=begin TML

---+ package Foswiki::PluggableAuth::CertificateAuthority

wrapper class for Crypt::OpenSSL::Verify

=cut

use strict;
use warnings;

=begin TML

---++ ClassMethod new(%params) -> $this

constructor

=cut

sub new {
  my $class = shift;

  my $this = bless({
    caFile => $Foswiki::cfg{PluggableAuth}{CAFile} || '',
    caPath => $Foswiki::cfg{PluggableAuth}{CAPath},
    #crlFile => $Foswiki::cfg{PluggableAuth}{CRLFile},
    @_
  }, $class);

  return $this;
}

=begin TML

---++ ObjectMethod DESTROY() 

finish this object

=cut

sub DESTROY {
  my $this = shift;

  $this->finish();
}

=begin TML

--++ ObjectMethod finish()

undef delegates

=cut

sub finish {
  my $this = shift;

  undef $this->{_ca};
}

=begin TML

---++ ObjectMethod init() -> $ca

tries to init the Crypt::OpenSSL::Verify delegate, returns undef if it fails

=cut

sub init {
  my $this = shift;

  if (defined $this->{_ca}) {
    return if $this->{_ca} eq '_undef_';
    return $this->{_ca};
  }

  eval 'require Crypt::OpenSSL::Verify';
  if ($@) {
    print STDERR "WARNING: Crypt::OpenSSL::Verify not installed\n";
    $this->{_ca} = '_undef_';
    return;
  } 

  my %args = ();

  #$args{"CRLfile"} = $this->{crlFile} if $this->{crlFile}; # SMELL: not supported by Crypt::OpenSSL::Verify ???
  $args{"CApath"} = $this->{caPath} if $this->{caPath} && !$this->{caFile};

  $this->{_ca} = Crypt::OpenSSL::Verify->new($this->{caFile}, \%args);

  return $this->{_ca};
}

=begin TML

---++ ObjectMethod verify($cert) -> $boolean

returns true if the certificate could be verified

=cut

sub verify {
  my ($this, $cert) = @_;

  return unless $cert;

  return if $cert->checkend(0);# SMELL: do we need this?

  my $ca = $this->init;
  return 0 unless $ca; # not able to validate

  my $isOk = 0;
  eval {
    $isOk = $ca->verify($cert);
  };

  return $isOk;
}

1;
