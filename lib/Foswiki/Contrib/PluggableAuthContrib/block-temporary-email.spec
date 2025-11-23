# ---++ Block Temporary Email
# Free API to block temporary and disposable email address
# available at <a href="https://block-temporary-email.com/" target="_blank">https://block-temporary-email.com/</a>.

# **BOOLEAN LABEL="Enabled"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{Enabled} = 0;

# **STRING CHECK="undefok emptyok" LABEL="API-Key" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{APIKey} = "";

# **STRING CHECK="undefok emptyok" EXPERT LABEL="Email Endpoint" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{EmailEndpoint} = "https://block-temporary-email.com/check/email";

# **STRING CHECK="undefok emptyok" EXPERT LABEL="Domain Endpoint" DISPLAY_IF="{PluggableAuth}{BlockTemporaryEmail}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{BlockTemporaryEmail}{DomainEndpoint} = "https://block-temporary-email.com/check/domain";
