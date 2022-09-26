import sqlite3
from sqlite3 import Error
database=""
def create_connection(db_file):
    conn = None
    try:
        database = r" g:/pythonaugust22/trail_prog/sqlitedatabase/pythonsqlite.db"
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("not connected")
    return conn

conn = create_connection(database)

if conn is not None:
    print("connected successfully")

else:
    print("Error! cannot create the database connection.")

