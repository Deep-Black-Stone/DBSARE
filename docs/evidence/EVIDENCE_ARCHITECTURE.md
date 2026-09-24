# Evidence Architecture

## Purpose

Evidence is the bridge between cybersecurity tools/system observations and DBSARE reasoning.

## Pipeline

```
Raw Output
 → Collector
 → Parser
 → Normalizer
 → Structured Evidence
 → Evidence Store
 → Correlation
```

## Provenance requirements

Where available, evidence should identify:

- source/tool
- observation timestamp
- collection context
- parser/transformations
- related entities
- integrity metadata
- confidence metadata
- raw-source reference

## Principle

A tool is an evidence source, not the DBSARE brain.
