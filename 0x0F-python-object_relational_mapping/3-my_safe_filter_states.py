#!/usr/bin/python3

"""No Sql injection. More info: https://bobby-tables.com/python."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; filter states with name arg[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
