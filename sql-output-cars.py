# Finally output only records that are for Ford vehicles.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT make, model, quantity FROM inventory WHERE make='Ford'")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
