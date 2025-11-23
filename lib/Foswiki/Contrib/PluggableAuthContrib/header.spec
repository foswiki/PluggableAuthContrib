# ---+ Pluggable Authentication

# ---++ General 
# **BOOLEAN LABEL="Debug"**
# Global debug flag. Each provider has got its own local flag as well.
$Foswiki::cfg{PluggableAuth}{Debug} = 0;

# **SELECT Topic,AuthZero LABEL="Registration Provider"**
# Choose the provider that should be used when a user needs to register locally. Note that the provider must
# be able to handle user registration.
$Foswiki::cfg{PluggableAuth}{RegistrationProvider} = 'Topic';

# **BOOLEAN LABEL="Allow Login Using Email Address"**
# Allow a user to log in to foswiki using the email addresses known to the
# password system (in addition to their username).
$Foswiki::cfg{PluggableAuth}{AllowLoginUsingEmailAddress} = 1;

# **BOOLEAN LABEL="Create UserTopics"**
$Foswiki::cfg{PluggableAuth}{CreateUserTopics} = 1;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics}" CHECK="undefok emptyok" **
# Global definition, each provider may optionally have a specific one.
$Foswiki::cfg{PluggableAuth}{NewUserTemplate} = '$Foswiki::cfg{SystemWebName}.PluggableAuthNewUserTemplate';

# **STRING 80 LABEL="New Group Template" CHECK="undefok emptyok" **
# Global definition, each provider may optionally have a specific one.
$Foswiki::cfg{PluggableAuth}{NewGroupTemplate} = '$Foswiki::cfg{SystemWebName}.PluggableAuthNewGroupTemplate';

# **BOOLEAN LABEL="Create Provider Groups"**
# Create user groups for each active provider. For each active user provider a name_group will be created which all users are added to who are integrated via this provider.
$Foswiki::cfg{PluggableAuth}{CreateProviderGroups} = 0;

# **BOOLEAN LABEL="Enable Gravatar Fallback"**
# Try to get a profile image from gravatar in case there is no other picture available. 
$Foswiki::cfg{PluggableAuth}{EnableGravatarFallback} = 0;

# **NUMBER**
# Network in seconds for the cache to expire, e.g. a default of 3600 seconds means fresh results are fetched every hour.
$Foswiki::cfg{PluggableAuth}{CacheExpire} = 3600;

# **STRING LABEL="Common Passwords File" CHECK="undefok emptyok"**
# a text file with commonly known passwords to be checked.
# the default is based on https://lucidar.me/en/security/list-of-100000-most-common-passwords/
$Foswiki::cfg{PluggableAuth}{CommonPasswordsFile} = '$Foswiki::cfg{ToolsDir}/common-passwords.txt';

# ---++ Rewrite Rules

# **STRING 100 LABEL="Exclude WikiNames"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeWikiNames} = 'WikiGuest, ProjectContributor, RegistrationAgent, UnknownUser, AdminGroup, NobodyGroup, AdminUser';

# **STRING 100 LABEL="Exclude LoginNames"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeLoginNames} = 'admin, guest';

# **STRING 100 LABEL="Exclude Group Names"**
# Prevent certain names from being used by providers
$Foswiki::cfg{PluggableAuth}{ExcludeGroupNames} = 'AdminGroup, NobodyGroup';

# **PERL LABEL="Rewrite WikiNames" CHECK="undefok emptyok"**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has 
# the form 
# <pre>{
#   'pattern1' => 'substitute1', 
#   'pattern2' => 'substitute2' 
# }</pre>
# consists of a name pattern that has to match the wiki name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{PluggableAuth}{RewriteWikiNames} = { 
  '^(.*)@.*$' => '$1' 
};

# **BOOLEAN LABEL="Normalize GroupNames"**
# Enable/disable normalization of group names as they are imported by a provider. 
# If enabled, Group names are wikified and appended by "Group"
$Foswiki::cfg{PluggableAuth}{NormalizeGroupNames} = 0;

# **PERL LABEL="Rewrite GroupNames" CHECK="undefok emptyok"**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has 
# the form 
# <pre>{
#   'pattern1' => 'substitute1', 
#   'pattern2' => 'substitute2' 
# }</pre>
# consists of a name pattern that has to match the group name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{PluggableAuth}{RewriteGroupNames} = {};

