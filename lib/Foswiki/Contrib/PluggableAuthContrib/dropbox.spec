# ---+++ Dropbox

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Dropbox}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Name} = 'Dropbox';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Dropbox}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Module} = 'Foswiki::PluggableAuth::Provider::Dropbox';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{NewUserTemplate} = '';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DisplayNameAttributes} = 'name.display_name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{WikiNameAttributes} = 'name.display_name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LoginNameAttribute} = 'account_id';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{FirstNameAttribute} = 'name.given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LastNameAttribute} = 'name.surname';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{PictureAttribute} = 'profile_photo_url';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{InitialsAttribute} = 'name.abbreviated_name';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Dropbox}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Dropbox}{LogoutURL} = '';
