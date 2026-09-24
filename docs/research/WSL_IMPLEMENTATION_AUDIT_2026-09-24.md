# WSL Implementation Audit — 2026-09-24

## Source

Read-only OpenCode audit of:

`/home/deepblackstone/DBSARE_AI_PFE`

No files were modified, created, deleted, installed, committed, or pushed during the audit.

## Executive finding

The WSL project is currently a **co-located research sandbox**, not an implemented DBSARE system.

The directory:

`~/DBSARE_AI_PFE/DBSARE/`

contains only an empty Git initialization and a Python virtual environment. It contains no Python implementation, no DBSARE Core, and no runtime.

The implemented code in the project is the separate `qwen3_analysis/` mechanistic-interpretability research track.

## Actual project composition

| Component | State |
|---|---|
| `DBSARE/` | Empty Git shell + venv; no implementation |
| `qwen3_analysis/` | 7 standalone Python research scripts + 6 JSON results |
| `qwen3_0.6b/` | Local Qwen3-0.6B weights |
| `qwen3_tokenizer/` | Local tokenizer |
| `QWEN3/Qwen3/` | Upstream Qwen3 clone/reference |
| `transformers/` | Upstream Transformers clone |
| Root | No project code/configuration/docs |

## WSL DBSARE implementation matrix

- Core: **Not implemented**
- Brain: **Not implemented**
- Memory: **Not implemented**
- Evidence: **Not implemented**
- Normalization: **Not implemented**
- Correlation: **Not implemented**
- Reasoning: **Not implemented**
- Investigation: **Not implemented**
- Policy/actions: **Not implemented**
- CLI: **Not implemented**
- GUI: **Not implemented**
- Voice: **Not implemented**
- Cyber collectors: **Not implemented**
- Lab: **Not implemented**
- Project tests: **Not implemented**

## Qwen research

The active WSL implementation is the Qwen3-0.6B research track.

### Experiment 8

Experiment 8 performs candidate-neuron causal intervention by zeroing one gated MLP neuron at the target token through a forward pre-hook on `down_proj`.

Reported metrics include:

- KL(baseline || ablated)
- top-1 change
- selectivity ratio
- z-score against 10 random controls per layer

Reported strong candidates:

- L0 N1345 — cyber > general
- L3 N3066 — cyber > general
- L21 N1658 — general > cyber

These are **causal effects in the tested contexts**, not proof of semantic cybersecurity neurons. The lexical vulnerability/weather confound remains a documented limitation.

## Actual executable pipeline

```
Hardcoded probe texts
        ↓
Qwen3-0.6B local model
        ↓
Forward hooks / positional intervention
        ↓
Statistical metrics
        ↓
JSON results
        ↓
Offline result analysis
```

This is a research pipeline, not a DBSARE defensive pipeline.

## Intended DBSARE pipeline

```
Linux telemetry
        ↓
Collectors
        ↓
Parser
        ↓
Normalizer
        ↓
Evidence Store
        ↓
Environment / Brain
        ↓
Correlation
        ↓
Reasoning
        ↓
Investigation
        ↓
Policy
        ↓
Authorized Action
        ↓
Verification
        ↓
Memory / Knowledge
```

None of this pipeline is implemented in the WSL project as of this audit.

## Key architectural observations

1. **Research/production boundary:** `DBSARE_AI_PFE` currently contains research and an empty DBSARE shell, not an integrated system.
2. **Qwen isolation:** Qwen research has no code-level connection to DBSARE.
3. **Greenfield Core:** The future DBSARE Core must be built from the documented architecture; it cannot be synchronized from an existing WSL Core because no such Core exists.
4. **Experiment 6.5 duplication:** The older contrastive script is superseded by the fuller selectivity script; canonical ownership should be documented before further research expansion.
5. **Environment duplication:** Both root and `DBSARE/` contain Python 3.12.13 virtual environments; neither represents a DBSARE runtime environment.
6. **Upstream isolation:** Qwen3 and Transformers sources are third-party references/dependencies, not DBSARE implementation.

## Next engineering target

The audit recommends a minimal greenfield implementation:

1. DBSARE Core lifecycle/orchestration
2. Evidence schema and store
3. One safe read-only Linux collector
4. Deny-by-default policy boundary
5. CLI entry point
6. Tests

The exact implementation sequence remains an architecture decision to be coordinated through Claude and OpenCode.

## Source-of-truth rule

- **Architecture/design:** GitHub documentation + coordinated Claude updates
- **Actual implementation:** WSL `~/DBSARE_AI_PFE`
- **Coding:** OpenCode
- **Research experiments:** `qwen3_analysis/`
- **Qwen3:** replaceable research/model component, not DBSARE itself

This audit is the baseline for future implementation synchronization.
