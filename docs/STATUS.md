# Repository Status

**Current coordination state:** GitHub contains the architecture/documentation foundation, while the authoritative WSL audit shows that the real DBSARE runtime is still greenfield.

## Implementation source of truth

For implementation claims, the current source of truth is /home/deepblackstone/DBSARE_AI_PFE.

OpenCode's 2026-09-24 audit found an empty DBSARE/ directory: zero DBSARE Python files and no Core, Brain, Memory, Evidence, Reasoning, Investigation, Policy, CLI, GUI, Voice, collectors, lab, or tests.

The implemented WSL code is the separate Qwen3 research track under qwen3_analysis/.

## Important distinction

The GitHub repository contains an earlier foundation implementation. That state does not prove that the WSL implementation has those capabilities. Until synchronization occurs, WSL takes precedence for implementation status.

## Qwen research state

Qwen3-0.6B activation, contrastive, and Experiment 8 causal-intervention research is implemented independently. Experiment 8 produced four hypothesis-consistent and three strong candidates under its stated criterion, but these are not proven cybersecurity neurons and the lexical confound remains open.

## Current workflow

Architecture discussion → Claude prompt → OpenCode implementation → WSL validation → synchronize verified state to GitHub.

See docs/WSL_IMPLEMENTATION_AUDIT.md.