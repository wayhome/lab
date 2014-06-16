#!/usr/bin/env python
# encoding: utf-8
import asyncio

@asyncio.coroutine
def slow_operation(future):
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.Task(slow_operation(future))
loop.run_until_complete(future)
#loop.run_until_complete(slow_operation(future))
print(future.result())
loop.close()
