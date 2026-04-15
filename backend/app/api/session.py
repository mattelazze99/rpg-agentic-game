"""Session endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..schemas.core_schemas import GameSessionResponse
from ..schemas.session_schema import SessionCreateRequest, SessionCreatedEnvelope
from ..services.session_service import create_session, get_session

router = APIRouter(prefix="/session", tags=["session"])


@router.post("/", response_model=SessionCreatedEnvelope)
def create_session_endpoint(request: SessionCreateRequest, db: Session = Depends(get_db)) -> SessionCreatedEnvelope:
    session = create_session(db, request)
    return SessionCreatedEnvelope(message="Session created successfully.", session=session)


@router.get("/{session_id}", response_model=GameSessionResponse)
def get_session_endpoint(session_id: str, db: Session = Depends(get_db)) -> GameSessionResponse:
    session = get_session(db, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
