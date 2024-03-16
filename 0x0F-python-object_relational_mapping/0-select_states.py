#!/usr/bin/python3
"""Connect to a database and query the states from
table <states>"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306
                         )
    cursor = db.cursor()

    query = 'SELECT * FROM states ORDER BY states.id'

    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
