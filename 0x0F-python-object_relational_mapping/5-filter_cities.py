#!/usr/bin/python3

"""Filter cities from a database."""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; list all cities by state
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               LEFT JOIN states ON cities.state_id = states.id
               WHERE states.name LIKE %s
               ORDER BY cities.id ASC"""
    cursor.execute(query, (argv[4],))
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))
    cursor.close()
    db.close()
