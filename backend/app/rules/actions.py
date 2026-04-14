"""Action definitions for the game rules.

This module defines the possible actions that agents and players can take in
the game world.  By codifying actions as data structures we can separate
intent proposals (from AI or human players) from deterministic validation and
state application.  For V1 this file contains placeholder classes.
"""

from dataclasses import dataclass


@dataclass
class Action:
    """Base type for all actions."""

    type: str


@dataclass
class MoveAction(Action):
    """Represents a movement action in the free scene.

    Attributes
    ----------
    actor_id: str
        Identifier of the character performing the move.
    dx: int
        Change in x‑position.
    dy: int
        Change in y‑position.
    """

    actor_id: str
    dx: int
    dy: int