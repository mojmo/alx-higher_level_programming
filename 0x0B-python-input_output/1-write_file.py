#!/usr/bin/python3
"""
This module contains a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to the specified file and returns
    the length of the written text.

    Args:
        filename (str): The name or path of the file to which the text
        will be written. Default is an empty string.
        text (str): The text to be written to the file.
        Default is an empty string.

    Returns:
        int: The length of the written text.
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
