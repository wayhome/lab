#!/usr/bin/env python
# encoding: utf-8
import asyncio

@asyncio.coroutine
def greet_every_two_seconds():
    while True:
        print('Hello World')
        yield from asyncio.sleep(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(greet_every_two_seconds())
