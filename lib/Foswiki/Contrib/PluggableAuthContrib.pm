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

package Foswiki::Contrib::PluggableAuthContrib;

=begin TML

---+ package Foswiki::Contrib::PluggableAuthContrib

<nop>PluggableAuth consists of the following modules:

   * Foswiki::PluggableAuth - this is a singleton class from where all other services are orchestrated
   * Foswiki::PluggableAuth::BaseObject - base class for users and groups
      * Foswiki::PluggableAuth::User - interface to user objects in the database
      * Foswiki::PluggableAuth::Group - interface to group objects in the database
   * Foswiki::PluggableAuth::HtPasswd
   * Foswiki::PluggableAuth::ImageGenerator - generates a default image for a user profile based on a text string
   * Foswiki::PluggableAuth::Macros::LDAP - implements the %LDAP macro
   * Foswiki::PluggableAuth::Macros::OTPINFO - implements the %OTPINFO macro
   * Foswiki::PluggableAuth::Macros::PAUTHGROUPS - implements the %PAUTHGROUPS macro
   * Foswiki::PluggableAuth::Macros::PAUTHUSERS - implements the %PAUTHUSERS macro
   * Foswiki::PluggableAuth::Macros::PROVIDERINFO - implements the %PROVIDERINFO macro
   * Foswiki::PluggableAuth::Macros::USERINFO - extends the %USERINFO macro
   * Foswiki::PluggableAuth::Provider - base class for all providers
      * Foswiki::PluggableAuth::Provider::Base - base user mapping covering built-in users and groups such as guest, admin, etc
      * Foswiki::PluggableAuth::Provider::BasicAuth - basic authentication provider
      * Foswiki::PluggableAuth::Provider::ClientCert - authentication using client certificates
      * Foswiki::PluggableAuth::Provider::Kerberos - kerberos authentication provider
      * Foswiki::PluggableAuth::Provider::Ldap - ldap identity provider(s); there may be multiple active providers (15 by default) to integrate different domains
      * Foswiki::PluggableAuth::Provider::OAuth - base class for OAuth providers including <nop>OpenID
         * Foswiki::PluggableAuth::Provider::Amazon 
         * Foswiki::PluggableAuth::Provider::Discord
         * Foswiki::PluggableAuth::Provider::Dropbox
         * Foswiki::PluggableAuth::Provider::Facebook
         * Foswiki::PluggableAuth::Provider::Github
         * Foswiki::PluggableAuth::Provider::LinkedIn
         * Foswiki::PluggableAuth::Provider::NextCloud
         * Foswiki::PluggableAuth::Provider::Slack 
         * Foswiki::PluggableAuth::Provider::OpenID - base class for all <nop>OpenID providers
            * Foswiki::PluggableAuth::Provider::AuthZero
            * Foswiki::PluggableAuth::Provider::Egroupware
            * Foswiki::PluggableAuth::Provider::Google
            * Foswiki::PluggableAuth::Provider::Keycloak
            * Foswiki::PluggableAuth::Provider::Microsoft
            * Foswiki::PluggableAuth::Provider::Yahoo
      * Foswiki::PluggableAuth::Provider::RemoteUser - identity provider reading a remote user from an HTTP request header
      * Foswiki::PluggableAuth::Provider::Saml - SAML provider based on [[CPAN:Net::SAML2][Net::SAML2]]
      * Foswiki::PluggableAuth::Provider::Topic - native Foswiki provider that stores users and groups in topics
      * Foswiki::PluggableAuth::Provider::Twitter - provider based on [[CPAN:Net::Twitter][Net::Twitter]]
   * Foswiki::PluggableAuth::Schema - base class for all database schema classes
      * Foswiki::PluggableAuth::Schema::MariaDB
      * Foswiki::PluggableAuth::Schema::MySQL
      * Foswiki::PluggableAuth::Schema::SQLite
   * Foswiki::PluggableAuth::TwoFactorAuth - two factor authentication service
   * Foswiki::PluggableAuth::UserAgent - user agent userd for various network operations
   * Foswiki::PluggableAuth::UsersConnector - connector for JQDataTablesPlugin as used in [[System.PluggableAuthUsers]]

Below classes connect <nop>PluggableAuth to Foswiki:

   * Foswiki::LoginManager::PluggableLogin - implements the Foswiki::LoginManager interface for single as well as two factor authentication
   * Foswiki::Users::PluggableUserMapping - implements the Foswiki::UserMapping interface
   * Foswiki::Users::PluggableUser - implements password manager Foswiki::Users::Password interface

=cut

use strict;
use warnings;

our $VERSION = '0.989';
our $RELEASE = '%$RELEASE%';
our $SHORTDESCRIPTION = 'Pluggable authentication and user management';
our $LICENSECODE = '%$LICENSECODE%';
our $NO_PREFS_IN_TOPIC = 1;

1;
