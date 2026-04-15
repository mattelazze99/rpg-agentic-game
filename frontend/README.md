# Frontend (Multi-Agent RPG)

This directory contains the initial frontend foundation for the **Multi-Agent RPG V1** project.

## Running the frontend

```bash
cd frontend
npm install
npm run dev
```

Optional `.env`:

```env
VITE_API_BASE=http://localhost:8000
```

## Pages

- `/` home
- `/session/create` create session
- `/session/:sessionId` session detail
- `/world/:sessionId` placeholder world view
- `/log/:sessionId` placeholder event log
