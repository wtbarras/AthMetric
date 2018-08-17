import sqlite3

def addRunToDb():
    # Connect to database
    conn = sqlite3.connect('rundata.db')
    # Insert a new run(currently just dummy data)
    conn.execute("INSERT INTO runs VALUES (0, '2018-1-1', 1.1, '1:1:11', 0)")
    # Save (commit) the changes
    conn.commit()
    # Close connection
    conn.close()