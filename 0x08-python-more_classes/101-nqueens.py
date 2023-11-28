#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens
on an NxN chessboard.

Usage:
    ./nqueens_solver.py N

N must be an integer greater than or equal to 4.

Attributes:
    is_safe_position (function): Checks if placing a queen at a specific
    row and column on the chessboard is safe.
    find_all_solutions (function): Solves the N-queens puzzle and returns
    a list of all possible solutions.

The solution represents with the format list of [row, col] pairs.
"""


def is_safe_position(board, row, col):
    """Check if placing a queen at a specific position is safe.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to check.
        col (int): The current column to check.

    Returns:
        bool: True if placing a queen at the position is safe, False otherwise.
    """

    for i in range(row):
        if (board[i] == col or board[i] == col + (row - i) or
                board[i] == col - (row - i)):
            return False
    return True


def find_all_solutions(board_size):
    """Solves the N-queens puzzle.

    Args:
        board_size (int): The size of the chessboard.

    Returns:
        list: A list of all possible solutions, where each solution is
              represented as a list of [row, col] pairs.
    """

    chessboard = [0] * board_size
    solutions = []

    def format_solution(chessboard):
        """Formats a solution to the desired format.

        Args:
            chessboard (list): The current state of the chessboard.

        Returns:
            list: A list of [row, col] pairs representing the solution.
        """

        return [[i, col] for i, col in enumerate(chessboard)]

    def backtrack(row):
        """Recursively backtracks to find all solutions.

        Args:
            row (int): The current row in the backtracking process.
        """

        if row == board_size:
            solutions.append(format_solution(chessboard))
            return

        for col in range(board_size):
            if is_safe_position(chessboard, row, col):
                chessboard[row] = col
                backtrack(row + 1)
                chessboard[row] = 0

    backtrack(0)
    return solutions


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens_solver.py N")
        sys.exit(1)

    n_value = sys.argv[1]

    if not n_value.isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(n_value) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions_list = find_all_solutions(int(n_value))
    for solution_item in solutions_list:
        print(solution_item)
