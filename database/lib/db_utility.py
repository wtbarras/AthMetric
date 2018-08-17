import sqlite3 as sql
import objects/user.py

# Add new user
def addUserToDb(User user):
    # Open db connection
    with sqlite3.connect("rundata.db") as conn:
        curr = conn.cursor()
        curr.execute("INSERT INTO users VALUES(0, 'tigerbarras@gmail.com', '1-1-11')")

# Adds a new run to DB
def addRunToDb():
    # Connect to database
    conn = sql.connect('rundata.db')
    # Insert a new run(currently just dummy data)
    conn.execute("INSERT INTO runs VALUES (0, '2018-1-1', 1.1, '1:1:11', 0)")
    # Save (commit) the changes
    conn.commit()
    # Close connection
    conn.close()

def getRunsForUser(id):
    # Connect to database
    conn = sql.connect('rundata.db')
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM runs WHERE id = ?', (id,))
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()