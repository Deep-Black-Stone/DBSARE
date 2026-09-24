# DBSARE Brain Architecture

## Definition

The Brain is DBSARE's structured representation of what it knows about the cybersecurity environment.

It is not merely a database and it is not the LLM context window.

## Core entities

- Host
- IP address
- MAC address
- Operating system
- User
- Process
- Service
- Port
- Domain
- DNS event
- Network connection
- Vulnerability
- Alert
- Incident
- Evidence
- Investigation
- Hypothesis
- Observation

## Example relationships

```
Host → runs → Service
Service → exposes → Port
Service → has → Vulnerability
Host → communicates_with → Host
Host → resolves → Domain
Host → generates → Event
Event → associated_with → Evidence
```

## Traversal example

```
Alert
 → Host
 → Services
 → Ports
 → Connections
 → DNS
 → Historical Observations
 → Vulnerabilities
 → Evidence
 → Investigation
 → Hypothesis
```

The exact graph implementation is an open architectural decision.
