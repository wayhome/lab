#!/usr/bin/env python
# encoding: utf-8
import time
from tornado import gen
from tornado.ioloop import IOLoop


@gen.coroutine
def delayed_msg(seconds, msg):
    yield gen.Task(IOLoop.current().call_later,
                   seconds)
    raise gen.Return(msg)


if __name__ == '__main__':
    @gen.coroutine
    def f():
        start = time.time()
        future1 = delayed_msg(2, '2')
        future2 = delayed_msg(3, '3')
        future3 = delayed_msg(1, '1')
        results = yield [future1, future2, future3]
        end = time.time()
        print "finished in %.1f sec: %r" % (end - start, results)

    IOLoop.current().run_sync(f)
