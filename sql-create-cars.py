# Homework 6.2.1

# Create database called "cars", and add a table called "inventory" that includes the following fields: "Make", "Model", and "Quantity".  Don't forget to include the proper data types.

# import the sqlite3 library
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)""")

