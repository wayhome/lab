# -*- coding: utf-8 -*-
from tornado import ioloop, gen
import toro
q = toro.JoinableQueue(maxsize=3)


@gen.coroutine
def producer():
    for item in range(10):
        print 'Sending', item
        yield q.put(item)


@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print '\t\t', 'Got', item
        finally:
            q.task_done()


if __name__ == '__main__':
    producer()
    consumer()
    loop = ioloop.IOLoop.instance()

    def stop(future):
        loop.stop()
        #future.result()  # Raise error if there is one

    # block until all tasks are done
    q.join().add_done_callback(stop)
    loop.start()
