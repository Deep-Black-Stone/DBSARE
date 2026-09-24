# Architectural Decisions

## ADR-001 — DBSARE is larger than its LLM

**Decision:** The system architecture treats the LLM as a replaceable backend component.

**Rationale:** Cybersecurity evidence, state, memory, permissions, investigation lifecycle and auditability cannot be delegated to a model context window.

## ADR-002 — Evidence has provenance

**Decision:** Evidence records must preserve source, time, transformation/provenance and integrity/confidence metadata where applicable.

**Rationale:** Cybersecurity conclusions must be traceable.

## ADR-003 — Brain and Memory are separate concepts

**Decision:** Brain models cyber-environment knowledge and relationships; Memory models retained experience/context/history.

**Rationale:** A graph of the environment is not equivalent to a history of what the system retained.

## ADR-004 — No unrestricted autonomous shell

**Decision:** Actions pass through policy and permission controls.

**Rationale:** Prevent uncontrolled modification and privilege escalation.

## ADR-005 — Documentation is source of truth

**Decision:** Architecture changes must be documented before or with implementation.

**Rationale:** Prevent implementation drift and silent architectural decisions.

## Open decisions

- Exact graph/storage technology.
- Exact memory storage technology.
- LLM runtime and model selection.
- Evidence schema serialization format.
- Policy language and enforcement implementation.
- GUI framework.
- Voice/STT/TTS stack.
- Sandbox/isolation mechanism.
