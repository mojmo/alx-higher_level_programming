#!/usr/bin/python3
"""
Defines the add_attribute function.
"""


def add_attribute(obj, attr_name, attr_val):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute is added.
        attr_name (str): The name of the attribute.
        attr_val: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_val)
