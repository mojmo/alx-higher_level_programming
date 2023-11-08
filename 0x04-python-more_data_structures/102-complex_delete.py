#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""

    if a_dictionary is None:
        return None

    deleted_keys = [key for key, val in a_dictionary.items() if val == value]

    for key in deleted_keys:
        if key in deleted_keys:
            del a_dictionary[key]

    return a_dictionary
