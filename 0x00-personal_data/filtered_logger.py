#!/usr/bin/env python3
"""
This module provides a function for obfuscating sensitive information in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replace occurrences of certain field values in a log message with a redaction string.

    Args:
        fields: A list of strings representing all fields to obfuscate.
        redaction: A string representing by what the field will be obfuscated.
        message: A string representing the log line.
        separator: A string representing by which character is separating all fields in the log line (message).

    Returns:
        A new string with the specified fields obfuscated.

    """
    pattern = fr'(?<={re.escape(separator)})({"|".join(fields)})\b'
    return re.sub(pattern, redaction, message)
