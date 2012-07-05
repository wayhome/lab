#!/usr/bin/python
# -*- coding: utf-8 -*-

import settings
import re
from sqlalchemy import create_engine

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r')@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$)'  # domain
    r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$', re.IGNORECASE)  # literal form, ipv4 address (SMTP 4.1.3)

engine = create_engine(settings.DB_URI,
                    strategy='threadlocal',
                    encoding='utf-8',
            )


def main(filter=None):
    status_mask = 0b110
    subscribe_mask = 0b1
    sql = """
        SELECT id, fullname, email
        FROM member
        WHERE  !(status & %s)
    """
    if filter:
        sql += " AND (email_settings & %s)"
        resultset = engine.execute(sql % (status_mask, subscribe_mask))
    else:
        resultset = engine.execute(sql % status_mask)
    for row in resultset.fetchall():
        if not email_re.match(row.email):
            print row.email


if __name__ == '__main__':
    main()
