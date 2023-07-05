#!/usr/bin/python3
"""add two integers
"""


def add_integer(a, b=98):
    """addition or two integers or floats

    Args:
        a (int): integer or float
        b (int, optional): integer or float. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: some of a + b
    """
    allowedtypes = (int, float)
    if not allowedtypes.__contains__(type(a)):
        raise TypeError("a must be an integer")
    if not allowedtypes.__contains__(type(b)):
        raise TypeError("b must be an integer")
    return int(a+b)
