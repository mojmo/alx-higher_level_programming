#!/usr/bin/python3
"""
This module contains a function that finds a peak
in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds and returns the peak value in a list of integers
    using a binary search.

    Args:
        list_of_integers (list of int): A list of integers to search.

    Returns:
        int or None: The peak value in the list, or None if the list is empty.

    Note:
        A peak value is an element in the list that is greater
        than its neighbors. The function uses a binary search
        algorithm to find the peak value. If there is more than
        one peak value, the function will return any one of them.
    """

    list_length = len(list_of_integers)

    if (list_of_integers == []):
        return None

    if (list_length == 1):
        return list_of_integers[0]
    elif (list_length == 2):
        return max(list_of_integers)

    mid = list_length // 2
    peak = list_of_integers[mid]

    left_val = list_of_integers[mid - 1]
    right_val = list_of_integers[mid + 1]

    if peak > left_val and peak > right_val:
        return peak
    elif peak < left_val:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
