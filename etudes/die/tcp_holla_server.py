#!/usr/bin/env python
# encoding: utf-8
import diesel


def holla_back(addr):
    while True:
        message = diesel.until_eol()
        shouted_message = message.upper()
        diesel.send(shouted_message)

diesel.quickstart(diesel.Service(holla_back, 4321))
