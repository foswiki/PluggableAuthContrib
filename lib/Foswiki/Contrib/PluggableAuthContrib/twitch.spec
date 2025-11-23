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
