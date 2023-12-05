#!/usr/bin/python3
"""
This module defines a function for saving a Python object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves the specified Python object to the specified JSON file.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name or path of the JSON file.

    Example:
        save_to_json_file({"key": "value"}, "output.json")
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
