"""Evidence-grounded reasoning records."""

from dataclasses import dataclass, field

@dataclass
class ReasoningRecord:
    evidence_ids: list[str] = field(default_factory=list)
    hypotheses: list[str] = field(default_factory=list)
    confidence: float | None = None
    rationale_summary: str = ""

class ReasoningEngine:
    def analyze(self, evidence_ids: list[str], hypothesis: str) -> ReasoningRecord:
        return ReasoningRecord(
            evidence_ids=evidence_ids,
            hypotheses=[hypothesis],
            rationale_summary="Evidence references and hypothesis recorded; no hidden chain-of-thought exposed.",
        )
