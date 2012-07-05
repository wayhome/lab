#!/usr/bin/python
# -*- coding: utf-8 -*-
import settings

import re
import time
import DNS

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r')@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$)'  # domain
    r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$', re.IGNORECASE)  # literal form, ipv4 address (SMTP 4.1.3)

normal_domains = ['qq.com',
                 'vip.qq.com',
                 'gmail.com',
                 '163.com',
                 '126.com',
                 'vip.sina.com',
                 'sina.com',
                 'sina.cn',
                 'hotmail.com',
                 'live.com',
                 'yahoo.com',
                 'yahoo.cn',
                 'ymail.com',
                 '189.cn',
                 'wo.com.cn',
                 'sohu.com',
                 'sohu-inc.com',
                 '139.com',
                 'staff.139.com',
                 'chuangxin.com',
                 'tianya.cn',
                 'infoq.com',
                 'ericsson.com',
                 'vip.sohu.net',
                 'pplive.com',
                 'aliyun-inc.com',
                 'umeng.com',
                 'dnspod.com',
                 '115.com',
                 'zhihu.com',
                 'v2ex.com',
                 'me.com',
                 'qiyi.com',
                 'tudou.com',
                 'alipay.com',
        ]

# custom for zhihu
custom_domains = settings.custom_domains
mx_records = {}

DNS.DiscoverNameServers()


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    """Retry decorator
    original from http://wiki.python.org/moin/PythonDecoratorLibrary#Retry
    """
    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            try_one_last_time = True
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                    try_one_last_time = False
                    break
                except ExceptionToCheck, e:
                    print args, kwargs
                    print "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            if try_one_last_time:
                return args  # 如果始终超时，把当前domain作为mx记录返回
            return
        return f_retry  # true decorator
    return deco_retry


@retry(Exception)
def query_mx(domain):
    if domain not in mx_records:
        mx_hosts = DNS.mxlookup(domain)
        mx_records[domain] = mx_hosts
        if not mx_hosts:
            print "invalid domain: ", domain
    return mx_records[domain]


def validate_email(email):
    if not email_re.match(email):
        return False
    else:
        domain = email.split("@")[1]
        if domain in normal_domains:
            return True
        if domain in custom_domains:
            return True
        return bool(query_mx(domain))
