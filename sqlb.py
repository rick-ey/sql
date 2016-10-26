# Create an SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database does not exist
conn = sqlite3.connect("new.db")

# get cursur object used to execute sql commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
