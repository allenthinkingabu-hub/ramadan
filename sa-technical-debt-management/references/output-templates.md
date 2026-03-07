# Output Content List & Templates — sa-technical-debt-management

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
| OUT-13 | Technical Debt Report | `technical-debt-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Debt Register | `debt-items/debt-register.md` | Markdown |
| OUT-17 | Prioritization Matrix | `debt-items/prioritization-matrix.md` | Markdown |
| OUT-18 | Remediation Strategy | `remediation-strategy.md` | Markdown |
| OUT-19 | Governance Policy | `governance-policy.md` | Markdown |

All paths are relative to the `technical-debt/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-technical-debt-management Agent
# Task: IA-DEV-004 Technical Debt Management
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-DEV-004"
  task_name: "Technical Debt Management"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technical Debt Management (IA-DEV-004)

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
# Work Log — Technical Debt Management (IA-DEV-004)

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

### Template: Technical Debt Report (OUT-13)

```markdown
# Technical Debt Report

## 1. Executive Summary
{One-paragraph overview of debt landscape, key findings, and recommendations}

## 2. Assessment Scope & Objectives
- **Purpose**: {why this debt assessment was conducted}
- **Scope**: {systems/components assessed}
- **Upstream References**: {links to Architecture Design, Code Reviews, SAD}

## 3. Debt Landscape Overview
### 3.1 Debt by Category
| Category | Count | Total Severity | Trend |
|:---|:---|:---|:---|
| Code-level | {count} | {severity} | Increasing / Stable / Decreasing |
| Architecture-level | {count} | {severity} | Increasing / Stable / Decreasing |
| Infrastructure | {count} | {severity} | Increasing / Stable / Decreasing |
| Documentation | {count} | {severity} | Increasing / Stable / Decreasing |
| Test | {count} | {severity} | Increasing / Stable / Decreasing |

### 3.2 Debt Heatmap
{Visual or tabular representation of debt concentration by component}

## 4. Debt Register
See: `debt-items/debt-register.md`

## 5. Prioritization
See: `debt-items/prioritization-matrix.md`

## 6. Remediation Strategy
See: `remediation-strategy.md`

## 7. Governance Policy
See: `governance-policy.md`

## 8. Metrics & KPIs
| Metric | Current | Target | Status |
|:---|:---|:---|:---|
| Total debt items | {count} | {target} | On Track / At Risk |
| Debt ratio | {ratio} | {target} | On Track / At Risk |
| Remediation velocity | {velocity} | {target} | On Track / At Risk |

## 9. Risks & Recommendations
| Risk | Impact | Probability | Recommendation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {recommendation} |

## 10. Appendices
- A: Detailed debt inventory
- B: Research references
- C: Static analysis results summary
```

### Template: Debt Register (OUT-16)

```markdown
# Debt Register — Technical Debt Management

## Generated: {timestamp}

## Debt Items

| Debt ID | Category | Component | Description | Severity | Impact | Cost of Delay | Effort | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| TD-001 | Code / Arch / Infra / Doc / Test | {component} | {description} | Critical/High/Med/Low | {impact} | {cost_per_sprint} | {story_points} | Open / In Progress / Resolved |
```

### Template: Prioritization Matrix (OUT-17)

```markdown
# Prioritization Matrix — Technical Debt Management

## Generated: {timestamp}

## Scoring Criteria

| Criteria | Weight | Description |
|:---|:---|:---|
| Business Impact | 30% | Impact on business operations and revenue |
| Technical Risk | 25% | Risk of system failure or degradation |
| Remediation Effort | 20% | Effort required to resolve (inverse scoring) |
| Cost of Delay | 25% | Cost of not addressing the debt per sprint |

## Prioritized Debt Items

| Priority | Debt ID | Description | Impact Score | Risk Score | Effort Score | CoD Score | Total | Recommendation |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| P1 | {debt_id} | {description} | {score} | {score} | {score} | {score} | {total} | Quick Win / Planned / Deferred |
```

### Template: Remediation Strategy (OUT-18)

```markdown
# Remediation Strategy — Technical Debt Management

## Generated: {timestamp}

## Strategy Overview
{High-level approach to debt remediation}

## Phase 1: Quick Wins (Sprint 1-2)
| Debt ID | Description | Effort | Owner |
|:---|:---|:---|:---|
| {debt_id} | {description} | {effort} | {owner} |

## Phase 2: Planned Refactoring (Sprint 3-6)
| Debt ID | Description | Effort | Owner |
|:---|:---|:---|:---|
| {debt_id} | {description} | {effort} | {owner} |

## Phase 3: Long-term Improvements (Sprint 7+)
| Debt ID | Description | Effort | Owner |
|:---|:---|:---|:---|
| {debt_id} | {description} | {effort} | {owner} |

## Resource Allocation
{Recommended % of sprint capacity for debt remediation}
```

### Template: Governance Policy (OUT-19)

```markdown
# Governance Policy — Technical Debt Management

## Generated: {timestamp}

## Debt Acceptance Criteria
{When is it acceptable to take on new debt}

## Thresholds & Limits
| Metric | Warning Threshold | Critical Threshold | Action |
|:---|:---|:---|:---|
| {metric} | {warning} | {critical} | {action} |

## Monitoring & Tracking
{How debt is tracked, reported, and reviewed}

## Review Cadence
{Frequency and format of debt review meetings}

## Escalation Process
{When and how to escalate debt concerns}
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technical Debt Management

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
