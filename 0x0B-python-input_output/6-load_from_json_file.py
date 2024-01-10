#!/usr/bin/python3
"""Load a python data structure object from a json file"""

from json import load


def load_from_json_file(filename):
    """Load a python data structure object a json <filename>.

        Args:
            filename: Pathname/name of the file.

        Return: A python data structure object.
    """
    with open(filename) as f:
        return load(f)
