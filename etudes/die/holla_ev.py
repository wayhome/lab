#!/usr/bin/env python
# encoding: utf-8
from diesel import quickstart, sleep, quickstop
from diesel.util.event import Event


def coordinator():
    # Pretend to do something ...
    sleep(3)

    # Done, fire the event.
    print "Coordinator done."
    ev.set()


def consumer():
    print "Waiting ..."
    ev.wait()
    print "The event was triggered!"


def late_consumer():
    sleep(4)
    consumer()
    quickstop()

ev = Event()

quickstart(coordinator, consumer, consumer, consumer, late_consumer)
