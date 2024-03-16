#!/usr/bin/python3
"""Query All the cities in the database, printing the city and it's state"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1],
                         host='localhost',
                         passwd=argv[2],
                         db=argv[3],
                         port=3306
                         )
    cur = db.cursor()

    query = """SELECT c.id, c.name, s.name
                FROM cities as c INNER JOIN states as s
                ON c.state_id = s.id
                ORDER BY c.id"""

    cur.execute(query)
    for row in cur.fetchall():
        print(row)
