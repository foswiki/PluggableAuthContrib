# ---+++ Discord

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Name} = 'Discord';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Module} = 'Foswiki::PluggableAuth::Provider::Discord';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}'" **
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DisplayNameAttributes} = 'username';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{WikiNameAttributes} = 'username';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Discord}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{PictureAttribute} = 'avatar';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Discord}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Discord}{LogoutURL} = '';
