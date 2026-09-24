"""Deterministic evidence correlation primitives."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Correlation:
    left_id: str
    relation: str
    right_id: str
    reason: str

class CorrelationEngine:
    def correlate(self, records: list[dict]) -> list[Correlation]:
        results = []
        by_host = {}
        for r in records:
            host = r.get("host")
            rid = r.get("id", "")
            if host and host in by_host:
                results.append(Correlation(by_host[host], "same_host", rid, "matching host identifier"))
            elif host:
                by_host[host] = rid
        return results
