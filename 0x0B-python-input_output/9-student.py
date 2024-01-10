#!/usr/bin/python3
"""Define a student class"""


class Student:
    """A student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation
            of all the attributes of an <self>.

            Args:
                self: The instance

            Return: YOU STILL DIDN'T GET IT?! !!!!!!!!!!!!
        """
        return self.__dict__
