# Implementation Matrix

> **State basis:** Latest read-only audit of `~/DBSARE_AI_PFE` on 2026-09-24. This matrix describes the **real WSL implementation state**. GitHub architecture/reference code is tracked separately and is not treated as WSL implementation evidence.

| Capability | Real WSL state | GitHub architecture/reference state | Next target |
|---|---|---|---|
| Linux runtime | Not implemented | Architecture/reference foundation | minimal Linux runtime + lifecycle |
| CLI | Not implemented | CLI architecture/reference exists | safe CLI entry point |
| Core | Not implemented | Core architecture/reference exists | minimal Core lifecycle/orchestration |
| LLM | Qwen3 research loader only; no DBSARE abstraction | LLM abstraction documented | replaceable DBSARE LLM boundary |
| Evidence identity/integrity | Not implemented | Evidence contracts/reference exist | evidence schema + store |
| Evidence collection | Not implemented | Collector architecture documented | first read-only collector |
| Evidence normalization | Not implemented | Normalization contract documented | deterministic normalization |
| Brain graph | Not implemented | Brain model documented | initial environment graph |
| Environment model | Not implemented | Environment architecture documented | host/service/environment state |
| Memory | Not implemented | Memory model documented | explicit memory boundary + persistence |
| Correlation | Not implemented | Correlation architecture documented | deterministic structured correlation |
| Reasoning | Not implemented | Reasoning model documented | evidence-grounded reasoning records |
| Investigation | Not implemented | Investigation lifecycle documented | bounded investigation state machine |
| Policy | Not implemented | Security/policy architecture documented | deny-by-default policy boundary |
| Actions | Not implemented | Authorized-action model documented | proposal-only action boundary |
| Audit | Not implemented | Audit architecture documented | durable audit events |
| GUI | Not implemented | GUI boundary documented | interface skeleton after core |
| Voice | Not implemented | Voice contract documented | interaction boundary after core |
| Lab | Not implemented | Lab architecture documented | synthetic controlled scenario |
| PFE integration | Not implemented | PFE scope documented | end-to-end integration |
| Qwen research | Implemented | Research scope documented | Exp9 + confound controls |
| Tests | No DBSARE project tests | Testing strategy documented | tests from Phase 1 onward |

## Status semantics

- **Implemented** = verified in the real WSL source.
- **Reference foundation** = architecture/documentation or bounded GitHub reference material; not proof of WSL implementation.
- **Planned** = accepted future work.
- **Research** = experimental investigation.

## Critical rule

Do not promote a GitHub reference foundation to **Implemented** until the corresponding WSL implementation exists and has been audited/validated.

The Qwen3 research track must remain separate from DBSARE system implementation.
