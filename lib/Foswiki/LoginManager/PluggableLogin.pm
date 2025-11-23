# Extension for Foswiki - The Free and Open Source Wiki, https://foswiki.org/
#
# PluggableAuthContrib is Copyright (C) 2020-2025 Michael Daum http://michaeldaumconsulting.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details, published at
# http://www.gnu.org/copyleft/gpl.html

package Foswiki::LoginManager::PluggableLogin;

=begin TML

---+ package Foswiki::LoginManager::PluggableLogin

This is a login manager covering all enabled providers.

=cut

use strict;
use warnings;

use Foswiki::Func ();
use Foswiki::LoginManager ();
use Foswiki::Users::BaseUserMapping;
use MIME::Base64 ();
use Error qw(:try);
#use Data::Dump qw(dump);

use constant TRACE => 0; # toggle me

our @ISA = ('Foswiki::LoginManager');

=begin TML

---++ ClassMethod new($session)

Construct the <nop>PluggableLogin object

=cut

sub new {
  my ($class, $session) = @_;

  _writeDebug("called new()");

  my $this = bless($class->SUPER::new($session), $class);

  # add keys to secret keys so that it cannot be accseed by %SESSION_VARIABLE%
  $Foswiki::LoginManager::secretSK{_PAUTH_SECRET} = 1;
  $Foswiki::LoginManager::secretSK{_PAUTH_FACTOR} = 1;
  $Foswiki::LoginManager::secretSK{_PAUTH_LEVEL} = 1;
  
  # fix the context
  $session->enterContext('can_login');
  $session->enterContext('can_remember_login') if $Foswiki::cfg{Sessions}{ExpireCookiesAfter};

  # make sure we can store the authLevel
  $session->enterContext('sessionRequired') unless $Foswiki::cfg{Sessions}{EnableGuestSessions};

  # re-registering these, so we use our own methods.
  #Foswiki::registerTagHandler( 'LOGOUT',           \&_LOGOUT );
  #Foswiki::registerTagHandler( 'LOGOUTURL',        \&_LOGOUTURL );
  Foswiki::registerTagHandler('LOGINURL', sub {
    my ($session, $params) = @_;
    return $this->loginUrl($params);
  });

  return $this;
}

=begin TML

---++ ObjectMethod finish()

break circular references

=cut

sub finish {
  my $this = shift;

  $this->SUPER::finish();
  undef $this->{_user};
  undef $this->{_authLevel};
}

=begin TML

---++ ObjectMethod login($request)

main entrance point 

=cut

sub login {
  my ($this, $request) = @_;

  _writeDebug("called login()");

  $request->delete('validation_key');

  my $state = $this->restoreRequestState;
  my $error;
  my $isOk;

  #_writeDebug("state=".dump($state));

  try {
    $isOk = $this->processSecondFactor($request, $state) if $this->getAuthLevel() == 2;
    return if $isOk;

    $isOk = $this->processLogin($request, $state) if $this->getAuthLevel() == 0;
    return if $isOk;

    $isOk = $this->initLogin($request, $state) if $this->getAuthLevel() == 0;
    return if $isOk;

  } catch Error with {
    $error = shift;
    print STDERR "ERROR: $error";
    $error =~ s/ at .*$//;
  };
  return if $isOk;

  # second factor 
  return $this->renderSecondFactor($request, $state, $error) if $this->getAuthLevel() == 1;

  # first factor
  return $this->renderLogin($request, $state, $error);
}

=begin TML

---++ ObjectMethod renderSecondFactor($request, $state, $error)

Render the user interface to enter the second factor code.

=cut

sub renderSecondFactor {
  my ($this, $request, $state, $error) = @_;

  _writeDebug("called renderSecondFactor");

  my $user = $this->{_user};
  my $uid;
  $uid = $user->prop("id") if defined $user;
  $uid = $request->param('username') || '' unless defined $uid;

  $this->setAuthLevel(2); 

  _writeDebug("uid=$uid");

  my $tmpl = Foswiki::Func::readTemplate("twofactorlogin");

  # FIX: do we need this yet again? see renderLogin

  my $path_info = $request->path_info();
  if ($path_info =~ m/['"]/g) {
    $path_info = substr($path_info, 0, ((pos $path_info) - 1));
  }

  my $banner = $this->{session}->templates->expandTemplate('LOG_IN_BANNER');

  # FIX: move this error handling somewhere else
  $error //= $state->{error} // '';
  undef $state->{error};
  _writeDebug("error=$error") if $error;


  $this->{session}{prefs}->setSessionPreferences(
    FOSWIKI_ORIGIN => $state->{key} // "",
    PATH_INFO => Foswiki::urlEncode(Foswiki::decode_utf8($path_info)),
    BANNER => $banner,
    ERROR => $error,
    LOGINNAME => $uid,
  );

  $request->delete('validation_key', 'foswiki_origin', 'sudo', 'username', 'password', 'accesscode', 'state', 'scope', 'authuser', 'prompt');

  my $topic = $this->{session}{topicName};
  my $web = $this->{session}{webName};
  my $meta = Foswiki::Meta->new($this->{session}, $web, $topic);

  $tmpl = $meta->expandMacros($tmpl);
  $tmpl = $meta->renderTML($tmpl);
  $tmpl =~ s/<nop>//g;
  $tmpl =~ s/<\/?noautolink>//g;

  $this->{session}->writeCompletePage($tmpl);
}

=begin TML

---++ ObjectMethod renderLogin()

Renders the login page

=cut

sub renderLogin {
  my ($this, $request, $state, $error) = @_;

  _writeDebug("called renderLogin");

  my $tmpl = Foswiki::Func::readTemplate("pauthlogin");

  my $path_info = $request->path_info();
  if ($path_info =~ m/['"]/g) {
    $path_info = substr($path_info, 0, ((pos $path_info) - 1));
  }

  my $banner = $this->{session}->templates->expandTemplate('LOG_IN_BANNER');
  my $note = '';

  # FIX: move this error handling somewhere else
  $error //= $state->{error} // '';
  undef $state->{error};
  _writeDebug("error=$error") if $error;

  unless ($error) {
    my $loginName = $request->param('username');
    my $loginPass = $request->param('password');

    if (defined $loginName && defined $loginPass && $loginName ne '' && $loginPass ne '') {
      my $topic = $this->{session}{topicName};
      my $web = $this->{session}{webName};
      $this->{session}->logger->log({
          level => 'info',
          action => 'login',
          webTopic => $web . '.' . $topic,
          extra => "AUTHENTICATION FAILURE - $loginName - ",
        }
      );
      $banner = $this->{session}->templates->expandTemplate('UNRECOGNISED_USER');
    }
  }

  $this->{session}{prefs}->setSessionPreferences(
    FOSWIKI_ORIGIN => $state->{key} // "",
    PATH_INFO => Foswiki::urlEncode(Foswiki::decode_utf8($path_info)),
    BANNER => $banner,
    NOTE => $note,
    ERROR => $error,
  );

  $request->delete('validation_key', 'foswiki_origin', 'sudo', 'username', 'password', 'accesscode', 'state', 'scope', 'authuser', 'prompt');

  my $topic = $this->{session}{topicName};
  my $web = $this->{session}{webName};
  my $meta = Foswiki::Meta->new($this->{session}, $web, $topic);

  $tmpl = $meta->expandMacros($tmpl);
  $tmpl = $meta->renderTML($tmpl);
  $tmpl =~ s/<nop>//g;
  $tmpl =~ s/<\/?noautolink>//g;

  $this->{session}->writeCompletePage($tmpl);
}

=begin TML

---++ ObjectMethod auth()

returns a Foswiki::PluggableAuth object

=cut

sub auth {
  #my $this = shift;
  return Foswiki::PluggableAuth->new();
}

=begin TML

---++ ObjectMethod loginUrl()

returns the login url

=cut

sub loginUrl {
  my ($this, $params) = @_;

  my ($web, $topic) = Foswiki::Func::normalizeWebTopicName($params->{web} // $this->{session}{webName}, $params->{topic} // $this->{session}{topicName});

  my %opts = (
   foswiki_origin => $this->saveRequestState,
  );

  $opts{pauth_provider} = $params->{pid} if defined $params->{pid};
  my $abs = Foswiki::Func::isTrue($params->{absolute}, 0)?1:0;

  return $this->{session}->getScriptUrl($abs, 'login', $web, $topic, %opts);
}

=begin TML

---++ ObjectMethod forceAuthentication()

enfoce authentication

=cut

sub forceAuthentication {
  my $this = shift;

  _writeDebug("called forceAuthentication");

  my $session = $this->{session};

  return 0 if $session->inContext('authenticated');

  my $request = $session->{request};
  my $response = $session->{response};

  # SMELL: This breaks some applications such as MS Excel. Return
  # A 200 instead of a 401.
  #   Respond with a 401 with an appropriate WWW-Authenticate
  #   that won't be snatched by the browser, but can be used
  #   by JS to generate login info.
  $response->header(
    -status => 200,

    #-WWW_Authenticate => 'FoswikiBasic realm="'
    #  . ( $Foswiki::cfg{AuthRealm} || "" ) . '"'
  );

  $request->param(
    -name => 'foswiki_origin',
    -value => $this->saveRequestState($request),
  );

  # Throw back the login page with the 401
  $this->login($request, $session);

  return 1;
}

=begin TML

---++ ObjectMethod restoreRequestState($key)

the request state is encoded into a base64 hash key. If restore the =foswiki_origin= present in the url or default to
the session value =foswiki_origin=. It'll do nothing if no foswiki origin can be found.

See Foswiki::LoginManager::PluggableLogin::saveRequestState().

=cut

sub restoreRequestState {
  my ($this, $key) = @_;

  _writeDebug("called restoreRequestState(".($key//'').")");

  unless (defined $key) {
    my $request = $this->{session}{request};
    $key = $request->param("foswiki_origin") // $request->param("state") // $this->getSessionValue("foswiki_origin", 1);
  }
  return unless $key;
  return unless $key =~ /^[A-Za-z0-9+\/]+$/; # only decode things that look base64-ish

  my $state = {
    key => $key
  };

  $key = MIME::Base64::decode_base64url($key);

  my $salt;
  ($state->{method}, $state->{action}, $state->{uri}, $salt) = split(',', $key, 4);

  return $state;
}

=begin TML

---++ ObjectMethod saveRequestState($request)

This captures the current values of the request uri, its method and action into the session value =foswiki_origin=.
This value is base64 encoded to be retrieved later on.

=cut

sub saveRequestState {
  my ($this, $request) = @_;

  _writeDebug("called saveRequestState");

  $request //= $this->{session}{request};

  my $uri = $request->uri();
  my $method = $request->method() || 'UNDEFINED';
  my $action = $request->action();
  my $salt = int(rand(1000)).time(); # add salt in case of the same session being authenticated at the same time
  my $key = MIME::Base64::encode_base64url("$method,$action,$uri,$salt");

  _writeDebug("... uri=$uri");
  _writeDebug("... method=$method");
  _writeDebug("... action=$action");
  _writeDebug("... salt=$salt");
  _writeDebug("... key=$key");

  $this->setSessionValue('foswiki_origin', $key);

  return $key;
}

=begin TML

---++ ObjectMethod initLogin()

initialize the current login either by asking all enabled identity providers in turn or the provider specified
in the =pauth_provider= url parameter. 

=cut

sub initLogin {
  my ($this, $request, $state) = @_;

  _writeDebug("called initLogin");

  my $pid = _getProviderId($request);
  if (defined $pid) {
    return if $pid eq 'internal';

    my $provider = $this->auth->getProvider($pid);

    _writeDebug("... provider=".$provider->prop("id"));
    return $provider->initLogin($request, $state);
  }

  my $isOk = 0;
  foreach my $provider ($this->auth->getProviders) {
    next if $provider->isInternalLogin;

    _writeDebug("... trying to init provider ".$provider->prop("id"));

    $isOk = $provider->initLogin($request, $state);
    last if $isOk;
  }

  _writeDebug("... isOk=$isOk");

  return $isOk;
}

=begin TML

---++ ObjectMethod processSecondFactor($request, $state)

Process the second factor code as being provided by the url parameters =username= and =accesscode=.
An exception will be thrown if the user us unknown or the access code does not match.

=cut

sub processSecondFactor {
  my ($this, $request, $state) = @_;

  _writeDebug("called processSecondFactor()");

  my $loginName = $request->param('username') || '';
  my $accessCode = $request->param('accesscode') || '';

  unless ($loginName && $accessCode) {
    $this->setAuthLevel(0); # restart login process
    return 0;
  }

  my $user = $this->auth->getUserByID($loginName);
  throw Error::Simple($this->auth->maketext("Unknown user")) unless $user;

  _writeDebug("checking second factor");
  if ($user->verifySecondFactor($accessCode)) {
    _writeDebug("access code is valid ... logging in");
    return $this->finishLogin($request, $state, $user);
  }

  $this->setAuthLevel(1);
  throw Error::Simple($this->auth->maketext("Invalid access code"));
}

=begin TML

---++ ObjectMethod processLogin($request, $state)

once the login has been inited it will be processed either by the provider specified in the
=pauth_provider= url parameter or any provider in charge of this login.

=cut

sub processLogin {
  my ($this, $request, $state) = @_;

  _writeDebug("called processLogin()");
  if ($state) {
    _writeDebug("... state: key=".($state->{key}//'undef').", method=".($state->{method}//'undef').", action=".($state->{action}//'undef').", uri=".($state->{uri}//'undef'));
  } else {
    _writeDebug("... initial state");
  }

  my $user;
  my $pid = _getProviderId($request);

  if (defined $pid && $pid ne 'internal') {
    my $provider = $this->auth->getProvider($pid);

    _writeDebug("... provider=".$provider->prop("id"));
    $user = $provider->processLogin($request, $state);
  }

  unless (defined $user) {
    foreach my $provider ($this->auth->getProviders) {
      _writeDebug("... testing provider=".$provider->prop("id"));
      $user = $provider->processLogin($request, $state);
      last if defined $user;
    }
  }

  if (defined $user) {
    _writeDebug("remembering user ".$user->stringify);
    $this->{_user} = $user;

    # If fo 2fa enabled then switch up auth level and return else finishLogin
    if ($user->isTwoFactorAuthEnabled) {
      $this->setAuthLevel(1);
      return 0;
    }
    return $this->finishLogin($request, $state, $user);
  }

  _writeDebug("... could not process login");
  $this->setAuthLevel(0); # reset auth level

  return 0;
}

=begin TML

---++ ObjectMethod finishLogin()

Finish the login, that is finally generate a valid user session. This method is called after
the first or second authentication factor.

=cut

sub finishLogin {
  my ($this, $request, $state, $user) = @_;

  _writeDebug("called finishLogin");

  _writeDebug("... logging in " . $user->stringify . ($user->isAdmin ? " (admin)" : ""));

  my $loginName = $user->prop("loginName");
  $this->userLoggedIn($loginName);
  $user->updateLoginDate;
  $user->createTopic;

  my $cgis = $this->{session}->getCGISession();
  #$cgis->clear(['_pauth_state']) if $cgis;

  my $topic = $this->{session}{topicName};
  my $web = $this->{session}{webName};

  $this->{session}->logger->log({
      level => 'info',
      action => 'login',
      webTopic => $web . '.' . $topic,
      extra => "AUTHENTICATION SUCCESS - $loginName - "
    }
  );

  my $uri;
  if ($state) {
    _writeDebug("state found ... ");
    $uri = $state->{uri};
    _writeDebug("... uri in state=$uri");

    # Unpack params encoded in the uri and restore them
    # to the query. If they were left in the query string they
    # would be lost if we redirect with passthrough.
    # First extract the params, ignoring any trailing fragment.
    if ($uri =~ s/\?([^#]*)//) {
      foreach my $pair (split(/[&;]/, $1)) {
        if ($pair =~ m/^(.*?)=(.*)$/) {
          $request->param($1, $2);
        }
      }
    }

    # deleting some params for security");
    $request->delete('validation_key', 'foswiki_origin', 'sudo', 'username', 'password', 'accesscode', 'state', 'scope', 'authuser', 'prompt');

    # restore the action too
    $request->action($state->{action}) if $state->{action};

    # restore the method used on origUrl so if it was a GET, we
    # get another GET.
    $request->method($state->{method}) if $state->{method};
  } else {
    _writeDebug("no state found ... redirecting to $web.$topic");
    $uri = $this->{session}->getScriptUrl(0, 'view', $web, $topic);
  }

  if ($uri) {
    _writeDebug("... redirecting to $uri");
    $this->{session}->redirect($uri, 1);
  } else {
    _writeDebug("... no redirect after logging in");
  }

  return 1;
}

=begin TML

---++ ObjectMethod loadSession()

Implements the Foswiki::LoginManager::loadSession() api. Note that depending on the
provider of the current user context variables =password_modifiable=, =two_factor_auth= and
=two_factor_auth_enabled= are set.

=cut

sub loadSession {
  my $this = shift;

  _writeDebug("called loadSession");
  my $authUser = $this->SUPER::loadSession(@_);
  _writeDebug("... authUser=".($authUser//'undef'));

  my $session = $this->{session};
  my $request = $session->{request};
  my $logout = $session && $request && $request->param('logout');
  return if $logout;

  # test provider from url
  my $pid = _getProviderId($request);
  if ($pid && $pid ne "internal") {
    my $provider = $this->auth->getProvider($pid);
    if ($provider->canSetPassword) {
      _writeDebug(" ... pid=$pid can set passwords");
      $session->enterContext('passwords_modifyable');
    } else {
      _writeDebug(" ... pid=$pid cannot set passwords");
    }
  }

  # test current user
  my $user = $this->auth->findUser(id => $authUser, loginName => $authUser); 
  if (defined $user) {
    _writeDebug("... user ".$user->stringify." found");
  } else {
    _writeDebug("... user $authUser not found");
    return;
  }

  my $provider = $user->getProvider();

  if ($user->isAdmin || ($provider && $provider->canSetPassword($user))) {
    _writeDebug("... user=".$user->stringify." can set password");
    $session->enterContext('passwords_modifyable');
  }

  # check two factor policy and force redirect to twofactorauth
  if ($provider && $provider->prop("TwoFactorAuthEnabled")) {
    #_writeDebug("entering 2fa for ".$provider->prop("id"));

    $session->enterContext('two_factor_auth');
    if ($user->isTwoFactorAuthEnabled()) {
      $session->enterContext('two_factor_auth_enabled');
    }

    if ($user->checkTwoFactorPolicy) {
      _writeDebug("2fa policy is fulfilled");
    } else {
      _writeDebug("2fa policy is violated");
      $session->enterContext('two_factor_auth_required');

      if ($session->inContext("command_line")) {
        _writeDebug("not redirecting on the command line");
      } else {
        if ($session->inContext("view")) {
          my ($web, $topic) = $user->getTopic();
          my $template = $request->param("template") // "";

          if ($session->{webName} ne $web ||
              $session->{topicName} ne $topic || 
              $template ne "twofactorauth") {

            my $url = $session->getScriptUrl(0, 'view', $web, $topic, template => "twofactorauth");

            _writeDebug("redirecting to $url");
            $request->delete("redirectto"); # remove any other redirect
            $session->redirect($url);
          } else {
            _writeDebug("we are in progress of configuring 2fa");
          }
        } else {
          _writeDebug("access denied for any non-view context");

          $session->{response}->status(403);
          $session->redirect('/', 0, 403);
          $session->leaveContext('authenticated');
        }
      }
    }
  }

  # TODO: force user into ChangePassword on password reset
  return $authUser;
}

=begin TML

---++ ObjectMethod redirectToLoggedOutUrl($authUser, $defaultUser)


=cut

sub redirectToLoggedOutUrl {
  my ($this, $authUser, $defaultUser) = @_;

  $defaultUser //= $Foswiki::cfg{DefaultUserLogin};

  _writeDebug("called redirectToLoggedOutUrl($authUser, $defaultUser)");

  my $session = $this->{session};
  my $web = $this->{session}{webName};
  my $topic = $this->{session}{topicName};

  $session->logger->log({
      level => 'info',
      action => 'logout',
      extra => "AUTHENTICATION LOGOUT - $authUser - ",
      user => $authUser
    }
  );
  $session->{request}->delete('logout');

  my $url;
  my $provider;
  my $user = $this->auth->findUser(loginName => $authUser);

  if ($user) {
    $user->logout();
    $provider = $user->getProvider();
  }

  $url = $provider->prop("LogoutURL") if $provider;
  $url ||= $session->getScriptUrl(1, 'view', $session->{webName}, $session->{topicName});

  if ($url) {
    _writeDebug("redirecting to $url");
    $session->redirect($url, 0);
  } else {
    _writeDebug("no redirect url on logout");
  }

  return $defaultUser;
}

=begin TML

---++ ObjectMethod getAuthLevel() -> $level

returns the current authentication level as stored in the user session. The authentication level indicates
the stage of the login:

   * 0: initial state of login
   * 1: first factor has been processed successfully
   * 2: second factor can been processed 

=cut

sub getAuthLevel {
  my $this = shift;

  $this->{_authLevel} //= $this->getSessionValue("_PAUTH_LEVEL", 1) || 0;

  return $this->{_authLevel};
}

=begin TML

---++ ObjectMethod setAuthLevel($val) -> $success

sets the authentication level. possible values are 0, 1 or 2. 

See Foswiki::LoginManager::PluggableLogin::getAuthLevel().

=cut

sub setAuthLevel {
  my ($this, $val) = @_;

  $this->{_authLevel} = $val || 0;

  _writeDebug("called setAuthLevel($this->{_authLevel})");
  return $this->setSessionValue('_PAUTH_LEVEL', $this->{_authLevel});
}


=begin TML

---++ ObjectMethod getSessionValue($key, $consume) -> $val

adds an additional boolean "comsume": if enabled will clear the value

=cut

sub getSessionValue {
  my ($this, $key, $comsume) = @_;

  my $val = $this->SUPER::getSessionValue($key);
  #_writeDebug("getSessionValue($key)=".($val//'undef'));
  $this->clearSessionValue($key) if $comsume;

  return $val;
}

### static helper

sub _getProviderId {
  my $request = shift;

  my $pid = $request->param('pauth_provider');

  return unless defined $pid;
  $pid =~ s/[^\d\w]//g;

  return $pid;
}

sub _writeDebug {
  print STDERR "PluggableLogin - $_[0]\n" if TRACE || $Foswiki::cfg{PluggableAuth}{Debug};
}

1;
