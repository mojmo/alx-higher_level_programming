#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds the biggest integer of a list."""

    if my_list:
        max_val = my_list[0]
        for val in my_list:
            if val > max_val:
                max_val = val
        return max_val
