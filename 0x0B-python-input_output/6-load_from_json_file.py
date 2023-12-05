#!/usr/bin/python3
"""
This module defines a function for loading a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from the specified JSON file.

    Args:
        filename (str): The name or path of the JSON file.

    Returns:
        The Python object loaded from the JSON file.

    Example:
        python_obj = load_from_json_file("input.json").
    """

    with open(filename) as f:
        return json.load(f)
