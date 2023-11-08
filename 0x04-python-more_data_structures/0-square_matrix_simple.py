#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""

    square_matrix = [[num ** 2 for num in row] for row in matrix]

    return square_matrix
