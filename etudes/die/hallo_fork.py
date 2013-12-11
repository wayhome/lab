#!/usr/bin/env python
# encoding: utf-8
from diesel import quickstart, fork, sleep, quickstop


def main():
    was_dispatched = dispatch('x')
    print "Dispatched:", was_dispatched


def dispatch(v):
    fork(work_on, v)
    return True


def work_on(v):
    sleep(2)
    print "Done working on %r" % v
    quickstop()

quickstart(main)
