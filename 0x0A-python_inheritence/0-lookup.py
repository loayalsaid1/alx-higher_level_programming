#!/usr/bin/python3
'''A functoin to print the properties of an object'''
def lookup(obj):
    '''Print the attributes of obj'''
    return list(dir(obj))
