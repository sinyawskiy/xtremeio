#! /usr/bin/python
# -*- coding: utf-8 -*-

class FrogException(Exception):
    pass

class Lamp(object):
    def __init__(self, i):
        self.i = i
        self.on = False

    def switch(self):
        self.on = not self.on
        print u'%s' % self

    def __unicode__(self):
        return u'Lamp №%(i)d switch %(status)s' % {
            'i': (self.i+1),
            'status': u'on' if self.on else u'off'
        }

class Lamps(object):
    def __init__(self):
        self.lamps = [Lamp(i) for i in xrange(100)]

    # turn on or turn off
    def press(self, i):
        self.lamps[i].switch()

    def __len__(self):
        return len(self.lamps)

    def __unicode__(self):
        return u'\n'.join(u'%s' % lamp for lamp in self.lamps)

class Frog(object):
    def __init__(self, number, lamps=None):
        if not lamps:
            lamps = Lamps()
        self.lamps = lamps
        if number < 1 or number > len(lamps):
            raise FrogException(u'Frog number should be greater then 0 or lower then equal number of lamps')
        self.number = number
        self.target = self.target_lamp()
        print u'Frog №%d init' % number

    def target_lamp(self):
        target = self.number-1
        while True:
            yield target
            target += self.number
            if target > len(self.lamps):
                return

    def jump(self):
        print u'Frog №%d jump' % self.number
        try:
            self.lamps.press(self.target.next())
        except StopIteration:
            print u'Frog №%d hasn\'t lamp to press' % self.number