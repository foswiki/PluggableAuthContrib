# ---+++ Xing

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="noemptyok iff:'{PluggableAuth}{Providers}{Xing}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{Name} = 'Xing';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Xing}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{Module} = 'Foswiki::PluggableAuth::Provider::Xing';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{LoginNameAttribute} = 'user_id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{FirstNameAttribute} = '';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{LastNameAttribute} = '';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{PictureAttribute} = '';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Xing}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Xing}{LogoutURL} = '';
