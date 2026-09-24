"""DBSARE orchestration core."""

from .brain import Brain
from .evidence import EvidencePipeline
from .investigation import InvestigationEngine

class DBSARECore:
    def __init__(self) -> None:
        self.brain = Brain()
        self.evidence = EvidencePipeline()
        self.investigation = InvestigationEngine()

    def status(self) -> str:
        return "DBSARE core online; observation/reasoning foundation initialized."
