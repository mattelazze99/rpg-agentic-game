"""World retrieval service."""

from sqlalchemy.orm import Session, joinedload

from ..models import GameSession
from ..schemas.core_schemas import WorldStateResponse


def get_world(db: Session, session_id: str) -> WorldStateResponse | None:
    session = (
        db.query(GameSession)
        .options(joinedload(GameSession.world_state))
        .filter(GameSession.session_id == session_id)
        .first()
    )
    if session is None or session.world_state is None:
        return None
    return WorldStateResponse.model_validate(session.world_state)
