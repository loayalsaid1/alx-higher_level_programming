#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """ Initialize a new square instance.

        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """return the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the value of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """get the area of the square"""
        return self.__size ** 2
