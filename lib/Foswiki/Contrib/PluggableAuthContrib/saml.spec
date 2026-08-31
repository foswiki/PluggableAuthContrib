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
