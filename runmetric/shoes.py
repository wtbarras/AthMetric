from flask import (
    Blueprint, request, session, render_template, redirect, url_for
)

from runmetric.auth import login_required
from runmetric.db import add_shoe, get_shoe_by_id, edit_shoe, delete_shoe
from runmetric.models.database.shoe import Shoe

bp = Blueprint('shoes', __name__, url_prefix='/shoes')

# Shoes root. Display all of a user's shoes
@bp.route('/', methods=('GET',))
@login_required
def display_shoes():
    return "SHOES"

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_shoe():
    if request.method == 'POST':
        # Get current user's id
        user_id = session.get('user_id')

        # Get data from request
        name = request.form['name']
        total_miles = request.form['total_miles']
        target_miles = request.form['target_miles']

        # Add shoe to db
        add_shoe(name, total_miles, target_miles, user_id)
        return ""
    else:
        return "CREATE SHOES"

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update_shoe(id):
    # Make sure that shoe exists
    if get_shoe_by_id(id) == None:
        return render_template('not_found.html'), 404

    if request.method == 'POST':
        # Get id for logged in user
        user_id = session.get('user_id')
        # Get data from form
        name = request.form['name']
        total_miles = request.form['total_miles']
        target_miles = request.form['target_miles']

        # Check if any fields are missing
        error = None
        if not name or not user_id:
            error = "Missing fields"

        # If there are errors, display them
        if error is not None:
            flash(error)
            return ""
        else:
            # Create shoe object
            shoe = Shoe(name, total_miles, target_miles, user_id)
            # Update shoe
            edit_shoe(id, shoe)
            # Redirect user back to main page
            return redirect(url_for('shoes.display_shoes'))
        return ""
    else:
        return 'UPDATE SHOES'

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    # Make sure that shoe exists
    if get_shoe_by_id(id) == None:
        return render_template('not_found.html'), 404

    delete_shoe(id)

    return 'DELETE SHOES'