"""Deterministic correlation of structured evidence records."""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Correlation:
    left_id: str
    relation: str
    right_id: str
    reason: str

class CorrelationEngine:
    """Create only explicitly supported, deterministic correlations."""

    def correlate(self, records: list[dict[str, Any]]) -> list[Correlation]:
        results: list[Correlation] = []
        seen: set[tuple[str, str, str]] = set()
        by_host: dict[str, str] = {}
        for record in records:
            rid = record.get("id")
            if not rid:
                continue
            host = record.get("host") or record.get("host_id")
            if host and host in by_host and by_host[host] != rid:
                item = Correlation(by_host[host], "same_host", rid, "matching host identifier")
                key = (item.left_id, item.relation, item.right_id)
                if key not in seen:
                    results.append(item)
                    seen.add(key)
            elif host:
                by_host[host] = rid

        for left in records:
            left_id = left.get("id")
            left_host = left.get("host_id")
            if not left_id or not left_host:
                continue
            for right in records:
                right_id = right.get("id")
                if right_id and right_id != left_id and right.get("id") == left_host:
                    item = Correlation(left_id, "belongs_to", right_id, "explicit host_id reference")
                    key = (item.left_id, item.relation, item.right_id)
                    if key not in seen:
                        results.append(item)
                        seen.add(key)
        return results
