#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from typing import Tuple, Optional
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

if getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

if getenv('AUTH_TYPE') == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def before_request() -> Optional[str]:
    """Handle the request by checking
    for authentication and authorization
    """
    # Create list of allowed_paths
    allowed_paths = ['/api/v1/status/',
                     '/api/v1/unathorized/',
                     '/api/v1/forbidden/',
                     '/api/v1/auth_session/login/']
    if auth is None:
        return
    if not auth.require_auth(request.path, allowed_paths):
        return
    auth_header = auth.authorization_header(request)
    session_cookie = auth.session_cookie(request)
    if auth_header is None and session_cookie is None:
        abort(401)
    if auth.current_user(request) is None:
        return abort(403)
    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> Tuple[jsonify, int]:
    """ Not found handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> Tuple[jsonify, int]:
    """ Not found handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
