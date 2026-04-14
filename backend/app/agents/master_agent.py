"""Stub implementation of the game master AI agent."""


class MasterAgent:
    """AI game master agent.

    Responsible for generating the game world, narrating events, controlling NPCs
    and orchestrating encounters.  The master must consult the rules engine
    before applying any state changes.  In V1 this class only defines the
    interface.
    """

    def generate_world(self) -> dict:
        """Generate the world, factions, locations and hooks.

        Returns
        -------
        dict
            A structured representation of the generated world.  For V1 this
            method raises `NotImplementedError`.
        """
        raise NotImplementedError("MasterAgent.generate_world is not yet implemented.")