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
