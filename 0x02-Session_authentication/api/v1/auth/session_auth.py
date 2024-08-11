#!/usr/bin/env python3
"""Session authentication module for the API."""

from base64 import b64decode
from uuid import uuid4
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class that inherits from Auth class.
    Args:
        Auth (type): Class inherited from
    """
    # Create a class attribute user_id_by_session_id
    # initialized by an empty dictionary #noqa
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id.
        Args:
            user_id (str, optional): user_id to create a session for.
            Defaults to None.
        Returns:
            str: The session ID if the user_id is valid, None otherwise
        """
        # Return None if user_id is None
        # Return None if user_id is not a string
        if not user_id and not isinstance(user_id, str):
            return
        session_id = str(uuid4())
        # Generate a Session ID using uuid module and uuid4()
        # like id in Base
        # Store the mapping of session_id to user_id in the dictionary,
        # Use this Session_id as key of dictionary user_id_by_session_id,
        # the value for this key must be user_id
        self.user_id_by_session_id[session_id] = user_id
        # Return the session_id
        return session_id
