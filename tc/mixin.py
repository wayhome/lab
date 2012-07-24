#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import tornado


class AsyncMixin(object):

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
        raise NotImplemented
