# Output Content List & Templates -- sa-data-privacy-governance

## Output Content List

| Output ID | Deliverable | File Path | Format |
|:---|:---|:---|:---|
| OUT-01 | Trigger Mechanism Config | `config/triggers.yaml` | YAML |
| OUT-02 | RACI Matrix Config | `config/raci.yaml` | YAML |
| OUT-03 | Skills List Config | `config/skills.yaml` | YAML |
| OUT-04 | Knowledge Domains Config | `config/knowledge-domains.yaml` | YAML |
| OUT-05 | Tools List Config | `config/tools.yaml` | YAML |
| OUT-06 | MCP Tools Config | `config/mcp-tools.yaml` | YAML |
| OUT-07 | Output Content List Config | `config/outputs.yaml` | YAML |
| OUT-08 | SOP Process Config | `config/sop.yaml` | YAML |
| OUT-09 | DoD Checklist Config | `config/dod.yaml` | YAML |
| OUT-10 | DoR Checklist Config | `config/dor.yaml` | YAML |
| OUT-11 | Conversation Log | `conversation-log.md` | Markdown |
| OUT-12 | Work Log | `work-log.md` | Markdown |
| OUT-13 | Data Privacy & Governance Report | `data-privacy-governance-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Governance Diagrams | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | Regulatory Compliance View | `diagrams/regulatory-compliance-view.md` | Markdown + Mermaid |
| OUT-18 | NFR Alignment Note | `nfr-alignment.md` | Markdown |

All paths are relative to the `data-privacy-governance/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-data-privacy-governance Agent
# Task: IA-REQ-006 Data Privacy & Governance
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-006"
  task_name: "Data Privacy & Governance"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Data Privacy & Governance (IA-REQ-006)

## Session Info
- Topic: {topic}
- Started: {timestamp}

---

## Entry #{N}
- **Phase**: {phase_name}
- **Timestamp**: {timestamp}
- **Agent Question**: {question}
- **User Response**: {response}
- **Notes**: {any_observations}
```

### Template: Work Log (OUT-12)

```markdown
# Work Log -- Data Privacy & Governance (IA-REQ-006)

## Session Info
- Topic: {topic}
- Started: {timestamp}

---

## [{timestamp}] {action_title}
- **Phase**: {phase}
- **Action**: {description_of_action}
- **Result**: {outcome}
- **Next Step**: {what_follows}
```

### Template: Data Privacy & Governance Report (OUT-13)

```markdown
# Data Privacy & Governance Report

## 1. Executive Summary
{One-paragraph overview of data privacy and governance decisions}

## 2. Scope & Objectives
- **Purpose**: {why this governance framework was created}
- **Scope**: {data domains, systems, and jurisdictions covered}
- **Constraints**: {regulatory and organizational constraints}
- **Upstream References**: {links to SAD, Integration Architecture, Technology Blueprint}

## 3. Data Classification Taxonomy
### 3.1 Sensitivity Levels
| Level | Label | Description | Examples | Handling Requirements |
|:---|:---|:---|:---|:---|
| L1 | Public | {description} | {examples} | {handling} |
| L2 | Internal | {description} | {examples} | {handling} |
| L3 | Confidential | {description} | {examples} | {handling} |
| L4 | Restricted | {description} | {examples} | {handling} |

### 3.2 Classification Criteria
{Decision tree or criteria for classifying data}
See: `diagrams/classification-taxonomy.md`

## 4. Data Retention Policy
### 4.1 Retention Schedule
| Data Category | Retention Period | Legal Basis | Deletion Method | Archive Strategy |
|:---|:---|:---|:---|:---|
| {category} | {period} | {regulation/policy} | {soft/hard delete} | {archive_approach} |

### 4.2 Legal Hold Process
{Procedures for preserving data under litigation or regulatory hold}

## 5. Data Residency Requirements
### 5.1 Geographic Constraints
| Data Type | Allowed Regions | Prohibited Regions | Transfer Mechanism |
|:---|:---|:---|:---|
| {data_type} | {allowed} | {prohibited} | {SCC/BCR/adequacy decision} |

### 5.2 Cross-Border Transfer Rules
{Standard Contractual Clauses, Binding Corporate Rules, adequacy decisions}

## 6. Access Control Model
### 6.1 RBAC/ABAC Design
{Role definitions, attribute policies, permission matrices}
See: `diagrams/access-control-model.md`

### 6.2 Least Privilege & Segregation of Duties
{Principle implementation, conflicting role detection}

### 6.3 Access Review Cadence
{Periodic review schedule, certification process, automated checks}

## 7. Consent Management
### 7.1 Consent Collection & Storage
{Consent mechanisms, granularity, storage format}

### 7.2 Data Subject Rights
{Access, rectification, erasure, portability workflows and SLA targets}

## 8. Regulatory Compliance View
See: `diagrams/regulatory-compliance-view.md`

## 9. NFR Alignment Note
See: `nfr-alignment.md`

## 10. Architecture Decision Records
| ADR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| ADR-001 | {decision} | {rationale} | Accepted |

## 11. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 12. Appendices
- A: Full regulatory mapping details
- B: Research references
- C: Stakeholder input summary
- D: Alternative governance approaches considered
```

### Template: Regulatory Compliance View (OUT-17)

```markdown
# Regulatory Compliance View -- Data Privacy & Governance

## Generated: {timestamp}

## 1. Regulation-to-Control Mapping

| Regulation | Article/Section | Requirement | Control | Implementation Status |
|:---|:---|:---|:---|:---|
| GDPR | Art. 5 | Data minimization | {control} | Planned / Implemented |
| CCPA | Sec. 1798.100 | Right to know | {control} | Planned / Implemented |

## 2. Privacy Impact Assessment (PIA)

| Trigger | Assessment Scope | Owner | Frequency |
|:---|:---|:---|:---|
| {trigger_event} | {scope} | {role} | {frequency} |

## 3. Data Processing Agreements

| Third Party | Data Shared | Purpose | DPA Status | Review Date |
|:---|:---|:---|:---|:---|
| {vendor} | {data_types} | {purpose} | Signed / Pending | {date} |

## 4. Breach Notification Procedures

| Scenario | Detection | Assessment Window | Notification Timeline | Audience |
|:---|:---|:---|:---|:---|
| {scenario} | {detection_method} | {hours} | {72h/without undue delay} | {DPA/data subjects/internal} |

## 5. Compliance Flow

\`\`\`mermaid
{compliance flow diagram source}
\`\`\`
```

### Template: NFR Alignment Note (OUT-18)

```markdown
# NFR Alignment Note -- Data Privacy & Governance

## Generated: {timestamp}

## NFR-to-Governance Mapping

| NFR Category | NFR Requirement | Governance Decision | How Addressed |
|:---|:---|:---|:---|
| Security | {nfr_requirement} | {decision} | {explanation} |
| Compliance | {nfr_requirement} | {decision} | {explanation} |
| Auditability | {nfr_requirement} | {decision} | {explanation} |
| Privacy | {nfr_requirement} | {decision} | {explanation} |

## Privacy SLO/SLI Targets

| Metric | SLI Definition | SLO Target | Alert Threshold |
|:---|:---|:---|:---|
| Consent response time | {definition} | {target} | {threshold} |
| DSAR response time | {definition} | {target} | {threshold} |
| Encryption coverage | {definition} | {target} | {threshold} |
| Access review completion | {definition} | {target} | {threshold} |

## Constraints

| Constraint ID | Description | Impact | Mitigation |
|:---|:---|:---|:---|
| CON-001 | {constraint} | {impact} | {mitigation} |

## Assumptions

| Assumption ID | Description | Risk if Invalid |
|:---|:---|:---|
| ASM-001 | {assumption} | {risk} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Data Privacy & Governance

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
