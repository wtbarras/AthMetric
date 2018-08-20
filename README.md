# running_data_parser
Parses a data on a series of runs and generates informative charts.

The end goal is to create a website and mobile app that can track workouts and provide better data visualisation to athletes to enable evidence based training.

# Set up database
To set up the database, cd into the running_data_parser/database directory and run:

```> sqlite3 rundata.py```

This will create a database called rundata.db in running_data_parser/database.
Next, you will need to run the database setup script:

```> python3 setup_database.py```

The script will set up all the database tables, assuming they do not already exist.

The final step is to copy the full path to the database file and paste it into db_path variable in db_utility.py.

# Tests
Testing will be done with pytest. Currently there are none, but they're coming soon.

# Goal
There are two main goals that will be acheived during this project:

1. Create a fitness tracker app that provides more evidence based insights than the current market leaders. Athletes should be able to see fine grain breakdowns of how differences in training effect their results.
2. Become proficient with technologies that I am currently a novice with, such as Flask, Sql, Google Cloud, and Docker. This will mean that some solutions might be overkill for the given situation, but a simpler solution might not help further this goal. 

# Progress
Currently the database and surrounding utilities are being set up. Right now, there are methods to add or display users, runs, and shoes.

## To Do
* Tests
* Set up Flask
* Set up Google Cloud
