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