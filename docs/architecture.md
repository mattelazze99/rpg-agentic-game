# Architecture Overview

This bundle keeps four layers separate:

1. **AI narrative/decision layer** — represented by agent runtime stubs.
2. **Canonical game state** — represented by SQLAlchemy domain models.
3. **Deterministic rules engine** — represented by a small rules engine stub.
4. **UI and rendering** — left outside the backend core; frontend can consume JSON APIs.

## Implemented backend structure

- `backend/app/main.py` — FastAPI app and startup wiring
- `backend/app/api/` — HTTP endpoints
- `backend/app/services/` — orchestration and read/write boundaries
- `backend/app/models/` — persistent ORM models
- `backend/app/schemas/` — API DTOs
- `backend/app/core/` — config and database
- `backend/app/agents/` — runtime stubs
- `backend/app/rules/` — deterministic rules stub

## Startup behavior

On application startup the backend creates the SQLite tables automatically. This guarantees that `http://localhost:8000/` responds immediately once `uvicorn` is running.
