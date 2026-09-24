# Permission Model

## Principle

No action is authorized merely because an LLM proposed it.

## Conceptual flow

```
Action Proposal
 → Policy Engine
 → Permission Check
 → Approval if required
 → Execution
 → Verification
 → Audit
```

Permissions should distinguish observation from modification and should support least privilege.

Potential future controls include tool allowlists, command constraints, resource scopes, user approval, rate limits and sandboxing.
