import pytest
from runmetric.db import get_db, count_runs, get_run

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
    # Make sure the endpoint works with the get method
    assert client.get('/create').status_code == 200

    # Post create data
    client.post('/create', data={'date': '1-1-2018', 'duration': '01:01:01', 'distance': '11.1', 'shoe_id': ''})

    # Check to make sure data ended up in database
    with app.app_context():
        count = count_runs()
        assert count == 2

def test_update_run(client, auth, app):
    auth.login()
    # Make sure the endpoint works with the get method
    assert client.get('/1/update').status_code == 200

    # Post update data
    client.post('/1/update', data={'date': '2-2-2011', 'duration': '01:11:11', 'distance': '12.1', 'shoe_id': ''})

    # Check to make sure the new data ended up in the original db entry
    with app.app_context():
        run = get_run(1)
        assert run['time'] == '01:11:11'
        assert run['distance'] == 12.1
        assert run['date'] == '2-2-2011'

def test_delete_run(client, auth, app):
    auth.login()

    # Post delete
    client.post('/1/delete')

    # Check to make sure data ended up in database
    with app.app_context():
        count = count_runs()
        assert count == 0