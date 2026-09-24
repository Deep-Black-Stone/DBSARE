# Implementation Matrix — WSL Source of Truth

Authoritative OpenCode audit: 2026-09-24.

| Capability | WSL actual state | Next target |
|---|---|---|
| DBSARE Core | Not implemented | lifecycle + orchestration |
| Linux runtime | Not implemented | minimal runtime foundation |
| CLI | Not implemented | safe CLI entry point |
| Evidence | Not implemented | validated evidence contract |
| Collectors | Not implemented | one read-only Linux collector |
| Normalization | Not implemented | deterministic boundary |
| Environment Model | Not implemented | host/service/network model |
| Brain | Not implemented | entity/relationship graph |
| Memory | Not implemented | explicit persistence boundary |
| Correlation | Not implemented | deterministic evidence correlation |
| Reasoning | Not implemented | evidence-grounded reasoning |
| Investigation | Not implemented | state machine + safe planner |
| Policy | Not implemented | deny-by-default policy boundary |
| Actions | Not implemented | authorized action boundary |
| Audit | Not implemented | auditable event records |
| LLM abstraction | Not implemented | replaceable DBSARE LLM contract |
| GUI | Not implemented | interaction boundary |
| Voice | Not implemented | interaction boundary |
| Lab | Not implemented | controlled reproducible lab |
| DBSARE tests | Not implemented | unit + integration + security tests |
| Qwen3 research | Implemented, research-only | stronger causal controls / Experiment 9 |

## Important distinction

GitHub currently contains an earlier foundation implementation. That is a separate repository state and must not be represented as proof that WSL has reached those capabilities.

WSL takes precedence for implementation claims.