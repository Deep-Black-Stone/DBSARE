# Data Flow

## Evidence pipeline

```
Tool / System Observation
 → Collector
 → Parser
 → Normalizer
 → Evidence Record
 → Evidence Store
 → Correlation
 → Environment Model / Brain
 → Reasoning
 → Investigation
 → Report / Recommendation
```

## Action pipeline

```
Reasoning
 → Action Proposal
 → Policy Evaluation
 → Permission Check
 → Approval if required
 → Execution
 → Verification
 → Audit
 → Memory / Investigation Outcome
```

## Trust boundary

Raw external observations cross into DBSARE as untrusted data. Parsing and normalization create structured representations, but semantic claims remain subject to provenance and confidence evaluation.
