#!/usr/bin/python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from tasks import add
from mixin import AsyncMixin

define("port", type=int, default=9999, help="server port")


class SyncHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("Hello, %s" % add(3, 4))


class AsyncHandler(tornado.web.RequestHandler, AsyncMixin):

    @tornado.web.asynchronous
    def get(self):
        self.apply(add, 3, 4)

    def reply(self, result):
        self.finish("Hello, %s" % result)

class MyHandler(tornado.web.RequestHandler):
    @asynchronous
    @gen.engine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield gen.Task(http_client.fetch, "http://zhihu.com")
        stuff = do_something(response)
        self.render("template.html", **stuff)


application = tornado.web.Application([
    (r"/sync", SyncHandler),
    (r"/async", AsyncHandler),
])

if __name__ == "__main__":
    parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
