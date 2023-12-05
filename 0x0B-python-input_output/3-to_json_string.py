#!/usr/bin/python3
"""
This module defines a function for converting a Python object
to a JSON-formatted string.
"""
import json


def to_json_string(my_obj):
    """
    Converts the specified Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: A JSON-formatted string representing the input Python object.

    Example:
        json_str = to_json_string({"key": "value"})
    """

    return json.dumps(my_obj)
