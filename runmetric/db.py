import sqlite3

import click
from werkzeug.security import generate_password_hash
from flask import current_app, g
from flask.cli import with_appcontext

from runmetric.models.database.run import Run
from runmetric.models.database.shoe import Shoe


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Register close_db and init_db_command with application
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Wrapper function for DB commands
# The SQL queries are in the model files, but this wrapper opens and closes the DB for them
def run_query(query_function, parameters=None):
    db = get_db()
    if parameters != None:
        results = query_function(db, parameters)
    else:
        results = query_function(db)
    db.commit()
    close_db()
    return results
# DB util functions

# Count the number of runs in the database
def count_runs():
    db = get_db()
    count = db.execute('SELECT COUNT(run_id) FROM run').fetchone()[0]
    close_db()
    return count

# Register a user
def register_user(email, password):
    db = get_db()
    db.execute(
        'INSERT INTO user (email, password) VALUES (?, ?)',
        (email, generate_password_hash(password)))
    db.commit()
    close_db()

# Get a user by email
def get_user_by_email(email):
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE email = ?',
        (email,)
    ).fetchone()
    close_db()
    return user
    
# Get a user by id
def get_user_by_id(user_id):
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE user_id = ?',
        (user_id,)
    ).fetchone()
    close_db()
    return user

# Create a new shoe
def add_shoe(name, total_miles, target_miles, user_id):
    db = get_db()
    db.execute(
        'INSERT INTO shoe (name, total_miles, target_miles, user_id)'
        'VALUES (?, ?, ?, ?)',
        (name, total_miles, target_miles, user_id)
    )
    db.commit()
    close_db()

# Edit a shoe
def edit_shoe(shoe_id, shoe):
    db = get_db()
    db.execute(
        'UPDATE shoe SET name = ?, total_miles = ?, target_miles = ?, user_id = ?'
        ' WHERE shoe_id = ?',
        (shoe.name, shoe.total_miles, shoe.target_miles, shoe.user_id, shoe_id)
    )
    db.commit()
    close_db()

# Delete a shoe
def delete_shoe(shoe_id):
    db = get_db()
    db.execute(
        'DELETE FROM shoe WHERE shoe_id = ?',
    (shoe_id,))
    db.commit()
    close_db()

# Get a shoe by id
def get_shoe_by_id(shoe_id):
    db = get_db()
    # Get run from db that matches the supplied id
    shoe = db.execute(
        'SELECT * FROM shoe WHERE shoe_id = ?',
        (shoe_id,)
    ).fetchone()
    close_db()
    return shoe

# Get all shoes for user
def get_shoes_for_user(user_id):
    db = get_db()
    shoes = db.execute(
        'SELECT * FROM shoe WHERE user_id = ?',
        (user_id,)
    ).fetchall()
    close_db()
    return shoes

# Count all shoes associated with user
def count_shoes():
    db = get_db()
    count = db.execute('SELECT COUNT(shoe_id) FROM shoe').fetchone()[0]
    close_db()
    return count

# Create a lifting activity
def create_lifting_activity():
    db = get_db()
    db.execute(
        'INSERT INTO shoe (desc, date, start_time, end_time, lift_data, lift_id, user_id)'
        'VALUES (?, ?, ?, ?, ?, ?, ?)',
        (desc, date, start_time, end_time, lift_data, lift_id, user_id)
    )
    db.commit()
    close_db()