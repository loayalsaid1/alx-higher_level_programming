#!/usr/bin/python3
''' INHERIT FROM <LIST> CLASS AND ADD FUNCTIONLITY TO IT'''


class MyList(list):
    '''SUB CLASS OF LIST
    ADD A METHOD TO PRINT A SORTED VERSION OF THE OBJECT'''

    def print_sorted(self):
        ''' PRINT A SORTED VERSION  OF <self>'''
        print((sorted(self)))
