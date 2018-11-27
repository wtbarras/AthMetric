class Run:

    def __init__(self, date, distance, time, user_id, shoe_id):
        self.date = date
        self.distance = distance
        self.time = time
        self.user_id = user_id
        self.shoe_id = shoe_id


    # NOTE:
    # All the below functions are meant to be used with the runmetric.db.run_query() method. The run query method is what opens the DB
    # connection and cleans it up afterward.

    # Add a run
    # For some reason adding @classmethod here breaks the method
    def add_run(self, db):
        db.execute(
            'INSERT INTO run (date, distance, time, user_id, shoe_id)'
            ' VALUES (?, ?, ?, ?, ?)',
            (self.date, self.distance, self.time, self.user_id, self.shoe_id))

    # Update a run
    def update_run(self, db, parameters):
        db.execute(
            'UPDATE run SET date = ?, time = ?, distance = ?, shoe_id = ?'
            ' WHERE run_id = ?',
            (self.date, self.time, self.distance, self.shoe_id, parameters[0])
        )

    # Delete a run
    @staticmethod
    def delete_run(db, parameters):
        db.execute(
            'DELETE FROM run WHERE run_id = ?',
            (parameters[0],))

    # Get all runs for this user
    @staticmethod
    def get_runs_for_user(db, parameters):
        runs = db.execute(
            'SELECT * FROM run WHERE user_id = ?',
            (parameters[0],)
        ).fetchall()
        return runs

    # Get a specific run entry
    @staticmethod
    def get_run_by_id(db, parameters):
        # Get run from db that matches the supplied id
        run = db.execute(
            'SELECT * FROM run WHERE run_id = ?',
            (parameters[0],)
        ).fetchone()
        return run

    # Count the number of runs in the database
    @staticmethod
    def count_runs():
        count = db.execute('SELECT COUNT(run_id) FROM run').fetchone()[0]
        return count