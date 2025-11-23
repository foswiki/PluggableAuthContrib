# ---+++ Facebook

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Facebook}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Name} = 'Facebook';

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Facebook}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Module} = 'Foswiki::PluggableAuth::Provider::Facebook';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{NewUserTemplate} = '';

# **STRING 80 LABEL="API ID" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{ClientID} = '';

# **STRING 80 LABEL="API Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{MailAttributes} = 'email';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LoginNameAttribute} = 'id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{InitialsAttribute} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Facebook}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Facebook}{LogoutURL} = '';
