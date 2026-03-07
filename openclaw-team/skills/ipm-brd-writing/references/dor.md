# Definition of Ready (DoR) — IPM-INC-003 BRD Writing

Prerequisites that must be satisfied before starting BRD creation.
Items marked **required** MUST be available; others are recommended.

| ID | Check | Required | Source | Fallback |
|----|-------|----------|--------|----------|
| DOR-001 | Topic / Business Problem Provided | Yes | User input | — |
| DOR-002 | Requirement Gathering artifacts available (IPM-INC-001) | Yes | Upstream task output | Request from PM |
| DOR-003 | Market Research findings available (IPM-INC-002) | Yes | Upstream task output | Request from PM |
| DOR-004 | Project Charter exists (PM deliverable) | No | PM Agent | Proceed with user as sponsor |
| DOR-005 | Project Sponsor Identified | No | User input or RACI | User is default sponsor |
| DOR-006 | Stakeholder Information Available | No | User input or org context | Ask user during elicitation |
| DOR-007 | Business Context Available | No | User input, docs, or web research | Research and confirm with user |
| DOR-008 | Initial Scope Indication | No | User input | Collaboratively define during elicitation |
| DOR-009 | Relevant Prior Documents | No | User-provided files | Proceed without if unavailable |
| DOR-010 | Industry / Domain Context Identifiable | Yes | Inferred from topic or explicit | — |
| DOR-011 | Output Location Defined | Yes | User input or default | Default: `~/.openclaw/workspace-ipm/outputs/IPM-INC-003/` |
| DOR-012 | Language Preference | No | User input | Default: English |
