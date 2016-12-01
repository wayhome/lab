#!/usr/bin/env python
# coding: utf-8

import sys
import thread
import threading
import time
import weakref
import gc
import gevent


class A(object):
    def __init__(self):
        self.x = 2


b = weakref.WeakKeyDictionary()


def current_thread_id(ref):
    global b
    greenlet = sys.modules.get('greenlet')
    if greenlet:
        print "has greenlet"
        current = greenlet.getcurrent()
        if current is not None and current.parent:
            b[current] = ref
            print "set"
            return id(current)
    c = threading.current_thread()
    b[c] = ref
    print "set"
    return thread.get_ident()


def greenlet_func():
    trace_id = A()
    i = current_thread_id(trace_id)
    gevent.sleep(0.2)

g = gevent.spawn(greenlet_func)
#g = threading.Thread(target=greenlet_func)
#g.start()
gevent.sleep(0.1)
print "values: ", b.values()
# g.join()
g = None
gevent.sleep(0.1)
gc.collect()
print "values: ", b.values()
print "cited: ", gc.get_referrers(b.values())
print "cite:", gc.get_referents(b.values())
