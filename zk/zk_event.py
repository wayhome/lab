#!/usr/bin/env python
# encoding: utf-8
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.client import KeeperState
from tornado.ioloop import IOLoop

zk = KazooClient(hosts='127.0.0.1:2181', read_only=True)


@zk.add_listener
def my_listener(state):
    if state == KazooState.LOST:
        # Register somewhere that the session was lost
        print "zk lost "
    elif state == KazooState.SUSPENDED:
        # Handle being disconnected from Zookeeper
        print "zk supspended"
    elif state == KazooState.CONNECTED:
        # Handle being connected/reconnected to Zookeeper
        print zk.client_state
        if zk.client_state == KeeperState.CONNECTED_RO:
            print("Read only mode!")
        else:
            print("Read/Write mode!")
    else:
        print "unkown state: {0}".format(state)


@zk.ChildrenWatch("/my/favorite/node")
def watch_children(children):
    print("Children are now: %s" % children)


@zk.DataWatch("/my/favorite")
def watch_node(data, stat):
    print("Watch Version: %s, data: %s" % (stat.version, data.decode("utf-8")))


def main():
    if not zk.exists("/my/favorite"):
        print "create path: /my/favorite"
        zk.ensure_path("/my/favorite")
        zk.create("/my/favorite/node", "a value")

    data, stat = zk.get("/my/favorite")
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    # List the children
    children = zk.get_children("/my/favorite")
    print("There are %s children with names %s" % (len(children), children))

    zk.set("/my/favorite", "some data")

    #zk.delete("/my/favorite/node", recursive=True)
    #zk.delete("/my/favorite", recursive=True)


if __name__ == '__main__':
    #zk = KazooClient(hosts='127.0.0.1:2181')
    #zk.add_listener(my_listener)
    zk.start()
    main()
    ioloop = IOLoop()
    ioloop.start()
