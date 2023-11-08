#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    if a_dictionary == None:
        return

    max_key = max(a_dictionary, key = a_dictionary.get)

    return max_key
