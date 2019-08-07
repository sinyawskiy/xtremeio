#! /usr/bin/python
# -*- coding: utf-8 -*-
from model import Frog, Lamps

if __name__ == '__main__':

    for i in xrange(10):
        frog = Frog(i+1)
        frog.jump()
        frog.jump()
        frog.jump()

    frog = Frog(100)
    frog.jump()
    frog.jump()

    lamps = Lamps()
    frogs = [Frog(i, lamps) for i in range(1,22,7)]

    for frog in frogs:
        frog.jump()

    print u'%s' % lamps