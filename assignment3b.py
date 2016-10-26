# Assignment 3b - Prompt the user whether he or she would like to perform an aggregation (AVG, MAX, MIN, or SUM) or exit the program altogether.

# Import libraries
import sqlite3

# Create the connection object
conn = sqlite3.connect("newnum.db")

# Create a cursor object used to execute SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# Loop until user enters valid operation number
while True:
    # Get user input
    x = input(prompt)

    # If user enters any choice from 1-4
    if x in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

        # retrieve data
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        # fetchone() retrieves one record from the query
        get = cursor.fetchone()

        # output result to screen
        print(operation + ": %f" % get[0])

    # if user enters 5
    elif x == "5":
        print("Exit")

        # exit loop
        break


