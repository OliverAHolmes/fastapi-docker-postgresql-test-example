"""Module for database setup and utilities using SQLModel and SQLAlchemy."""

from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker
from config import settings


if settings.ENV == "testing":
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5433/testdb"
else:
    SQLALCHEMY_DATABASE_URL = f"postgresql://user:password@localhost:5432/devdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db():
    """Creates a new database if it doesn't exist, and removes it if we are in testing mode."""

    if settings.ENV == "testing":
        SQLModel.metadata.drop_all(engine)

    # Create tables if they don't exist
    SQLModel.metadata.create_all(engine)


def get_db():
    """Gets a new database session and closes it when done.

    Yields:
        Session: a new database session
    """

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
