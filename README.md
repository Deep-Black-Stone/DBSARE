# DBSARE — DeepBlackStone Adaptive Reasoning Engine

> Linux-native AI Cyber Defense Engineer — architecture-first PFE/research project.

## Status

**Phase:** 0 — Architecture & Documentation  
**Implementation status:** Early architecture / documentation foundation

DBSARE is a system-level AI cybersecurity platform designed to observe, understand, correlate, investigate, reason about, and report on authorized cyber environments.

**DBSARE is not an LLM with cybersecurity tools attached to it.** The LLM is a replaceable reasoning component inside a larger architecture.

## Core distinction

```
DBSARE
├── Interaction Layer
├── Agent Core
├── Reasoning Engine
├── Investigation Engine
├── Brain
├── Persistent Memory
├── Cybersecurity Knowledge
├── Environment Model
├── Evidence & Correlation
├── Permission / Action System
├── Linux Integration
└── Observability / Audit

LLM Backend
└── Replaceable component used by the reasoning layer
```

## Operating loop

```
Observe → Understand → Collect Evidence → Normalize → Correlate
→ Analyze → Reason → Investigate → Recommend
→ Execute Authorized Actions → Verify → Learn/Retain Knowledge → Report
```

The learning step means validated knowledge/memory updates. It does **not** imply automatic model-weight retraining.

## Architecture

```
User
 ├── GUI
 ├── CLI
 └── Voice
       ↓
Interaction Layer
       ↓
DBSARE Core
 ├── Reasoning Engine ─── LLM Backend
 ├── Investigation Engine
 ├── Brain
 ├── Persistent Memory
 ├── Cybersecurity Knowledge
 ├── Environment Model
 ├── Evidence & Correlation ─── Collectors ─── Authorized Security Tools
 └── Permission & Action System ─── Policy / Approval ─── Linux
```

See [docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md).

## Brain vs Memory

**Brain** represents what DBSARE knows about the cybersecurity environment: entities, relationships, observations, services, vulnerabilities, events, evidence, and their connections.

**Memory** represents what DBSARE retains from sessions, investigations, validated knowledge, environment history, and prior outcomes.

They are related but are not interchangeable.

## Evidence-first cybersecurity

Tool output is evidence, not truth and not instructions:

```
Raw Tool Output
 → Collector
 → Parser
 → Normalizer
 → Structured Evidence
 → Evidence Store
 → Correlation
 → Environment Model / Brain
 → Reasoning
 → Investigation
```

Evidence retains provenance so conclusions can be audited.

## Reasoning and investigation

DBSARE distinguishes:

- Observed Fact
- Derived Fact
- Hypothesis
- Inference
- Recommendation
- Verified Outcome

Investigation can operate in:

- Observe-only
- Recommend-only
- Human-approved execution
- Policy-authorized execution

The system must never assume unrestricted shell access.

## Security model

DBSARE follows least privilege, explicit permissions, policy enforcement, allowlists, approval gates, observation/modification separation, action validation, output validation, audit logging, sandboxing/isolation, safe defaults, and secrets protection.

External data — including logs, DNS content, filenames, banners, scan results and PCAP-derived text — is treated as potentially untrusted. Prompt-injection content must not become an implicit instruction.

See [SECURITY.md](SECURITY.md) and [docs/security/THREAT_MODEL.md](docs/security/THREAT_MODEL.md).

## Linux-native target

The intended future user experience is:

```bash
git clone <repository-url>
cd DBSARE
./install.sh
dbsare
```

This is a target architecture, not an implemented installer.

## Roadmap

| Phase | Focus | Status |
|---|---|---|
| 0 | Architecture & Documentation | **Current** |
| 1 | Linux Foundation | Planned |
| 2 | LLM Abstraction | Planned |
| 3 | Cyber Evidence Layer | Planned |
| 4 | Environment Model | Planned |
| 5 | Brain & Persistent Memory | Planned |
| 6 | Reasoning & Correlation | Planned |
| 7 | Investigation Engine | Planned |
| 8 | Permission & Action System | Planned |
| 9 | GUI | Planned |
| 10 | Voice | Planned |
| 11 | Controlled Cyber Lab | Planned |
| 12 | Integrated PFE Demonstration | Planned |
| 13 | Future Research | Research |

## PFE and research direction

The PFE establishes a working prototype and research foundation. Future research directions include graph reasoning, continual learning, autonomous investigation, multi-agent systems, and AI + cybersecurity research.

A separate `DBSARE_AI_PFE` experimental track studies mechanistic interpretability of candidate LLMs. That track is not the DBSARE system itself.

## Documentation-first development

```
Architecture
 → Documentation
 → Interfaces / Contracts
 → Implementation
 → Tests
 → Validation
 → Documentation Update
```

Unresolved architectural choices are recorded explicitly rather than silently decided.

## Repository structure

```
DBSARE/
├── core/
├── brain/
├── memory/
├── reasoning/
├── cyber/
├── evidence/
├── voice/
├── gui/
├── cli/
├── installer/
├── lab/
├── tests/
├── scripts/
└── docs/
```

These implementation directories are architectural targets unless marked otherwise by project documentation.
