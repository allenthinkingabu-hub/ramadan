# Definition of Ready (DoR) — IA-REQ-009 Requirements Traceability & Compliance Mapping

Prerequisites that must be satisfied before starting Requirements Traceability & Compliance Mapping.
Items marked **required** MUST be available; others are recommended.

| ID | Check | Required | Source | Fallback |
|----|-------|----------|--------|----------|
| DOR-001 | Task context / business problem provided | Yes | User input or upstream | — |
| DOR-002 | Upstream task artifacts available | Yes | Upstream task output | Request from PM |
| DOR-003 | Project Charter exists (PM deliverable) | No | PM Agent | Proceed with user as sponsor |
| DOR-004 | Stakeholder information available | No | User input or org context | Ask user during elicitation |
| DOR-005 | Business context available | No | User input, docs, or web research | Research and confirm with user |
| DOR-006 | Initial scope indication | No | User input | Collaboratively define during elicitation |
| DOR-007 | Relevant prior documents | No | User-provided files | Proceed without if unavailable |
| DOR-008 | Industry / domain context identifiable | Yes | Inferred from topic or explicit | — |
| DOR-009 | Output location defined | Yes | User input or default | Default: `~/.openclaw/workspace-sa/outputs/IA-REQ-009/` |
| DOR-010 | Language preference | No | User input | Default: English |
