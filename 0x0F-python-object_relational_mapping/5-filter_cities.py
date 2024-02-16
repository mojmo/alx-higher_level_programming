#!/usr/bin/python3

"""
Script to fetch and print names of cities in a specified state from the
database hbtn_0e_4_usa (case-sensitive).

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
    cur.execute("""SELECT cities.`name`
                FROM `cities`
                    INNER JOIN `states`
                    ON cities.`state_id` = states.`id`
                WHERE BINARY states.`name` = %s
                ORDER BY cities.`id` ASC""", (argv[4],))

    for row in cur.fetchall():
        print(row[0], end=", ")
    print()

    cur.close()
    conn.close()
