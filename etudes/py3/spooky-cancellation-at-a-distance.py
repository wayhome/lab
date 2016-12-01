import asyncio
loop = asyncio.get_event_loop()

async def child(name, fut, event):
    print("{} started".format(name))
    try:
        event.set()
        await fut
    except asyncio.CancelledError:
        print("{} cancelled".format(name))

async def main():
    fut = asyncio.Future()

    # Start two tasks, and give them a chance to block on the same future.
    event1 = asyncio.Event()
    task1 = loop.create_task(child("task 1", fut, event1))
    # await event1.wait()

    event2 = asyncio.Event()
    task2 = loop.create_task(child("task 2", fut, event2))
    await event2.wait()

    # Cancel task1...
    task1.cancel()
    # ...then block on task2.
    await task2

loop.run_until_complete(main())
