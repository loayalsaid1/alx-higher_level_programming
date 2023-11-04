#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        pass
    else:
        item = my_list[idx]
        my_list.remove(item)
    return my_list
