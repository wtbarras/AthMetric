import sqlite3

# Before running this script, you need to create the rundate db
#   > sqlite3 rundate.db

# Open db connection
with sqlite3.connect("rundata.db") as conn:
    curr = conn.cursor()

    # Create table for users


    # Create table for runs
    curr.execute("CREATE TABLE IF NOT EXISTS runs ( \
        user_id integer PRIMARY KEY, \
        date varchar(255), \
        distance real, \
        time varchar(255), \
        shoe_id integer, \
        FOREIGN KEY (shoe_id) REFERENCES shoes (shoe_id) \
    );")

    # Create table for shoes