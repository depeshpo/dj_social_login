from .base import *

SECRET_KEY = 'loo5lsmt^yn)(hgw9h1g13^n)0uhd0+xqa0jnb!'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'APP': {
            'client_id': '<client_id>',
            'secret': '<secret_key>'
        },
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '<google_client_id>',
            'secret': '<google_secret_key>',  # secret not required for rest API
            'key': ''
        }
    },
    'github': {
        'APP': {
            'client_id': '<client_id>>',
            'secret': '<secret_key>>'
        },
        'SCOPE': [
            'user',
            'read:org',
        ],
    }
}
