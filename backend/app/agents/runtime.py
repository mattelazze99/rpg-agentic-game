"""Agent runtime stubs."""

from dataclasses import dataclass


@dataclass
class AIPlayerRuntime:
    name: str
    persona: str

    def propose_action(self) -> dict:
        return {"type": "wait", "reason": f"{self.name} is observing the situation."}


@dataclass
class MasterRuntime:
    name: str
    style: str

    def describe_scene(self, scene_name: str) -> str:
        return f"{self.name} frames the scene '{scene_name}' in a {self.style.lower()} voice."
