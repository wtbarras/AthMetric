import os
import tempfile

import pytest

from runmetric import runmetric

@pytest.fixture
def client():
    # mkstemp() returns a file handle and a random file name.
    # These will be used for the test db
    db_fd, runmetric.app.config['DATABASE'] = tempfile.mkstemp()
    runmetric.app.config['TESTING'] = True
    client = runmetric.app.test_client()

    with runmetric.app.app_context():
        runmetric.init_db()

    yield client

    os.close(db_fd)
    os.unlink(runmetric.app.config['DATABASE'])