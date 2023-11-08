#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

    if a_dictionary is None or len(a_dictionary) == 0:
        return

    max_val = 0
    max_key = ''

    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key
