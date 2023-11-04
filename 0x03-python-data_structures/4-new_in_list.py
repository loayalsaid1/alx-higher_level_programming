#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()

    if idx >= len(my_list) or idx < 0:
        pass
    else:
        copy[idx] = element

    return copy
