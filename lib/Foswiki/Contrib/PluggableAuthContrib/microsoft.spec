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
