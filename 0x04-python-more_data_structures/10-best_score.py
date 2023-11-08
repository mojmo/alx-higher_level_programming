#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    if a_dictionary is None:
        return None

    max_key = max(sorted(a_dictionary), key=lambda key: a_dictionary[key])

    return max_key
