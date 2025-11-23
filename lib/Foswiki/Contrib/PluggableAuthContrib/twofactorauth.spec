# ---++ Two Factor Authentication
# General settings for the TwoFactorAuth module. Note that you have to configure
# the two factor auth per provider as required.

# **BOOLEAN LABEL="Debug"**
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Debug} = 0;

# **SELECT optional,mandatory,mandatory-for-admins LABEL="Policy" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Policy} = 'optional';

# **STRING LABEL="Policy Exceptions" CHECK="undefok emptyok"**
# List of WikiUsers that are excempted from the two-factor policy.
# Please make sure that this list of exceptions is short and reasonable.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{PolicyExceptions} = '';

# **NUMBER LABEL="Maximum Attempts" CHECK="undefok emptyok"**
# Number of login attempts allowed in a certain period of time.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{MaxAttempts} = 4;

# **NUMBER LABEL="Attempts Period" CHECK="undefok emptyok"**
# Period of time within which a certain amount of login attempts are allowed.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{AttemptsPeriod} = 30;

# **BOOLEAN LABEL="Notify Security Alert"**
# Notify user when second factor failed about the password possibly being compromised
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{NotifySecurityAlert} = 0;

# **STRING LABEL="Logo URL" CHECK="undefok emptyok"**
# Logo to be displayed in the 2FA token app on your mobile device. 
# Note that the url of this logo has to be accessible to the outside world, i.e. your mobile device
# when the token is initiated.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{LogoUrl} = 'https://foswiki.org/pub/System/ProjectLogos/foswiki-logo-large.png';

# **STRING LABEL="Issuer" CHECK="undefok emptyok"**
# Name of the site associated with the one-time password on your mobile device.
# This defaults to the WIKITOOLNAME if left empty.
$Foswiki::cfg{PluggableAuth}{TwoFactorAuth}{Issuer} = '';

