#!/usr/bin/python3
"""Defind a base class"""


import json


class Base:
    """Base class for all the upcomming classes
        It's rule is manages IDs of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init instances

            Args:
                id: the id of the instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Get the json representation of objects

            Args:
                list_dictionaries: A list of dictionaries of instaceattributes

            Return: A list of json strings
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        result = []
        for object in list_dictionaries:
            result += json.dumps(object)

        return str(result)
