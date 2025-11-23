# ---+++ Mastodon

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Mastodon}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Name} = 'Mastodon';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Mastodon}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Module} = 'Foswiki::PluggableAuth::Provider::Mastodon';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{NewUserTemplate} = '';

# **STRING 80 LABEL="Server" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{Server} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DisplayNameAttributes} = 'display_name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{WikiNameAttributes} = 'display_name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{MailAttributes} = 'acct';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{FirstNameAttribute} = '';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LastNameAttribute} = '';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{PictureAttribute} = 'avatar_static';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Mastodon}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Mastodon}{LogoutURL} = '';
