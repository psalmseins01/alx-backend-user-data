#!/usr/bin/env python3
"""Basic Authentication module"""

from api.v1.auth.auth import Auth


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
