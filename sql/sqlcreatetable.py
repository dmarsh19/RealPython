# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# to create a database in memory only (no file associated), will delete after connection close
##conn = sqlite3.connect(":memory:")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

# close the database connection
conn.close()
