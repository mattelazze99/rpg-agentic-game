"""Schemas for world queries and responses."""

from pydantic import BaseModel


class WorldResponse(BaseModel):
    """Response containing a summary of the game world."""

    summary: str