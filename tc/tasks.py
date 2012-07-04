#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from celery.task import task

@task
def add(x, y):
    time.sleep(1)
    return x+y

