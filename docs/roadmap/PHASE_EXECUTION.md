# DBSARE Phase Execution Plan

## Phase 0 — Architecture & Documentation
**Status: Foundation completed.** Architecture, contracts, trust boundaries, failure model, security model, research scope, lab model, and documentation index are present.

## Phase 1 — Linux Foundation
**Status: Initial implementation started.** Python package, CLI entry point, runtime health primitive, packaging, and foundation tests are present. Remaining work: installer, distro detection, service lifecycle, configuration, resource detection, and integration tests.

## Phase 2 — LLM Abstraction
**Status: Architecture + interface foundation.** The LLM remains replaceable. Backend adapters, capability discovery, timeout/error policy, and evaluation harness remain implementation work.

## Phase 3 — Cyber Evidence Layer
**Status: Initial implementation started.** Evidence object, provenance fingerprint, and ingestion boundary exist. Remaining work: real collectors, parsers, schema validation, retention, and storage.

## Phase 4 — Environment Model
**Status: Design complete; implementation foundation started.** Brain entities/relationships provide the initial model. Remaining work: persistent graph, identity resolution, temporal state, and synchronization.

## Phase 5 — Brain & Persistent Memory
**Status: Initial abstractions started.** Memory abstraction exists. Remaining work: persistent stores, retrieval, consolidation, knowledge validation, and retention policy.

## Phase 6 — Reasoning & Correlation
**Status: Initial implementation started.** Reasoning records exist. Remaining work: correlation, deterministic rules, LLM-assisted analysis, uncertainty propagation, and evaluation.

## Phase 7 — Investigation Engine
**Status: Initial implementation started.** Investigation state machine exists. Remaining work: planner, evidence requests, timelines, hypothesis lifecycle, stopping criteria, and replay.

## Phase 8 — Permission & Action System
**Status: Safe foundation started.** Modifying actions are denied by default. Remaining work: policy language, allowlists, approvals, execution isolation, verification, and audit storage.

## Phase 9 — GUI
**Status: Planned implementation.** GUI will consume the same Core APIs and expose dashboard, network, hosts, services, alerts, investigations, evidence, timeline, Brain graph, reports, permissions, and status.

## Phase 10 — Voice
**Status: Planned implementation.** Voice remains an interaction layer: microphone -> STT -> intent -> Core -> response -> TTS.

## Phase 11 — Controlled Cyber Lab
**Status: Architecture defined.** The lab will use isolated, authorized targets and reproducible scenarios.

## Phase 12 — Integrated PFE Demonstration
**Status: Planned integration.** End-to-end evidence -> Brain -> reasoning -> investigation -> recommendation -> verification -> report evaluation.

## Phase 13 — Future Research
**Status: Research.** Graph reasoning, continual knowledge acquisition, autonomous investigation, multi-agent systems, trustworthy AI, and AI + cybersecurity research.

## Engineering rule
A feature is marked **Implemented** only after repository verification and tests. Roadmap diagrams are not implementation claims.
