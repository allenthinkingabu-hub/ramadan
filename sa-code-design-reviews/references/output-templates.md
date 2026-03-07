# Output Content List & Templates — sa-code-design-reviews

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
| OUT-13 | Code & Design Review Report | `code-design-review-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Compliance Matrix | `compliance-matrix.md` | Markdown |
| OUT-17 | Remediation Plan | `remediation-plan.md` | Markdown |
| OUT-18 | Review Decision Log | `review-decision-log.md` | Markdown |

All paths are relative to the `code-design-reviews/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-code-design-reviews Agent
# Task: IA-DEV-002 Code & Design Reviews
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-DEV-002"
  task_name: "Code & Design Reviews"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Code & Design Reviews (IA-DEV-002)

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
# Work Log — Code & Design Reviews (IA-DEV-002)

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

### Template: Code & Design Review Report (OUT-13)

```markdown
# Code & Design Review Report

## 1. Executive Summary
{One-paragraph overview of review scope, key findings, and overall compliance status}

## 2. Review Scope & Objectives
- **Purpose**: {why this review was conducted}
- **Scope**: {code/PRs/designs reviewed}
- **Review Type**: Code Review / PR Review / Design Review
- **Upstream References**: {links to Architecture Design, Technical Guidance, SAD}

## 3. Review Findings
### 3.1 Critical Findings
| Finding ID | Component | Severity | Description | Architecture Reference |
|:---|:---|:---|:---|:---|
| RF-001 | {component} | Critical/High/Med/Low | {finding} | {arch_ref} |

### 3.2 Architecture Compliance Status
| Component | Status | Notes |
|:---|:---|:---|
| {component} | Compliant / Non-Compliant / Partial | {notes} |

### 3.3 Design Pattern Compliance
{Assessment of design pattern usage against approved patterns}

### 3.4 NFR Compliance
{Assessment of NFR implementation: performance, security, resilience}

## 4. Compliance Matrix
See: `compliance-matrix.md`

## 5. Remediation Plan
See: `remediation-plan.md`

## 6. Review Decision
| Decision | Conditions | Reviewer |
|:---|:---|:---|
| Approve / Request Changes / Reject | {conditions} | SA (IA-DEV-002) |

See: `review-decision-log.md`

## 7. Risks & Concerns
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 8. Appendices
- A: Detailed file-by-file findings
- B: Research references
- C: Review checklist used
```

### Template: Compliance Matrix (OUT-16)

```markdown
# Compliance Matrix — Code & Design Reviews

## Generated: {timestamp}

## Architecture Compliance

| Requirement ID | Architecture Requirement | Implementation Status | Evidence | Gap Description |
|:---|:---|:---|:---|:---|
| {req_id} | {requirement} | Compliant / Non-Compliant / Partial | {file_or_component} | {gap_if_any} |

## NFR Compliance

| NFR Category | Requirement | Implementation | Status | Notes |
|:---|:---|:---|:---|:---|
| Performance | {requirement} | {implementation} | Pass / Fail | {notes} |
| Security | {requirement} | {implementation} | Pass / Fail | {notes} |
| Resilience | {requirement} | {implementation} | Pass / Fail | {notes} |
```

### Template: Remediation Plan (OUT-17)

```markdown
# Remediation Plan — Code & Design Reviews

## Generated: {timestamp}

## Prioritized Issues

| Priority | Finding ID | Component | Issue | Suggested Fix | Effort | Deadline |
|:---|:---|:---|:---|:---|:---|:---|
| P1 | {finding_id} | {component} | {issue} | {fix} | {effort} | {deadline} |
```

### Template: Review Decision Log (OUT-18)

```markdown
# Review Decision Log — Code & Design Reviews

## Generated: {timestamp}

## Decisions

| Decision ID | Review Subject | Decision | Conditions | Rationale | Status |
|:---|:---|:---|:---|:---|:---|
| RD-001 | {subject} | Approve / Request Changes / Reject | {conditions} | {rationale} | Final |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Code & Design Reviews

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
