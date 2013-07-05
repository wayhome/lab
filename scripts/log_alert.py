#!/usr/bin/env python
# encoding: utf-8
import logging

logging.ALERT = 35
logging.addLevelName(logging.ALERT, 'ALERT')


def alert(self, message, *args, **kwargs):
    self.log(logging.ALERT, message, *args, **kwargs)

logging.Logger.alert = alert

if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger("zhihu")
    logger.alert("hello")
