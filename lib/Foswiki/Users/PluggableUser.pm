# Extension for Foswiki - The Free and Open Source Wiki, https://foswiki.org/
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

package Foswiki::Users::PluggableUser;

=begin TML

---+ package Foswiki::Users::PluggableUser

This is a password manager covering all enabled providers.

=cut

use strict;
use warnings;

use Foswiki::Users::Password ();
use Foswiki::ListIterator ();
use Foswiki::Plugins ();
our @ISA = ('Foswiki::Users::Password');

use Error qw( :try );

=begin TML

---++ readOnly() -> $boolean

returns true if the current user's provider allows to change the password

=cut

sub readOnly {
  my $this = shift;

  return 1 unless defined $this->{session};
  
  # depends on the current user's provider
  my $user = $this->auth->getUserByID($this->{session}{user})->load();
  return 1 unless defined $user;
  return 1 unless $user->isUnknown;

  return $user->getProvider->canSetPassword ? 0 : 1;
}

=pod

---++ isManagingEmails() -> $boolean

returns true if the current user's provider mangages emails

=cut

sub isManagingEmails {
  my $this = shift;

  return 0 unless defined $this->{session};
  
  my $user = $this->auth->getUserByID($this->{session}{user})->load();
  return 0 unless defined $user;
  return 0 unless $user->isUnknown;

  return $user->getProvider->canSetPassword ? 0 : 1;
}

=begin TML

---++ ObjectMethod getEmails($login) -> @emails

Fetch the email address(es) for the given login. 

=cut

sub getEmails {
  my ($this, $login) = @_;

  my @emails = ();

  my $user = $this->auth->getUserByID($this->{session}{user})->load();
  push @emails, $user->prop("email") if defined $user && ! $user->isUnknown;

  return @emails;
}

sub auth {
  #my $this = shift;

  return Foswiki::PluggableAuth->new();
}

=begin TML

---++ ObjectMethod fetchPass($loginName) -> $hash

Implements Foswiki::Password

Returns encrypted password if succeeds.
Returns 0 if login is invalid.
Returns undef otherwise.

=cut

sub fetchPass {
  my ($this, $loginNane) = @_;

  my $ret = 0;
  my $enc = '';
  my $userInfo;

  if ($loginNane) {
    my $user = $this->auth->findUser(loginName => $loginName);
    if ($user) {
      $ret = $user->getPassword;

      $userInfo = {
        cuid => $user->prop("id"),
        password => $ret,
        emails => $user->prop("email"),
      };

    } else {
      $this->{error} = "Login $loginNane invalid";
      $ret = undef;
    }

  } else {
    $this->{error} = 'No user';
  }

  return wantarray ? ($ret, $userInfo) : $ret;
}

=begin TML

---++ ObjectMethod checkPassword( $loginName, $passwordU ) -> $boolean

Finds if the password is valid for the given user.

Returns 1 on success, undef on failure.

=cut

sub checkPassword {
  my ($this, $loginName, $passwordU) = @_;

  my $isOk = 0;
  $this->{error} = undef;
  
  my $user = $this->auth->findUser(loginName => $loginName);
  $isOk = $user->checkPassword($passwordU) if defined $user;

  $this->{error} = 'Invalid user/password' unless $isOk;

  return $isOk;
}

=begin TML

---++ ObjectMethod removeUser($loginName) -> $boolean

Delete the users entry.

=cut

sub removeUser {
  my ($this, $loginName) = @_;
  $this->{error} = undef;

  my $user = $this->auth->findUser(loginName => $loginName);
  return 0 unless defined $user;
  return 0 unless $user->isDeleteable;

  return $user->delete;
}

=begin TML

---++ ObjectMethod setPassword( $loginName, $newPassU, $oldPassU ) -> $boolean

If the $oldPassU matches matches the user's password, then it will
replace it with $newPassU.

If $oldPassU defined but incorrect, will return 0.

If $oldPassU undefined, will force the change irrespective of
the existing password, adding the user if necessary.

Otherwise returns 1 on success, undef on failure.

=cut

sub setPassword {
  my ($this, $loginName, $newUserPassword, $oldUserPassword) = @_;

  my $user = $this->auth->findUser(loginName => $loginName);
  return 0 unless defined $user;
  return $user->setPassword($newPassword, $oldPassword);
}

# probably unused, so we don't care to optimize this
sub canFetchUsers {
  return 1;
}

# probably unused, so we don't care to optimize this
sub fetchUsers {
  my $this = shift;

  my @list = map {$_->prop("loginName")} $this->auth->eachUser(enabled => 1)->all;

  return new Foswiki::ListIterator(\@list);
}

1;
