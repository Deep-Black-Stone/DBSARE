"""Deterministic normalization from generic evidence into Brain entities.

This module intentionally performs only schema-level normalization. It does not
execute network discovery or infer security conclusions from untrusted text.
"""
from typing import Any
from .brain import Brain, Entity
from .evidence import Evidence

SUPPORTED = {"host", "service", "port", "dns_event", "connection", "vulnerability", "alert"}

def normalize(evidence: Evidence, brain: Brain) -> list[Entity]:
    payload = evidence.payload
    kind = evidence.kind
    if kind not in SUPPORTED:
        return []
    entities: list[Entity] = []
    if kind == "host":
        entity = Entity(
            payload.get("id") or payload.get("ip") or evidence.id,
            "host",
            {k: v for k, v in payload.items() if k not in {"id"}},
        )
        entities.append(brain.upsert(entity))
    elif kind == "service":
        service_id = payload.get("id") or f"service:{payload.get('host_id','unknown')}:{payload.get('name','unknown')}"
        entity = Entity(service_id, "service", dict(payload))
        entities.append(brain.upsert(entity))
        host_id = payload.get("host_id")
        if host_id and host_id in brain.entities:
            brain.relate(host_id, "runs", service_id)
    elif kind == "port":
        port_id = payload.get("id") or f"port:{payload.get('host_id','unknown')}:{payload.get('port','unknown')}"
        entity = Entity(port_id, "port", dict(payload))
        entities.append(brain.upsert(entity))
        host_id = payload.get("host_id")
        if host_id and host_id in brain.entities:
            brain.relate(host_id, "exposes", port_id)
    else:
        entity_id = payload.get("id") or f"{kind}:{evidence.id}"
        entities.append(brain.upsert(Entity(entity_id, kind, dict(payload))))
    return entities
