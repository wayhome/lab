#!/usr/bin/python
# -*- coding: utf-8 -*-

import DNS, smtplib

DNS.DiscoverNameServers()

def main(hostname):
    mx_hosts = DNS.mxlookup(hostname)
    print mx_hosts

if __name__ == '__main__':
    import sys
    main(sys.argv[1])

