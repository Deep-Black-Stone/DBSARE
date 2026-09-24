# Repository Status

**Current milestone:** Integrated defensive reasoning foundation (Phases 3–7 foundations).

## Verified repository capabilities
- Python packaging metadata and CLI foundation
- deterministic in-memory Brain entity/relationship model
- duplicate-safe graph relationships and neighborhood traversal
- evidence ingestion with UUID identity, UTC observation time, canonical JSON, and SHA-256 integrity fingerprint
- evidence lookup, kind filtering, and structured export
- deterministic evidence normalization into selected Brain entity types
- deterministic correlation of explicit structured relationships
- evidence-grounded reasoning records with bounded confidence
- investigation state machine and safe investigation planner
- safe default policy boundary
- explicit memory categories
- SQLite persistence boundary for memory and evidence
- runtime health reporting
- foundation and integration tests

## Current end-to-end defensive path

```
Structured Evidence
      ↓
Evidence Identity + Integrity
      ↓
Normalization
      ↓
Brain / Environment Model
      ↓
Deterministic Correlation
      ↓
Reasoning Record
      ↓
Investigation Plan
      ↓
Audit / Report Boundary
```

## Not claimed as implemented
- real LLM inference or Qwen3 runtime
- Nmap/Nessus/Wireshark/tshark/Suricata collectors
- production graph database
- autonomous privileged or modifying actions
- production GUI
- STT/TTS voice pipeline
- complete isolated lab deployment
- full PFE end-to-end evaluation
- continual model training or automatic weight updates

Repository status remains conservative: a foundation interface is not treated as a production subsystem.
