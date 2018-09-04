import os
import tempfile

import pytest
from runmetric import create_app
from runmetric.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # Make temporary file for test database
    db_fd, db_path = tempfile.mkstemp()

    # Create instance of app using test configuration
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # Initialize the database using the temp file from above
    # Run the data.sql script to set up test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()



# For testing authentication    
class AuthActions(object):
    def __init__(self, client):
        self._client = client
    
    def login(self, email='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'email': email, 'password': password}
        )

    def logout(self):
        return self._client.post('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)