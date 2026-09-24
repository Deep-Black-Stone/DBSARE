# System Architecture

## Status

**[Proposed] Phase 0 architecture**

## Mission

DBSARE is a Linux-native AI cybersecurity system that combines evidence collection, environment modeling, graph-oriented knowledge, persistent memory, reasoning, investigation, policy-controlled actions, and user interaction.

## Layer model

### Interaction Layer
GUI, CLI and Voice provide access to the same DBSARE core.

### Agent Core
Coordinates state, capabilities, evidence, reasoning, investigation, memory and policy.

### Reasoning Engine
Transforms trusted/normalized context into hypotheses, analysis, recommendations and investigation decisions. An LLM may support this layer but does not own the architecture.

### Investigation Engine
Runs a stateful investigation lifecycle: identify event, identify assets, retrieve evidence, build timeline, correlate, form hypotheses, determine missing evidence, collect authorized evidence, analyze, explain, recommend, execute if authorized, verify and retain outcome.

### Brain
Represents cybersecurity entities and relationships.

### Memory
Retains contextual and historical information.

### Environment Model
Represents the current and historical state of the observed environment.

### Evidence & Correlation
Collects, parses, normalizes, stores and correlates observations.

### Permission & Action System
Controls all potentially modifying operations.

### Observability
Records system health, decisions, actions and audit events.

## Master flow

```
Interaction
   ↓
Core
   ├→ Reasoning ← Evidence / Environment / Knowledge
   ├→ Investigation
   ├→ Brain ↔ Environment
   ├→ Memory ↔ Brain
   ├→ Evidence → Collectors → Authorized Tools
   └→ Actions → Policy / Approval → Linux
```

## Architectural invariant

The LLM is replaceable. DBSARE must remain conceptually valid if its LLM backend changes or is temporarily unavailable.
