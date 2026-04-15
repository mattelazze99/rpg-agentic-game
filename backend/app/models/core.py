"""Core ORM models for canonical game state."""

from __future__ import annotations

import enum
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from .base import Base


class SessionStatus(str, enum.Enum):
    pending = "pending"
    active = "active"
    completed = "completed"
    cancelled = "cancelled"


class SceneType(str, enum.Enum):
    free = "free"
    combat = "combat"


class QuestStatus(str, enum.Enum):
    open = "open"
    completed = "completed"
    failed = "failed"


class EncounterStatus(str, enum.Enum):
    pending = "pending"
    active = "active"
    resolved = "resolved"


class LootType(str, enum.Enum):
    weapon = "weapon"
    armour = "armour"
    consumable = "consumable"
    quest = "quest"
    misc = "misc"


class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True)
    session_id = Column(String, unique=True, index=True, nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.pending, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at = Column(DateTime, nullable=True)

    world_state = relationship("WorldState", uselist=False, back_populates="session", cascade="all, delete-orphan")
    scenes = relationship("SceneState", back_populates="session", cascade="all, delete-orphan", order_by="SceneState.id")
    human_player = relationship("HumanPlayer", uselist=False, back_populates="session", cascade="all, delete-orphan")
    ai_players = relationship("AIPlayerAgent", back_populates="session", cascade="all, delete-orphan", order_by="AIPlayerAgent.index")
    master_agent = relationship("MasterAgent", uselist=False, back_populates="session", cascade="all, delete-orphan")
    characters = relationship("Character", back_populates="session", cascade="all, delete-orphan", order_by="Character.id")
    quests = relationship("Quest", back_populates="session", cascade="all, delete-orphan", order_by="Quest.id")
    encounters = relationship("Encounter", back_populates="session", cascade="all, delete-orphan", order_by="Encounter.id")
    event_log_entries = relationship("EventLogEntry", back_populates="session", cascade="all, delete-orphan", order_by="EventLogEntry.id")


class HumanPlayer(Base):
    __tablename__ = "human_players"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False, unique=True)
    name = Column(String, nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True, unique=True)

    session = relationship("GameSession", back_populates="human_player")
    character = relationship("Character", foreign_keys=[character_id], back_populates="human_owner", uselist=False)


class AIPlayerAgent(Base):
    __tablename__ = "ai_player_agents"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    index = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    persona = Column(Text, nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True, unique=True)

    session = relationship("GameSession", back_populates="ai_players")
    character = relationship("Character", foreign_keys=[character_id], back_populates="ai_owner", uselist=False)


class MasterAgent(Base):
    __tablename__ = "master_agents"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False, unique=True)
    name = Column(String, nullable=False, default="Game Master")
    style = Column(String, nullable=True)

    session = relationship("GameSession", back_populates="master_agent")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    name = Column(String, nullable=False)
    class_name = Column(String, nullable=True)
    level = Column(Integer, default=1, nullable=False)
    race = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    stats = Column(JSON, nullable=True)

    session = relationship("GameSession", back_populates="characters")
    human_owner = relationship("HumanPlayer", foreign_keys=[HumanPlayer.character_id], back_populates="character")
    ai_owner = relationship("AIPlayerAgent", foreign_keys=[AIPlayerAgent.character_id], back_populates="character")
    inventory_items = relationship("InventoryItem", back_populates="character", cascade="all, delete-orphan", order_by="InventoryItem.id")


class WorldState(Base):
    __tablename__ = "world_states"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), unique=True, nullable=False)
    summary = Column(Text, nullable=True)
    tone = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    session = relationship("GameSession", back_populates="world_state")


class SceneState(Base):
    __tablename__ = "scene_states"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    scene_type = Column(Enum(SceneType), default=SceneType.free, nullable=False)
    map_data = Column(JSON, nullable=True)

    session = relationship("GameSession", back_populates="scenes")
    npcs = relationship("NPC", back_populates="scene", cascade="all, delete-orphan", order_by="NPC.id")
    encounters = relationship("Encounter", back_populates="scene", cascade="all, delete-orphan", order_by="Encounter.id")


class NPC(Base):
    __tablename__ = "npcs"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    scene_id = Column(Integer, ForeignKey("scene_states.id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    role = Column(String, nullable=True)

    scene = relationship("SceneState", back_populates="npcs")
    session = relationship("GameSession")
    quests = relationship("Quest", back_populates="npc", order_by="Quest.id")


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    npc_id = Column(Integer, ForeignKey("npcs.id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(QuestStatus), default=QuestStatus.open, nullable=False)
    reward = Column(JSON, nullable=True)

    session = relationship("GameSession", back_populates="quests")
    npc = relationship("NPC", back_populates="quests")


class Encounter(Base):
    __tablename__ = "encounters"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    scene_id = Column(Integer, ForeignKey("scene_states.id"), nullable=True)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    participants = Column(JSON, nullable=True)
    status = Column(Enum(EncounterStatus), default=EncounterStatus.pending, nullable=False)

    session = relationship("GameSession", back_populates="encounters")
    scene = relationship("SceneState", back_populates="encounters")


class LootItem(Base):
    __tablename__ = "loot_items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    item_type = Column(Enum(LootType), default=LootType.misc, nullable=False)
    value = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    properties = Column(JSON, nullable=True)

    inventory_items = relationship("InventoryItem", back_populates="item", cascade="all, delete-orphan", order_by="InventoryItem.id")


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("loot_items.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    equipped = Column(Boolean, default=False, nullable=False)

    character = relationship("Character", back_populates="inventory_items")
    item = relationship("LootItem", back_populates="inventory_items")


class EventLogEntry(Base):
    __tablename__ = "event_log_entries"

    id = Column(Integer, primary_key=True)
    session_db_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    event_type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    data = Column(JSON, nullable=True)

    session = relationship("GameSession", back_populates="event_log_entries")
