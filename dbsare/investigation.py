"""Defensive investigation state machine."""

from dataclasses import dataclass, field

@dataclass
class Investigation:
    id: str
    state: str = "created"
    hypotheses: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)

class InvestigationEngine:
    STATES = ("created", "collecting", "analyzing", "validated", "reported", "closed")

    def __init__(self) -> None:
        self.active: dict[str, Investigation] = {}

    def create(self, investigation_id: str) -> Investigation:
        inv = Investigation(investigation_id)
        self.active[inv.id] = inv
        return inv

    def transition(self, investigation_id: str, state: str) -> Investigation:
        if state not in self.STATES:
            raise ValueError("invalid investigation state")
        inv = self.active[investigation_id]
        inv.state = state
        return inv

    def summary(self) -> str:
        return f"active_investigations={len(self.active)}"
