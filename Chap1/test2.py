#!/usr/bin/python2.7

class Joe(object):
    def callme(self):
        print('calling "callme" method with instance: ')
        print(self)


KoJoe = Joe()
KoJoe.callme()
print KoJoe