import pytest
from runmetric.db import get_db

def test_index(client, auth):
    response = client.get('/', follow_redirects=True)
    assert b"Log In" in response.data
    assert b"Register" in response.data