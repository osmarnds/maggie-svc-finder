# -*- coding: utf-8 -*-
'''Frontend blueprint views. Contains routes regarding serving static html/css/js files'''

from flask import Blueprint, Response, request, send_file

frontend_bp = Blueprint('frontend', __name__, url_prefix='', static_url_path='/', static_folder='./static')

@frontend_bp.route('/')
@frontend_bp.route('/Index.html')
def get_static():
    '''Send the Index.html file, make it so it is not cached'''
    return send_file('./app/frontend/static/Index.html', cache_timeout=0)

@frontend_bp.before_request
def before_request():
    '''Executed before every request in this blueprint.
    If the user didn't send a token redirect him to be authenticated'''
    if request.cookies.get('auth_token') is None and not request.path.endswith('.map'):
        return Response(status=302, headers={'Location': '/api/login/oauth'})
