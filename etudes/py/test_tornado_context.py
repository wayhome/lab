#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gunicorn -k gevent test_tornado_context
"""
import tornado.ioloop
import tornado.web
import tornado.wsgi
from tornado import gen
from tornado.stack_context import StackContextInconsistentError, _state


class LocalContext(object):

    def __init__(self):
        self.active = True

    def __enter__(self):
        self.old_contexts = _state.contexts
        self.new_contexts = (self.old_contexts[0], self)
        _state.contexts = self.new_contexts
        return self

    def __exit__(self, type, value, traceback):
        self.active = False
        final_contexts = _state.contexts
        _state.contexts = self.old_contexts

        if final_contexts is not self.new_contexts:
            raise StackContextInconsistentError(
                'stack_context inconsistency (may be caused by yield '
                'within a "with StackContext" block)')

        self.new_contexts = None

    @classmethod
    def current(cls):
        for ctx in reversed(_state.contexts):
            if isinstance(ctx, cls) and ctx.active:
                return ctx


def get_name():
    context = LocalContext.current()
    return context.name


class BaseHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def _execute(self, transforms, *args, **kwargs):
        with LocalContext():
            return super(BaseHandler, self)._execute(transforms, *args, **kwargs)


class MainHandler(BaseHandler):

    def get(self, name):
        context = LocalContext.current()
        context.name = name
        return self.write("Hello, " + get_name())

application = tornado.web.Application([
    (r"/(.*)", MainHandler),
])
application = tornado.wsgi.WSGIAdapter(application)
