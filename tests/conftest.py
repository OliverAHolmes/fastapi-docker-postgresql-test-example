import db
import pytest
import os


@pytest.fixture(scope="function")
def db_session():
    # Connect to your test database and create tables
    db.create_db()

    yield

    # Tear down: Disconnect and drop the tables and delete the database file
    os.remove("test.db")
