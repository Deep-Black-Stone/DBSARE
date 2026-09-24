# Investigation Engine

## Purpose

The Investigation Engine coordinates stateful cybersecurity investigations.

## Lifecycle

```
Event / Alert
 → Identify Event
 → Identify Affected Assets
 → Retrieve Related Evidence
 → Build Timeline
 → Correlate
 → Form Hypotheses
 → Determine Missing Evidence
 → Request Additional Authorized Evidence
 → Analyze
 → Explain
 → Recommend
 → Permission Check
 → Execute Authorized Action
 → Verify
 → Store Outcome
```

## Operating modes

- Observe-only
- Recommend-only
- Human-approved execution
- Policy-authorized execution

The engine must preserve an investigation state and audit trail.
