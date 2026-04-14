"""Schemas for creating and returning characters."""

from pydantic import BaseModel


class CharacterCreateRequest(BaseModel):
    """Request body for creating a character."""

    name: str


class CharacterResponse(BaseModel):
    """Response returned after creating or retrieving a character."""

    character_id: str
    name: str
    message: str