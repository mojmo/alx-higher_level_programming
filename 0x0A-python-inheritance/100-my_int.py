#!/usr/bin/python3
"""
Defines the MyInt class, a subclass of int with
inverted == and != operators.
"""


class MyInt(int):
    """
    A class representing an integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.

        Note:
            super().__ne__(other) is equivalent to int(self) != other

        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """

        return super().__eq__(other)
