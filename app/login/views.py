# -*- coding: utf-8 -*-
'''Login blueprint views. Contains routes regarding authentication'''

import os
import json
from datetime import datetime
from time import time
import requests
from jwt import decode, encode
from flask import Blueprint, Response, request, jsonify, current_app
from app.decorators import authorize
from app.logging import pcf_logger

login_bp = Blueprint('login', __name__, url_prefix='/api/login')

@login_bp.route('/whoami', methods=["GET"])
@authorize
def whoami():
    '''Returns username of the user who called this method'''
    return jsonify({'username': request.environ['username']})

@login_bp.route('/oauth', methods=["GET"])
def login(): #pragma: no cover
    '''Route that performs OAuth authentication'''
    config = current_app.config

    if config.get('OAUTH_DOMAIN') is None:
        pcf_logger.critical('No SSO configuration found. This should happen when running on localhost only.')
        resp = Response(status=302, headers={'Location': '/'})
        jwt_token = encode({
                'sub': os.environ.get('username', 'root'),
                'exp': int(time()) + (60 * 60 * 24)
            },
            config['JWT_KEY'])
        resp.set_cookie('auth_token',
                    value=jwt_token,
                    expires=datetime.fromtimestamp(int(time()) + (60 * 60 * 24)),
                    httponly=True,
                    samesite='strict'
                   )
        return resp

    if request.args.get('code') is None:
        return Response(
            status=302,
            headers={
                'Location': '{}?response_type=code&state=&client_id={}'.format(
                    config['OAUTH_DOMAIN'] + '/oauth/authorize',
                    config['OAUTH_CLIENT_ID']
                )
            }
        )

    # Decode the oAuth token we got from PCF
    oauth_url = '{}?grant_type=authorization_code&code={}'.format(
        config['OAUTH_DOMAIN'] + '/oauth/token', request.args.get('code')
        )
    oauth_response = requests.get(
        oauth_url,
        auth=(config['OAUTH_CLIENT_ID'], config['OAUTH_CLIENT_SECRET'])
        ).content
    encoded_oauth_token = json.loads(oauth_response).get("access_token")
    oauth_token = decode(
        encoded_oauth_token,
        key=current_app.config['OAUTH_PUBLIC_KEY'],
        verify=True,
        algorithms=current_app.config['OAUTH_ALG'],
        audience='openid')

    # Create our own JWT token
    jwt_token = encode({
        'jti': oauth_token.get('jti'),
        'sub': oauth_token.get('user_name'),
        'email': oauth_token.get('email'),
        'exp': oauth_token.get('exp')
        },
        config['JWT_KEY'])
    resp = Response(status=302, headers={'Location': '/'})
    resp.set_cookie('auth_token',
                    value=jwt_token,
                    domain=request.headers['Host'],
                    expires=datetime.fromtimestamp(oauth_token.get('exp')),
                    secure=True,
                    httponly=True,
                    samesite='strict'
                   )

    return resp
