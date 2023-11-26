#!/usr/bin/python3

"""

Module for text manipulation.

This module provides functions for manipulating text,
specifically for adding 2 new lines after each '.', '?', and ':'
in a given text.

"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        lines = [line.strip(" ") for line in text.split(delim)]
        text = f"{delim}\n\n".join(lines)

    print(text, end="")
