"""Session request and response schemas."""

from pydantic import BaseModel

from .core_schemas import GameSessionResponse


class SessionCreateRequest(BaseModel):
    human_player_name: str | None = None


class SessionCreatedEnvelope(BaseModel):
    message: str
    session: GameSessionResponse
