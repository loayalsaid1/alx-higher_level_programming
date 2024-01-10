#!/usr/bin/python3
"""Dump a JSON representation of an object to a file"""


from json import dump


def save_to_json_file(my_obj, filename):
    """Dump a JSON representation of <my_obj>
        to <filename>.

        Args:
            my_obj: The python object.
            filename: Pathname/name of the file.

        Return: None
    """
    with open(filename, 'w') as f:
        dump(my_obj, f)
