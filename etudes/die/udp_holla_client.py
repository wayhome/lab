#!/usr/bin/env python
# encoding: utf-8
import diesel


class HollaClient(diesel.UDPClient):
    @diesel.call
    def holla(self, message):
        diesel.send(message + '\r\n')
        evt, data = diesel.first(sleep=5, datagram=True)
        if evt == 'sleep':
            data = 'nothing :-('
        return data.strip()

if __name__ == '__main__':
    def demo():
        client = HollaClient('localhost', 1234)
        with client:
            while True:
                msg = raw_input('message> ')
                print "reply> %s" % client.holla(msg)

    diesel.quickstart(demo)
