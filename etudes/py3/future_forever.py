#!/usr/bin/env python
# encoding: utf-8
import asyncio

@asyncio.coroutine
def slow_operation(future):
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')


def got_result(future):
    print(future.result())
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.Task(slow_operation(future))
future.add_done_callback(got_result)
try:
    loop.run_forever()
finally:
    loop.close()
