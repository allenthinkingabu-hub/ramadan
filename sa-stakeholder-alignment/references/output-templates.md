# Output Content List & Templates -- sa-stakeholder-alignment

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
| OUT-13 | Stakeholder Alignment Report | `stakeholder-alignment-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Stakeholder Map | `stakeholder-map.md` | Markdown |
| OUT-17 | Decision Criteria Matrix | `decision-criteria.md` | Markdown |
| OUT-18 | Workshop Outcomes | `workshop-outcomes.md` | Markdown |

All paths are relative to the `stakeholder-alignment/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-stakeholder-alignment Agent
# Task: IA-INC-006 Stakeholder Alignment
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-006"
  task_name: "Stakeholder Alignment"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Stakeholder Alignment (IA-INC-006)

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
# Work Log -- Stakeholder Alignment (IA-INC-006)

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

### Template: Stakeholder Alignment Report (OUT-13)

```markdown
# Stakeholder Alignment Report

## 1. Executive Summary
{One-paragraph overview of alignment outcomes, key decisions, and remaining open items}

## 2. Alignment Scope & Objectives
- **Purpose**: {why this stakeholder alignment was performed}
- **Scope**: {what decisions/topics are covered}
- **Participants**: {stakeholder groups involved}
- **Upstream References**: {links to SAD, Technology Blueprint, Risk Identification reports}

## 3. Stakeholder Landscape
### 3.1 Stakeholder Map
{Summary of stakeholder groups, influence, interest, and engagement approach}
See: `stakeholder-map.md`

### 3.2 Stakeholder Priorities
| Stakeholder Group | Top Priority | Secondary Priority | Constraints |
|:---|:---|:---|:---|
| Business | {priority} | {priority} | {constraints} |
| Product | {priority} | {priority} | {constraints} |
| Security | {priority} | {priority} | {constraints} |
| Operations | {priority} | {priority} | {constraints} |

## 4. Decision Criteria
### 4.1 Weighted Evaluation Framework
{Summary of agreed decision criteria and weights}
See: `decision-criteria.md`

### 4.2 Trade-off Analysis
{Key trade-offs discussed and resolution approach}

## 5. Workshop Outcomes
### 5.1 Agreed Scope Boundaries
{What is in scope and out of scope, agreed by all parties}

### 5.2 Risk Posture
{Accepted risk tolerance per stakeholder group}

### 5.3 Key Decisions Made
| Decision ID | Decision | Rationale | Agreed By | Date |
|:---|:---|:---|:---|:---|
| DEC-001 | {decision} | {rationale} | {stakeholders} | {date} |

See: `workshop-outcomes.md`

## 6. Consensus Record
### 6.1 Signed-off Items
{Decisions with full stakeholder agreement}

### 6.2 Dissenting Opinions
{Recorded disagreements with resolution paths}

### 6.3 Open Items & Action Items
| Item ID | Description | Owner | Due Date | Status |
|:---|:---|:---|:---|:---|
| ACT-001 | {description} | {owner} | {date} | Open |

See: `consensus-record.md`

## 7. Recommendations
1. {recommendation_1}
2. {recommendation_2}

## 8. Appendices
- A: Full stakeholder map
- B: Workshop agendas and minutes
- C: Research references
- D: Decision criteria scoring sheets
```

### Template: Stakeholder Map (OUT-16)

```markdown
# Stakeholder Map -- Stakeholder Alignment (IA-INC-006)

## Generated: {timestamp}

## Influence/Interest Matrix

| Stakeholder | Role/Group | Influence | Interest | Engagement Strategy |
|:---|:---|:---:|:---:|:---|
| {name} | {group} | High/Med/Low | High/Med/Low | {strategy} |

## Engagement Strategy by Quadrant
- **High Influence, High Interest**: Manage closely -- active collaboration
- **High Influence, Low Interest**: Keep satisfied -- regular updates
- **Low Influence, High Interest**: Keep informed -- open communication
- **Low Influence, Low Interest**: Monitor -- periodic updates

## Communication Plan
| Stakeholder Group | Channel | Frequency | Content |
|:---|:---|:---|:---|
| {group} | {channel} | {frequency} | {content_type} |
```

### Template: Decision Criteria Matrix (OUT-17)

```markdown
# Decision Criteria Matrix -- Stakeholder Alignment (IA-INC-006)

## Generated: {timestamp}

## Weighted Criteria
| Criterion | Weight | Business | Product | Security | Operations | Notes |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| {criterion} | {weight}% | {score} | {score} | {score} | {score} | {notes} |

## Priority Rankings by Stakeholder
| Rank | Business | Product | Security | Operations |
|:---|:---|:---|:---|:---|
| 1 | {priority} | {priority} | {priority} | {priority} |
| 2 | {priority} | {priority} | {priority} | {priority} |
| 3 | {priority} | {priority} | {priority} | {priority} |

## Trade-off Analysis
| Trade-off | Option A | Option B | Resolution | Agreed By |
|:---|:---|:---|:---|:---|
| {tradeoff} | {option_a} | {option_b} | {resolution} | {stakeholders} |
```

### Template: Workshop Outcomes (OUT-18)

```markdown
# Workshop Outcomes -- Stakeholder Alignment (IA-INC-006)

## Generated: {timestamp}

## Agreed Scope Boundaries
### In Scope
- {item_1}
- {item_2}

### Out of Scope
- {item_1}
- {item_2}

### Deferred
- {item_1} -- Reason: {reason}

## Risk Posture
| Risk Area | Business Tolerance | Security Tolerance | Ops Tolerance | Agreed Posture |
|:---|:---|:---|:---|:---|
| {risk_area} | {tolerance} | {tolerance} | {tolerance} | {agreed} |

## Action Items
| ID | Action | Owner | Due Date | Priority | Status |
|:---|:---|:---|:---|:---|:---|
| ACT-001 | {action} | {owner} | {date} | P1/P2/P3 | Open |

## Escalation Paths
| Conflict Type | First Escalation | Second Escalation | Final Authority |
|:---|:---|:---|:---|
| {type} | {person/role} | {person/role} | {person/role} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Stakeholder Alignment

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
