#!/usr/bin/python3
"""
Defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified
    class or a subclass thereof; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified
        class or a subclass thereof, False otherwise.
    """

    return isinstance(obj, a_class)
