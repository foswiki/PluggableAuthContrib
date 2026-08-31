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
