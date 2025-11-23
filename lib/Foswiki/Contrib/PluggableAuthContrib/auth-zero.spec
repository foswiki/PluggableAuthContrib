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
