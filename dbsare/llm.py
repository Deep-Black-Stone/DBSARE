"""Model-agnostic LLM contract."""
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class LLMRequest:
    prompt: str
    system: str = ""

@dataclass(frozen=True)
class LLMResponse:
    text: str
    model: str
    metadata: dict

class LLMBackend(Protocol):
    def generate(self, request: LLMRequest) -> LLMResponse: ...

class UnconfiguredLLM:
    def generate(self, request: LLMRequest) -> LLMResponse:
        raise RuntimeError("No LLM backend is configured.")
