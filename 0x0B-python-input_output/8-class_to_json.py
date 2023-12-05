#!/usr/bin/python3
"""
This module defines a function for converting a class instance
to a JSON-formatted dictionary.
"""


def class_to_json(obj):
    """
    Converts the specified class instance to a JSON-formatted dictionary.

    Args:
        obj: The class instance to be converted.

    Returns:
        dict: A dictionary representing the attributes of the class instance.
    """

    return obj.__dict__
