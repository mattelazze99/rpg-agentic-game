# Architecture Overview

This document explains the high‑level architecture of **Multi‑Agent RPG V1** and
serves as a guide for developers contributing to the project.  The
architecture emphasises clear separation between narrative generation, game
state, deterministic rules and user interface.  Such separation enables
testability, extensibility and maintainability.

## System layers

The project is organised into four primary layers, each with a distinct
responsibility:

1. **AI narrative/decision layer**
   - Responsible for generating dialogue, scene descriptions, NPC behaviour and
     intent proposals.
   - Implemented via agent classes (`backend/app/agents`).
   - Agents may propose actions but cannot directly modify canonical state.

2. **Canonical game state**
   - Stores all persistent session data such as characters, inventories,
     positions, quests and event history.
   - Implemented via SQLAlchemy ORM models (`backend/app/models`) and managed
     by the service layer.

3. **Deterministic rules engine**
   - Validates proposed actions, resolves checks and combat, and enforces
     game mechanics.
   - Located in the `backend/app/rules` package.
   - Never relies on AI or probabilistic components.

4. **UI and rendering**
   - Implemented in the React frontend (`frontend/`), which consumes the API
     and presents the game world to users.
   - Includes pages, components and an API client to interact with the backend.

Each layer communicates only with its neighbours.  For example, the AI
narrative layer may propose an action that is validated by the rules engine
before updating the canonical state.  The UI layer reads state via the API and
presents it; it never contains game logic.

## Module boundaries

- **Backend**: The Python backend is divided into packages:
  - `app/main.py` – FastAPI application factory and router registration.
  - `app/api/` – HTTP endpoints.  Thin controllers that translate between HTTP
    requests and the service layer.
  - `app/services/` – Business logic orchestrating models, rules and agents.
  - `app/models/` – ORM definitions for all persistent entities.
  - `app/rules/` – Deterministic game logic: validating and applying actions.
  - `app/agents/` – Interfaces and stubs for AI players and the game master.
  - `app/schemas/` – Pydantic models for request/response bodies.
  - `app/core/` – Configuration and infrastructure such as database connection.

- **Frontend**: The TypeScript/React frontend is organised into:
  - `src/` – Application source code.
  - `src/pages/` – Page components mapped to routes.
  - `src/components/` – Reusable UI components.
  - `src/api/` – API client functions to call backend endpoints.
  - `vite.config.ts` – Build configuration for development and production.

## Session lifecycle

1. **Pre‑session discussion**: During character creation the three AI players
   and the human discuss preferences and constraints.  This conversation will
   be facilitated in a future milestone by the agent layer and UI.

2. **Master worldbuilding**: The master agent generates a setting summary,
   factions, tone and initial quest hooks.  The result includes both
   narrative text and structured data.

3. **Character creation**: Based on the discussion and worldbuilding, the AI
   players and human create characters.  Character sheets are validated by
   the rules engine.

4. **Starting scene**: The master agent establishes the opening scene and
   starting area.

5. **Free scene**: Players move freely in a top‑down location without a grid.
   Actions and speech are proposed and validated before affecting state.

6. **Combat**: When combat starts, the rules engine switches to a hex grid.
   Initiative, movement and attacks are resolved deterministically.

7. **Loot and inventory**: Loot is pre‑generated and distributed among
   characters.  Ownership and transfers are handled through the canonical state.

## Agent lifecycle

AI agents are scoped to a single session and have no memory across sessions.
Their responsibilities include:

- Generating narrative descriptions and dialogue.
- Proposing actions during free scenes and combat.
- Respecting the rules engine and canonical state when acting.
- Exhibiting distinct preferences and personalities.

## V1 non‑goals

Version 1 intentionally limits scope to provide a stable foundation.  The
following are **not** part of V1:

- Full tabletop ruleset implementation.
- Persistent accounts or cross‑session memory.
- Multiplayer networking or real‑time features beyond the single human player.
- Comprehensive UI design.  The frontend is currently a placeholder.