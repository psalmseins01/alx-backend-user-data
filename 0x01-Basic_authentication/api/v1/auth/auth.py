#!/usr/bin/env python3
"""Auth module for api authentication management"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Template for the authentication systems implemented for this app.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function that takes a path and a list of excluded paths as arguments
        and then returns a boolean value.

        Returns True if `path` is None.
        Returns True if `excluded_paths` is either None or empty.
        Returns False if `path` is in `excluded_paths`.
        You can assume excluded_paths contains string path always ending by
        a /. This method must be slash tolerant: path=/api/v1/status and
        path=/api/v1/status/ must be returned False if excluded_paths contains
        /api/v1/status/.

        Args:
            path (str): The path to check against the list of excluded paths.
            excluded_paths (List[str]): List of excluded paths.

        Returns:
            bool: True if the path is not in the excluded paths list,
            False otherwise.
        """
        # You can assume excluded_paths contains string path ending /
        if path and not path.endswith('/'):
            path = path + '/'
        # if path is not None then return true
        if not path or path not in excluded_paths:
            return True
        # If path is None, return True
        # If excluded_paths is None or Empty, return True
        if not excluded_paths or excluded_paths == []:
            return True
        # Returns False if path is in excluded_paths
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> None:
        """
        Function that gets the value of the Authorization header
        from the request

            request (request, optional): Flask request obj. Defaults to None.

        Returns:
            str: The value of the Authorization header or None if not present.
        """
        return

    def current_user(self, request=None) -> None:
        """This function takes a request object as an optional argument
        (defaults to None) and returns a value of type 'User'. The purpose
        and how the request object is used will be determined later.
        For now, it simply returns None.
        """
        return
