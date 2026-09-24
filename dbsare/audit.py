"""Audit event model."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class AuditEvent:
    actor: str
    event: str
    target: str
    result: str
    timestamp: str

    @classmethod
    def create(cls, actor: str, event: str, target: str, result: str) -> "AuditEvent":
        return cls(actor, event, target, result, datetime.now(timezone.utc).isoformat())
