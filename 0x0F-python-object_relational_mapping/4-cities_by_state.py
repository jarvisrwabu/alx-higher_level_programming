#!/usr/bin/python3

"""List all cities from a database."""

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
               LEFT JOIN states ON cities.state_id = states.id"""
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
