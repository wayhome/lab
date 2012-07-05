#!/usr/bin/python
# -*- coding: utf-8 -*-
DB_URI = "mysql://zhihu:zhihu@127.0.0.1/zhihu?charset=utf8"
custom_domains = []

try:
    from local_settings import *
except Exception, e:
    raise e
