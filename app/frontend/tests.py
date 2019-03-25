# -*- coding: utf-8 -*-
'''Tests for frontned module.'''

from unittest import TestCase

from app.app import create_app

class FrontEndTest(TestCase):
    '''Tests for frontend module'''

    def setUp(self):
        self.app = create_app()

    def tearDown(self):
        pass

    def test_frontend_root(self):
        '''
            Should return index.html with HTTP 200
            Should return mimetype text/html
        '''
        with self.app.test_client() as client:
            resp = client.get('/')
            assert resp.status_code == 200
            assert resp.mimetype == 'text/html'
            assert resp.content_length > 0

    def test_404(self):
        '''Should return HTTP 404 error'''
        with self.app.test_client() as client:
            resp = client.get('/invalid_resource.html')
            assert resp.status_code == 404

    def test_not_logged_in(self):
        '''Should return HTTP 302 '''
        with self.app.test_client() as client:
            client.cookie_jar.clear()
            resp = client.get('/')
            assert resp.status_code == 302
