from asyncio import coroutine, get_event_loop, async



@coroutine
def func0():
    a = yield from func1()


@coroutine
def func1():
    b = yield from func2()
    return b


@coroutine
def func2():
    c = yield from func3()
    return c

@coroutine
def func3():
    raise KeyError('hehe')


ioloop = get_event_loop()

f = async(func0())
ioloop.run_until_complete(f)
