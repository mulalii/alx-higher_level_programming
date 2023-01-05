#!/usr/bin/python3
"""
2-matrix_divided module
2-matrix_divided module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div
    Args:
    matrix: List of lists with containing int or float
    
    Returns:
        list: List of lists (divided matrix)
    Raises:
    TypeError: If matrix is not list of lists (with ints or floats)
    TypeError: If sublists are not all same size
    TypeError: if div is not int or float
    ZeroDivisionError: If div is zero
    """
    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        size = None
        for row in matrix:
            if type(row) is not list or len(row) == 0:
                raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
            if size is None:
                size = len(row)
            elif size != len(row):
                raise TypeError("Each row of the matrix must have the same size")
            for elem in row:
                if type(elem) not in (float, int):
                    raise TypeError("matrix must be a matrix (list of lists) " +
                                    "of integers/floats")
                    return [[round(elem / div, 2) for elem in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
