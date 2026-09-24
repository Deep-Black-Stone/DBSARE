# Trust Boundaries

## Boundary 1 — User ↔ Interaction Layer
User input is interpreted according to explicit interface contracts.

## Boundary 2 — External Observations ↔ Evidence Layer
Logs, scan results, DNS data, banners, filenames and packet-derived text are untrusted data.

## Boundary 3 — Evidence ↔ Reasoning
Only normalized, validated context should enter reasoning workflows, with provenance retained.

## Boundary 4 — Reasoning ↔ Actions
Reasoning can propose actions; policy and permissions authorize them.

## Boundary 5 — Actions ↔ Linux Environment
Execution occurs within explicit resource and privilege boundaries.

No boundary may be bypassed merely because an LLM requested it.