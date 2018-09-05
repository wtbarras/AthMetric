from flask import (
    Blueprint
)

from runmetric.auth import login_required

bp = Blueprint('shoes', __name__, url_prefix='/shoes')

# Shoes root. Display all of a user's shoes
@bp.route('/')
@login_required
def display_shoes():
    return "SHOES"

@bp.route('/create')
@login_required
def create_shoe():
    return "CREATE SHOES"

@bp.route('/update')
@login_required
def update_shoe():
    return 'UPDATE SHOES'

@bp.route('/delete')
@login_required
def delete_shoe():
    return 'DELETE SHOES'