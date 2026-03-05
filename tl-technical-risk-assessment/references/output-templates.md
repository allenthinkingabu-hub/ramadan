# Output Content List & Templates — tl-technical-risk-assessment

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
| OUT-13 | Technical Risk Assessment Report | `technical-risk-assessment-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Risk Register | `risk-register.md` | Markdown |
| OUT-17 | Dependency Map | `dependency-map.md` | Markdown |
| OUT-18 | Mitigation Strategy Plan | `mitigation-plan.md` | Markdown |
| OUT-19 | Risk Monitoring Framework | `monitoring-framework.md` | Markdown |

All paths are relative to the `technical-risk-assessment/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — tl-technical-risk-assessment Agent
# Task: TL-INC-004 Technical Risk Assessment
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-INC-004"
  task_name: "Technical Risk Assessment"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technical Risk Assessment (TL-INC-004)

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
# Work Log — Technical Risk Assessment (TL-INC-004)

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

### Template: Technical Risk Assessment Report (OUT-13)

```markdown
# Technical Risk Assessment Report

## 1. Executive Summary
{One-paragraph overview of key risks identified and overall risk posture}

## 2. Assessment Scope & Objectives
- **Purpose**: {why this risk assessment was conducted}
- **Scope**: {systems, integrations, and technologies covered}
- **Methodology**: {risk assessment approach used}
- **Upstream References**: {links to IA-INC-001..008 reports}

## 3. Risk Register Summary
{Top risks by severity}
See: `risk-register.md`

## 4. Dependency Map
{External and internal dependency analysis}
See: `dependency-map.md`

## 5. Mitigation Strategy
{Mitigation actions and contingency plans}
See: `mitigation-plan.md`

## 6. Risk Monitoring Framework
{KRIs, monitoring cadence, escalation paths}
See: `monitoring-framework.md`

## 7. Risk Heat Map
| | Low Impact | Medium Impact | High Impact | Critical Impact |
|:---|:---:|:---:|:---:|:---:|
| High Probability | {risks} | {risks} | {risks} | {risks} |
| Medium Probability | {risks} | {risks} | {risks} | {risks} |
| Low Probability | {risks} | {risks} | {risks} | {risks} |

## 8. Appendices
- A: Detailed risk analysis worksheets
- B: Research references
- C: Historical risk data
```

### Template: Risk Register (OUT-16)

```markdown
# Technical Risk Register

## Risk Entries

| Risk ID | Category | Description | Probability | Impact | Score | Owner | Mitigation | Status |
|:---|:---|:---|:---:|:---:|:---:|:---|:---|:---|
| RISK-001 | {category} | {description} | H/M/L | H/M/L | {score} | {owner} | {mitigation_ref} | Open/Mitigated/Accepted |
```

### Template: Dependency Map (OUT-17)

```markdown
# Dependency Map

## External Dependencies

| Dep ID | System/Service | Type | SLA | Risk Level | Fallback |
|:---|:---|:---|:---|:---|:---|
| DEP-001 | {system} | API/Data/Auth/Infra | {sla} | H/M/L | {fallback_strategy} |

## Internal Dependencies

| Dep ID | Team/Component | Type | Interface | Risk Level |
|:---|:---|:---|:---|:---|
| DEP-INT-001 | {team_component} | {type} | {interface} | H/M/L |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technical Risk Assessment

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
