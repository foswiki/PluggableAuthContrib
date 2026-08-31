# ---+++ Basic Auth

# This provider authenticates the user using the HTTP Basic authentication scheme. 

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{BasicAuth}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Name} = 'Basic Authentication';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{BasicAuth}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Module} = 'Foswiki::PluggableAuth::Provider::BasicAuth';

# **STRING 80 LABEL="Authentication Realm" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Realm} = '';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{Visible} = 0;

# **BOOLEAN LABEL="AutoLogin" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{AutoLogin} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{BasicAuth}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{BasicAuth}{LogoutURL} = '';
