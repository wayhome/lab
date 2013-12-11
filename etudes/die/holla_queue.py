#!/usr/bin/env python
# encoding: utf-8
from diesel import sleep, quickstart
from diesel.util.queue import Queue


def producer(queue):
    def _produce():
        for i in xrange(20):
            queue.put('Item %d' % i)
            sleep(0.5)
    return _produce


def consumer(ident, queue):
    def _consume():
        item = queue.get()
        while True:
            item = queue.get()
            print "%s got %s" % (ident, item)
            sleep(1)
    return _consume

q = Queue()
quickstart(producer(q), consumer('A', q), consumer('B', q))
