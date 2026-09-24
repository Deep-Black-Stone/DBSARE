"""GUI boundary. Production UI remains separate from Core."""
class GUIFacade:
    def __init__(self, core) -> None:
        self.core = core

    def snapshot(self) -> dict:
        return {"status": self.core.status(), "brain": self.core.brain.summary(), "evidence": self.core.evidence.summary(), "investigation": self.core.investigation.summary()}
