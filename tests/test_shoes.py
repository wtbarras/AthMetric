import pytest

from runmetric.db import count_shoes

# Make sure GET method endpoints cannot be accessed when logged out
@pytest.mark.parametrize(('path'), (
    ('/shoes/'),
    ('/shoes/create'),
    ('/shoes/1/update')
))
def test_login_required_shoes_get(client, path):
    response = client.get(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

# Make sure POST method endpoints cannot be accessed when logged out
@pytest.mark.parametrize(('path'), (
    ('/shoes/create'),
    ('/shoes/1/update'),
    ('/shoes/1/delete')
))
def test_login_required_shoes_post(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'

# Test the creation of a new shoe entry
def test_create_run(client, auth, app):
    # Log in so that route actually works
    auth.login()

    # Get current number of shoes in db
    with app.app_context():
        pre_shoe_count = count_shoes()

    # Add shoe
    path = '/shoes/create'
    client.post(path, data={'name': 'Newton Kismet 2', 'total_miles': '0', 'target_miles': '500'})

    with app.app_context():
        post_shoe_count = count_shoes()
    assert post_shoe_count == pre_shoe_count + 1