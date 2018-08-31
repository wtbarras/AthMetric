# running_data_parser
Parses a data on a series of runs and generates informative charts.

The end goal is to create a website and mobile app that can track workouts and provide better data visualisation to athletes to enable evidence based training.

# Flask
This app is running on a Flask server. Most of the setup is based on this [doc](http://flask.pocoo.org/docs/1.0/tutorial/factory/).
## Running Flask
### Linux and MacOS
```
> export FLASK_APP=runmetric
> export FLASK_ENV=development
> flask run
```
### Windows PowerShell
```
> $env:FLASK_APP = "runmetric"
> $env:FLASK_ENV = "development"
> flask run
```
### Windows CMD
```
> set FLASK_APP=runmetric
> set FLASK_ENV=development
> flask run
```

# Database
The current database for this app is sqlite3. It was chosen strictly because it is simple. If the app ever begins seeing heavy traffic, it will definitely need to be swapped out. I might switch to a Google Cloud SQL database sooner rather than later, just as a way to experiment with the product.
### Initialize database
To initialize the database, run this command:
```
> flask init-db
```
This will run the init_db_command() function from the db.py file. The database will be created in the instance directory, which is not meant to be tracked in version control.

# UI
Currently I am using MDL to handle most of the UI work. Eventually I would like it to have a somewhat more unique look, but for now it just needs to not look terrible. Any feedback on how the website looks would be appreciated. 

# Installing
This app can be installed like any other python package. From the top level directory in the project, run this command:
```
> pip install -e .
```
To make sure that it is installed, run:
```
> pip list
```
Runmetric 1.0.0 will appear in the list.

# Tests
Tests are containced in the 'tests' directory. The testing tool used is pytest. This should be installed with the rest of the project when using the method described in the 'Installing' section.
To run the tests, run the following command from the top level directory in the project:
```
> pytest
```
This should automatically find the tests in the 'tests' directory and run all of them.

# Goal
There are three main goals that will be acheived during this project:

1. Create a fitness tracker app that provides more evidence based insights than the current market leaders. Athletes should be able to see fine grain breakdowns of how differences in training effect their results.
2. Become proficient with technologies that I am currently a novice with, such as Flask, Sql, Google Cloud, and Docker. This will mean that some solutions might be overkill for the given situation, but a simpler solution might not help further this goal. 
3. Expose aggregated anonymized user data via an API. This will allow others to benefit from the data that is collected.

# Progress
Currently the database and surrounding utilities are being set up. Right now, there are methods to add or display users, runs, and shoes.

## To Do
* Shoes
    - Util functions
        - Add
        - Delete
        - Edit
    - Endpoints
        - Add
        - Delete
        - Edit
    - UI
        - Display all shoes in shoe tab
* Some UI work to make things look a little less 2005
    - Nice landing page
    - ~~Change interface to tabs~~
    - Login/Logout buttons on top bar
    - ~~Display runs~~
    - Format run entries
    - Make add run button sit in bottom right
    - Make add run button only show up on RUNS tab
    - Add 'add shoe' button with same specs as add run button
* Tests
    - ~~Set up test framework in general~~
    - Run tests
    - Shoe tests
    - Can the UI be tested?
* DevOps
    - Google Cloud
        - Get app running on GC
        - Move DB to GC SQL: https://cloud.google.com/sql/docs/
            - Look into whether or not a noSql db would be better
        - GC build: https://cloud.google.com/cloud-build/
    - Docker
* General
    - Come up with a better name
    - Get a logo