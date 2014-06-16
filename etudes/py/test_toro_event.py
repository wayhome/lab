# -*- coding: utf-8 -*-
from tornado import ioloop, gen
import toro

event = toro.Event()


@gen.coroutine
def waiter():
    print "I'll wait right here"
    yield event.wait()
    print "i'm done waiting"


@gen.coroutine
def setter():
    print "Abount to set"
    event.set()
    print "Done setting"

waiter()
setter()
loop = ioloop.IOLoop.current()
loop.start()
