# ---++ Certificate Authority
# For some parameters a CA configuration is required, such as connecting to an upstream LDAP directory using TLS over SASL
# or verifying client certificates.

# **STRING 80 LABEL="CA File" CHECK="undefok emptyok" **
# Filename containing the certificate of the CA which signed the server’s certificate.
$Foswiki::cfg{PluggableAuth}{CAFile} = '';

# **STRING 80 LABEL="CA Path" CHECK="undefok emptyok" **
# Pathname of the directory containing CA certificates. 
$Foswiki::cfg{PluggableAuth}{CAPath} = '/etc/ssl/certs';
