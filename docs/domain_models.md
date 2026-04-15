# Core Domain Models

## Implemented entities

- `GameSession`
- `HumanPlayer`
- `AIPlayerAgent`
- `MasterAgent`
- `Character`
- `WorldState`
- `SceneState`
- `NPC`
- `Quest`
- `Encounter`
- `LootItem`
- `InventoryItem` as the inventory ownership boundary
- `EventLogEntry`

## Key relationships

- A `GameSession` owns world state, scenes, quests, encounters, event log entries, one human player, three AI players and one master agent.
- Players own characters through dedicated foreign keys.
- Characters own inventory entries through `InventoryItem`.
- Scenes own NPCs and encounters.
- NPCs can offer quests.
- Encounters are scoped to a scene and a session.
- Event log entries are session-scoped.

## V1 simplifications

- Inventory is modeled as `InventoryItem` instead of a standalone aggregate table.
- Encounter participants are stored as JSON identifiers for now.
- Agent memory is not persisted across sessions.
- Combat resolution is intentionally deferred; only encounter structure is modeled.
