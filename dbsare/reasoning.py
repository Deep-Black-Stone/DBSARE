"""Evidence-grounded reasoning records with explicit uncertainty."""
from dataclasses import dataclass, field

@dataclass
class ReasoningRecord:
    evidence_ids: list[str] = field(default_factory=list)
    hypotheses: list[str] = field(default_factory=list)
    confidence: float | None = None
    rationale_summary: str = ""

    def __post_init__(self) -> None:
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if not self.evidence_ids:
            raise ValueError("reasoning requires at least one evidence reference")
        if not self.hypotheses:
            raise ValueError("reasoning requires at least one hypothesis")

class ReasoningEngine:
    def analyze(self, evidence_ids: list[str], hypothesis: str, confidence: float | None = None) -> ReasoningRecord:
        return ReasoningRecord(
            evidence_ids=list(dict.fromkeys(evidence_ids)),
            hypotheses=[hypothesis],
            confidence=confidence,
            rationale_summary="Evidence references and hypothesis recorded; no hidden chain-of-thought exposed.",
        )
