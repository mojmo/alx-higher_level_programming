#!/usr/bin/python3

"""

A module contains a method that prints the entire name.

"""


def say_my_name(first_name, last_name=""):
    """Print a formatted string with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")