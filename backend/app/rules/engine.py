"""Deterministic rules engine stub."""


class RulesEngine:
    def validate_action(self, state: object, action: object) -> bool:
        return True

    def apply_action(self, state: object, action: object) -> object:
        return state
