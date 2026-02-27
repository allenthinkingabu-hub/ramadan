# Output Content List & Templates — sa-technology-selection

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
| OUT-13 | Technology Selection Report | `technology-selection-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |

All paths are relative to the `technology-selection/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-technology-selection Agent
# Task: IA-INC-003 Technology Selection
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-003"
  task_name: "Technology Selection"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technology Selection (IA-INC-003)

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
# Work Log — Technology Selection (IA-INC-003)

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

### Template: Technology Selection Report (OUT-13)

```markdown
# Technology Selection Report

## 1. Executive Summary
{One-paragraph overview of technology selection objectives, process, and key recommendations}

## 2. Evaluation Scope & Objectives
- **Purpose**: {why this technology selection was conducted}
- **Scope**: {what technology categories are covered}
- **Constraints**: {budget, timeline, infrastructure, team constraints}
- **Upstream References**: {links to Technical Discovery / Feasibility Analysis reports}

## 3. Evaluation Criteria & Weights
| Criterion | Weight | Description |
|:---|:---:|:---|
| {criterion_name} | {weight%} | {description} |

## 4. Technology Candidates (per category)
### 4.1 {Category Name}
| Candidate | Type | License | Maturity | Community |
|:---|:---|:---|:---|:---|
| {candidate} | {OSS/Commercial/SaaS} | {license} | {maturity} | {community_health} |

## 5. Weighted Scoring Matrix
| Candidate | {Criterion 1} | {Criterion 2} | ... | Weighted Total |
|:---|:---:|:---:|:---:|:---:|
| {candidate} | {score} | {score} | ... | {total} |

## 6. TCO Comparison
| Cost Component | {Candidate A} | {Candidate B} | {Candidate C} |
|:---|---:|---:|---:|
| License / Subscription | {cost} | {cost} | {cost} |
| Implementation | {cost} | {cost} | {cost} |
| Operations (annual) | {cost} | {cost} | {cost} |
| Training | {cost} | {cost} | {cost} |
| **3-Year TCO** | **{total}** | **{total}** | **{total}** |

## 7. Vendor & Licensing Analysis
| Vendor | License Model | Support Tiers | Lock-in Risk | Viability |
|:---|:---|:---|:---|:---|
| {vendor} | {model} | {tiers} | {risk_level} | {viability_assessment} |

## 8. Proof-of-Concept Recommendations
| PoC # | Technology | Objective | Duration | Success Criteria |
|:---|:---|:---|:---|:---|
| PoC-001 | {technology} | {objective} | {duration} | {criteria} |

## 9. Risk Assessment
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 10. Final Recommendation
### Recommended Stack
| Category | Recommended Technology | Rationale |
|:---|:---|:---|
| {category} | {technology} | {rationale} |

### Rationale Summary
{Comprehensive rationale for the recommended technology stack}

## 11. Appendices
- A: Full scoring matrix details
- B: Research references
- C: Stakeholder input summary
- D: Alternative technologies considered
- E: Vendor communication log
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technology Selection

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
