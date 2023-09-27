"""Module for backend configuration using Pydantic's BaseSettings."""

# pylint: disable=too-few-public-methods
from pydantic import BaseSettings


class Settings(BaseSettings):
    """A class used to manage application settings through environment variables."""

    ENV: str = "development"
    db_path: str

    @property
    def db_path(self) -> str:
        """Property method to decide which database path to use based on the environment.

        Returns:
            str: Path to the database file.
        """
        return "test.db" if self.ENV == "testing" else "database.db"


# pylint: disable=too-few-public-methods
settings = Settings()
