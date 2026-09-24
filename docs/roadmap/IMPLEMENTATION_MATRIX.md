# Implementation Matrix

| Capability | Current repository state | Next target |
|---|---|---|
| Linux runtime | Foundation implemented | installer lifecycle + resource-aware runtime |
| CLI | Foundation implemented (status, brain, evidence, investigate, health) | operational workflows and richer output |
| Evidence identity/integrity | Implemented | stronger schema validation + durable store |
| Evidence collection | JSON collector foundation | real authorized cybersecurity collectors |
| Evidence normalization | Deterministic normalization implemented | broader schemas + parser coverage |
| Brain graph | In-memory implemented | persistent graph + temporal model |
| Environment model | Foundation implemented | identity resolution + synchronization |
| Memory | Explicit categories + SQLite persistence boundary | retrieval/consolidation/validation |
| Correlation | Deterministic structured correlation implemented | richer correlation rules + temporal correlation |
| Reasoning | Evidence-grounded record + bounded confidence | LLM-assisted reasoning + uncertainty propagation |
| Investigation | State machine + safe planner implemented | evidence requests + timelines + replay |
| Policy | Safe boundary implemented; modifying actions denied by default | approvals + allowlists + execution isolation |
| Audit | Foundation implemented | durable audit/event storage |
| LLM | Replaceable contract + OpenAI-compatible adapter | real model runtime integration and evaluation |
| GUI | Static/boundary foundation | production interactive interface |
| Voice | Contract/boundary foundation | STT/TTS pipeline |
| Lab | Synthetic controlled scenario | reproducible isolated cyber lab |
| PFE integration | Defensive pipeline foundation | full end-to-end evaluation |

## Status semantics

- **Foundation implemented** = repository code exists and is intentionally bounded.
- **Implemented** = capability is present at the documented scope.
- **Planned** = not yet implemented.
- **Research** = future experimental direction.

The matrix deliberately does not claim Qwen3 inference, real security-tool collectors, autonomous privileged actions, production GUI/voice, or complete PFE evaluation.
