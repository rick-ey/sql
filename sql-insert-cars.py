# Using the “inventory” table from the previous homework assignment, add (INSERT) 5 records (rows of data) to the table. Make sure 3 of the vehicles are Fords while the other 2 are Hondas. Use any model and quantity for each.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # insert multipel records using a tuple
    cars = [
          ('Ford', 'Escape', 6),
          ('Honda', 'Civic', 3),
          ('Ford', 'Mustang', 11),
          ('Honda', 'Accord', 4),
          ('Ford', 'F150', 21)
           ]

    # insert data into table
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)
