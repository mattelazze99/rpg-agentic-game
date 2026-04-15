# Multi-Agent RPG V1

This repository contains an early foundation for a **Multi-Agent RPG** inspired by tabletop fantasy systems. It is under active development and currently includes high-level design documents along with an initial frontend application.

## Repository structure

| Path | Description |
| --- | --- |
| `frontend/` | React + TypeScript client for session management and placeholder views. |
| `00_master_instructions.md` | Global design principles and mandatory architectural guidelines. |
| `02_prompt_backend_foundation.md` | Specification for implementing the backend foundation. |
| `03_prompt_frontend_foundation.md` | Specification for implementing the frontend foundation. |

## Development

### Frontend

The frontend lives in the `frontend/` directory. It provides basic screens to create and view sessions and placeholder views for the world and event log. The client communicates with the backend via HTTP using a small wrapper in `src/api/api.ts`.

### Backend

The backend is not included in this bundle.
