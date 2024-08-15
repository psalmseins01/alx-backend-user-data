#!/usr/bin/env python3
"""Authentication module
"""

import bcrypt


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
