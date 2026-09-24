"""DBSARE orchestration core."""
from .audit import AuditEvent
from .brain import Brain
from .config import Config
from .evidence import EvidencePipeline
from .investigation import InvestigationEngine
from .memory import Memory
from .policy import PolicyEngine
from .reasoning import ReasoningEngine
from .environment import EnvironmentModel

class DBSARECore:
    def __init__(self, config: Config | None = None) -> None:
        self.config = config or Config.from_env()
        self.brain = Brain()
        self.environment = EnvironmentModel(self.brain)
        self.evidence = EvidencePipeline()
        self.memory = Memory()
        self.reasoning = ReasoningEngine()
        self.investigation = InvestigationEngine()
        self.policy = PolicyEngine()
        self.audit: list[AuditEvent] = []

    def record_audit(self, actor: str, event: str, target: str, result: str) -> AuditEvent:
        item = AuditEvent.create(actor, event, target, result)
        self.audit.append(item)
        return item

    def status(self) -> str:
        return (
            "DBSARE core online; "
            f"mode={self.config.mode}; "
            f"brain={len(self.brain.entities)}; "
            f"evidence={len(self.evidence.items)}; "
            f"memory={len(self.memory.entries)}"
        )
