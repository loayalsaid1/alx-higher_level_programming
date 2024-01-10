#!/usr/bin/python3
"""Define a student class"""


class Student:
    """A student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation
            of all the attributes of an <self>.
            ----
            If <attrs> are list of strings, Get only the names in that list.

            Args:
                self: The instance.
                attrs: List of allowed names

            Return: Dictionary of attributes based on above conditions.
        """
        condition = type(attrs) is list and\
            any(type(attr) is not str for attr in attrs)
        if attrs is None or condition:
            return self.__dict__

        dic = {}
        for attr in attrs:
            if attr in self.__dict__:
                dic[attr] = self.__dict__[attr]
        return dic

    def reload_from_json(self, json):
        """Replace attributes of <self>
            based on the data from <json>.

            Args:
                self: You guess it!
                json: A dict holdig key-value data.

            Return: Nothing!
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
