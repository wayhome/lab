from tornado.gen import Return, coroutine
from tornado.ioloop import IOLoop


@coroutine
def func0():
    a = yield func1()
    raise Return(a)


@coroutine
def func1():
    b = yield func2()
    raise Return(b)


@coroutine
def func2():
    c = yield func3()
    raise Return(c)


@coroutine
def func3():
    raise KeyError('hehe')


IOLoop.current().run_sync(func0)
