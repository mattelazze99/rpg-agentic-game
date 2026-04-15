# Multi-Agent RPG V1

Repository bundle with a runnable FastAPI backend foundation and the first serious set of core domain models for a web-based multi-agent RPG.

## Included

- Runnable FastAPI backend
- SQLite persistence with automatic table creation on startup
- Core domain models for sessions, players, characters, world state, scenes, quests, encounters, loot and event logs
- API routes for root, health, session creation/retrieval and world retrieval
- Simple service layer and serialization boundaries
- Basic deterministic rules engine stub
- Agent runtime stubs
- Pytest API smoke tests

## Quick start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

- `http://localhost:8000/`
- `http://localhost:8000/docs`
- `http://localhost:8000/health`

## Main endpoints

- `GET /` — basic service info
- `GET /health` — health check
- `POST /session/` — create a new session with seeded world and agents
- `GET /session/{session_id}` — retrieve a session snapshot
- `GET /world/{session_id}` — retrieve the session world state

## Notes

This is a coherent backend base intended to solve the earlier issue where `localhost:8000` kept loading without a working root endpoint or complete app wiring.
