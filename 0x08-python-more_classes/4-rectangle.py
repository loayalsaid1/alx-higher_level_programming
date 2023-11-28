#!/usr/bin/python3
""" Module to represent a rectangle and operations on it"""


class Rectangle:
    """
    A class to represent a rectangle and operations one it
    """
    def __init__(self, width=0, height=0):
        """initialize the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """
        Return the perimeter of it: (<width> + <height>) * 2
        in case any of the width or the heigth is zero, return 0
        """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        else:
            return 0

    def area(self):
        """Return the area of it, <width> * <height>"""
        return self.width * self.height

    def __str__(self):
        """Represent the string representation of the rectnalge
        with '#' symbols"""
        rectangle = ""
        if not (self.width and self.height):
            return rectangle

        for h in range(self.height - 1):
            rectangle += self.width * '#'
            rectangle += '\n'
        rectangle += self.width * '#'

        return rectangle

    def __repr__(self):
        """return the developer verstion of the object (A representation
        that can create a new object if passed to evel())"""
        return f"Rectangle({self.width}, {self.height})"
