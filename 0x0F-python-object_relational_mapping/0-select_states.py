#!/usr/bin/python3

"""
This script connects to a MySQL database and fetches all records
from a table named 'states'. It requires three command-line
arguments: MySQL username, password, and database name.
"""

import MySQLdb
from sys import argv

if __name__ == 'main':
    # Connect to the MySQL database using the provided credentials
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
