#!/usr/bin/python2.7

class MyNum(object):
    #__init__ constructor "sets up" each instance of an object, to ensure
    #it's prepared to perform it's function 
    def __init__(self):
        print 'calling __init__'
        self.val = 0

    def increment(self):
        self.val = self.val +1

dd = MyNum()
dd.increment()
dd.increment()
print dd.val

print
