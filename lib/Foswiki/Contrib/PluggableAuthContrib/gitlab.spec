# ---+++ GitLab

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::OpenID"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{GitLab}{Enabled}' noemptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Name} = 'GitLab';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{GitLab}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Module} = 'Foswiki::PluggableAuth::Provider::GitLab';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Visible} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{SyncOnLogin} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{NewUserTemplate} = '';

# **STRING 80 LABEL="Tenant" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{Tenant} = 'gitlab.com';

# **STRING 80 LABEL="Client ID" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{ClientID} = '';

# **STRING 80 LABEL="Client Secret" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" **
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{ClientSecret} = '';

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="DisplayName Attributes"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DisplayNameAttributes} = 'name';

# **STRING 80 LABEL="DisplayName Separator"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DisplayNameSeparator} = ' ';

# **STRING 80 LABEL="WikiName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{WikiNameAttributes} = 'name';

# **STRING 80 LABEL="Mail Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MailAttributes} = 'email';

# **STRING 80 LABEL="Mail Verified Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MailVerifiedAttribute} = 'email_verified';

# **STRING 80 LABEL="LoginName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LoginNameAttribute} = 'sub';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{FirstNameAttribute} = 'given_name';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{MiddleNameAttribute} = '';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LastNameAttribute} = 'family_name';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{PictureAttribute} = 'picture';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{InitialsAttribute} = '';

# **STRING 80 LABEL="Group Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{GroupsAttribute} = '';

# **STRING 80 LABEL="Allowed Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{AllowedGroups} = '';

# **STRING 80 LABEL="Denied Groups"  DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{DeniedGroups} = '';

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{GitLab}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{GitLab}{LogoutURL} = '';
