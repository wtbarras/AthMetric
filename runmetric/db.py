import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from runmetric.models.database.run import Run


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


# DB util functions

# Add a run
def add_run(user_id, run):
    db = get_db()
    db.execute(
        'INSERT INTO run (date, distance, time, user_id, shoe_id)'
        ' VALUES (?, ?, ?, ?, ?)',
        (run.date, run.distance, run.time, user_id, run.shoe_id))
    db.commit()
    close_db()

# Update a run
def update_run(run_id, run):
    db = get_db()
    db.execute(
        'UPDATE run SET date = ?, time = ?, distance = ?, shoe_id = ?'
        ' WHERE run_id = ?',
        (run.date, run.time, run.distance, run.shoe_id, run_id)
    )
    db.commit()
    close_db()

# Delete a run
def delete_run(run_id):
    db = get_db()
    db.execute(
        'DELETE FROM run WHERE run_id = ?',
        (run_id,))
    db.commit()
    close_db()


# Get a specific run entry
def get_run(run_id):
    db = get_db()
    # Get run from db that matches the supplied id
    run = db.execute(
        'SELECT * FROM run WHERE run_id = ?',
        (run_id,)
    ).fetchone()
    close_db()
    return run

# Register a user

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