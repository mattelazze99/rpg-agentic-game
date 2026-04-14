# Version 1 Scope and Non‑Goals

This document clarifies the intended capabilities of **Multi‑Agent RPG V1** and
explicitly lists features that are postponed for future versions.  By
codifying the scope the project can remain focused and avoid feature creep.

## Included in V1

- **Session creation** via a simple API call.
- **Three AI players** and **one AI master** as separate agent classes, with
  stub implementations ready for future integration with large language models.
- **Social pre‑session discussion** scaffolding described in the architecture
  documentation, to be implemented later.
- **Structured worldbuilding** generation via the master agent (currently a stub).
- **Limited character creation**: request and response models prepared for
  character creation; validation via the rules engine will be added later.
- **One starting hub or location**: placeholder world summary returned by the
  `/world` endpoint.
- **Event log**: session service returns human‑readable messages; a full event
  log will be implemented in the persistence layer in future iterations.
- **Basic UI**: a React application with routing and components ready to be
  extended; currently displays a welcome screen.
- **Documentation**: architecture, session lifecycle and agent lifecycle
  explanations.

## Deferred to future versions

- **Full tabletop rules engine**: complex checks, spells, classes and
  conditions will be added incrementally.
- **Persistent user accounts** and cross‑session progression.
- **Rich map rendering** beyond simple top‑down display.
- **Networking** for multiple human players.
- **Audio, animations or 3D graphics**.
- **Integration with specific language models**.  The agent stubs do not
  connect to any AI API yet.