#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Create a Square class and initiate the instase with a variable"""
    def __init__(self, size=0):
        """Init function, initialize object with size attribute
        with proper exceptions"""
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
