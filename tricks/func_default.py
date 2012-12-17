#!/usr/bin/python
# -*- coding: utf-8 -*-
#  http://ph.in.zhihu.com/w/style_guide/#default-argument-values
import time


def report(when=time.time()):
    print when

report()
time.sleep(2)
report()


def func(data=[]):
    data.append(1)
    return data

print func()
print func()
print func()


def func2(data={}):
    data[time.time()] = time.time()
    return data

print func2()
print func2()
print func2()
