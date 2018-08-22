from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from runmetric.auth import login_required
from runmetric.db import get_db

bp = Blueprint('runs', __name__)

# Root. Displays user's runs
@bp.route('/')
@login_required
def index():
    db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    runs = db.execute(
        'SELECT * FROM run WHERE user_id = ?',
        (session.get('user_id'),)
    ).fetchall()
    return render_template('runs/index.html', runs=runs)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        # Get id for logged in user
        user_id = session.get('user_id')
        # Get data from form
        date = request.form['date']
        distance = request.form['distance']
        time = request.form['duration']
        shoe_id = request.form['shoe_id']

        # Check if any fields are missing
        error = None
        if not date or not distance or not time:
            error = "Missing fields"

        # If there are errors, display them
        if error is not None:
            flash(error)
        else:
            # Add run to database
            db = get_db()
            db.execute(
                'INSERT INTO run (date, distance, time, user_id, shoe_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (date, distance, time, user_id, shoe_id)
                )
            db.commit()
            return redirect(url_for('runs.index'))
    else:
        return render_template('runs/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    print(id)
    db = get_db()
    runs = db.execute(
        'SELECT * FROM run WHERE run_id = ?',
        (id,)
    )
    # In case the above query returns more than one row, we'll only use the first one
    # But it should only ever return one row, since run_id is the primary key
    run = runs.fetchone()
    return render_template('runs/update.html', run=run)
