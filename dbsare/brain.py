"""In-memory environment graph for the initial foundation."""

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
        self.entities[entity.id] = entity
        return entity

    def relate(self, source: str, relation: str, target: str) -> None:
        if source in self.entities and target in self.entities:
            self.relationships.append((source, relation, target))

    def summary(self) -> str:
        return f"entities={len(self.entities)} relationships={len(self.relationships)}"
