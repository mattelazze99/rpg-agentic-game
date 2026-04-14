"""Stub implementation of a player AI agent."""


class PlayerAgent:
    """AI player agent.

    This class defines the interface for an AI‑controlled player.  It must
    propose actions based on the current canonical game state while obeying
    deterministic rules.  In V1 it raises `NotImplementedError` to signal
    that the implementation has not yet been provided.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def propose_action(self, state: object) -> object:
        """Suggest the next action for this player.

        Parameters
        ----------
        state: object
            The current canonical game state.

        Returns
        -------
        object
            A proposed action.  The exact type will be defined in the rules
            module.  For now this method raises `NotImplementedError`.
        """
        raise NotImplementedError("PlayerAgent.propose_action is not yet implemented.")