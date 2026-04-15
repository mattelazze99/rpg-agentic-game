"""Session orchestration and serialization."""

from __future__ import annotations

from uuid import uuid4

from sqlalchemy.orm import Session, joinedload

from ..models import (
    AIPlayerAgent,
    Character,
    Encounter,
    EncounterStatus,
    EventLogEntry,
    GameSession,
    HumanPlayer,
    LootItem,
    LootType,
    MasterAgent,
    NPC,
    Quest,
    QuestStatus,
    SceneState,
    SceneType,
    SessionStatus,
    WorldState,
    InventoryItem,
)
from ..schemas.core_schemas import GameSessionResponse
from ..schemas.session_schema import SessionCreateRequest


def _to_session_response(session: GameSession) -> GameSessionResponse:
    return GameSessionResponse.model_validate(session)


def _load_session(db: Session, session_id: str) -> GameSession | None:
    return (
        db.query(GameSession)
        .options(
            joinedload(GameSession.world_state),
            joinedload(GameSession.human_player).joinedload(HumanPlayer.character).joinedload(Character.inventory_items).joinedload(InventoryItem.item),
            joinedload(GameSession.ai_players).joinedload(AIPlayerAgent.character).joinedload(Character.inventory_items).joinedload(InventoryItem.item),
            joinedload(GameSession.master_agent),
            joinedload(GameSession.scenes).joinedload(SceneState.npcs).joinedload(NPC.quests),
            joinedload(GameSession.scenes).joinedload(SceneState.encounters),
            joinedload(GameSession.quests),
            joinedload(GameSession.encounters),
            joinedload(GameSession.event_log_entries),
        )
        .filter(GameSession.session_id == session_id)
        .first()
    )


def create_session(db: Session, request: SessionCreateRequest) -> GameSessionResponse:
    session = GameSession(session_id=f"sess-{uuid4().hex[:8]}", status=SessionStatus.active)

    human_character = Character(
        session=session,
        name=request.human_player_name or "Human Adventurer",
        class_name="Wanderer",
        race="Human",
        level=1,
        description="The player-controlled adventurer.",
        stats={"might": 10, "agility": 10, "mind": 10},
    )
    session.human_player = HumanPlayer(name=request.human_player_name or "Human Player", character=human_character)

    ai_specs = [
        (1, "Aldren", "cautious strategist", "Scholar", "Elf"),
        (2, "Brakka", "bold frontliner", "Guardian", "Orc"),
        (3, "Cira", "curious trickster", "Rogue", "Halfling"),
    ]
    for index, agent_name, persona, class_name, race in ai_specs:
        character = Character(
            session=session,
            name=agent_name,
            class_name=class_name,
            race=race,
            level=1,
            description=f"AI character piloted by {agent_name}.",
            stats={"might": 9 + index, "agility": 8 + index, "mind": 7 + index},
        )
        session.ai_players.append(
            AIPlayerAgent(index=index, name=agent_name, persona=persona, character=character)
        )

    session.master_agent = MasterAgent(name="Mira", style="Measured fantasy narrator")
    session.world_state = WorldState(
        summary="A frontier valley where old ruins, local factions and a fragile peace create immediate adventure hooks.",
        tone="Grounded heroic fantasy",
        data={
            "starting_area": "Briar Glen",
            "factions": ["Wardens of the Pass", "Ashen Knives", "Moss Abbey"],
            "quest_hooks": ["Missing courier", "Ruined watchtower lights", "Bandit toll road"],
        },
    )

    opening_scene = SceneState(
        name="Briar Glen Square",
        description="A compact village square with a fountain, market stalls and a road leading north toward a ruined watchtower.",
        scene_type=SceneType.free,
        map_data={"mode": "free", "poi": ["fountain", "inn", "north road"]},
    )
    session.scenes.append(opening_scene)

    npc = NPC(
        name="Captain Elira Voss",
        description="Veteran warden captain trying to keep the valley stable.",
        role="Quest giver",
        scene=opening_scene,
        session=session,
    )
    opening_scene.npcs.append(npc)

    quest = Quest(
        session=session,
        npc=npc,
        name="Lights at the Watchtower",
        description="Investigate strange lights reported at the old northern watchtower and return with evidence.",
        status=QuestStatus.open,
        reward={"gold": 25, "item": "Warden's Signet"},
    )
    session.quests.append(quest)

    encounter = Encounter(
        session=session,
        scene=opening_scene,
        name="Watchtower Ambush",
        description="A small tactical encounter against scavengers occupying the ruins.",
        participants=[1, 2, 3, 4],
        status=EncounterStatus.pending,
    )
    session.encounters.append(encounter)

    signet_item = LootItem(
        name="Warden's Signet",
        description="A small silver badge recognized by the valley guard.",
        item_type=LootType.quest,
        value=0,
        weight=0.1,
        properties={"reputation_bonus": True},
    )

    practice_blade = LootItem(
        name="Practice Blade",
        description="A serviceable short sword for early encounters.",
        item_type=LootType.weapon,
        value=8,
        weight=2.0,
        properties={"damage": "1d6"},
    )

    human_character.inventory_items.append(InventoryItem(item=practice_blade, quantity=1, equipped=True))
    human_character.inventory_items.append(InventoryItem(item=signet_item, quantity=1, equipped=False))

    session.event_log_entries.extend(
        [
            EventLogEntry(event_type="session.created", message="Session initialized successfully.", data={"phase": "setup"}),
            EventLogEntry(event_type="world.generated", message="Initial world state generated.", data={"starting_area": "Briar Glen"}),
            EventLogEntry(event_type="quest.available", message="Quest 'Lights at the Watchtower' is now available.", data={"quest": "Lights at the Watchtower"}),
        ]
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    loaded = _load_session(db, session.session_id)
    if loaded is None:
        raise RuntimeError("Session was created but could not be reloaded.")
    return _to_session_response(loaded)


def get_session(db: Session, session_id: str) -> GameSessionResponse | None:
    session = _load_session(db, session_id)
    if session is None:
        return None
    return _to_session_response(session)
