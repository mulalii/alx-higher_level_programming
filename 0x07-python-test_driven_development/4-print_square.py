#!/usr/bin/python3
"""
4-print_square.py
4-print_square.py module supplies one function, print_square(size)
"""


def print_square(size):
    """Function that prints a square
    Args:
        size: int size of the square to print
    Raises:
        TypeError: If size is not an int
        TypeError: If size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
