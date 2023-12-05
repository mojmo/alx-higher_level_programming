#!/usr/bin/python3
"""

This module defines a function for inserting a line of text into
a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing
    a specific string.

    Args:
        filename (str): The name or path of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each line containing
        the search string.
    """

    new_text = ""
    with open(filename, "r") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, "w") as f:
        f.write(new_text)
