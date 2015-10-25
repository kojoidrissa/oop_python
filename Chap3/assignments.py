#!/usr/bin/python2.7

class MaxSizeList(object):
    def __init__(self, size):
        self.maxlen = size
        self.struct = []

    def push(self, item):
        self.struct.append(item)
        if len(self.struct) > self.maxlen:
            self.struct.pop(0)

    def get_list(self):
        return self.struct