import pytest

# Make sure get methods cannot be accessed when logged out
@pytest.mark.parametrize(('path'), (
    ('/shoes/'),
    ('/shoes/create'),
    ('/shoes/1/update')
))
def test_login_required_shoes_get(client, path):
    response = client.get(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'