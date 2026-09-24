"""Safe investigation planner: plans evidence needs without executing them."""
from dataclasses import dataclass

@dataclass(frozen=True)
class InvestigationStep:
    name: str
    purpose: str
    requires_authorization: bool = False

class InvestigationPlanner:
    def plan(self, hypothesis: str) -> list[InvestigationStep]:
        return [
            InvestigationStep("retrieve_related_evidence", "Collect already-authorized evidence related to the hypothesis."),
            InvestigationStep("build_timeline", "Order observations by time and source."),
            InvestigationStep("evaluate_hypothesis", "Compare evidence against the hypothesis."),
            InvestigationStep("report", "Produce findings, uncertainty, and recommended next step."),
        ]
