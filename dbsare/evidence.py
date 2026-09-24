"""Evidence collection boundary, normalization hooks, and integrity primitives."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
import uuid
from typing import Any

@dataclass
class Evidence:
    source: str
    kind: str
    payload: dict[str, Any]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    observed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sha256: str = ""

    def __post_init__(self) -> None:
        if not self.source.strip() or not self.kind.strip():
            raise ValueError("evidence source and kind are required")
        if not isinstance(self.payload, dict):
            raise TypeError("evidence payload must be a dictionary")
        canonical = self.canonical_payload()
        raw = f"{self.source}|{self.kind}|{self.id}|{self.observed_at}|{canonical}".encode()
        self.sha256 = hashlib.sha256(raw).hexdigest()

    def canonical_payload(self) -> str:
        return json.dumps(self.payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id, "source": self.source, "kind": self.kind,
            "observed_at": self.observed_at, "payload": self.payload,
            "sha256": self.sha256,
        }

class EvidencePipeline:
    def __init__(self) -> None:
        self.items: list[Evidence] = []

    def ingest(self, source: str, kind: str, payload: dict[str, Any]) -> Evidence:
        item = Evidence(source=source, kind=kind, payload=payload)
        self.items.append(item)
        return item

    def get(self, evidence_id: str) -> Evidence | None:
        return next((item for item in self.items if item.id == evidence_id), None)

    def by_kind(self, kind: str) -> list[Evidence]:
        return [item for item in self.items if item.kind == kind]

    def export(self) -> list[dict[str, Any]]:
        return [item.as_dict() for item in self.items]

    def summary(self) -> str:
        return f"evidence_items={len(self.items)}"
