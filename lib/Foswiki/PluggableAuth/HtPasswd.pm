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

package Foswiki::PluggableAuth::HtPasswd;

=begin TML

---+ package Foswiki::PluggableAuth::HtPasswd

TODO

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::ListIterator ();
use Error qw(:try);
use Fcntl qw( :DEFAULT :flock );

use constant TRACE => 0;

=begin TML

---++ ClassMethod new() -> $this

constructor

=cut

sub new {
  my $class = shift;

  my $this = bless ({
    _data => {},
  }, $class);

  if ($Foswiki::cfg{Htpasswd}{AutoDetect}) {

    # For autodetect, soft errors are allowed.  If the .htpasswd file contains
    # a password for an unsupported encoding, it will not match.
    eval 'use Digest::SHA'; 
    $this->{SHA} = 1 unless ($@);
    eval 'use Crypt::PasswdMD5'; 
    $this->{APR} = 1 unless ($@);
    eval 'use Crypt::Eksblowfish::Bcrypt;'; 
    $this->{BCRYPT} = 1 unless ($@);
    eval 'use Crypt::Argon2'; 
    $this->{ARGON2} = 1 unless ($@);
  }

  if ( $Foswiki::cfg{Htpasswd}{Encoding} eq 'md5'
    || $Foswiki::cfg{Htpasswd}{Encoding} eq 'htdigest-md5')
  {
    require Digest::MD5;
    if ($Foswiki::cfg{AuthRealm} =~ m/\:/) {
      print STDERR "ERROR: the AuthRealm cannot contain a ':' (colon) as it corrupts the password file\n";
      throw Error::Simple("ERROR: the AuthRealm cannot contain a ':' (colon) as it corrupts the password file");
    }
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'crypt') {
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'plain') {
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'sha1') {
    require Digest::SHA;
    $this->{SHA} = 1;
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'apache-md5') {
    require Crypt::PasswdMD5;
    $this->{APR} = 1;
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'crypt-md5') {
    eval 'use Crypt::PasswdMD5'; 
    $this->{APR} = 1 unless ($@);
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'bcrypt') {
    eval 'use Crypt::Eksblowfish::Bcrypt;'; 
    $this->{BCRYPT} = 1 unless ($@);
  } elsif ($Foswiki::cfg{Htpasswd}{Encoding} eq 'argon2') {
    eval 'use Crypt::Argon2;'; 
    $this->{ARGON2} = 1 unless ($@);
  } else {
    print STDERR "ERROR: unknown {Htpasswd}{Encoding} setting : " . $Foswiki::cfg{Htpasswd}{Encoding} . "\n";
    throw Error::Simple("ERROR: unknown {Htpasswd}{Encoding} setting : " . $Foswiki::cfg{Htpasswd}{Encoding} . "\n");
  }

  return $this;
}

sub finish {
  my $this = shift;

  undef $this->{SHA};
  undef $this->{APR};
  undef $this->{BCRYPT};
  undef $this->{ARGON2};
}

sub eachEntry {
  my $this = shift;

  # Read passwords with shared lock
  $this->read(1);
  my @entries = sort values %{$this->{_data}};

  return Foswiki::ListIterator->new(\@entries);
}

sub save {
  my $this = shift;

  my $lockHandle;
  my $error;

  try {
    $lockHandle = _lockPasswdFile(LOCK_EX);

    my $content = $this->dumpPasswords();

    my $fh;

    my $enc = $Foswiki::cfg{Htpasswd}{CharacterEncoding} || 'utf-8';
    open($fh, ">:encoding($enc)", $Foswiki::cfg{Htpasswd}{FileName})
      || throw Error::Simple("$Foswiki::cfg{Htpasswd}{FileName} open failed: $!");
    print $fh $content;
    close($fh);

  } catch Error with {
    $error = shift;
  } finally {
    _unlockPasswdFile($lockHandle);
  };

  throw $error if defined $error;
}

sub read {
  my ($this, $lockShared) = @_;

  _writeDebug("called read()");

  return $this->{_data} unless defined $this->{_data};

  _writeDebug("Htpasswd FileName=$Foswiki::cfg{Htpasswd}{FileName}");
  return {} unless -e $Foswiki::cfg{Htpasswd}{FileName};

  my $data = {};
  $lockShared |= 0;
  my $lockHandle;
  $lockHandle = _lockPasswdFile(LOCK_SH) if $lockShared;

  my $IN_FILE;
  local $/ = "\n";

  my $enc = $Foswiki::cfg{Htpasswd}{CharacterEncoding} || 'utf-8';
  open($IN_FILE, "<:encoding($enc)", $Foswiki::cfg{Htpasswd}{FileName})
    || throw Error::Simple($Foswiki::cfg{Htpasswd}{FileName} . ' open failed: ' . $!);

  my $line = '';
  my $tID;
  my $pwcount = 0;

  while (defined($line = <$IN_FILE>)) {
    next if $line =~ /^\s*$/;
    next if (substr($line, 0, 1) eq '#');
    chomp $line;
    $pwcount++;
    my @fields = split(/:/, $line, 5);

    if (TRACE) {
      print STDERR "\nSplit LINE $line\n";
      foreach my $f (@fields) { print STDERR "split: $f\n"; }
    }

    my $uid = shift @fields;
    $data->{$uid}{login} = $uid;

    if ($Foswiki::cfg{Htpasswd}{AutoDetect}) {
      my $tPass = shift @fields;

      # tPass is either a password or a realm
      if (
        $tPass eq $Foswiki::cfg{AuthRealm}
        || ( defined $fields[0]
          && length($fields[0]) == 32
          && defined $fields[1]
          && $fields[1] =~ m/@/)
        )
      {
        $data->{$uid}{enc} = 'htdigest-md5';
        $data->{$uid}{realm} = $tPass;
        $data->{$uid}{pass} = shift @fields;
        $data->{$uid}{emails} = shift @fields || '';
        _writeDebug("Auto ENCODING-1 $data->{$uid}{enc}");
        next;
      }

      if (length($tPass) == 33 && substr($tPass, 0, 5) eq '{SHA}') {
        $data->{$uid}{enc} = 'sha1';
      } elsif (length($tPass) == 34 && substr($tPass, 0, 2) eq '$1') {
        $data->{$uid}{enc} = 'crypt-md5';
      } elsif (length($tPass) == 37 && substr($tPass, 0, 6) eq '$apr1$') {
        $data->{$uid}{enc} = 'apache-md5';
      } elsif (length($tPass) == 60 && substr($tPass, 0, 4) eq '$2a$') {
        $data->{$uid}{enc} = 'bcrypt';
      } elsif (length($tPass) == 13
        && (!$fields[0] || $fields[0] =~ m/@/))
      {
        $data->{$uid}{enc} = 'crypt';
      } elsif (length($tPass) > 60
        && substr($tPass, 0, 9) eq '$argon2$')
      {

        $data->{$uid}{enc} = 'argon2';
      } elsif (
        length($tPass) >> 0
        && (!$fields[0]
          || $fields[0] =~ m/@/)
        )
      {
        $data->{$uid}{enc} = 'plain';
      } elsif (
        length($tPass) == 0
        && (!$fields[0]
          || $fields[0] =~ m/@/)
        )
      {
        # Password is zero length, no way to determine encoding.
        $data->{$uid}{enc} = 'unknown';
      }

      if ($data->{$uid}{enc}) {
        $data->{$uid}{pass} = $tPass;
        $data->{$uid}{emails} = shift @fields || '';
        _writeDebug("Auto ENCODING-2 $data->{$uid}{enc}");
        next;
      }

      _writeDebug("Fell through - must be htdigest-md5   " . length($tPass) . "--$tPass");

      # Fell through - only thing left is digest encoding
      $data->{$uid}{enc} = 'htdigest-md5';
      $data->{$uid}{realm} = $tPass;
      $data->{$uid}{pass} = shift @fields;
      $data->{$uid}{emails} = shift @fields || '';
      _writeDebug("Auto ENCODING-3 $data->{$uid}{enc}");
    }

    # Static configuration
    else {
      $data->{$uid}{enc} = $Foswiki::cfg{Htpasswd}{Encoding};
      $data->{$uid}{realm} = shift @fields
        if ($Foswiki::cfg{Htpasswd}{Encoding} eq 'md5'
        || $Foswiki::cfg{Htpasswd}{Encoding} eq 'htdigest-md5');
      $data->{$uid}{pass} = shift @fields;
      $data->{$uid}{emails} = shift @fields || '';

      _writeDebug("Static Encoding - $uid:  $data->{$uid}{enc} pass $data->{$uid}{pass} emails $data->{$uid}{emails}");
    }
  }
  close($IN_FILE);

  _writeDebug("Loaded $pwcount passwords");
  $this->{_data} = $data;

  _unlockPasswdFile($lockHandle) if $lockShared;

  return $data;
}

sub getPassword {
  my ($this, $uid) = @_;

  throw Error::Simple("No user") unless defined $uid;

  $this->read(1);

  return unless exists $this->{_data}{$uid};

  my $passwd = $this->{_data}{$uid}{pass};

  return wantarray ? ($passwd, $this->{_data}{$uid}) : $passwd;
}

sub setEmail {
  my ($this, $user, $email) = @_;

  return unless $user;
  my $uid = $user->prop("id");

  $this->read(1);
  $this->{_data}{$uid}{emails} = $email;
  $this->save();

  return 1;
}

sub deletePassword {
  my ($this, $uid) = @_;

  $this->read(1);
  delete $this->{_data}{$uid};
  $this->save();
}

sub savePassword {
  my ($this, %params) = @_;

  my $uid = $params{uid};
  my $password = $params{password};

  throw Error::Simple("invalid call to savePassword: login not defined") unless defined $uid;
  throw Error::Simple("invalid call to savePassword: password not defined") unless defined $password;

  my $encoding = $params{encoding} // $Foswiki::cfg{Htpasswd}{Encoding} // 'apache-md5';
  my $realm = $params{realm} // "";

  $this->read(1);

  $this->{_data}{$uid}{login} = $uid;
  $this->{_data}{$uid}{pass} = $password;
  $this->{_data}{$uid}{enc} = $encoding;
  $this->{_data}{$uid}{realm} = $realm;

  $this->save();
}

sub dumpPasswords {
  my $this = shift;

  my @entries;
  foreach my $uid (sort keys %{$this->{_data}}) {

    my $entry = "$uid:";
    if ( $this->{_data}{$uid}{pass}
      && $this->{_data}{$uid}{enc}
      && ($this->{_data}{$uid}{enc} eq 'md5' || $this->{_data}{$uid}{enc} eq 'htdigest-md5'))
    {
      # htdigest format
      $entry .= "$this->{_data}{$uid}{realm}:";
    }

    $this->{_data}{$uid}{pass} ||= '';
    $this->{_data}{$uid}{emails} ||= '';
    $entry .= $this->{_data}{$uid}{pass} . ':' . $this->{_data}{$uid}{emails};

    push @entries, $entry;
  }

  return join("\n", @entries) . "\n";
}

# static helpers
sub _lockPasswdFile {
  my $operator = @_;
  my $lockFileName = $Foswiki::cfg{Htpasswd}{LockFileName}
    || "$Foswiki::cfg{WorkingDir}/htpasswd.lock";

  sysopen(my $fh, $lockFileName, O_RDWR | O_CREAT, oct(666))
    || throw Error::Simple($lockFileName . ' open or create password lock file failed -' . 'check access rights: ' . $!);
  flock $fh, $operator;

  return $fh;
}

sub _unlockPasswdFile {
  my $fh = shift;
  close($fh);
}

sub _writeDebug {
  print STDERR "PluggableAuth::HtPasswd - $_[0]\n" if TRACE;
}


1;
