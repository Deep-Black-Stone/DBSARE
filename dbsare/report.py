"""Auditable report representation."""
from dataclasses import dataclass, field

@dataclass
class Report:
    title: str
    facts: list[str] = field(default_factory=list)
    hypotheses: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    verification: list[str] = field(default_factory=list)

    def as_text(self) -> str:
        sections=[f"# {self.title}", "## Facts", *[f"- {x}" for x in self.facts], "## Hypotheses", *[f"- {x}" for x in self.hypotheses], "## Recommendations", *[f"- {x}" for x in self.recommendations], "## Verification", *[f"- {x}" for x in self.verification]]
        return "\n".join(sections)
