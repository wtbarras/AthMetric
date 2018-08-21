from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from runmetric.auth import login_required
from runmetric.db import get_db

bp = Blueprint('runs', __name__)

@bp.route('/')
def index():
    db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    runs = db.execute(
        'SELECT * FROM run'
    ).fetchall()
    return render_template('runs/index.html', runs=runs)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # Get id for logged in user
        user_id = session.get('user_id')
        # Get data from form
        date = request.form['date']
        distance = request.form['distance']
        time = request.form['time']
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
                'INSERT INTO run (date, distace, time, user_id, shoe_id)'
                ' VALUES (?, ?, ?, ?)',
                (date, distance, time, user_id, shoe_id)
                )
            db.commit()
            return redirect(url_for('runs.index'))
    else:
        return render_template('runs/create.html')