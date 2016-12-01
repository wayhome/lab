# -*- coding: utf-8 -*-
import time
import logging

import tornado.ioloop
import tornado.web
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, url):
        full_url = 'http://www.google.com' + self.request.uri
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(full_url, callback=self.download_gr)

    def download_gr(self, response):
        if response.error:
            self.write(str(response.code))
        else:
            self.write(response.body)
        self.finish()

application = tornado.web.Application([
    (r"/main/(.*)", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
