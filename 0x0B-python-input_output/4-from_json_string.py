#!/usr/bin/python3
"""
This module defines a function for parsing a JSON-formatted string
and converting it to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Parses the specified JSON-formatted string and converts
    it to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be parsed.

    Returns:
        The Python object represented by the input JSON-formatted string.

    Example:
        python_obj = from_json_string('{"key": "value"}')
    """

    return json.loads(my_str)
