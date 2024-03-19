#!/usr/bin/python3
"""Query All the cities in a state provided by the user"""


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

    query = """SELECT c.name
                FROM cities as c INNER JOIN states as s
                ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id"""

    cur.execute(query, (argv[4], ))
    result = cur.fetchall()
    print(", ".join([row[0] for row in result]))

    cur.close()
    db.close()
