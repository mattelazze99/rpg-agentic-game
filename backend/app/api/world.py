"""World endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..schemas.world_schema import WorldEnvelope
from ..services.world_service import get_world

router = APIRouter(prefix="/world", tags=["world"])


@router.get("/{session_id}", response_model=WorldEnvelope)
def get_world_endpoint(session_id: str, db: Session = Depends(get_db)) -> WorldEnvelope:
    world = get_world(db, session_id)
    if world is None:
        raise HTTPException(status_code=404, detail="World state not found")
    return WorldEnvelope(session_id=session_id, world=world)
