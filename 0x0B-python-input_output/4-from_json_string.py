#!/usr/bin/python3
"""Get the python data structure object
    out of aJSON string.
"""


from json import loads


def from_json_string(my_str):
    """Get the python data structure object
    out of <my_str> JSON string.

        Args:
            my_str: The Json string

        Return: Isn't it obvious yet!, ha??
    """
    return loads(my_str)
