# Entity Model

## Phase 0 conceptual contract

Every entity should have a stable identity, type, provenance references and lifecycle metadata where applicable.

### Host
Identity, addresses, identifiers, observed OS, hostname and evidence references.

### Service
Identity, host relationship, protocol, port, state, banner/version observations and provenance.

### Vulnerability
Identifier, affected entity, severity metadata, source and evidence references.

### Event
Timestamp, type, affected entities, source and evidence references.

### Investigation
Identity, trigger, state, hypotheses, evidence references, actions and outcome.

These are conceptual contracts, not implemented schemas.
