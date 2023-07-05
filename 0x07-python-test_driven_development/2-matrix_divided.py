#!/usr/bin/python3
"""Write a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix divider with doctest

    Args:
        matrix (list): floats/int 2d matrix
        div (int): _description_

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        float: round 2 of int
    """
    if [(int, float).__contains__(type(i))
            for sub in matrix for i in sub].__contains__(False):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if [len(row) == matrix[i+1] for i, row in
            enumerate(matrix) if i < (len(matrix)-1)].__contains__(True):
        raise TypeError(
            "Each row of the matrix must have the same size")
    if not (int, float).__contains__(type(div)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round((i/div), ndigits=2) for i in sub] for sub in matrix]
