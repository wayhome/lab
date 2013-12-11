#!/usr/bin/env python
# encoding: utf-8


class IterCLS(object):

    def __init__(self, driver):
        self._driver = driver

    def __iter__(self):
        for i in range(10):
            yield self._driver.print_num(i)


class FooDriver(object):

    @classmethod
    def print_num(cls, num):
        print "hello: ", num
        return num+1

if __name__ == '__main__':
    iter_obj = iter(IterCLS(FooDriver))
    print iter_obj.next()
