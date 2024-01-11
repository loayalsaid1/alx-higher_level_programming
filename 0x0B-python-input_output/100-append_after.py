#!/usr/bin/python3
"""Function to append a text to a file after existence of curtain text"""


def append_after(filename="", search_string="", new_string=""):
    """Function to append a text to a file after
        existence of curtain text.

        Args:
            filename: Pathname/name of the file.
            search_string: Obvious enough, right?
            new_string: Text to add the next line of the line where
                search_string exists.

            Return: None
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
