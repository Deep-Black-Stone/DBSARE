# Threat Model

## Assets

- Credentials and secrets
- Evidence integrity
- Environment state
- User-controlled configuration
- Investigation history
- Brain and Memory data
- Action permissions
- Audit records

## Threats

### Prompt injection through observed data
Malicious instructions may appear in logs, DNS records, banners, filenames, web content or scan output.

### Tool-output poisoning
An evidence source may contain misleading or adversarial content.

### Unauthorized action
A reasoning error or compromised component may propose a dangerous modification.

### Privilege escalation
A tool or action path may attempt to exceed its authorized scope.

### Evidence tampering
Attackers may attempt to alter or erase observations.

## Mitigations

Untrusted-data labeling, policy enforcement, least privilege, validation, provenance, audit logs, isolation and human approval where required.
