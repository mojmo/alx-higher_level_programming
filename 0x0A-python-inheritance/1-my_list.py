#!/usr/bin/python3
"""
Defines the MyList class.
"""


class MyList(list):
    """
    A class that extends the built-in list class and adds a public
    instance method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
