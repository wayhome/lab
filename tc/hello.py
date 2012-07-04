#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from tasks import add

define("port", type=int, default=9999, help="server port")


class SyncHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("Hello, %s" % add(3, 4))


class AsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.apply(add, 3, 4)

    def apply(self, method, *args, **kwargs):
        res = method.delay(*args, **kwargs)
        self.wait_for_result(res, self.reply)

    def wait_for_result(self, res, callback, t=10):
        if t > 0:
            if res.ready():
                callback(res.result)
            else:
                tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 0.1,
                        lambda: self.wait_for_result(res, callback, t - 0.1))
        else:
            callback(None)

    def reply(self, result):
        self.finish("Hello, %s" % result)


application = tornado.web.Application([
    (r"/sync", SyncHandler),
    (r"/async", AsyncHandler),
])

if __name__ == "__main__":
    parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
