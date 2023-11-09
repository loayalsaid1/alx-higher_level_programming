#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return None
    d = a_dictionary
    to_delete = list(filter(lambda key: d[key] == value, d.keys()))
    for key in to_delete:
        del d[key]
    return d
