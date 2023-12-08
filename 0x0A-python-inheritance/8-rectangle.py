#!/usr/bin/python3
"""8-rectangle module"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """raise an exception!"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is int or not"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangel(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Iniitialzie the object"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
