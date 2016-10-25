# Create an SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database does not exist
conn = sqlite3.connect("new.db")

# get cursur object used to execute sql commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

# close the database connection
conn.close()
