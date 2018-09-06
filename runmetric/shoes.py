from flask import (
    Blueprint, request, session
)

from runmetric.auth import login_required
from runmetric.db import add_shoe

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
    return 'UPDATE SHOES'

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete_shoe(id):
    return 'DELETE SHOES'