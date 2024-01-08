#!/usr/bin/python3
''' CHECK IF AN OBJECT INHERITES FROM A CLASS OR NOT'''


def inherits_from(obj, a_class):
    '''CHECK IF AN OBJECT'CLASS INHERITS FROM A CLASS DIRECTLY OF NOT'''
    obj_type = type(obj)
    if obj_type is a_class:
        return False

    return issubclass(obj_type, a_class)
