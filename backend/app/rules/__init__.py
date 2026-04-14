"""Rules engine package.

Contains deterministic logic for validating and applying actions, resolving
combat, movement and other game mechanics.  The AI agents must not override
these rules; they may only propose actions which are then checked by the
engine.
"""