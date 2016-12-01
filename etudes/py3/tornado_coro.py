#!/usr/bin/env python
# encoding: utf-8
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    #return response.body

if __name__ == '__main__':
    url = 'http://www.zhihu.com'
    print(fetch_coroutine(url))
