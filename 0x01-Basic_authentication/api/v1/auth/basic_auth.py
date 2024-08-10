#!/usr/bin/env python3
"""Basic Authentication module"""

from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic authentication class.

    Args:
        Auth (type): Class inherited from
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Function that extracts the Base64 part
        of the Authorization header.
        Args:
            authorization_header (str): Authorization header string.
        Returns:
            str: Base64 part of 'Authorization header'
            returns None if the header is invalid.
        """
        # Return None if authorization_header is None
        if authorization_header is None:
            return
        # Return None if authorization_header is not a string
        if not isinstance(authorization_header, str):
            return
        # Return None if authorization_header doesn’t start by Basic
        # (with a space at the end)
        if not authorization_header.startswith('Basic '):
            return
        # Otherwise, return the value after Basic (after the space)
        auth_value = authorization_header.split(' ')[1]
        # You can assume authorization_header contains only one Basic
        return auth_value

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes the Base64 string `base64_authorization_header` and
        returns the decoded value as a UTF8 string.
        Args:
            base64_authorization_header (str): A Base64 encoded string to be
            decoded.
        Returns:
            str: The decoded value as a UTF8 string.
        """
        if not base64_authorization_header:
            return
        if not isinstance(base64_authorization_header, str):
            return
        try:
            decoded_str = base64.b64decode(base64_authorization_header,
                                           validate=True)
            # Return the decoded value as UTF8 string
            # convering the bytes into readable string
            return decoded_str.decode('utf-8')
        except Exception:
            return

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user email and password from the decoded header string.
        Args:
            decoded_header (str): A decoded header string.
        Returns:
            (str, str) Tuple containing the email and password.
        """
        # Return None, None if decoded_base64_authorization_header is None
        if not decoded_base64_authorization_header:
            return None, None
        # Return None, None if decoded_base64_authorization_header
        # is not a string
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        # Return None, None if decoded_base64_authorization_header
        # doesn’t contain
        if ":" not in decoded_base64_authorization_header:
            return None, None
        # Otherwise, return the user email and the user password
        # these 2 values must be separated by a :
        try:
            email, password = decoded_base64_authorization_header.split(':')
        except ValueError:
            return None, None
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the User instance that corresponds to
        the email and password.
        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.
        Returns:
            User: Returns the User object or None
            if the user is not found or the
            password is not valid.
        """
        # Return None if user_email is None or not a string
        if not user_email or not isinstance(user_email, str):
            return
        # Return None if user_pwd is None or not a string
        if not user_pwd or not isinstance(user_pwd, str):
            return
        # Return None if your database (file) doesn’t contain
        # any User instance with email equal to user_email
        # you should use the class method search of the User
        # to lookup the list of users based on their email.
        # Don’t forget to test all cases:
        # “what if there is no user in DB?”, etc.
        try:
            user = User.search({"email": user_email})
        except Exception:
            return
        if not user:
            return
        if not user.is_valid_password(user_pwd):
            return
        return user
