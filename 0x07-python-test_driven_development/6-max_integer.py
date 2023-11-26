#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


mylist = [
            9689.76543, 654.3567, 765432.45, -86.757,
            9.87654323, 54.3245, 8864.7, 82.0, 7228, 91, 4.22]

print(max_integer(mylist))
