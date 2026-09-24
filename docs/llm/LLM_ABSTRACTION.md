# LLM Abstraction

## Principle

Qwen3 or another model is a replaceable backend, not DBSARE itself.

## Interface responsibility

The abstraction should eventually define:

- model invocation
- structured input/output
- context assembly
- timeout/error handling
- capability metadata
- token/resource limits
- model availability state

The initial architecture must remain model-agnostic.

## DBSARE_AI_PFE

Mechanistic interpretability experiments on candidate models are a separate research track and must not be confused with the DBSARE system architecture.
