# Output Content List & Templates -- sa-risk-identification

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
| OUT-13 | Risk Identification Report | `risk-identification-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Risk Register | `risk-register.md` | Markdown |
| OUT-17 | Dependency Map | `diagrams/dependency-map.md` | Markdown + Mermaid |
| OUT-18 | Mitigation Strategies | `mitigation-strategies.md` | Markdown |

All paths are relative to the `risk-identification/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-risk-identification Agent
# Task: IA-INC-004 Risk Identification
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-004"
  task_name: "Risk Identification"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Risk Identification (IA-INC-004)

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
# Work Log -- Risk Identification (IA-INC-004)

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

### Template: Risk Identification Report (OUT-13)

```markdown
# Risk Identification Report

## 1. Executive Summary
{One-paragraph overview of risk landscape, key findings, and critical risks}

## 2. Assessment Scope & Objectives
- **Purpose**: {why this risk identification was performed}
- **Scope**: {what systems/components/integrations are covered}
- **Methodology**: {risk assessment framework used}
- **Upstream References**: {links to SAD, Integration Architecture, Technical Discovery reports}

## 3. Risk Register Summary
### 3.1 Risk Distribution by Category
| Category | Critical | High | Medium | Low | Total |
|:---|:---:|:---:|:---:|:---:|:---:|
| Technical | {n} | {n} | {n} | {n} | {n} |
| Integration | {n} | {n} | {n} | {n} | {n} |
| Dependency | {n} | {n} | {n} | {n} | {n} |
| NFR | {n} | {n} | {n} | {n} | {n} |

### 3.2 Top 10 Risks
| Rank | Risk ID | Description | Severity | Category |
|:---|:---|:---|:---|:---|
| 1 | {risk_id} | {description} | Critical/High | {category} |

See: `risk-register.md` for full register

## 4. Dependency Analysis
### 4.1 System Dependency Graph
{Reference to dependency map diagram}
See: `diagrams/dependency-map.md`

### 4.2 Critical Path Dependencies
{Dependencies that are on the critical delivery path}

### 4.3 External Dependencies
{Third-party systems, APIs, services that the solution depends on}

## 5. Integration Challenge Analysis
### 5.1 Integration Point Inventory
{List of integration points with risk assessment}

### 5.2 Protocol & Contract Risks
{Mismatches, versioning issues, backward compatibility concerns}

### 5.3 Data Consistency Risks
{Eventual consistency, data synchronization, conflict resolution challenges}

See: `integration-challenges.md`

## 6. Mitigation Strategy Summary
### 6.1 Avoidance Strategies
{Risks that can be avoided through design changes}

### 6.2 Reduction Strategies
{Risks that can be reduced through specific technical approaches}

### 6.3 Transfer Strategies
{Risks transferred to third parties or other teams}

### 6.4 Acceptance Criteria
{Risks accepted with justification and monitoring plan}

See: `mitigation-strategies.md`

## 7. Residual Risk Assessment
| Risk ID | Original Severity | Mitigation | Residual Severity | Monitoring |
|:---|:---|:---|:---|:---|
| {risk_id} | Critical/High | {mitigation_applied} | Medium/Low | {how_monitored} |

## 8. Recommendations
1. {recommendation_1}
2. {recommendation_2}

## 9. Appendices
- A: Full risk register
- B: Dependency map diagrams
- C: Research references
- D: Stakeholder input summary
```

### Template: Risk Register (OUT-16)

```markdown
# Risk Register -- Risk Identification (IA-INC-004)

## Generated: {timestamp}

## Risk Entries

| Risk ID | Category | Description | Likelihood | Impact | Severity | Owner | Mitigation | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| RSK-001 | Technical | {description} | High/Med/Low | High/Med/Low | Critical/High/Med/Low | {owner} | {mitigation} | Open |

## Risk Categories
- **Technical**: Technology maturity, skill gaps, architecture complexity
- **Integration**: Interface mismatches, protocol incompatibilities, data consistency
- **Dependency**: External system dependencies, third-party vendor risks, infrastructure
- **NFR**: Performance, scalability, security, availability shortfalls
- **Organizational**: Team capacity, knowledge silos, process gaps
```

### Template: Dependency Map (OUT-17)

```markdown
# Dependency Map -- Risk Identification (IA-INC-004)

## Description
{System dependency graph showing inter-system and external dependencies}

## Diagram

\`\`\`mermaid
graph LR
    A[System A] --> B[System B]
    A --> C[External API]
    B --> D[Database]
    C --> E[Third-Party Service]
\`\`\`

## Critical Path Dependencies
| Dependency | From | To | Type | Risk Level | Notes |
|:---|:---|:---|:---|:---|:---|
| {dep_name} | {source} | {target} | Hard/Soft | High/Med/Low | {notes} |

## Notes
{Any additional notes about dependency risks and circular dependencies}
```

### Template: Mitigation Strategies (OUT-18)

```markdown
# Mitigation Strategy Matrix -- Risk Identification (IA-INC-004)

## Generated: {timestamp}

## Risk-to-Mitigation Mapping

| Risk ID | Risk Description | Strategy | Mitigation Action | Contingency Plan | Residual Risk |
|:---|:---|:---|:---|:---|:---|
| RSK-001 | {description} | Avoid/Reduce/Transfer/Accept | {action} | {contingency} | Low/Med |

## High-Severity Contingency Plans
### RSK-{N}: {risk_title}
- **Trigger Condition**: {when contingency activates}
- **Response Steps**: {ordered steps}
- **Responsible Party**: {owner}
- **Recovery Time Objective**: {RTO}
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Risk Identification

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
