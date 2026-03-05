# Output Content List & Templates -- tl-technical-decision-making

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
| OUT-13 | Technical Decision Making Report | `technical-decision-making-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Trade-off Analysis | `trade-off-analysis.md` | Markdown |
| OUT-17 | Decision Register | `decision-register.md` | Markdown |

All paths are relative to the `technical-decision-making/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- tl-technical-decision-making Agent
# Task: TL-DEV-003 Technical Decision Making
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-DEV-003"
  task_name: "Technical Decision Making"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Technical Decision Making (TL-DEV-003)

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
# Work Log -- Technical Decision Making (TL-DEV-003)

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

### Template: Technical Decision Making Report (OUT-13)

```markdown
# Technical Decision Making Report

## 1. Executive Summary
{One-paragraph overview of decisions made and their rationale}

## 2. Decision Context
- **Purpose**: {why these technical decisions were needed}
- **Scope**: {what areas decisions cover}
- **Constraints**: {technical and business constraints}

## 3. Decisions Summary
| ADR# | Decision | Status | Impact |
|:---|:---|:---|:---|
| ADR-001 | {decision} | Accepted/Proposed/Superseded | High/Med/Low |

## 4. Detailed Decision Records
### ADR-001: {Decision Title}
- **Status**: Accepted
- **Context**: {why this decision was needed}
- **Decision**: {what was decided}
- **Alternatives Considered**: {other options evaluated}
- **Consequences**: {positive and negative consequences}
- **Rationale**: {why this option was chosen}

## 5. Trade-off Analysis Summary
{High-level summary of key trade-offs}

## 6. Implementation Impact
{How decisions affect implementation plan}

## 7. Appendices
- A: Detailed evaluation matrices
- B: Research references
- C: Stakeholder input summary
```

### Template: Trade-off Analysis (OUT-16)

```markdown
# Trade-off Analysis -- Technical Decision Making

## Generated: {timestamp}

## Decision: {decision_title}

### Evaluation Criteria

| Criterion | Weight | Description |
|:---|:---:|:---|
| {criterion} | {weight} | {description} |

### Options Comparison

| Option | {Criterion 1} | {Criterion 2} | {Criterion 3} | Total Score |
|:---|:---:|:---:|:---:|:---:|
| {option_1} | {score} | {score} | {score} | {total} |

### Recommendation
{Recommended option with rationale}
```

### Template: Decision Register (OUT-17)

```markdown
# Decision Register -- Technical Decision Making

## Generated: {timestamp}

| Decision ID | Decision | Date | Status | Owner | Rationale | Impact |
|:---|:---|:---|:---|:---|:---|:---|
| DEC-001 | {decision} | {date} | Active/Superseded/Deprecated | {owner} | {rationale} | {impact} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Technical Decision Making

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
