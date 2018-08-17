import sqlite3

# Before running this script, you need to create the rundate db
#   > sqlite3 rundate.db

# Open db connection
with sqlite3.connect("rundata.db") as conn:
    curr = conn.cursor()

    # Create table for users
    curr.execute("CREATE TABLE IF NOT EXISTS users ( \
        user_id integer PRIMARY KEY, \
        email varchar(255), \
        sign_up_date varchar(255) \
    );")

    # Create table for runs
    curr.execute("CREATE TABLE IF NOT EXISTS runs ( \
        run_id integer PRIMARY KEY, \
        date varchar(255), \
        distance real, \
        time varchar(255), \
        user_id integer, \
        shoe_id integer, \
        FOREIGN KEY (user_id) REFERENCES users (user_id), \
        FOREIGN KEY (shoe_id) REFERENCES shoes (shoe_id) \
    );")

    # Create table for shoes
    curr.execute("CREATE TABLE IF NOT EXISTS shoes (\
        shoe_id integer PRIMARY KEY, \
        name varchar(255), \
        total_miles real, \
        target_miles real \
    );")