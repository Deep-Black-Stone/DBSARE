# Evidence Normalization

Normalization converts heterogeneous tool/system outputs into common structured representations.

Conceptual stages:

```
Raw Output
 → Parse
 → Validate
 → Normalize
 → Attach Provenance
 → Correlate
```

## Current implementation

`dbsare.normalization.normalize()` provides a deterministic schema-level boundary from a validated `Evidence` object into the in-memory Brain.

Currently supported evidence kinds:

- `host`
- `service`
- `port`
- `dns_event`
- `connection`
- `vulnerability`
- `alert`

For `host`, `service`, and `port`, the normalizer creates or updates Brain entities and establishes only relationships explicitly represented by structured fields. Unsupported kinds return no entities rather than attempting free-text interpretation.

## Safety and provenance

Normalization does not execute commands, perform network discovery, or treat observed text as instructions. Evidence remains the authoritative source object; Brain entities are derived representations.

Normalization must preserve source meaning and must not silently invent fields or certainty. Future collectors should parse and validate their own source formats before handing structured evidence to this boundary.
