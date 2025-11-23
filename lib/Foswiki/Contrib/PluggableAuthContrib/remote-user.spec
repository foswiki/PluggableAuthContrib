# ---+++ Remote User

# This provider authenticates the user by any means available to the web server. This then sets the REMOTE_USER variable which in turn
# is picked up by Foswiki. Note that the provided remote user must be registered to the site already.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{RemoteUser}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Name} = 'Remote User';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"  CHECK="iff:'{PluggableAuth}{Providers}{RemoteUser}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Module} = 'Foswiki::PluggableAuth::Provider::RemoteUser';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{Visible} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{NewUserTemplate} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{RemoteUser}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{RemoteUser}{LogoutURL} = '';
