# Observability Architecture

DBSARE must be observable as a security-sensitive system.

## Signals
Structured logs, audit events, action lifecycle events, evidence-ingestion metrics, investigation transitions, backend health, Brain/Memory health, policy decisions, and verification results.

## Correlation
Use investigation, evidence, action, audit, and request identifiers to connect events across subsystems.

## Security
Do not log secrets by default. Protect audit records. Record actor, policy decision, action, and outcome for privileged operations. Treat external text as untrusted data.

Instrumentation is planned.
