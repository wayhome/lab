#!/usr/bin/env python
# encoding: utf-8
from diesel import quickstart, quickstop, sleep
from diesel.util.event import Countdown

# This "done" event won't be set until it is ticked 3 times.
done = Countdown(3)


def main():
    for i in range(3):
        print "Tick ..."
        sleep(1)
        done.tick()


def stop_when_done():
    done.wait()
    print "Boom!"
    quickstop()

quickstart(main, stop_when_done)
