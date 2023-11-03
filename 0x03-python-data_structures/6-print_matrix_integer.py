#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers."""

    for row in matrix:
        row_str = ""

        for ele in row:
            row_str += "{:d} ".format(ele)

        print(row_str[:-1])
