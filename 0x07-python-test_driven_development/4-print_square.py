#!/usr/bin/python3
"""4-print_square.py module"""


def print_square(size):
    """Print a square of '#' symbols of height <size>
    and accept only positive integers
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print('#', end="")
        print()
