"""Session API endpoints.

This module exposes REST endpoints for creating and querying game sessions.  It
delegates business logic to the service layer and returns Pydantic models as
responses.
"""

from fastapi import APIRouter

from ..schemas.session_schema import SessionCreateRequest, SessionResponse
from ..services.session_service import create_session


router = APIRouter()


@router.post("/", response_model=SessionResponse)
def new_session(request: SessionCreateRequest) -> SessionResponse:
    """Create a new game session.

    Parameters
    ----------
    request: SessionCreateRequest
        The request body containing parameters for session creation.  For V1 this
        is empty but reserved for future options.

    Returns
    -------
    SessionResponse
        A structured response with the new session identifier and a human‑readable message.
    """
    # Delegate to the service layer.  Additional logic such as persistence and
    # agent initialisation will be added in future iterations.
    return create_session(request)