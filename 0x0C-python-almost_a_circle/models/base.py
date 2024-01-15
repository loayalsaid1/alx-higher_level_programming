#!/usr/bin/python3
"""Defind a base class"""


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
