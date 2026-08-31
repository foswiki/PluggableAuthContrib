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
