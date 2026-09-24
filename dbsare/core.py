"""DBSARE orchestration core."""
from .audit import AuditEvent
from .brain import Brain
from .config import Config
from .correlation import CorrelationEngine
from .environment import EnvironmentModel
from .evidence import Evidence, EvidencePipeline
from .investigation import InvestigationEngine
from .investigator import InvestigationPlanner
from .memory import Memory
from .normalization import normalize
from .policy import PolicyEngine
from .reasoning import ReasoningEngine

class DBSARECore:
    def __init__(self, config: Config | None = None) -> None:
        self.config = config or Config.from_env()
        self.brain = Brain()
        self.environment = EnvironmentModel(self.brain)
        self.evidence = EvidencePipeline()
        self.memory = Memory()
        self.reasoning = ReasoningEngine()
        self.correlation = CorrelationEngine()
        self.investigation = InvestigationEngine()
        self.planner = InvestigationPlanner()
        self.policy = PolicyEngine()
        self.audit: list[AuditEvent] = []

    def ingest_evidence(self, source: str, kind: str, payload: dict) -> Evidence:
        item = self.evidence.ingest(source, kind, payload)
        normalize(item, self.brain)
        self.record_audit("core", "evidence_ingested", item.id, "accepted")
        return item

    def correlate_evidence(self) -> list:
        correlations = self.correlation.correlate(self.evidence.export())
        for item in correlations:
            if item.left_id in self.brain.entities and item.right_id in self.brain.entities:
                self.brain.relate(item.left_id, item.relation, item.right_id)
        return correlations

    def investigate(self, hypothesis: str, evidence_ids: list[str]):
        record = self.reasoning.analyze(evidence_ids, hypothesis)
        investigation = self.investigation.create(f"inv-{len(self.investigation.active) + 1}")
        investigation.hypotheses.append(hypothesis)
        return investigation, self.planner.plan(hypothesis), record

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
