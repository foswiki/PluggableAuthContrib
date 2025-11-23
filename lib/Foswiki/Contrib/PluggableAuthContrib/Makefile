SPECS=\
  header.spec \
  twofactorauth.spec \
  block-temporary-email.spec \
  ca.spec \
  provider.spec \
  topic.spec \
  remote-user.spec \
  basic-auth.spec \
  client-cert.spec \
  kerberos.spec \
  ldap.spec \
  amazon.spec \
  auth-zero.spec \
  discord.spec \
  dropbox.spec \
  egroupware.spec \
  facebook.spec \
  github.spec \
  gitlab.spec \
  google.spec \
  keycloak.spec \
  linkedin.spec \
  mastodon.spec \
  microsoft.spec \
  next-cloud.spec \
  saml.spec \
  slack.spec \
  twitch.spec \
  yahoo.spec \

#  xing.spec 
#  twitter.spec 

NUM_LDAPS=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# custom settings
-include Makefile.include

all: Config.spec

clean:
	@echo "cleaning up"
	@rm -f Config.spec ldap.spec

Config.spec: $(SPECS) Makefile 
	@echo "creating Config.spec for PluggableAuthContrib"
	@(cat $(SPECS); echo "1;") > $@

ldap.spec: ldap-template.spec Makefile
	@echo "creating ldap.spec for LDAPs $(NUM_LDAPS)"
	@(for i in $(NUM_LDAPS); do \
	  sed "s/\%i\%/$$i/g" ldap-template.spec; \
	done) > $@
