#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """ Initialize a new square instance.

        Args:
            size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
