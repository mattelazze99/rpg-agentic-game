"""Database models for the game domain.

Importing this package will register all SQLAlchemy models so that they can be
created by metadata operations.  Additional models should be imported in this
module to ensure they are discovered by Alembic migrations or other tools.
"""

from .base import Base  # noqa: F401
from .session import Session  # noqa: F401
# Additional models (e.g. Character, World) can be imported here as they are
# implemented.