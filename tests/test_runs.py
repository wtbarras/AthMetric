import pytest
from runmetric.db import get_db

def test_index(client, auth):
    # Make sure that the log in page is displayed if we haven't logged in yet
    response = client.get('/', follow_redirects=True)
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # Log in
    auth.login()
    # Make sure we get the main page now that we're logged in
    response = client.get('/')
    assert b'Logout' in response.data

@pytest.mark.parametrize(('path'),(
    '/create',
    '/1/delete',
    '/1/update',
))
def test_login_required(client, path):
    # Make sure that these paths redirect non logged in users to the login page
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

@pytest.mark.parametrize(('path'),(
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    # Log in so we don't get redirected to login page
    auth.login()

    response = client.post(path)
    assert response.status_code == 404

def test_create_run(client, auth, app):
    auth.login()

def test_update_run(client, auth, app):
    auth.login()

def test_delete_run(client, auth, app):
    auth.login()