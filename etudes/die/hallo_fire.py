#!/usr/bin/env python
# encoding: utf-8
import random

from diesel import quickstart, fire, wait, sleep, quickstop


def pump():
    for i in xrange(5):
        fire('thing')
        print "Fired 'thing'"
        sleep(1)
    quickstop()


def on(event):
    def handle():
        while True:
            wait(event)
            print "Saw %r" % event
            sleep(3 * random.random())
    return handle

quickstart(pump, on('thing'), on('thing'), on('thing'))
