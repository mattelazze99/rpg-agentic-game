"""Application configuration.

Uses Pydantic's `BaseSettings` to load configuration from environment variables
or a `.env` file.  See FastAPI documentation for further examples on
environment‑based settings management.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Environment‑aware settings for the application."""

    # Database connection URL.  In development we use a local SQLite file.  For
    # production deployments this can be pointed at a PostgreSQL database.
    database_url: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"


# Instantiate a single settings object that can be imported throughout the app
settings = Settings()