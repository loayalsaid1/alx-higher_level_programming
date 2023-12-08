#!/usr/bin/python3
"""I don't know ?!"""


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
