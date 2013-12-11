#!/usr/bin/env python
# encoding: utf-8
import random

from diesel import quickstart, sleep
from diesel.util.pool import ConnectionPool

from tcp_holla_client import HollaClient


make_client = lambda: HollaClient('localhost', 4321)
close_client = lambda c: c.close()
holla_pool = ConnectionPool(make_client, close_client, pool_size=3)

counter = 0


def actor():
    global counter
    while True:
        sleep(random.random())
        msg = "Message %d" % counter
        counter += 1
        with holla_pool.connection as client:
            print client.holla(msg)

quickstart(actor, actor, actor, actor, actor, actor)
