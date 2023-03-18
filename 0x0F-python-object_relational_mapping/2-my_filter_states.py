#!/usr/bin/python3
"""
Access to the database and get the states
from the database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE '{}'\
                 ORDER BY states.id".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
