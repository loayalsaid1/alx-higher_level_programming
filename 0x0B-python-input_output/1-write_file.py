#!/usr/bin/python3
"""Write to a file and create it if it does exist"""


def write_file(filename="", text=""):
    """Write to a file.
        Overwrite it incase it's already their.

        Args:
            filename: The name of the file.
            text: The text to insert.

        Return: The number of chars writen.
    """
    with open(filename, "w") as f:
        return f.write(text)
