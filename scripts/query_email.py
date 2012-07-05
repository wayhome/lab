#!/usr/bin/python
# -*- coding: utf-8 -*-

import settings
from sqlalchemy import create_engine

from email_validation import validate_email


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
    with file("/tmp/invalid_email.txt", "w") as f:
        for row in resultset.fetchall():
            if validate_email(row.email):
                continue
            print row.id, row.email.encode("utf8")
            f.write("{0},{1}\n".format(row.id, row.email.encode("utf8")))
            

if __name__ == '__main__':
    main()
