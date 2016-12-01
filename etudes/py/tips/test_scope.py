#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = 10


def test(x=None):
    def test2():
        return x + 2
    return test2()


def foo():
    return x + 1


def bar():
    global x
    x = x + 1
    return x

if __name__ == "__main__":
    print test(5)
    print foo()
    print bar()
