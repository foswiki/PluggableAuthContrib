# ---+ Pluggable Authentication

# ---++ General 
# **BOOLEAN LABEL="Debug"**
# Global debug flag. Each provider has got its own local flag as well.
$Foswiki::cfg{PluggableAuth}{Debug} = 0;

# **SELECT Topic,AuthZero LABEL="Registration Provider"**
# Choose the provider that should be used when a user needs to register locally. Note that the provider must
# be able to handle user registration.
$Foswiki::cfg{PluggableAuth}{RegistrationProvider} = 'Topic';

# **BOOLEAN LABEL="Allow Login Using Email Address"**
# Allow a user to log in to foswiki using the email addresses known to the
# password system (in addition to their username).
$Foswiki::cfg{PluggableAuth}{AllowLoginUsingEmailAddress} = 1;

# **BOOLEAN LABEL="Create UserTopics"**
$Foswiki::cfg{PluggableAuth}{CreateUserTopics} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics}" CHECK="undefok emptyok" **
# Global definition, each provider may optionally have a specific one.
$Foswiki::cfg{PluggableAuth}{NewUserTemplate} = '$Foswiki::cfg{SystemWebName}.PluggableAuthNewUserTemplate';

# **STRING 80 LABEL="New Group Template" CHECK="undefok emptyok" **
# Global definition, each provider may optionally have a specific one.
$Foswiki::cfg{PluggableAuth}{NewGroupTemplate} = '$Foswiki::cfg{SystemWebName}.PluggableAuthNewGroupTemplate';

# **BOOLEAN LABEL="Create Provider Groups"**
# Create user groups for each active provider. For each active user provider a name_group will be created which all users are added to who are integrated via this provider.
$Foswiki::cfg{PluggableAuth}{CreateProviderGroups} = 0;

# **BOOLEAN LABEL="Enable Gravatar Fallback"**
# Try to get a profile image from gravatar in case there is no other picture available. 
$Foswiki::cfg{PluggableAuth}{EnableGravatarFallback} = 0;

# **NUMBER**
# Network in seconds for the cache to expire, e.g. a default of 3600 seconds means fresh results are fetched every hour.
$Foswiki::cfg{PluggableAuth}{CacheExpire} = 3600;

# **STRING LABEL="Common Passwords File" CHECK="undefok emptyok"**
# a text file with commonly known passwords to be checked.
# the default is based on https://lucidar.me/en/security/list-of-100000-most-common-passwords/
$Foswiki::cfg{PluggableAuth}{CommonPasswordsFile} = '$Foswiki::cfg{ToolsDir}/common-passwords.txt';

# ---++ Rewrite Rules

# **STRING 100 LABEL="Exclude WikiNames"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeWikiNames} = 'WikiGuest, ProjectContributor, RegistrationAgent, UnknownUser, AdminGroup, NobodyGroup, AdminUser';

# **STRING 100 LABEL="Exclude LoginNames"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeLoginNames} = 'admin, guest';

# **STRING 100 LABEL="Exclude Group Names"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeGroupNames} = 'AdminGroup, NobodyGroup';

# **PERL LABEL="Rewrite WikiNames" CHECK="undefok emptyok"**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has 
# the form 
# <pre>{
#   'pattern1' => 'substitute1', 
#   'pattern2' => 'substitute2' 
# }</pre>
# consists of a name pattern that has to match the wiki name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{PluggableAuth}{RewriteWikiNames} = { 
  '^(.*)@.*$' => '$1' 
};

# **BOOLEAN LABEL="Normalize GroupNames"**
# Enable/disable normalization of group names as they are imported by a provider. 
# If enabled, Group names are wikified and appended by "Group"
$Foswiki::cfg{PluggableAuth}{NormalizeGroupNames} = 0;

# **PERL LABEL="Rewrite GroupNames" CHECK="undefok emptyok"**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has 
# the form 
# <pre>{
#   'pattern1' => 'substitute1', 
#   'pattern2' => 'substitute2' 
# }</pre>
# consists of a name pattern that has to match the group name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{PluggableAuth}{RewriteGroupNames} = {};

# ---++ Two Factor Authentication
# General settings for the TwoFactorAuth module. Note that you have to configure
# the two factor auth per provider as required.

# **BOOLEAN LABEL="Debug"**
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Debug} = 0;

# **SELECT optional,mandatory,mandatory-for-admins LABEL="Policy" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Policy} = 'optional';

# **STRING LABEL="Policy Exceptions" CHECK="undefok emptyok"**
# List of WikiUsers that are excempted from the two-factor policy.
# Please make sure that this list of exceptions is short and reasonable.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{PolicyExceptions} = '';

# **NUMBER LABEL="Maximum Attempts" CHECK="undefok emptyok"**
# Number of login attempts allowed in a certain period of time.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{MaxAttempts} = 4;

# **NUMBER LABEL="Attempts Period" CHECK="undefok emptyok"**
# Period of time within which a certain amount of login attempts are allowed.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{AttemptsPeriod} = 30;

# **BOOLEAN LABEL="Notify Security Alert"**
# Notify user when second factor failed about the password possibly being compromised
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{NotifySecurityAlert} = 0;

# **STRING LABEL="Logo URL" CHECK="undefok emptyok"**
# Logo to be displayed in the 2FA token app on your mobile device. 
# Note that the url of this logo has to be accessible to the outside world, i.e. your mobile device
# when the token is initiated.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{LogoUrl} = 'https://foswiki.org/pub/System/ProjectLogos/foswiki-logo-large.png';

# **STRING LABEL="Issuer" CHECK="undefok emptyok"**
# Name of the site associated with the one-time password on your mobile device.
# This defaults to the WIKITOOLNAME if left empty.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Issuer} = '';

# ---++ Block Temporary Email
# Free API to block temporary and disposable email address
# available at <a href="https://block-temporary-email.com/" target="_blank">https://block-temporary-email.com/</a>.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled} = 0;

# **STRING CHECK="undefok emptyok" LABEL="API-Key" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{APIKey} = "";

# **STRING CHECK="undefok emptyok" EXPERT LABEL="Email Endpoint" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{EmailEndpoint} = "https://block-temporary-email.com/check/email";

# **STRING CHECK="undefok emptyok" EXPERT LABEL="Domain Endpoint" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{DomainEndpoint} = "https://block-temporary-email.com/check/domain";
# ---++ Certificate Authority
# For some parameters a CA configuration is required, such as connecting to an upstream LDAP directory using TLS over SASL
# or verifying client certificates.

# **STRING 80 LABEL="CA File" CHECK="undefok emptyok" **
# Filename containing the certificate of the CA which signed the server’s certificate.
$Foswiki::cfg{PluggableAuth}{CAFile} = '';

# **STRING 80 LABEL="CA Path" CHECK="undefok emptyok" **
# Pathname of the directory containing CA certificates. 
$Foswiki::cfg{PluggableAuth}{CAPath} = '/etc/ssl/certs';
# ---++ Provider

# ---+++ Topic

# The Topic provider implements the default identity provider native to Foswiki. This provider
# may be disabled in case of all users being managed by an external service, such as LDAP, OpenID etc.

# **BOOLEAN LABEL="Enabled" EXPERT**
# this provider is always required: please do not disable unless you know what you do.
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Enabled} = 1;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Topic}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Name} = 'Topic';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Topic}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Module} = 'Foswiki::PluggableAuth::Provider::Topic';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Visible} = 0;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{SyncOnLogin} = 1;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
# Formfield Name
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{DisplayNameAttribute} = 'TopicTitle';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{FirstNameAttribute} = 'FirstName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{MiddleNameAttribute} = 'MiddleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{LastNameAttribute} = 'LastName';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{InitialsAttribute} = 'Initials';

# **SELECT topic,htpasswd,passwordmanager LABEL="Email Source" CHECK="undefok emptyok" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{EmailSource} = 'htpasswd';

# **STRING 80 LABEL="Email Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled} && {PluggableAuth}{Providers}{Topic}{EmailSource} == 'topic'" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{EmailAttribute} = 'Email';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{LogoutURL} = '';
# ---+++ Remote User

# This provider authenticates the user by any means available to the web server. This then sets the REMOTE_USER variable which in turn
# is picked up by Foswiki. Note that the provided remote user must be registered to the site already.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{RemoteUser}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Name} = 'Remote User';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"  CHECK="iff:'{PluggableAuth}{Providers}{RemoteUser}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Module} = 'Foswiki::PluggableAuth::Provider::RemoteUser';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Visible} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{NewUserTemplate} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{LogoutURL} = '';
# ---+++ Basic Auth

# This provider authenticates the user using the HTTP Basic authentication scheme. 

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{BasicAuth}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Name} = 'Basic Authentication';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{BasicAuth}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Module} = 'Foswiki::PluggableAuth::Provider::BasicAuth';

# **STRING 80 LABEL="Authentication Realm" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Realm} = '';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Visible} = 0;

# **BOOLEAN LABEL="AutoLogin" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{AutoLogin} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{LogoutURL} = '';
# ---+++ Client Certificate

# This provider implements single sign on using client certificates. Note that you need to configure your web server to validate the 
# client certificate. It will then pass down the client's distinguishable name in an environment variable. This is the email address
# which the certificate has been created for. A user with that email address must be registered before in order to perform the automatic sign in.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{ClientCert}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Name} = 'Client Certificate';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}"  CHECK="iff:'{PluggableAuth}{Providers}{ClientCert}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Module} = 'Foswiki::PluggableAuth::Provider::ClientCert';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Visible} = 0;

# **STRING 80 LABEL="Environment Variable" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" **
# specifies the environment variable that holds the raw client certificate of the client.
# Add this to your nginx config =fastcgi_param SSL_CLIENT_CERT $ssl_client_raw_cert;=.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{EnvVariable} = 'SSL_CLIENT_CERT';

# **BOOLEAN LABEL="Verify Certificates" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
# enable/disable verification of the client certificates.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{VerifyCertificates} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{LogoutURL} = '';
# ---+++ Kerberos

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Kerberos}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Name} = 'Kerberos Single Sign On';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Kerberos}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Module} = 'Foswiki::PluggableAuth::Provider::Kerberos';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Visible} = 0;

# **BOOLEAN LABEL="AutoLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{AutoLogin} = 1;

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{KeyTab} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
# Note that this setting has to match the one in LDAP or any other identity provider.
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{LogoutURL} = '';
# ---+++ LDAP 1

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Name} = 'LDAP Provider (1)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LogoutURL} = '';
# ---+++ LDAP 2

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Name} = 'LDAP Provider (2)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LogoutURL} = '';
# ---+++ LDAP 3

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Name} = 'LDAP Provider (3)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LogoutURL} = '';
# ---+++ LDAP 4

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Name} = 'LDAP Provider (4)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LogoutURL} = '';
# ---+++ LDAP 5

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Name} = 'LDAP Provider (5)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LogoutURL} = '';
# ---+++ LDAP 6

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Name} = 'LDAP Provider (6)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LogoutURL} = '';
# ---+++ LDAP 7

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Name} = 'LDAP Provider (7)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LogoutURL} = '';
# ---+++ LDAP 8

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Name} = 'LDAP Provider (8)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LogoutURL} = '';
# ---+++ LDAP 9

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Name} = 'LDAP Provider (9)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LogoutURL} = '';
# ---+++ LDAP 10

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Name} = 'LDAP Provider (10)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LogoutURL} = '';
# ---+++ LDAP 11

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Name} = 'LDAP Provider (11)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LogoutURL} = '';
# ---+++ LDAP 12

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Name} = 'LDAP Provider (12)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LogoutURL} = '';
# ---+++ LDAP 13

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Name} = 'LDAP Provider (13)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LogoutURL} = '';
# ---+++ LDAP 14

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Name} = 'LDAP Provider (14)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LogoutURL} = '';
# ---+++ LDAP 15

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Name} = 'LDAP Provider (15)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LogoutURL} = '';
# ---+++ Amazon

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="noemptyok iff:'{PluggableAuth}{Providers}{Amazon}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{Name} = 'Amazon';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Amazon}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{Module} = 'Foswiki::PluggableAuth::Provider::Amazon';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{LoginNameAttribute} = 'user_id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{FirstNameAttribute} = '';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{LastNameAttribute} = '';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{PictureAttribute} = '';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Amazon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Amazon}{LogoutURL} = '';
# ---+++ Auth Zero

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{AuthZero}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Name} = 'Auth0';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{AuthZero}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Module} = 'Foswiki::PluggableAuth::Provider::AuthZero';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{Tenant} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{FirstNameAttribute} = 'firstName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{LastNameAttribute} = 'lastName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{AuthZero}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{AuthZero}{LogoutURL} = '';
# ---+++ Discord

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Name} = 'Discord';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Module} = 'Foswiki::PluggableAuth::Provider::Discord';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DisplayNameAttributes} = 'username';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{WikiNameAttributes} = 'username';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{PictureAttribute} = 'avatar';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{LogoutURL} = '';
# ---+++ Dropbox

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Dropbox}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Name} = 'Dropbox';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Dropbox}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Module} = 'Foswiki::PluggableAuth::Provider::Dropbox';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DisplayNameAttributes} = 'name.display_name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{WikiNameAttributes} = 'name.display_name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LoginNameAttribute} = 'account_id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{FirstNameAttribute} = 'name.given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LastNameAttribute} = 'name.surname';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{PictureAttribute} = 'profile_photo_url';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{InitialsAttribute} = 'name.abbreviated_name';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LogoutURL} = '';
# ---+++ Egroupware

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Name} = 'Egroupware';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Module} = 'Foswiki::PluggableAuth::Provider::Egroupware';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{Tenant} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Egroupware}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{PictureAttribute} = '';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Egroupware}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Egroupware}{LogoutURL} = '';
# ---+++ Facebook

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Facebook}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Name} = 'Facebook';

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Facebook}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Module} = 'Foswiki::PluggableAuth::Provider::Facebook';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{NewUserTemplate} = '';

# **STRING 80 LABEL="API ID" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{ClientID} = '';

# **STRING 80 LABEL="API Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LogoutURL} = '';
# ---+++ Github

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Github}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Name} = 'Github';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Github}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Module} = 'Foswiki::PluggableAuth::Provider::Github';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{PictureAttribute} = 'avatar_url';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Ennabled" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{LogoutURL} = '';
# ---+++ GitLab

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{GitLab}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Name} = 'GitLab';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{GitLab}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Module} = 'Foswiki::PluggableAuth::Provider::GitLab';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Tenant} = 'gitlab.com';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LogoutURL} = '';
# ---+++ Google

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Google}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Name} = 'Google';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Google}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Module} = 'Foswiki::PluggableAuth::Provider::Google';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{Tenant} = 'accounts.google.com';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Google}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Google}{LogoutURL} = '';
# ---+++ Keycloak

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Name} = 'Keycloak';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Module} = 'Foswiki::PluggableAuth::Provider::Keycloak';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{Tenant} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Keycloak}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{PictureAttribute} = '';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Keycloak}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Keycloak}{LogoutURL} = '';
# ---+++ LinkedIn

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{LinkedIn}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{Name} = 'LinkedIn';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{LinkedIn}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{Module} = 'Foswiki::PluggableAuth::Provider::LinkedIn';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{LinkedIn}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{LinkedIn}{LogoutURL} = '';
# ---+++ Mastodon

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Mastodon}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Name} = 'Mastodon';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Mastodon}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Module} = 'Foswiki::PluggableAuth::Provider::Mastodon';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{NewUserTemplate} = '';

# **STRING 80 LABEL="Server" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Server} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DisplayNameAttributes} = 'display_name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{WikiNameAttributes} = 'display_name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{MailAttributes} = 'acct';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{FirstNameAttribute} = '';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LastNameAttribute} = '';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{PictureAttribute} = 'avatar_static';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LogoutURL} = '';
# ---+++ Microsoft

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Microsoft}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Name} = 'Microsoft';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Microsoft}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Module} = 'Foswiki::PluggableAuth::Provider::Microsoft';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{Tenant} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{ClientSecret} = '';

# **BOOLEAN LABEL="Discovery Hack" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" **
# enable this if the user id token fails to validate. sometimes azure requires an extra appid parameter to the jwks_uri endpoint. 
# otherwise it does not return the correct set of public keys that the id token is encrypted with.
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{DiscoveryHack} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{LoginNameAttribute} = 'oid';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{PictureAttribute} = '';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Microsoft}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Microsoft}{LogoutURL} = '';
# ---+++ NextCloud

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Name} = 'NextCloud';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Module} = 'Foswiki::PluggableAuth::Provider::NextCloud';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{NewUserTemplate} = '';

# **STRING 80 LABEL="Domain Url" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DomainUrl} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DisplayNameAttributes} = 'display-name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{WikiNameAttributes} = 'display-name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{PictureAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{LogoutURL} = '';
# ---+++ SAML

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{SAML}{Enabled}' noemptyok"  **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Name} = 'SAML';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{SAML}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Module} = 'Foswiki::PluggableAuth::Provider::Saml';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{NewUserTemplate} = '';

# **STRING 80 LABEL="Metadata" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# Identifier of the Service Provide (SP) entity (must be a URI).
# Foswiki is the Service Provider as it provides the Service
# Local Copy of Metadata from Identity Provider
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Metadata} = 'https://localhost/metadata.xml';

# **STRING 80 LABEL="ACS URL" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# ACS URL Location where the from the IdP will be returned.
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{Issuer} = 'https://foswiki.local';

# **STRING 80 LABEL="Provider Name" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# Service Provider (Application) name
# Bug in Net::SAML2 prevents this from being sent
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{ProviderName} = 'Foswiki';

# **STRING 80 LABEL="Service Provider Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# Specify the certificate instead of using certs directory.
# Service Provider Signing Certificate
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{ServiceProviderCertificate} = '/var/www/foswiki/saml/sign.pem';

# **STRING 80 LABEL="Service Provider Key" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# Specify the private key instead of using the certs directory.
# Service Provider Signing Key
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{ServiceProviderKey} = '/var/www/foswiki/saml/sign.key';

# **STRING 80 LABEL="CACert" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}"**
# The CA Cert for the Identity Providers Certificate. 
# Instead of use the whole x509cert you can use a fingerprint in order to validate a SAMLResponse.
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{CACert} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{FirstNameAttribute} = 'FirstName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{MiddleNameAttribute} = 'MiddleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{LastNameAttribute} = 'LastName';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{InitialsAttribute} = 'Initials';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{DisplayNameAttributes} = 'FirstName, LastName';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{WikiNameAttributes} = 'FirstName, LastName';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{MailAttribute} = 'Email';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{PictureAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{SAML}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{SAML}{LogoutURL} = '';
# ---+++ Slack

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Name} = 'Slack';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Module} = 'Foswiki::PluggableAuth::Provider::Slack';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DisplayNameAttributes} = 'user.name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{WikiNameAttributes} = 'user.name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{MailAttributes} = 'user.email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{LoginNameAttribute} = 'user.id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{PictureAttribute} = 'user.image_192';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{LogoutURL} = '';
# ---+++ Twitch

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitch}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{Name} = 'Twitch';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitch}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{Module} = 'Foswiki::PluggableAuth::Provider::Twitch';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{DisplayNameAttributes} = 'preferred_username';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{WikiNameAttributes} = 'preferred_username';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Twitch}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitch}{LogoutURL} = '';
# ---+++ Yahoo

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Yahoo}{Enabled}' noemptyok"  **
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Name} = 'Yahoo';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Yahoo}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Module} = 'Foswiki::PluggableAuth::Provider::Yahoo';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{Tenant} = 'api.login.yahoo.com';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Yahoo}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Yahoo}{LogoutURL} = '';
1;
