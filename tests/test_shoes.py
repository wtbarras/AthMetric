import pytest

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