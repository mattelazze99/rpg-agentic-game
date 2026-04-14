"""Session database model."""

from sqlalchemy import Column, Integer, String

from .base import Base


class Session(Base):
    """Represent a game session stored in the database."""

    __tablename__ = "sessions"

    id: int = Column(Integer, primary_key=True, index=True)
    session_id: str = Column(String, unique=True, index=True, nullable=False)
    status: str = Column(String, default="pending")