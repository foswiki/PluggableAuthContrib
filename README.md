PluggableAuth brings together all the different ways of identifying and authenticating users to Foswiki. 
Foswiki itself has a way of plugging in different schemes for mapping users and groups. However, it only allows one specific
implementation to be plugged in, not many. Nor does Foswiki have a central database to store these entities.
This is what PluggableAuth does: at its core it is a database fed from various sources that form the set of users, groups and membership between them, along with any kind of information associated with an identity.

Currenty the following identity and authenticatcion providers are supported:

* Amazon (oauth)
* AuthZero (openid)
* BasicAuth (native)
* ClientCert (tls/ssl)
* Discord (oauth)
* Dropbox (oauth)
* Egroupware (openid)
* Facebook (oauth)
* Github (oauth)
* Gitlab (openid)
* Google (openid)
* Keycloak (openid)
* Kerberos (ldap sso)
* LDAP (several of them)
* LinkedIn (openid)
* Mastodon (oauth)
* Microsoft/Azure (openid)
* NextCloud (oauth)
* RemoteUser (native)
* SAML 2.0
* Topic (native)
* Twitch (openid)
* Slack (oauth)
* Yahoo (openid)

Most of the above providers are based on either OAuth2 or OpenID, as indicated. These are mostly used for public sites to simplify the registration process for people who want to contribute to the wiki.

BasicAuth is the most classic way of authenticating on the web, using a .htpasswd type of user and password management. BasicAuth provider and Topic provider are natively known to Foswiki. PluggableAuth reads this information from the system and caches the information it finds in its central user database, like all the other providers.

The Topic provider is mostly of use to import already existing users to PluggableAuth while migrating from a previous configuration.

ClientCert is an interesting authentication provider for organisations is running their own Certification Authority roling out user certificates to people. These are an excellent choise for a passwordless single sign-on solution.

Kerberos is another industry standard authentication provider for single sign on, most commonly used in conjunction with an LDAP identity provider. PluggableAuth is configured to connect up to 15 different LDAP servers. This can of course be extended if you need to connect to more LDAP servers.

AuthZero is an interesting external service that in itself serves as an integration platform for even more identity providers. Basically, it allows you to completely outsource user management and thus provide identity and authentication services to all sorts of web services in your organisation.

There have been some issues with the Yahoo OpenID connector that have not yet been resolved. It seems to be a bug on their part as far as the problem has been analysed.
The Microsort provider allows Foswiki to be integrated into an Azure platform strategy. This is very similar to AuthZero, but more complicated.
