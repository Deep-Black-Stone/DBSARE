"""Evidence collection boundary and integrity primitives."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib, json, uuid

@dataclass
class Evidence:
    source: str
    kind: str
    payload: dict
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    observed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sha256: str = ""

    def __post_init__(self) -> None:
        canonical=json.dumps(self.payload, sort_keys=True, separators=(",",":"))
        raw=f"{self.source}|{self.kind}|{self.id}|{self.observed_at}|{canonical}".encode()
        self.sha256=hashlib.sha256(raw).hexdigest()

class EvidencePipeline:
    def __init__(self) -> None:
        self.items: list[Evidence]=[]

    def ingest(self, source: str, kind: str, payload: dict) -> Evidence:
        item=Evidence(source=source, kind=kind, payload=payload)
        self.items.append(item)
        return item

    def summary(self) -> str:
        return f"evidence_items={len(self.items)}"
