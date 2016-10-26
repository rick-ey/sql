# Create an SQLite3 database and table

# executemany() method

# import the sqlite3 library
import sqlite3

# create a new database if the database does not exist
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
             ]

    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

