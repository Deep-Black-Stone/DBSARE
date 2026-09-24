"""Permission boundary for future authorized actions."""

from dataclasses import dataclass

@dataclass(frozen=True)
class ActionRequest:
    action: str
    target: str
    modifying: bool = False

class PolicyEngine:
    def authorize(self, request: ActionRequest) -> bool:
        # Safe foundation: no modifying action is automatically authorized.
        return not request.modifying
