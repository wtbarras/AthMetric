import pytest
from flask import g, session
from runmetric.db import get_db

def test_register(client, app):
    # Check that the /auth/register endpoint is functional
    assert client.get('/auth/register').status_code == 200

    # Register a user with username a and password a
    response = client.post(
        '/auth/register', 
        data={'email': 'a', 'password':'a'}
    )

    # Check that the register page redirects to the login page
    'http://localhost/auth/login' == response.headers['Location']

    # Check that a user with the same username as above ended up in the database
    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE email = 'a'"
        ).fetchone is not None

#Run the below test with three different sets of inputs
@pytest.mark.parametrize(('email', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, email, password, message):
    response = client.post(
        '/auth/register',
        data={'email': email, 'password':password}
    )
    assert message in response.data