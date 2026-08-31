# ---+++ Kerberos

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Kerberos}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Name} = 'Kerberos Single Sign On';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Kerberos}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Module} = 'Foswiki::PluggableAuth::Provider::Kerberos';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{Visible} = 0;

# **BOOLEAN LABEL="AutoLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{AutoLogin} = 1;

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{KeyTab} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
# Note that this setting has to match the one in LDAP or any other identity provider.
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Kerberos}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Kerberos}{LogoutURL} = '';
