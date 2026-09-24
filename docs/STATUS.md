# Repository Status

**Current milestone:** Architecture/documentation foundation synchronized with the latest WSL audit.

## Source-of-truth policy

The GitHub repository is currently the **architecture, documentation, contracts, roadmap, and coordination repository** for DBSARE.

The latest read-only audit of the real WSL project at `~/DBSARE_AI_PFE` (2026-09-24) established that:

- `~/DBSARE_AI_PFE/DBSARE/` contains only an empty Git initialization and a Python virtual environment.
- There is **no real DBSARE Core implementation in WSL**.
- There are no WSL implementations of Brain, Memory, Evidence, Reasoning, Investigation, Policy, Actions, CLI, GUI, Voice, or Cyber Collectors.
- The implemented WSL code is the separate `qwen3_analysis/` mechanistic-interpretability research track.
- Qwen3 research has no code-level dependency on DBSARE.
- Therefore, the WSL implementation is currently a **greenfield DBSARE implementation target**, not an implementation that can be synchronized into this repository.

## Current repository capabilities

The GitHub repository contains architecture and bounded reference/foundation code developed during the documentation phase. These repository-side foundations must **not** be interpreted as proof that the corresponding DBSARE system exists in the WSL source of truth.

Repository documentation covers:

- system architecture
- component boundaries
- Brain / Memory concepts
- evidence architecture and contracts
- reasoning and investigation models
- security / trust boundaries
- Linux integration targets
- GUI / CLI / voice contracts
- testing and evaluation strategy
- controlled lab architecture
- PFE and research scope
- roadmap and implementation matrix

## WSL implementation reality

**Verified 2026-09-24 from OpenCode read-only audit:**

| Component | WSL state |
|---|---|
| DBSARE Core | Not implemented |
| Brain | Not implemented |
| Memory | Not implemented |
| Evidence pipeline | Not implemented |
| Normalization | Not implemented |
| Correlation | Not implemented |
| Reasoning | Not implemented |
| Investigation | Not implemented |
| Policy / Actions | Not implemented |
| CLI | Not implemented |
| GUI | Not implemented |
| Voice | Not implemented |
| Cyber collectors | Not implemented |
| Controlled lab | Not implemented |
| Project tests | Not implemented |
| Qwen3 research | Implemented separately |

## Qwen3 research state

The WSL research track contains seven standalone Python scripts and six JSON result files.

Experiment 8 provides causal-in-context intervention evidence for selected Qwen3-0.6B neurons, but the results **do not establish semantic “cybersecurity neurons.”** The documented lexical vulnerability/weather confound remains unresolved.

Qwen3 remains an experimental model/research component, not DBSARE itself.

## Synchronization rule

Until the real WSL implementation exists:

1. Do not copy or invent DBSARE Core code into GitHub based on the architecture alone.
2. Do not claim WSL implementation for components that the WSL audit marked absent.
3. Architecture decisions may continue to evolve in GitHub documentation.
4. Claude remains the architecture/prompt coordination layer.
5. OpenCode remains responsible for actual WSL implementation.
6. WSL remains the implementation source of truth.
7. After an implementation milestone, the real WSL state must be audited before synchronized implementation is represented as verified in GitHub.

This is intentionally conservative: **design is not implementation, and Qwen research is not DBSARE.**
