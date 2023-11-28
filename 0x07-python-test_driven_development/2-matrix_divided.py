#!/usr/bin/python3
"""Matrix divided module
check for valid matix and divided it"""


def matrix_divided(matrix, div):
    """Check for valid matrix:
        a list of lists of floats or integers
        and return a matrix of rounded floats to 2 decimal digits
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mat_err = "matrix must be a matrix (list of lists) \
of integers/floats"
    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError(mat_err)

    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[i-1]):
            size_err = "Each row of the matrix must have the same size"
            raise TypeError(size_err)

        for column in matrix[i]:
            if type(column) not in {int, float}:
                raise TypeError(mat_err)

    return [[float(round(x/div, 2))for x in row] for row in matrix]
