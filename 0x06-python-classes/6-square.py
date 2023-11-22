#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new square instance.

        Args:
            size: The size of the squar
            position: Positionof the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with # symbols"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for row in range(self.size):
            [print(" ", end="") for j in range(self.position[0])]
            for colomn in range(self.size):
                print("#", end="")
            print()
