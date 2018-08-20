import sqlite3 as sql
from .user import User

db_path = '/Users/melanieguido/.dev/running_data_parser/database/rundata.db'

# Add new user
def add_user_to_db(user):
    # Open db connection
    with sql.connect(db_path) as conn:
        curr = conn.cursor()
        curr.execute("INSERT INTO users VALUES(NULL, ?, ?)", (user.email, user.sign_up_date))

# List all users
def list_users():
    # Open db connection
    with sql.connect(db_path) as conn:
        curr = conn.cursor()
        users = curr.execute("SELECT * FROM users")
        for row in users:
            print(row)

# Add new run
def add_run_to_db(run):
    # Connect to database
    conn = sql.connect(db_path)
    # Insert a new run
    conn.execute("INSERT INTO runs VALUES (NULL, ?, ?, ?, ?, ?)", (run.date, run.distance, run.time, run.user_id, run.shoe_id))
    # Save (commit) the changes
    conn.commit()
    # Close connection
    conn.close()

# List runs for user
def list_runs_for_user(id):
    # Connect to database
    conn = sql.connect(db_path)
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM runs WHERE user_id = ?', (id,))
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()

# List all runs
def list_all_runs():
    # Connect to database
    conn = sql.connect(db_path)
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM runs')
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()


# Add shoe
def add_shoe_to_db(shoe):
    # Connect to database
    conn = sql.connect(db_path)
    # Insert run
    conn.execute('INSERT INTO shoes VALUES (NULL, ?, ?, ?, ?)', (shoe.name, shoe.total_miles, shoe.target_miles, shoe.user_id))
    # Save changes
    conn.commit()
    # Close connection
    conn.close()

# List shoes for user
def list_shoe_for_user(id):
    # Connect to database
    conn = sql.connect(db_path)
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM shoes WHERE user_id = ?', (id,))
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()

# List all shoes
def list_all_shoes():
    # Connect to database
    conn = sql.connect(db_path)
    # Get all runs for this user id
    runs = conn.execute('SELECT * FROM shoes')
    # Print runs
    for row in runs:
        print(row)
    # Close connection
    conn.close()