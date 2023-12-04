#!/usr/bin/python3
"""
This script defines a function 'lookup' that takes an object as
an argument and returns a list of attributes and methods
associated with that object.
"""


def lookup(obj):
    """
    This function takes an object as an argument and returns a list
    of attributes and methods associated with that object.

    Args:
        obj (object): The input object for which the attributes
        and methods need to be looked up.

    Returns:
        list: A list containing the names of attributes and methods
        associated with the input object.
    """

    return dir(obj)
