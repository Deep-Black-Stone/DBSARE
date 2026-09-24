"""Deterministic in-memory environment graph for the initial DBSARE foundation."""
from dataclasses import dataclass, field

@dataclass
class Entity:
    id: str
    type: str
    attributes: dict = field(default_factory=dict)

class Brain:
    def __init__(self) -> None:
        self.entities: dict[str, Entity] = {}
        self.relationships: list[tuple[str, str, str]] = []

    def upsert(self, entity: Entity) -> Entity:
        if not entity.id or not entity.type:
            raise ValueError("entity id and type are required")
        self.entities[entity.id] = entity
        return entity

    def relate(self, source: str, relation: str, target: str) -> None:
        if source not in self.entities or target not in self.entities:
            raise KeyError("both relationship endpoints must exist")
        if not relation:
            raise ValueError("relationship type is required")
        edge = (source, relation, target)
        if edge not in self.relationships:
            self.relationships.append(edge)

    def neighbors(self, entity_id: str, relation: str | None = None) -> list[Entity]:
        ids = {
            target for source, rel, target in self.relationships
            if source == entity_id and (relation is None or rel == relation)
        }
        return [self.entities[item] for item in ids]

    def related_to(self, entity_id: str, relation: str | None = None) -> list[Entity]:
        ids = {
            source for source, rel, target in self.relationships
            if target == entity_id and (relation is None or rel == relation)
        }
        return [self.entities[item] for item in ids]

    def summary(self) -> str:
        return f"entities={len(self.entities)} relationships={len(self.relationships)}"
