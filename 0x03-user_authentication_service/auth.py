#!/usr/bin/python3
"""Hashing a password"""
import bcrypt


def _hash_password(password:str) ->str:
    """ Reurn a salted password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

