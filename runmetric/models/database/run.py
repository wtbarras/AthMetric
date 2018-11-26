class Run:

    def __init__(self, date, distance, time, user_id, shoe_id):
        self.date = date
        self.distance = distance
        self.time = time
        self.user_id = user_id
        self.shoe_id = shoe_id

    # Add a run
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

    # # Delete a run
    # def delete_run(run_id):
    #     db = get_db()
    #     db.execute(
    #         'DELETE FROM run WHERE run_id = ?',
    #         (run_id,))
    #     db.commit()
    #     close_db()

    # # Get all runs for this user
    # def get_runs_for_user(id):
    #     db = get_db()
    #     runs = db.execute(
    #         'SELECT * FROM run WHERE user_id = ?',
    #         (id,)
    #     ).fetchall()
    #     close_db()
    #     return runs

    # # Get a specific run entry
    # def get_run_by_id(run_id):
    #     db = get_db()
    #     # Get run from db that matches the supplied id
    #     run = db.execute(
    #         'SELECT * FROM run WHERE run_id = ?',
    #         (run_id,)
    #     ).fetchone()
    #     close_db()
    #     return run

    # # Count the number of runs in the database
    # def count_runs():
    #     db = get_db()
    #     count = db.execute('SELECT COUNT(run_id) FROM run').fetchone()[0]
    #     close_db()
    #     return count

    # # Register a user
    # def register_user(email, password):
    #     db = get_db()
    #     db.execute(
    #         'INSERT INTO user (email, password) VALUES (?, ?)',
    #         (email, generate_password_hash(password)))
    #     db.commit()
    #     close_db()

    # # Get a user by email
    # def get_user_by_email(email):
    #     db = get_db()
    #     user = db.execute(
    #         'SELECT * FROM user WHERE email = ?',
    #         (email,)
    #     ).fetchone()
    #     close_db()
    #     return user
        
    # # Get a user by id
    # def get_user_by_id(user_id):
    #     db = get_db()
    #     user = db.execute(
    #         'SELECT * FROM user WHERE user_id = ?',
    #         (user_id,)
    #     ).fetchone()
    #     close_db()
    #     return user

    # # Create a new shoe
    # def add_shoe(name, total_miles, target_miles, user_id):
    #     db = get_db()
    #     db.execute(
    #         'INSERT INTO shoe (name, total_miles, target_miles, user_id)'
    #         'VALUES (?, ?, ?, ?)',
    #         (name, total_miles, target_miles, user_id)
    #     )
    #     db.commit()
    #     close_db()

    # # Edit a shoe
    # def edit_shoe(shoe_id, shoe):
    #     db = get_db()
    #     db.execute(
    #         'UPDATE shoe SET name = ?, total_miles = ?, target_miles = ?, user_id = ?'
    #         ' WHERE shoe_id = ?',
    #         (shoe.name, shoe.total_miles, shoe.target_miles, shoe.user_id, shoe_id)
    #     )
    #     db.commit()
    #     close_db()

    # # Delete a shoe
    # def delete_shoe(shoe_id):
    #     db = get_db()
    #     db.execute(
    #         'DELETE FROM shoe WHERE shoe_id = ?',
    #     (shoe_id,))
    #     db.commit()
    #     close_db()

    # # Get a shoe by id
    # def get_shoe_by_id(shoe_id):
    #     db = get_db()
    #     # Get run from db that matches the supplied id
    #     shoe = db.execute(
    #         'SELECT * FROM shoe WHERE shoe_id = ?',
    #         (shoe_id,)
    #     ).fetchone()
    #     close_db()
    #     return shoe

    # # Get all shoes for user
    # def get_shoes_for_user(user_id):
    #     db = get_db()
    #     shoes = db.execute(
    #         'SELECT * FROM shoe WHERE user_id = ?',
    #         (user_id,)
    #     ).fetchall()
