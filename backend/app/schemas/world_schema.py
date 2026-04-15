"""World response schema."""

from pydantic import BaseModel

from .core_schemas import WorldStateResponse


class WorldEnvelope(BaseModel):
    session_id: str
    world: WorldStateResponse
