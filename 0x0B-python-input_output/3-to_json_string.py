#!/usr/bin/python3
"""Get the JSON format of an object"""


from json import dumps


def to_json_string(object):
    """Return JSON format of <object>.

        Args:
            object: The object to get the format of

        Return: Isn't it obvious yet!, ha??
    """
    return dumps(object)
