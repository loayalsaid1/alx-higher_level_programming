#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    cpy = dict(zip(cpy.keys(), map(lambda x: x*2, cpy.values())))
    return cpy
