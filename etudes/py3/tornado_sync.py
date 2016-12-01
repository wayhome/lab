#!/usr/bin/env python
# encoding: utf-8
from tornado.httpclient import HTTPClient

def sychronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

if __name__ == '__main__':
    url = 'http://www.zhihu.com'
    print(sychronous_fetch(url)[:10])
