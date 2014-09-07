# Insert Commands

# import the sqlite3 library
import sqlite3

################################################

# connect to existing database or create a new database if the database doesn't exist
##conn = sqlite3.connect("new.db")
##
### to create a database in memory only (no file associated), will delete after connection close
####conn = sqlite3.connect(":memory:")
##
### get a cursor object used to execute SQL commands
##cursor = conn.cursor()
##
### create a table
##cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
##cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
##
### commit the changes, without this statement the changes only persist in memory
##conn.commit()
##
### close the database connection
##conn.close()

###############################################

# to avoid using commit() and to update automatically
##with sqlite3.connect("new.db") as connection:
##    c = connection.cursor()
##    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
##    c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
##
### close the database connection
##c.close()

#################################################

# executemany() method
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 2700000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 1500000)
    ]

    # insert data into table (? acts as placeholder(parameterized statements), avoids %s string substitutions which could cause dangerous SQL injection)
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

# close the database connection
c.close()
