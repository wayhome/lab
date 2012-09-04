#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from unitbench import Benchmark

from redis import Redis

client = Redis(host='localhost', port=6379)

class RedisBenchmark(Benchmark):

    def setup(self):
        self.cur_time = int(time.time())

    def warmup(self):
        return 0

    def input(self):
        for i in range(10):
            yield i

    def bench_zad(self, input):
        i=1
        while i < 150000:
            key = "feedlist:{0}".format(i)
            i = i+1
            client.zadd(key, 1232444, self.cur_time)


if __name__ == "__main__":
    RedisBenchmark().run()
