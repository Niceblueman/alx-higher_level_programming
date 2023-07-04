#!/usr/bin/python3
"""_summary_
"""
import sys


def is_safe(board, row, col, N):
    """Check if the current position is safe for a queen

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    """Check the left side of the row

    Args:
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.'] * N for _ in range(N)]
    solutions = []

    def backtrack(col):
        """Base case: all queens have been placed

        Args:
            col (_type_): _description_
        """
        if col == N:
            solution = [''.join(row) for row in board]
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'

    backtrack(0)

    return solutions


if __name__ == '__main__':
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """Check the number of arguments"""
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """Check the number of arguments"""
    solutions = solve_nqueens(N)
    for solution in solutions:
        print('\n'.join(solution))
        print()
