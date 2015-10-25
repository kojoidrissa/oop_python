#!/usr/bin/python2.7

class MaxSizeList(object):
    '''
    MaxSizeList(int) --> object containing a list with a maximum length
    of int
    '''
    def __init__(self, size):
        self.max_size = size
        self.inner_struct = []

    def push(self, item):
        ''' Appends an item to the list in the object'''
        self.inner_struct.append(item)
        if len(self.inner_struct) > self.max_size:
            self.inner_struct.pop(0)

    def get_list(self):
        '''returns the list'''
        return self.inner_struct
