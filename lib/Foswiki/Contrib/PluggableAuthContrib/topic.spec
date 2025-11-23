# ---+++ Topic

# The Topic provider implements the default identity provider native to Foswiki. This provider
# may be disabled in case of all users being managed by an external service, such as LDAP, OpenID etc.

# **BOOLEAN LABEL="Enabled" EXPERT**
# this provider is always required: please do not disable unless you know what you do.
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Enabled} = 1;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Topic}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Name} = 'Topic';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Topic}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Module} = 'Foswiki::PluggableAuth::Provider::Topic';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{Visible} = 0;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{SyncOnLogin} = 1;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
# Formfield Name
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{DisplayNameAttribute} = 'TopicTitle';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{FirstNameAttribute} = 'FirstName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{MiddleNameAttribute} = 'MiddleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{LastNameAttribute} = 'LastName';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{InitialsAttribute} = 'Initials';

# **SELECT topic,htpasswd,passwordmanager LABEL="Email Source" CHECK="undefok emptyok" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{EmailSource} = 'htpasswd';

# **STRING 80 LABEL="Email Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled} && {PluggableAuth}{Providers}{Topic}{EmailSource} == 'topic'" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{EmailAttribute} = 'Email';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Topic}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Topic}{LogoutURL} = '';
