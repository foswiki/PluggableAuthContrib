# ---+++ Twitter

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitter}{Enabled}' noemptyok"  **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{Name} = 'Twitter';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitter}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{Module} = 'Foswiki::PluggableAuth::Provider::Twitter';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitter}{Enabled}'"  **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Twitter}{Enabled}'"  **
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Twitter}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Twitter}{LogoutURL} = '';
