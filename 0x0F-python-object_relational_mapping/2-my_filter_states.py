#!/usr/bin/python3

"""Return state from argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; filter names starting with 'N'
    cursor = db.cursor()
    query = """SELECT * FROM states WHERE name LIKE '{:s}'""".format(argv[4])
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
