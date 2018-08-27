# running_data_parser
Parses a data on a series of runs and generates informative charts.

The end goal is to create a website and mobile app that can track workouts and provide better data visualisation to athletes to enable evidence based training.

# Flask
This app is running on a Flask server. Most of the setup is based on this [doc](http://flask.pocoo.org/docs/1.0/tutorial/factory/).
## Running Flask
### Linux and MacOS
```
export FLASK_APP=runmetric
export FLASK_ENV=development
flask run
```
### Windows PowerShell
```
$env:FLASK_APP = "runmetric"
$env:FLASK_ENV = "development"
flask run
```
### Windows CMD
```
set FLASK_APP=runmetric
set FLASK_ENV=development
flask run
```

# Database
The current database for this app is sqlite3. It was chosen strictly because it is simple. If the app ever begins seeing heavy traffic, it will definitely need to be swapped out. I might switch to a Google Cloud SQL database sooner rather than later, just as a way to experiment with the product.
### Initialize database
To initialize the database, run this command:
```
flask init-db
```
This will run the init_db_command() function from the db.py file. The database will be created in the instance directory, which is not meant to be tracked in version control.

# Tests
Testing will be done with pytest. Currently there are none, but they're coming soon.

# Goal
There are three main goals that will be acheived during this project:

1. Create a fitness tracker app that provides more evidence based insights than the current market leaders. Athletes should be able to see fine grain breakdowns of how differences in training effect their results.
2. Become proficient with technologies that I am currently a novice with, such as Flask, Sql, Google Cloud, and Docker. This will mean that some solutions might be overkill for the given situation, but a simpler solution might not help further this goal. 
3. Expose aggregated anonymized user data via an API. This will allow others to benefit from the data that is collected.

# Progress
Currently the database and surrounding utilities are being set up. Right now, there are methods to add or display users, runs, and shoes.

## To Do
* Set up Flask - Currently need to redo my database utility functions to work with the new flask database.
* Add delete function
* Tests
* Set up Google Cloud
