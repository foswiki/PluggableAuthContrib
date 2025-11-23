# ---+++ NextCloud

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Name} = 'NextCloud';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Module} = 'Foswiki::PluggableAuth::Provider::NextCloud';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{NewUserTemplate} = '';

# **STRING 80 LABEL="Domain Url" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DomainUrl} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DisplayNameAttributes} = 'display-name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{WikiNameAttributes} = 'display-name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{NextCloud}{Enabled}' undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{PictureAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{NextCloud}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{NextCloud}{LogoutURL} = '';
