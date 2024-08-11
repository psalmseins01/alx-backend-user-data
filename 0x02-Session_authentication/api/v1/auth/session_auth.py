#!/usr/bin/env python3
"""Session authentication module for the API."""

from base64 import b64decode
import uuid
from typing import Optional, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class that inherits from Auth class.
    Args:
        Auth (type): Class inherited from
    """
    pass
