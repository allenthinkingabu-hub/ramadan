# Output Content List & Templates -- tl-unblocking-the-team

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
| OUT-13 | Unblocking Report | `unblocking-the-team-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Blocker Resolution Report | `blocker-resolution-report.md` | Markdown |
| OUT-17 | Escalation Framework | `escalation-framework.md` | Markdown |

All paths are relative to the `unblocking-the-team/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- tl-unblocking-the-team Agent
# Task: TL-DEV-004 Unblocking the Team
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-DEV-004"
  task_name: "Unblocking the Team"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Unblocking the Team (TL-DEV-004)

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
# Work Log -- Unblocking the Team (TL-DEV-004)

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

### Template: Unblocking Report (OUT-13)

```markdown
# Unblocking the Team Report

## 1. Executive Summary
{Overview of blockers identified and resolved}

## 2. Blockers Inventory
| Blocker ID | Description | Severity | Affected Members | Duration | Status |
|:---|:---|:---|:---|:---|:---|
| BLK-001 | {description} | Critical/High/Medium | {names} | {duration} | Resolved/In Progress |

## 3. Resolution Details
### BLK-001: {Blocker Title}
- **Root Cause**: {root cause analysis}
- **Resolution**: {what was done to resolve}
- **Prevention**: {how to prevent recurrence}

## 4. Escalation Framework Summary
{Overview of escalation procedures established}

## 5. Knowledge Transfer
{Lessons learned and team guidance}

## 6. Appendices
- A: Debugging logs
- B: Resolution scripts
- C: Team communication records
```

### Template: Blocker Resolution Report (OUT-16)

```markdown
# Blocker Resolution Report -- Unblocking the Team

## Generated: {timestamp}

| Blocker ID | Category | Root Cause | Resolution | Time to Resolve | Preventive Action |
|:---|:---|:---|:---|:---|:---|
| BLK-001 | {category} | {root_cause} | {resolution} | {time} | {prevention} |
```

### Template: Escalation Framework (OUT-17)

```markdown
# Escalation Framework -- Unblocking the Team

## Generated: {timestamp}

## Escalation Levels

| Level | Criteria | Responder | SLA |
|:---|:---|:---|:---|
| L1 | {criteria} | {responder} | {sla} |

## Escalation Paths by Blocker Type

| Blocker Type | L1 | L2 | L3 |
|:---|:---|:---|:---|
| {type} | {l1_action} | {l2_action} | {l3_action} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Unblocking the Team

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
