# Assignment 3a - Add 100 random integers, ranging from 0 to 100, to a new database called newnum.db

# Import libraries

import sqlite3
import random

# Establish connection and create newnum.db

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # Delete database table if it exists
    c.execute("DROP TABLE if exists numbers")

    # Create database table
    c.execute("CREATE TABLE numbers(num int)")

    # User a loop and random to insert 100 values 0 - 100
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))
