# Output Content List & Templates -- tl-code-review-quality-gatekeeping

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
| OUT-13 | Code Review Quality Gatekeeping Report | `code-review-quality-gatekeeping-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Review Standards Document | `review-standards.md` | Markdown |
| OUT-17 | Quality Gate Report | `quality-gate-report.md` | Markdown |

All paths are relative to the `code-review-quality-gatekeeping/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- tl-code-review-quality-gatekeeping Agent
# Task: TL-DEV-001 Code Review & Quality Gatekeeping
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-DEV-001"
  task_name: "Code Review & Quality Gatekeeping"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Code Review & Quality Gatekeeping (TL-DEV-001)

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
# Work Log -- Code Review & Quality Gatekeeping (TL-DEV-001)

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

### Template: Code Review Quality Gatekeeping Report (OUT-13)

```markdown
# Code Review & Quality Gatekeeping Report

## 1. Executive Summary
{One-paragraph overview of review standards and quality gate approach}

## 2. Scope & Objectives
- **Purpose**: {why code review gatekeeping is needed}
- **Scope**: {what codebases/components are covered}
- **Quality targets**: {measurable quality objectives}

## 3. PR Review Checklist
### 3.1 Code Quality Checks
{Checklist items for code quality}

### 3.2 Architectural Compliance Checks
{Checklist items for architecture adherence}

### 3.3 Security Review Checks
{Security-focused review items}

### 3.4 Performance Review Checks
{Performance-focused review items}

## 4. Quality Gate Definitions
### 4.1 Gate: Code Submission
{Entry criteria, checks, exit criteria}

### 4.2 Gate: PR Review Approval
{Entry criteria, checks, exit criteria}

### 4.3 Gate: Merge Readiness
{Entry criteria, checks, exit criteria}

## 5. Review Process
### 5.1 Review Types
{Quick review, standard review, deep review definitions}

### 5.2 Review Workflow
{Step-by-step review process}

### 5.3 Escalation Procedures
{When and how to escalate}

## 6. Automated Checks
{Linter configuration, static analysis, automated test requirements}

## 7. Metrics & KPIs
{Review turnaround time, defect detection rate, review coverage}

## 8. Appendices
- A: Review checklist templates
- B: Quality gate configuration
- C: Tool configuration guides
```

### Template: Review Standards Document (OUT-16)

```markdown
# Review Standards -- Code Review & Quality Gatekeeping

## Generated: {timestamp}

## 1. Review Types

| Type | Scope | Time Target | Reviewer Count |
|:---|:---|:---|:---|
| Quick Review | Minor changes, typos, config | < 30 min | 1 |
| Standard Review | Features, bug fixes | < 4 hours | 2 |
| Deep Review | Architecture changes, security | < 1 day | 2+ |

## 2. Severity Classification

| Severity | Description | Action Required |
|:---|:---|:---|
| Critical | Security vulnerability, data loss risk | Must fix before merge |
| Major | Architecture violation, significant bug | Must fix before merge |
| Minor | Code style, minor optimization | Should fix, can defer |
| Suggestion | Alternative approach, improvement idea | Optional, author decides |

## 3. Escalation Procedures
{When to escalate, escalation path, response expectations}
```

### Template: Quality Gate Report (OUT-17)

```markdown
# Quality Gate Report -- Code Review & Quality Gatekeeping

## Generated: {timestamp}

## Quality Gate Definitions

| Gate ID | Gate Name | Entry Criteria | Exit Criteria | Automated |
|:---|:---|:---|:---|:---:|
| QG-001 | {gate_name} | {entry_criteria} | {exit_criteria} | Yes/No |

## Compliance Tracking

| Metric | Target | Current | Status |
|:---|:---|:---|:---|
| {metric_name} | {target_value} | {current_value} | On Track / At Risk / Off Track |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Code Review & Quality Gatekeeping

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
