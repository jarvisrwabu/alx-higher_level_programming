#!/usr/bin/python3
"""Connect to a MySQL server using the module MySQLdb."""

import MySQLdb
import sys
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
