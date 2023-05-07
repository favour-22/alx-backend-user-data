#!/usr/bin/env python3
"""
Hashing
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt.

    Args:
        password: The password to hash.

    Returns:
        A salted, hashed password as a byte string.
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a plaintext password matches a hashed password.

    Args:
        hashed_password: The hashed password as a byte string.
        password: The plaintext password to check.

    Returns:
        True if the plaintext password matches the hashed password, False otherwise.
    """
    # Hash the plaintext password with the same salt as the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
