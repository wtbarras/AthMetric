import sqlite3 as sql
from .user import User

db_path = '/Users/melanieguido/.dev/running_data_parser/database/rundata.db'

# Add new user
def add_user_to_db(user):
    # Open db connection
    with sql.connect(db_path) as conn:
        curr = conn.cursor()
        curr.execute("INSERT INTO users VALUES(NULL, 'tigerbarras@gmail.com', '1-1-11')")

def list_users():
    # Open db connection
    with sql.connect(db_path) as conn:
        curr = conn.cursor()
        users = curr.execute("SELECT * FROM users")
        for row in users:
            print(row)

# Adds a new run to DB
def add_run_to_db(run):
    # Connect to database
    conn = sql.connect('rundata.db')
    # Insert a new run(currently just dummy data)
    conn.execute("INSERT INTO runs VALUES (0, '2018-1-1', 1.1, '1:1:11', 0)")
    # Save (commit) the changes
    conn.commit()
    # Close connection
    conn.close()

def list_runs_for_user(id):
    # Connect to database
    conn = sql.connect('rundata.db')
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM runs WHERE id = ?', (id,))
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()