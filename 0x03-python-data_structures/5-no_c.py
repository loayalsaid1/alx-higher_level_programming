#!/usr/bin/python3
def no_c(my_string):
    table = str.maketrans("", "", "Cc")
    return my_string.translate(table)
