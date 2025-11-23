# ---+++ Github

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Github}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Name} = 'Github';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Github}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Module} = 'Foswiki::PluggableAuth::Provider::Github';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{PictureAttribute} = 'avatar_url';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Ennabled" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Github}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Github}{LogoutURL} = '';
