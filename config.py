"""Module for backend configuration using Pydantic's BaseSettings."""

# pylint: disable=too-few-public-methods
from pydantic import BaseSettings


class Settings(BaseSettings):
    """A class used to manage application settings through environment variables."""

    ENV: str = "development"


# pylint: disable=too-few-public-methods
settings = Settings()
