"""Database connection utilities.

Defines a SQLAlchemy engine and session factory for connecting to the
application's database.  Uses the URL configured in the settings module.  At
runtime other modules can import `SessionLocal` and `engine` to interact with
the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if settings.database_url.startswith("sqlite") else {},
)
"""The SQLAlchemy engine connected to the configured database."""

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""Session factory bound to the database engine."""