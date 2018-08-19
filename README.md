# running_data_parser
Parses a data on a series of runs and generates informative charts

# Set up database
To set up the database, cd into the running_data_parser/database directory and run:
```sqlite3 rundata.py```
This will create a database called rundata.db in running_data_parser/database.
Next, you will need to run the database setup script:
```python3 setup_database.py```
The script will set up all the database tables, assuming they do not already exist.