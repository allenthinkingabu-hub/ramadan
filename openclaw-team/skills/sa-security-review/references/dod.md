# Definition of Done (DoD) -- sa-security-review

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `security-review/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `security-review/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `security-review/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `security-review/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `security-review/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `security-review/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `security-review/config/outputs.yaml` exists AND all templates in `security-review/templates/` |
| DoD-08 | SOP process checklist | `security-review/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `security-review/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `security-review/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `security-review/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `security-review/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Security Review report | `security-review/security-review-report.md` exists with complete deliverables |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `security-review/research/` contains saved research process and results |
| DoD-17 | Threat Model | `security-review/assessments/threat-model.md` exists with STRIDE/DREAD threat model with mitigations |
| DoD-18 | Vulnerability Assessment | `security-review/assessments/vulnerability-assessment.md` exists with identified vulnerabilities with severity and remediation |
| DoD-19 | Security Policy Compliance | `security-review/security-policy-compliance.md` exists with policy compliance matrix with gap analysis |
| DoD-20 | Security Test Plan | `security-review/security-test-plan.md` exists with penetration test and security scan planning |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
