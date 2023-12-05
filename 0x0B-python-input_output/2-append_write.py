#!/usr/bin/python3
"""
This module defines a function for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the specified text to the specified file
    and returns the length of the appended text.

    Args:
        filename (str): The name or path of the file to which the text
        will be appended. Default is an empty string.
        text (str): The text to be appended to the file.
        Default is an empty string.

    Returns:
        int: The length of the appended text.
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
