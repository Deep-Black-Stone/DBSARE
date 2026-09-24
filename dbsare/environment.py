"""Environment model facade over the Brain."""
from .brain import Brain, Entity

class EnvironmentModel:
    def __init__(self, brain: Brain | None = None) -> None:
        self.brain = brain or Brain()

    def register_host(self, host_id: str, **attributes) -> Entity:
        return self.brain.upsert(Entity(host_id, "host", attributes))

    def register_service(self, service_id: str, **attributes) -> Entity:
        return self.brain.upsert(Entity(service_id, "service", attributes))
