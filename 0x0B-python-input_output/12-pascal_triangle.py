#!/usr/bin/python3
"""Create pascall triangle"""


def pascal_triangle(n):
    """Create pascall triangle

        Args:
            n: number of rows
        Return: A list of lists each represening a row
    """
    result = []
    a, b = [1], [1, 1]

    if n > 0:
        result.append(a)
    if n > 1:
        result.append(b)

    a, b = b, []
    for i in range(2, n):
        b.append(1)
        b += [a[j-1] + a[j] for j in range(1, i)]
        b.append(1)

        result.append(b)

        a, b = b, []

    return result
