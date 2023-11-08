#!/usr/bin/python3
def search_replace(my_list, search, replace):
    map_object = map(lambda x: replace if x == search else x, my_list)
    return list(map_object)
