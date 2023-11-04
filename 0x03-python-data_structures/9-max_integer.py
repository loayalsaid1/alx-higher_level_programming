#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        copy = my_list.copy()
        copy.sort()
        copy.reverse()
        return copy[0]
    else:
        return None
