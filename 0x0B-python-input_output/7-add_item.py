#!/usr/bin/python3
"""Add all the arguments to a list and save it to a json file
    WITHOUT OVERWRITING THE OBEJCTS IN THE LIST IF THE FILE EXISTS ALREADY
"""


from sys import argv
from os.path import exists
from json import load, dump


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


def load_from_json_file(filename):
    """Load a python data structure object a json <filename>.

        Args:
            filename: Pathname/name of the file.

        Return: A python data structure object.
    """
    with open(filename) as f:
        return load(f)


file_name = "add_item.json"
objects_list = []

if exists(file_name):
    old_objects = load_from_json_file(file_name)
    objects_list += old_objects

objects_list += [argv[i] for i in range(1, len(argv))]
save_to_json_file(objects_list, file_name)
