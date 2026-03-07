# Output Content List & Templates -- sa-security-review

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
| OUT-13 | Security Review Report | `security-review-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Threat Model | `assessments/threat-model.md` | Markdown |
| OUT-17 | Vulnerability Assessment | `assessments/vulnerability-assessment.md` | Markdown |
| OUT-18 | Security Policy Compliance | `security-policy-compliance.md` | Markdown |
| OUT-19 | Security Test Plan | `security-test-plan.md` | Markdown |

All paths are relative to the `security-review/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-security-review Agent
# Task: IA-QA-002 Security Review
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-QA-002"
  task_name: "Security Review"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Security Review (IA-QA-002)

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
# Work Log -- Security Review (IA-QA-002)

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

### Template: Security Review Report (OUT-13)

```markdown
# Security Review Report

## 1. Executive Summary
{One-paragraph overview of security review approach and key findings}

## 2. Scope & Objectives
- **Purpose**: {why security review was conducted}
- **Scope**: {systems, components, and areas covered}
- **Upstream References**: {links to upstream deliverables}

## 3. Methodology
{Approach, frameworks, and techniques used -- STRIDE, DREAD, OWASP}

## 4. Findings & Deliverables

### 4.1 Threat Model
{Summary of threat model}
See: `assessments/threat-model.md`

### 4.2 Vulnerability Assessment
{Summary of vulnerability assessment}
See: `assessments/vulnerability-assessment.md`

### 4.3 Security Policy Compliance
{Summary of security policy compliance}
See: `security-policy-compliance.md`

### 4.4 Security Test Plan
{Summary of security test plan}
See: `security-test-plan.md`

## 5. Recommendations
| Priority | Recommendation | Impact | Effort |
|:---|:---|:---|:---|
| High/Med/Low | {recommendation} | {impact} | {effort} |

## 6. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 7. Appendices
- A: Detailed analysis data
- B: Research references
- C: Stakeholder input summary
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Security Review

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
