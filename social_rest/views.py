from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from allauth.account.adapter import DefaultAccountAdapter

# Create your views here.
from rest_auth.registration.views import SocialLoginView


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # client_class = OAuth2Client
    # callback_url = 'http://localhost:8000/accounts/google/login/callback/'


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    # client_class = OAuth2Client
    # callback_url = 'https://development.com:8000/accounts/google/login/callback/'


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    # callback_url = 'http://localhost:8000/accounts/github/login/callback/'
    # client_class = OAuth2Client
