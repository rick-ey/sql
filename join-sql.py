# JOINing data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:

    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT DISTINCT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city""")

    rows = c.fetchall()

    for r in rows:
        print("City: {}".format(r[0]))
        print("Population: {}".format(str(r[1])))
        print("Region: {}".format(r[2]))
        print()
