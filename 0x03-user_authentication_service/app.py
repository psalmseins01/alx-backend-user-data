#!/usr/bin/env python3
"""app module"""
from flask import (Flask, jsonify,
                   Response, request, abort)
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/')
def home() -> Response:
    """Home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> Response:
    """POST /users
    Return:
        - JSON payload of the form containing various information
    HTTP Status codes:
    - 200 OK: User successfully registered
    - 400 Bad Request: Invalid request method
                        email already registered
    - 500 Internal Server Error: Unexpected error during registration
    """
    if request.method == "POST":
        email_feild = request.form.get("email")
        email = email_feild.strip()
        passwd_feild = request.form.get("password")
        passwd = passwd_feild.strip()
        try:
            AUTH.register_user(email, passwd)
            return jsonify({"email": email,
                            "message": "user created"})
        except Exception:
            return jsonify({"message": "email already registered"})
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
