from runmetric import create_app

# Test to make sure that the TESTING config is not set by default
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# Test that test endpoint /hello returns 'Hello, World!'
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'