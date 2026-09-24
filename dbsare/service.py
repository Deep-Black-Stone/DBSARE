"""Core service lifecycle state."""
from dataclasses import dataclass

@dataclass
class ServiceState:
    running: bool = False

class DBSAREService:
    def __init__(self) -> None:
        self.state=ServiceState()

    def start(self) -> None:
        self.state.running=True

    def stop(self) -> None:
        self.state.running=False
