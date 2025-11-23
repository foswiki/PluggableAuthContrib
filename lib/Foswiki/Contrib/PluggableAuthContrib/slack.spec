# ---+++ Slack

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Name} = 'Slack';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Module} = 'Foswiki::PluggableAuth::Provider::Slack';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DisplayNameAttributes} = 'user.name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{WikiNameAttributes} = 'user.name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{MailAttributes} = 'user.email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{LoginNameAttribute} = 'user.id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Slack}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{PictureAttribute} = 'user.image_192';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Slack}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Slack}{LogoutURL} = '';
