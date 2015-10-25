#!/usr/bin/python2.7

class MaxSizeList(object):
    '''
    MaxSizeList(int) --> object containing a list with a maximum length
    of int
    '''
    def __init__(self, size):
        self.maxlen = size
        self.struct = []

    def push(self, item):
        ''' Appends an item to the list in the object'''
        self.struct.append(item)
        if len(self.struct) > self.maxlen:
            self.struct.pop(0)

    def get_list(self):
        '''returns the list'''
        return self.struct