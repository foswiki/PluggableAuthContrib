# ---+++ LDAP %i%

# **BOOLEAN LABEL="Enabled" CHECKER="PluggableAuth::Providers::Ldap::Enabled"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Enabled} = 0;

# **BOOLEAN LABEL="Debug" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Debug} = 0;

# **STRING 80 LABEL="Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}' noemptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Name} = 'LDAP Provider (%i%)';

# **STRING 80 LABEL="Domain Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{DomainName} = '';

# **STRING 80 LABEL="Module" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}' noemptyok" EXPERT**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Module} = 'Foswiki::PluggableAuth::Provider::Ldap';

# **BOOLEAN LABEL="Visible" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Visible} = 0;

# **STRING 80 LABEL="Allowed IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{AllowedIPAddresses} = '';

# **STRING 80 LABEL="Denied IP Addresses" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{DeniedIPAddresses} = '';

# **STRING 80 LABEL="Host" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# IP address (or hostname) of one or multiple LDAP servers. Multiple server URIs may be specified
# comma separated. Each will be tried in order until a connection is made. Please note that the
# system might slow down considerably if some of the servers are not reachable.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Host} = '';

# **NUMBER LABEL="Port" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Port used when binding to the LDAP server. Note that this setting is overridden by any port specification
# part of the Host URI(s).
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Port} = 389;

# **NUMBER LABEL="Timeout" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Connection timeout talking to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Timeout} = 5;

# **BOOLEAN LABEL="IPv6" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{IPv6} = 0;

# **NUMBER LABEL="Protocol Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{Version} = 3;

# **STRING 80 LABEL="Bind DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{BindDN} = '';

# **PASSWORD LABEL="Bind Password" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" **
# The password used when binding to the LDAP server
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{BindPassword} = '';

# **BOOLEAN LABEL="Use SASL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECKER="PluggableAuth::Providers::Ldap::UseSASL"**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{UseSASL} = 0;

# **STRING 80 LABEL="SASL Mechanism" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok" **
# List of SASL authentication mechanism to try
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{SASLMechanism} = 'GSSAPI PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING 80 LABEL="KeyTab" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{KeyTab} = '';

# **STRING 80 LABEL="Principal Name" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PrincipalName} = '';

# **BOOLEAN LABEL="Use TLS" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" **
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{UseTLS} = 0;

# **STRING 80 LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok" **
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{TLSVersion} = 'tlsv1';

# **SELECT required, optional, none LABEL="TLS Version" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok" **
# Specify how to verify the servers certificate.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{TLSVerify} = 'required';

# **STRING 80 LABEL="TLS Client Certificate" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok" **
# Client side certificate file.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{TLSClientCert} = '';

# **STRING 80 LABEL="TLS Client Key" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{UseSASL}" CHECK="undefok emptyok" **
# Client side private key file
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{TLSClientKey} = '';

# **NUMBER LABEL="PageSize" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PageSize} = 500;

# **STRING 80 LABEL="Base DN" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok" **
# Base DN to use in searches
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{BaseDN} = 'dc=nodomain';

# **BOOLEAN LABEL="Ignore Referrals" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" **
# Use this switch to prune LDAP referrals and references. Normally admins may use referrals and reference objects to guide search paths
# in a directory or among several servers to follow a certain URL. The normal behavior is to follow
# these referrals and continue search there recursively. However under certain conditions these referrals may
# result in a search to traverse a very large array of different paths that may or may not
# be online and when not result in undesirable timeouts. In general best practice would
# be to maintain the directory in a consistent state and remove stale referrals not to harm queries performance.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{IgnoreReferrals} = 0;

# **BOOLEAN LABEL="Import Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" **
# Enable use of LDAP users. If you switch this off the user-related settings
# have no effect. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{ImportUsers} = 1;

# **BOOLEAN LABEL="Prefetch Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}"**
# Import users and create their profile pages before they logged in the first time. If disabled user profile pages will be created as they log in the first time.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PrefetchUsers} = 1;

# **BOOLEAN LABEL="Synchronize on Login" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}"**
# update user data during the login operation
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{SyncOnLogin} = 1;

# **BOOLEAN LABEL="Keep Old Users" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" **
# Keep or delete old users. If enabled old users will be disabled instead of deleting them from the database.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{KeepOldUsers} = 0;

# **STRING 80 LABEL="New User Template" DISPLAY_IF="{PluggableAuth}{CreateUserTopics} && {PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{NewUserTemplate} = '';

# **PERL LABEL="UserBase" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# A list of trees where to search for users records. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{UserBase} = ['ou=people,dc=nodomain'];

# **STRING 120x30 LABEL="UserFilter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{UserFilter} = '(objectClass=posixAccount)';

# **SELECT sub,one LABEL="UserScope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{UserScope} = 'sub';

# **BOOLEAN LABEL="AllowChangePassword" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" **
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{AllowChangePassword} = 0;

# **STRING 80 LABEL="LoginName Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{LoginNameAttribute} = 'uid';

# **STRING 80 LABEL="Mail Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{MailAttribute} = 'mail';

# **STRING 80 LABEL="WikiName Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok" **
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{WikiNameAttributes} = 'cn';

# **STRING 80 LABEL="FirstName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{FirstNameAttribute} = 'givenName';

# **STRING 80 LABEL="MiddleName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{MiddleNameAttribute} = 'middleName';

# **STRING 80 LABEL="LastName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{LastNameAttribute} = 'sn';

# **STRING 80 LABEL="DisplayName Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="iff:'{PluggableAuth}{Providers}{Ldap%i%}{Enabled}'"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{DisplayNameAttribute} = 'displayName';

# **STRING 80 LABEL="Picture Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PictureAttribute} = 'thumbnailPhoto';

# **STRING 80 LABEL="Initials Attribute"  DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{InitialsAttribute} = 'initials';

# **BOOLEAN LABEL="CaseSensitiveLogin" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" **
# Enable/disable case sensitive login names. If disabled case doesn't matter logging in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{CaseSensitiveLogin} = 0;

# **BOOLEAN LABEL="Import Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" **
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{ImportGroups} = 1;

# **PERL LABEL="Group Base" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# A list of trees where to search for group records.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{GroupBase} = ['ou=group,dc=nodomain'];

# **STRING 120x30 LABEL="Group Filter" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{GroupFilter} = 'objectClass=posixGroup';

# **SELECT sub,one LABEL="Group Scope" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{GroupScope} = 'sub';

# **STRING 80 LABEL="Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{GroupAttribute} = 'cn';

# **STRING 80 LABEL="Primary Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING 80 LABEL="Inner Group Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{InnerGroupAttribute} = 'memberUid';

# **STRING 80 LABEL="Member Attribute" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" CHECK="undefok emptyok" **
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{MemberAttribute} = 'memberUid';

# **BOOLEAN LABEL="Member Indirection" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" **
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{MemberIndirection} = 0;

# **BOOLEAN LABEL="Ignore Private Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportGroups}" **
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{IgnorePrivateGroups} = 1;

# **PERL LABEL="Virtual Groups" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
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
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{VirtualGroups} = [];

# **PERL LABEL="Virtual Members" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
# Create groups based on a member query. Each configuration in the list below creates one named group gathering all members found by the query.
# <pre>
# [ ... { group => "...", nameAttr => "ou", filter => "objectClass=person", base => "ou=People,ou=dc=mycompany,dc=local" }, scope => "sub"... ]
# </pre>
# Note that multiple configurations of this kind may be specified.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{VirtualMembers} = [];

# **PERL LABEL="Person Attributes" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {Plugins}{SolrPlugin}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok"**
# This is a map of LDAP attributes to be added to the solr document when the current is a user profile page. These attributes are
# added to the profile page as if they where formfield values of the given name. Each entry in this map has got the format
# <pre>attributeName => 'fieldName'</pre>
# where <code>fieldName</code> is a valid formfield name and <code>attributeName</code> is an LDAP attribute name to be fetched from the LDAP directory.
# In those cases where an formfield of the same name as the LDAP attribute is found, the formfield value takes higher precedence.
# Note that you might map multiple LDAP attributes onto the same field name. This will help in those cases where user records might follow different
# conventions across all of your LDAP directory.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{PersonAttributes} = {
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

# **BOOLEAN LABEL="Two Factor Authentication Enabled" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled} && {PluggableAuth}{Providers}{Ldap%i%}{ImportUsers}" CHECK="undefok emptyok"**
# enable/disable two factor authentication.
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{TwoFactorAuthEnabled} = 0;

# **URL LABEL="Logout URL" DISPLAY_IF="{PluggableAuth}{Providers}{Ldap%i%}{Enabled}" CHECK="undefok emptyok"**
$Foswiki::cfg{PluggableAuth}{Providers}{Ldap%i%}{LogoutURL} = '';
