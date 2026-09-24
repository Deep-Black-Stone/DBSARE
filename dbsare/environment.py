"""Environment model facade over the Brain."""
from .brain import Brain, Entity

class EnvironmentModel:
    def __init__(self, brain: Brain | None = None) -> None:
        self.brain = brain or Brain()

    def register_host(self, host_id: str, **attributes) -> Entity:
        return self.brain.upsert(Entity(host_id, "host", attributes))

    def register_service(self, service_id: str, **attributes) -> Entity:
        entity = self.brain.upsert(Entity(service_id, "service", attributes))
        host_id = attributes.get("host_id")
        if host_id and host_id in self.brain.entities:
            self.brain.relate(host_id, "runs", service_id)
        return entity

    def register_port(self, port_id: str, **attributes) -> Entity:
        entity = self.brain.upsert(Entity(port_id, "port", attributes))
        host_id = attributes.get("host_id")
        if host_id and host_id in self.brain.entities:
            self.brain.relate(host_id, "exposes", port_id)
        return entity
