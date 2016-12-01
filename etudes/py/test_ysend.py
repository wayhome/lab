#!/usr/bin/env python
# encoding: utf-8


def consumer():
    while True:
        v = yield
        print v
        if v == 11:
            raise Exception


def producer():
    c = consumer()
    c.send(None)
    for i in range(10):
        c.send(i)
    c.send(None)
    c.send(2)
    c.send(None)
    try:
        for i in range(1, 12):
            c.send(i)
    except Exception as e:
        print e
    c.send(None)


if __name__ == '__main__':
    producer()
