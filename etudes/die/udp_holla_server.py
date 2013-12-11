#!/usr/bin/env python
# encoding: utf-8
import diesel


def holla_back():
    while True:
        message = diesel.receive(diesel.datagram)
        shouted_message = message.upper()
        diesel.send(shouted_message)

diesel.quickstart(diesel.UDPService(holla_back, 1234))
