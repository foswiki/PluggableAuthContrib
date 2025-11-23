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

package Foswiki::PluggableAuth::Schema::SQLite;

=begin TML

---+ package Foswiki::PluggableAuth::Schema::SQLite

Database schema when using a <nop>MySQL. WARNING: please only use SQLite for 
testing. A production environment should use one of the other database configurations.

=cut

use strict;
use warnings;

use Foswiki::PluggableAuth::Schema;
our @ISA = ('Foswiki::PluggableAuth::Schema');

=begin TML

---++ ObjectMethod getDefinition() -> $schema.

returns the database definition. This is then processed by Foswiki::DBI

=cut

sub getDefinition {
  my $this = shift;

  my $adminLogin = $Foswiki::cfg{AdminUserLogin} || 'admin';
  my $adminWikiName = $Foswiki::cfg{AdminUserWikiName} || 'AdminUser';
  my $adminEmail = $Foswiki::cfg{WebMasterEmail} || '';
  my $guestLogin = $Foswiki::cfg{DefaultUserLogin} || 'guest';
  my $guestWikiName = $Foswiki::cfg{DefaultUserWikiName} || 'WikiGuest';
  my $adminGroup = $Foswiki::cfg{SuperAdminGroup} || "AdminGroup";

  my @schema = ([
    "CREATE TABLE IF NOT EXISTS %prefix%users (
            id TEXT NOT NULL PRIMARY KEY,
            pid TEXT NOT NULL,
            loginName TEXT NOT NULL,
            wikiName TEXT NOT NULL,
            displayName TEXT,
            email TEXT,
            firstName TEXT,
            middleName TEXT,
            lastName TEXT,
            initials TEXT,
            picture TEXT,
            registrationDate INTEGER,
            loginDate INTEGER,
            enabled INTEGER DEFAULT 1
    )",
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_users_loginName ON %prefix%users (loginName, pid)",
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_users_wikiName ON %prefix%users (wikiName)",

    "CREATE TABLE IF NOT EXISTS %prefix%passwords (
            uid TEXT NOT NULL REFERENCES %prefix%users(id),
            password CHAR(135),
            encoding TEXT,
            realm TEXT
    )",
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_passwords_uid ON %prefix%passwords (uid)",

    "CREATE TABLE IF NOT EXISTS %prefix%groups (
            id TEXT NOT NULL PRIMARY KEY,
            pid TEXT NOT NULL,
            wikiName TEXT NOT NULL,
            displayName TEXT,
            count INTEGER DEFAULT 0,
            enabled INTEGER DEFAULT 1
    )",
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_groups_name ON %prefix%groups (wikiName)",

    "CREATE TABLE IF NOT EXISTS %prefix%group_members (
            gid TEXT NOT NULL REFERENCES %prefix%groups(id),
            mid TEXT NOT NULL
    )",
    "CREATE INDEX IF NOT EXISTS %prefix%idx_group_members_gid ON %prefix%group_members (gid)",
    "CREATE INDEX IF NOT EXISTS %prefix%idx_group_members_mid ON %prefix%group_members (mid)",
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_group_members ON %prefix%group_members (gid, mid)",
    "CREATE TABLE IF NOT EXISTS %prefix%user_keys (
            id TEXT NOT NULL PRIMARY KEY,
            uid TEXT NOT NULL REFERENCES %prefix%users(id),
            enabled INTEGER DEFAULT 1,
            type TEXT,
            description TEXT,
            counter INTEGER DEFAULT 0,
            attemptTime INTEGER DEFAULT 0,
            keyHandle BLOB,
            publicKey BLOB,
            attestation TEXT
    )",
    "CREATE INDEX IF NOT EXISTS %prefix%idx_user_keys_uid ON %prefix%user_keys (uid)",
    "CREATE TABLE IF NOT EXISTS %prefix%providers (
            id TEXT NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            enabled INTEGER DEFAULT 0
    )",
    "CREATE INDEX IF NOT EXISTS %prefix%idx_providers_name ON %prefix%providers (name)",
  ], [
    "INSERT OR IGNORE INTO %prefix%users (pid, id, loginName, wikiName, displayName, firstName, lastName, initials, email) VALUES
      ('Base', 'BaseUserMapping_111', 'ProjectContributor', 'ProjectContributor', 'Project Contributor', 'Project', 'Contributor', 'PC', ''),
      ('Base', 'BaseUserMapping_222', 'RegistrationAgent', 'RegistrationAgent', 'Registration Agent', 'Registration', 'Agent', 'RA', ''),
      ('Base', 'BaseUserMapping_333', '$adminLogin', '$adminWikiName', 'Admin User', 'Admin', 'User', 'AU', '$adminEmail'),
      ('Base', 'BaseUserMapping_666', '$guestLogin', '$guestWikiName', 'Wiki Guest', 'Wiki', 'Guest', 'WG', ''),
      ('Base', 'BaseUserMapping_999', 'unknown', 'UnknownUser', 'Unknown User', 'Unknown', 'User', 'UU', '')"
  ], ["INSERT OR IGNORE INTO %prefix%groups (pid, id, wikiName, displayName) VALUES
      ('Base', 'BaseGroup', 'BaseGroup', 'Base Group'),
      ('Base', 'NobodyGroup', 'NobodyGroup', 'Nobody Group'),
      ('Base', '$adminGroup', '$adminGroup', 'Admin Group')"
  ], [
    "CREATE UNIQUE INDEX IF NOT EXISTS %prefix%idx_user_keys_type ON %prefix%user_keys (uid, type)",
  ]);

  return \@schema;
}

1;
