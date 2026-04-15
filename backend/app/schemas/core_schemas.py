"""Pydantic DTOs for API contracts."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class LootItemResponse(ORMModel):
    id: int
    name: str
    description: str | None = None
    item_type: str
    value: float | None = None
    weight: float | None = None
    properties: dict[str, Any] | None = None


class InventoryItemResponse(ORMModel):
    id: int
    quantity: int
    equipped: bool
    item: LootItemResponse


class CharacterResponse(ORMModel):
    id: int
    name: str
    class_name: str | None = None
    level: int
    race: str | None = None
    description: str | None = None
    stats: dict[str, Any] | None = None
    inventory_items: list[InventoryItemResponse] = Field(default_factory=list)


class CharacterCreateRequest(BaseModel):
    name: str
    class_name: str | None = None
    race: str | None = None
    description: str | None = None
    stats: dict[str, Any] | None = None


class HumanPlayerResponse(ORMModel):
    id: int
    name: str | None = None
    character: CharacterResponse | None = None


class AIPlayerResponse(ORMModel):
    id: int
    index: int
    name: str
    persona: str | None = None
    character: CharacterResponse | None = None


class MasterAgentResponse(ORMModel):
    id: int
    name: str
    style: str | None = None


class WorldStateResponse(ORMModel):
    id: int
    summary: str | None = None
    tone: str | None = None
    data: dict[str, Any] | None = None


class QuestResponse(ORMModel):
    id: int
    name: str
    description: str | None = None
    status: str
    reward: dict[str, Any] | None = None


class NPCResponse(ORMModel):
    id: int
    name: str
    description: str | None = None
    role: str | None = None
    quests: list[QuestResponse] = Field(default_factory=list)


class EncounterResponse(ORMModel):
    id: int
    name: str | None = None
    description: str | None = None
    participants: list[int] | None = None
    status: str


class SceneStateResponse(ORMModel):
    id: int
    name: str
    description: str | None = None
    scene_type: str
    map_data: dict[str, Any] | None = None
    npcs: list[NPCResponse] = Field(default_factory=list)
    encounters: list[EncounterResponse] = Field(default_factory=list)


class EventLogEntryResponse(ORMModel):
    id: int
    timestamp: datetime
    event_type: str
    message: str
    data: dict[str, Any] | None = None


class GameSessionResponse(ORMModel):
    id: int
    session_id: str
    status: str
    created_at: datetime
    ended_at: datetime | None = None
    world_state: WorldStateResponse | None = None
    human_player: HumanPlayerResponse | None = None
    ai_players: list[AIPlayerResponse] = Field(default_factory=list)
    master_agent: MasterAgentResponse | None = None
    scenes: list[SceneStateResponse] = Field(default_factory=list)
    quests: list[QuestResponse] = Field(default_factory=list)
    encounters: list[EncounterResponse] = Field(default_factory=list)
    event_log_entries: list[EventLogEntryResponse] = Field(default_factory=list)
