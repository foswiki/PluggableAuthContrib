# ---+++ Client Certificate

# This provider implements single sign on using client certificates. Note that you need to configure your web server to validate the 
# client certificate. It will then pass down the client's distinguishable name in an environment variable. This is the email address
# which the certificate has been created for. A user with that email address must be registered before in order to perform the automatic sign in.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{ClientCert}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Name} = 'Client Certificate';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}"  CHECK="iff:'{PluggableAuth}{Providers}{ClientCert}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Module} = 'Foswiki::PluggableAuth::Provider::ClientCert';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{Visible} = 0;

# **STRING 80 LABEL="Environment Variable" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" **
# specifies the environment variable that holds the raw client certificate of the client.
# Add this to your nginx config =fastcgi_param SSL_CLIENT_CERT $ssl_client_raw_cert;=.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{EnvVariable} = 'SSL_CLIENT_CERT';

# **BOOLEAN LABEL="Verify Certificates" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
# enable/disable verification of the client certificates.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{VerifyCertificates} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{DeniedIPAddresses} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{ClientCert}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{ClientCert}{LogoutURL} = '';
