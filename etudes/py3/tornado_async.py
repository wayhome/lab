#!/usr/bin/env python
# encoding: utf-8
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

def async_fetch(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(lambda f: my_future.set_result(f.result()))
    return my_future

if __name__ == '__main__':
    url = 'http://www.zhihu.com'
    IOLoop.instance().run_sync(lambda:print(async_fetch(url).result()))
