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
