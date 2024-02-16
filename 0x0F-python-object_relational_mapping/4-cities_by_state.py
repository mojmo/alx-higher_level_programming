#!/usr/bin/python3

"""
Script to fetch and print information about cities and their corresponding
tates from the database hbtn_0e_4_usa.

Usage: ./script_name.py mysql_username mysql_password database_name
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
    cur.execute("""SELECT cities.`id` , cities.`name`, states.`name`
                FROM `cities`
                    INNER JOIN `states`
                    ON cities.`state_id` = states.`id`
                ORDER BY cities.`id` ASC""")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
