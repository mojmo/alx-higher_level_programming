#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified level.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = []

    for _ in range(n):
        # starts with 1
        row = [1]

        # Check if there is any previous row in triangle.
        # If yes, generate the current row based on the previous row.
        if triangle:
            prev_row = triangle[-1]

            # if prev_row =                 [1, 2 ,1]
            #                                |  |
            # then prev_row[1:] =           [2, 1]
            # zip(prev_row, prev_row[1:]) = (1, 2) and (2, 1)
            for pair in zip(prev_row, prev_row[1:]):
                row.extend([sum(pair)])

            # row += [sum(pair) for pair in zip(prev_row, prev_row[1:])]
            row.append(1)

        # ends with 1
        triangle.append(row)

    return triangle
