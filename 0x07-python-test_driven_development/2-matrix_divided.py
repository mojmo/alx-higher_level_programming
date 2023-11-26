#!/usr/bin/python3

"""

A module contains a function for dividing a matrix by divisor.

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix
        div (int or float): The divisor

    Raises:
        TypeError: If the input matrix is not a list of lists, if it is empty,
                   if any row is empty, or if it contains elements other
                   than integers or floats.
                   If the divisor is not a number.
                   If all rows of the matrix do not have the same size.
        ZeroDivisionError: If the divisor is 0.

    Returns:
        list of lists: The resulting matrix after division.
    """

    # Check that matrix is a list of list and contain only int or float
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if ((not isinstance(matrix, list) or not matrix) or
        (not all(isinstance(sublist, list) and sublist and
                 all(isinstance(element, (int, float)) for element in sublist)
                 for sublist in matrix))):
        raise TypeError(err_msg)

    # Check if all the rows have the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return divided_matrix
