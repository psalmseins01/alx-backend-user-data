#!/usr/bin/python3
"""Auth module for api authentication management"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
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
        # If path is None, return True
        if not path:
            return True
        # If excluded_paths is None or Empty, return True
        if not excluded_paths:
            return True
        # Remove the trailing slash from the path
        path = path.rstrip("/")
        # Check if path is in excluded_paths. Return False if path is
        # in excluded_paths
        # Loop through excluded paths
        for excluded_path in excluded_paths:
            # Check if given path starts with excluded path, with * at the end
            if excluded_path.endswith("*") and \
                    path.startswith(excluded_path[:-1]):
                # Return False if path starts with excluded path with * at end
                return False
            # Check if the given path is equal to the excluded path
            elif path == excluded_path.rstrip("/"):
                # Return False if the path is equal to the excluded path
                return False
        # If not in excluded_paths, return True
        return False

    def authorization_header(self, request=None) -> None:
        """
        """
        return

    def current_user(self, request=None) -> None:
        """
        """
        return


if __name__ == "__main__":
    a = Auth()
    print(a.require_auth("/api/v1/status/", ["/api/v1/status"]))
    print(a.authorization_header())
    print(a.current_user())
