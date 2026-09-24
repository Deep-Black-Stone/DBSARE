# Component Architecture

**[Proposed]**

| Component | Responsibility | Must not own |
|---|---|---|
| Interaction Layer | GUI/CLI/Voice access | Core reasoning state |
| Agent Core | Orchestration and lifecycle | Direct unrestricted execution |
| Reasoning Engine | Analysis, hypotheses, recommendations | Authorization |
| Investigation Engine | Stateful investigations | Unbounded autonomy |
| Brain | Entities and relationships | Raw transient context only |
| Memory | Retained context/history/knowledge | Authorization |
| Environment Model | Current/historical environment state | User interface |
| Evidence Layer | Collection, parsing, normalization, provenance | Final conclusions |
| Action System | Controlled execution | LLM authority |
| LLM Backend | Language/model inference | System architecture |

Interfaces between components should be documented before implementation.