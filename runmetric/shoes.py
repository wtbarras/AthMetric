from flask import (
    Blueprint
)

from runmetric.auth import login_required

bp = Blueprint('shoes', __name__, url_prefix='/shoes')

# Shoes root. Display all of a user's shoes
@bp.route('/', methods=('GET',))
@login_required
def display_shoes():
    return "SHOES"

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_shoe():
    return "CREATE SHOES"

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update_shoe(id):
    return 'UPDATE SHOES'

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete_shoe(id):
    return 'DELETE SHOES'