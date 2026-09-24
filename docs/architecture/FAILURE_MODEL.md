# Failure Model

DBSARE must fail safely and visibly when evidence, tools, models, storage, permissions, or execution fail.

## Failure classes
- Input or evidence failure
- Collection failure
- Parsing/normalization failure
- Correlation failure
- Reasoning failure
- LLM/backend failure
- Memory/Brain persistence failure
- Policy/permission failure
- Execution failure
- Verification failure

## Required behavior
1. Fail closed for privileged or modifying actions.
2. Preserve raw evidence when safe.
3. Record failure and provenance.
4. Distinguish unavailable evidence from negative evidence.
5. Never invent missing state.
6. Permit safe degraded observation/recommendation operation.
7. Verify authorized actions.

Conceptual recovery: Detect -> Contain -> Preserve Evidence -> Diagnose -> Recover -> Verify -> Record.

Phase 0 defines the model; implementation is planned.
