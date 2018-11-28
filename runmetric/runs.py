from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from runmetric.auth import login_required
from runmetric.models.database.run import Run
from runmetric.db import run_query

bp = Blueprint('runs', __name__)

# Root. Displays user's runs
@bp.route('/')
@login_required
def index():
    # Get id for logged in user
    user_id = session.get('user_id')
    # Get all runs for user
    parameters = [user_id,]
    runs = run_query(Run.get_runs_for_user, parameters)
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
            return ""
        else:
            # Create run object
            run = Run(date, distance, time, user_id, shoe_id)
            # Add run to database
            run_query(run.add_run)
            # Redirect user back to main page
            return redirect(url_for('runs.index'))
    else:
        return render_template('runs/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    # Make sure that run exists
    if run_query(Run.get_run_by_id, [id,]) == None:
        return render_template('not_found.html'), 404
        
    if request.method == 'POST':
        # Get id for logged in user
        user_id = session.get('user_id')
        # Get data from form
        date = request.form['date']
        duration = request.form['duration']
        distance = request.form['distance']
        shoe_id = request.form['shoe_id']

        # Check if any fields are missing
        error = None
        if not date or not distance or not duration:
            error = "Missing fields"

        # If there are errors, display them
        if error is not None:
            flash(error)
            return ""
        else:
            # Create run object
            run = Run(date, distance, duration, user_id, shoe_id)
            # Update run
            parameters = [id,]
            run_query(run.update_run, parameters)
            # Redirect user back to main page
            return redirect(url_for('runs.index'))
    else:
        # GET
        # Get run by id from db
        run = run_query(Run.get_run_by_id, [id,])
        # Render update page for that run
        return render_template('runs/update.html', run=run)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    # Make sure that run exists
    if run_query(Run.get_run_by_id, [id,]) == None:
        return render_template('not_found.html'), 404

    parameters = [id,]
    run_query(Run.delete_run, parameters)
    # Redirect user back to main page
    return redirect(url_for('runs.index'))