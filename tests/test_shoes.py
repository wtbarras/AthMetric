import pytest

from runmetric.db import count_shoes, get_shoe_by_id

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

# Test updating a shoe entry
def test_update_shoe(auth, client, app):
    # Log in so that route actually works
    auth.login()

    response = client.post('/shoes/2/update')
    assert response.status_code == 404

    new_name = 'Newton Kismet 2'
    new_total_miles = 15
    new_target_miles = 500

    response = client.post('/shoes/1/update', data={'name': new_name, 'total_miles': new_total_miles, 'target_miles': new_target_miles})
    with app.app_context():
        shoe = get_shoe_by_id(1)
        assert shoe['name'] == new_name
        assert shoe['total_miles'] == new_total_miles
        assert shoe['target_miles'] == new_target_miles

# Test deleting a shoe entry
def test_delete_shoe(auth, client, app):
    # Log in so that route actually works
    auth.login()

    # Check that a nonexistant run cannot be deleted
    response = client.post('/shoes/420/delete')
    assert response.status_code == 404

    # Check that an existing run can be deleted
    with app.app_context():
        pre_shoe_count = count_shoes()

    client.post('/shoes/1/delete')

    client.post()