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
