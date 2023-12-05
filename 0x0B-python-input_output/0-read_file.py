#!/usr/bin/python3
"""
This module contains a function for reading and printing
the contents of a file.
"""


def read_file(filename=""):
    """
    Reads the contents of the specified file and prints them to the console.

    Args:
        filename (str): The name or path of the file to be read.
        Default is an empty string.
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
