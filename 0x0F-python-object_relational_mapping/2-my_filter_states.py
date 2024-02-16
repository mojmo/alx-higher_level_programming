#!/usr/bin/python3

"""
Script to fetch and print information about a state from the database
hbtn_0e_0_usa based on the provided state name.

Usage: ./script_name.py mysql_username mysql_password database_name state_name
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
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
    cur.execute("""SELECT *
                FROM `states`
                WHERE BINARY(`name`) = '{}'
                ORDER BY id ASC""".format(argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
