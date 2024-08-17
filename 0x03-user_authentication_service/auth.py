#!/usr/bin/env python3
"""Authentication module
"""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound


from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Function that hashes a password and returns bytes
    Args:
        password (str): The password to be hashed.
    Returns:
        bytes: The hashed password
    """
    encoded_password = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password.
        Args:
            email (str): user email
            password (str): user password
        Returns:
            User: A User object representing the newly created user.
        Raises:
            ValueError: If a user with the given email already exist
        """
        try:
            check_user = self._db.find_user_by(email=email)

            if check_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed_pwd = _hash_password(password)
        new_user = self._db.add_user(
                email=email, hashed_password=hashed_pwd)
        return new_user
