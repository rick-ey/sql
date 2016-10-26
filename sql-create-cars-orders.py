# Add another table to accompany your “inventory” table called “orders”. This table should have the following fields: “make”, “model”, and “order_date”. Make sure to only include makes and models for the cars found in the inventory table. Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD).

# Finally output the car’s make and model on one line, the quantity on another line, and then the order_dates on subsequent lines below that.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # CREATE the orders table
    c.execute("""CREATE TABLE orders('make' TEXT, 'model' TEXT, 'order_date' DATE)""")

    # INSERT records to orders table
    car_orders = [
                ('Ford', 'Escape', '2016-10-30'),
                ('Ford', 'Escape', '2016-11-30'),
                ('Ford', 'Escape', '2016-12-30'),
                ('Honda', 'Civic', '2016-10-30'),
                ('Honda', 'Civic', '2016-11-30'),
                ('Honda', 'Civic', '2016-12-30'),
                ('Ford', 'Mustang', '2016-10-30'),
                ('Ford', 'Mustang', '2016-11-30'),
                ('Ford', 'Mustang', '2016-12-30'),
                ('Honda', 'Accord', '2016-10-30'),
                ('Honda', 'Accord', '2016-11-30'),
                ('Honda', 'Accord', '2016-12-30'),
                ('Ford', 'F150', '2016-10-30'),
                ('Ford', 'F150', '2016-11-30'),
                ('Ford', 'F150', '2016-12-30')
                 ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", car_orders)




