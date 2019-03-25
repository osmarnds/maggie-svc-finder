# -*- coding: utf-8 -*-
'''Tests for Login module.'''

import json
import os
from unittest import TestCase
from time import time
from jwt import encode
from app.config import config
from app.app import create_app

class LoginTest(TestCase):
    '''Tests for login module'''

    def setUp(self):
        self.app = create_app()

    def tearDown(self):
        pass

    def test_login(self):
        '''Test dummy OAuth '''
        with self.app.test_client() as client:
            resp = client.get('/api/login/whoami')
            assert json.loads(resp.data).get('username') == os.environ.get('username', 'root')

    def test_no_token(self):
        '''Should return HTTP 401 '''
        with self.app.test_client() as client:
            client.cookie_jar.clear()
            resp = client.get('/api/login/whoami')
            assert resp.status_code == 401

    def test_bad_token(self):
        '''Should return invalid token error '''
        with self.app.test_client() as client:
            client.set_cookie('localhost.local', 'auth_token', 'bad_token')
            resp = client.get('/api/login/whoami')
            assert resp.data == b'{ "error": "token_invalid"}'

    def test_expired_token(self):
        '''Should return expired token error '''
        with self.app.test_client() as client:
            expired_jwt_token = encode({
                'sub': 'some_user',
                'exp': int(time()) -1
                }, config.JWT_KEY)
            client.set_cookie('localhost.local', 'auth_token', expired_jwt_token)
            resp = client.get('/api/login/whoami')
            assert resp.data == b'{ "error": "token_expired"}'
