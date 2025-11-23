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
