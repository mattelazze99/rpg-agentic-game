# Multi‑Agent RPG V1

This repository hosts **Multi‑Agent RPG V1**, a web‑based 2D role‑playing game inspired by tabletop fantasy systems such as **Dungeons & Dragons**.  The project is designed around one human player, three distinct AI players and one AI game master, all scoped strictly to a single session with no memory carry‑over.  It separates narrative generation, canonical game state, deterministic rules and user interface into well defined layers to ensure clarity and extensibility.

## Goals

The objective of this initial milestone is to provide a serious and extensible foundation that supports:

- A Python backend exposing a JSON API for session management, worldbuilding and game state operations.
- A TypeScript/React frontend that consumes the API and renders the game world in the browser.
- A rules engine that keeps gameplay deterministic and separates legal moves from AI suggestions.
- Placeholders for AI agents (players and master) that will later connect to language models and generate narrative or propose actions.
- Clear documentation describing system layers, module boundaries and the intended lifecycle of sessions and agents.

This repository is **not** a complete game.  It intentionally limits the scope of version 1 to create a coherent baseline on which future iterations can build.

## Repository structure

The top level folders are organised as follows:

| Path        | Purpose                                                            |
|-------------|--------------------------------------------------------------------|
| `backend/`  | Python FastAPI application containing the API, domain models, rules engine, agent runtimes and services. |
| `frontend/` | React + TypeScript application responsible for rendering the game UI and communicating with the backend. |
| `docs/`     | Architecture documentation and design notes.                        |

Additional root files include:

- `.gitignore` – rules to prevent committing generated files and local environments.
- `requirements.txt` (inside `backend/`) – Python dependencies for the backend.
- `package.json` (inside `frontend/`) – npm dependencies for the frontend.

## Getting started

### Prerequisites

- [Python 3.10+](https://www.python.org) with `venv` or similar for managing packages
- [Node.js 18+](https://nodejs.org) for the frontend

### Backend

1. Navigate to the `backend/` directory:

   ```sh
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.  Visit `http://localhost:8000/docs` for interactive documentation provided by FastAPI.

### Frontend

1. Navigate to the `frontend/` directory:

   ```sh
   cd frontend
   npm install
   npm run dev
   ```

2. Open `http://localhost:5173` in your browser to see the placeholder interface.

## Contributing

Contributions should adhere to the layered architecture outlined in the `docs` directory.  Please avoid adding AI logic directly to the rules or state layers.  All AI capabilities should be implemented through clearly defined agent interfaces.
