"""Evidence collection boundary and normalization primitives."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib

@dataclass
class Evidence:
    source: str
    kind: str
    payload: dict
    observed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sha256: str = ""

    def __post_init__(self) -> None:
        raw = repr((self.source, self.kind, self.payload, self.observed_at)).encode()
        self.sha256 = hashlib.sha256(raw).hexdigest()

class EvidencePipeline:
    def __init__(self) -> None:
        self.items: list[Evidence] = []

    def ingest(self, source: str, kind: str, payload: dict) -> Evidence:
        item = Evidence(source=source, kind=kind, payload=payload)
        self.items.append(item)
        return item

    def summary(self) -> str:
        return f"evidence_items={len(self.items)}"
