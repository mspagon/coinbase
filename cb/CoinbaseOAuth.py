import os
import requests
import urllib.parse

class CoinbaseOauthError(Exception):
    pass


class CoinbaseOAuth():
    COINBASE_AUTHORIZE_URL = 'https://www.coinbase.com/oauth/authorize'
    COINBASE_TOKEN_URL = 'https://api.coinbase.com/oauth/token'

    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, scope=None, state=None):
        if not client_id:
            client_id = os.getenv('COINBASE_CLIENT_ID')
        if not client_secret:
            client_secret = os.getenv('COINBASE_CLIENT_SECRET')
        if not redirect_uri:
            redirect_uri = os.getenv('COINBASE_REDIRECT_URI')

        if not client_id:
            raise CoinbaseOauthError('No client ID')

        if not client_secret:
            raise CoinbaseOauthError('No secret key')

        if not redirect_uri:
            raise CoinbaseOauthError('No redirect uri')

        self.client_id = client_id
        self.client_secret = client_secret
        self.token_info = None
        self.scope = scope
        self.redirect_uri = redirect_uri

    def get_authorize_url(self):

        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
        }

        params = urllib.parse.urlencode(params)

        return self.COINBASE_AUTHORIZE_URL + '?' + params

    def get_token(self, code, grant_type='authorization_code'):
        params = {
            'grant_type': grant_type,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }


def main():
    c = CoinbaseOAuth()
    print(c.client_id, c.client_secret, c.redirect_uri)

if __name__ == '__main__':
    main()