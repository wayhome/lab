#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent.monkey import patch_all
patch_all()  # noqa

import gevent
import kafka
import time
from cfbclient import config

if kafka.__version__ == "0.9.5":
    from kafka import KafkaClient, SimpleProducer
    client = KafkaClient(config.kafka.hosts)
    producer = SimpleProducer(client, async=False)
else:
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=config.kafka.hosts_list)


def produce(num):
    gevent.sleep(1)
    end = 2 * (num + 1)
    for i in range(num, end):
        if kafka.__version__ == "0.9.5":
            producer.send_messages('test-topic', str(i) * 1024)
        else:
            producer.send('test-topic', str(i) * 1024)

    print('finished %s' % i)

start = time.time()
gevent.joinall([gevent.spawn(produce, i) for i in range(100)])
end = time.time()
print("finished all in %ss" % (end - start))
