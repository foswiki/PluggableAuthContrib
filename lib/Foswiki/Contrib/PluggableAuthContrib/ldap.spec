# ---+++ LDAP 1

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Name} = 'LDAP Provider (1)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap1}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled} && {PluggableAuth}{Providers}{Ldap1}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap1}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap1}{LogoutURL} = '';
# ---+++ LDAP 2

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Name} = 'LDAP Provider (2)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap2}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled} && {PluggableAuth}{Providers}{Ldap2}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap2}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap2}{LogoutURL} = '';
# ---+++ LDAP 3

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Name} = 'LDAP Provider (3)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap3}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled} && {PluggableAuth}{Providers}{Ldap3}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap3}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap3}{LogoutURL} = '';
# ---+++ LDAP 4

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Name} = 'LDAP Provider (4)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap4}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled} && {PluggableAuth}{Providers}{Ldap4}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap4}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap4}{LogoutURL} = '';
# ---+++ LDAP 5

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Name} = 'LDAP Provider (5)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap5}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled} && {PluggableAuth}{Providers}{Ldap5}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap5}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap5}{LogoutURL} = '';
# ---+++ LDAP 6

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Name} = 'LDAP Provider (6)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap6}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled} && {PluggableAuth}{Providers}{Ldap6}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap6}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap6}{LogoutURL} = '';
# ---+++ LDAP 7

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Name} = 'LDAP Provider (7)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap7}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled} && {PluggableAuth}{Providers}{Ldap7}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap7}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap7}{LogoutURL} = '';
# ---+++ LDAP 8

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Name} = 'LDAP Provider (8)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap8}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled} && {PluggableAuth}{Providers}{Ldap8}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap8}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap8}{LogoutURL} = '';
# ---+++ LDAP 9

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Name} = 'LDAP Provider (9)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap9}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled} && {PluggableAuth}{Providers}{Ldap9}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap9}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap9}{LogoutURL} = '';
# ---+++ LDAP 10

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Name} = 'LDAP Provider (10)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap10}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled} && {PluggableAuth}{Providers}{Ldap10}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap10}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap10}{LogoutURL} = '';
# ---+++ LDAP 11

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Name} = 'LDAP Provider (11)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap11}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled} && {PluggableAuth}{Providers}{Ldap11}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap11}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap11}{LogoutURL} = '';
# ---+++ LDAP 12

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Name} = 'LDAP Provider (12)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap12}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled} && {PluggableAuth}{Providers}{Ldap12}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap12}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap12}{LogoutURL} = '';
# ---+++ LDAP 13

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Name} = 'LDAP Provider (13)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap13}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled} && {PluggableAuth}{Providers}{Ldap13}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap13}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap13}{LogoutURL} = '';
# ---+++ LDAP 14

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Name} = 'LDAP Provider (14)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap14}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled} && {PluggableAuth}{Providers}{Ldap14}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap14}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap14}{LogoutURL} = '';
# ---+++ LDAP 15

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Name} = 'LDAP Provider (15)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap15}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a group query. This is a list of queries for organizational units or similar records that may be used to group
# user objects with structural properties rather than logical properties as represented by real group objects. Each query
# identifies a base from where member user objects are gathered. The format of this list looks like:
# <pre>
# [ ... { nameAttr => "ou", filter => "objectClass=organizationalUnit", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# The <code>nameAttr</code> definies the attribute holding the group name, e.g. the name of the organizationalUnit;
# The <code>filter</code> is used to search for objects, starting at the given <code>base</code>. Once a virtual group was found
# a secondary search for user objects is performed and added to this group.
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{PersonAttributes} = {
  company => 'OrganisationName',
  department => 'Department',
  division => 'Division',
  title => 'Profession',
  c => 'Country',
  physicalDeliveryOfficeName => 'Address',
  postalAddress => 'Address',
  streetAddress => 'Address',
  facsimileTelephoneNumber => 'Telefax',
  l => 'Location',
  mobile => 'Mobile',
  telephoneNumber => 'Telephone',
  title => 'Title',
};

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled} && {PluggableAuth}{Providers}{Ldap15}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap15}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap15}{LogoutURL} = '';
