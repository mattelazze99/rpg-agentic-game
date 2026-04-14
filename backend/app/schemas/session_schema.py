"""Session request and response schemas."""

from pydantic import BaseModel


class SessionCreateRequest(BaseModel):
    """Parameters required to create a new game session.

    For V1 this is intentionally empty; future versions may include world or
    rule options.
    """
    pass


class SessionResponse(BaseModel):
    """Response returned after successfully creating a session."""

    session_id: str
    message: str