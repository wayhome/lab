#!/usr/bin/env python
# encoding: utf-8
import os
import process


def my_fork():
    child_pid = os.fork()
    if child_pid == 0:
        print "child process: %s" % os.getpid()
        print "envionment: %s" % os.environ["PATH"]
        r = process.run("./test.sh")
        r.wait()
        print "subprocess envionment: %s" % r.stdout
    else:
        print "parent process: %s" % os.getpid()
        print "envionment: %s" % os.environ["PATH"]


if __name__ == '__main__':
    my_fork()
