# Output Content List & Templates — tl-technology-stack-decision

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
| OUT-13 | Technology Stack Decision Report | `technology-stack-decision-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Technology Decision Matrix | `technology-decision-matrix.md` | Markdown |
| OUT-17 | Stack Specification | `stack-specification.md` | Markdown |
| OUT-18 | Compatibility & Integration Analysis | `compatibility-analysis.md` | Markdown |
| OUT-19 | Migration & Adoption Plan | `adoption-plan.md` | Markdown |

All paths are relative to the `technology-stack-decision/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — tl-technology-stack-decision Agent
# Task: TL-INC-002 Technology Stack Decision
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-INC-002"
  task_name: "Technology Stack Decision"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technology Stack Decision (TL-INC-002)

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
# Work Log — Technology Stack Decision (TL-INC-002)

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

### Template: Technology Stack Decision Report (OUT-13)

```markdown
# Technology Stack Decision Report

## 1. Executive Summary
{One-paragraph overview of technology decisions made and key rationale}

## 2. Decision Scope & Objectives
- **Purpose**: {why these technology decisions were needed}
- **Scope**: {what layers/components are covered}
- **Constraints**: {budget, licensing, team skills, compliance}
- **Upstream References**: {links to IA-INC-001..008 reports}

## 3. Technology Decision Matrix
{Summary of evaluation criteria and scoring}
See: `technology-decision-matrix.md`

## 4. Stack Specification
{Final technology selections by category}
See: `stack-specification.md`

## 5. Compatibility Analysis
{Inter-component compatibility and integration verification}
See: `compatibility-analysis.md`

## 6. Migration & Adoption Plan
{If replacing existing stack, migration path and training needs}
See: `adoption-plan.md`

## 7. Technology Decision Records
| TDR# | Decision | Alternatives Considered | Rationale | Status |
|:---|:---|:---|:---|:---|
| TDR-001 | {decision} | {alternatives} | {rationale} | Accepted |

## 8. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 9. Cost Analysis
| Component | License Model | Estimated Cost | Notes |
|:---|:---|:---|:---|
| {component} | {model} | {cost} | {notes} |

## 10. Appendices
- A: Detailed evaluation scorecards
- B: Research references
- C: Vendor comparison notes
- D: Team skills assessment input
```

### Template: Technology Decision Matrix (OUT-16)

```markdown
# Technology Decision Matrix

## Evaluation Criteria

| Criteria ID | Criteria | Weight | Description |
|:---|:---|:---|:---|
| EC-001 | {criteria_name} | {weight_pct}% | {description} |

## Evaluation Results

| Technology | Category | EC-001 | EC-002 | EC-003 | Weighted Score | Recommendation |
|:---|:---|:---|:---|:---|:---|:---|
| {technology} | {category} | {score} | {score} | {score} | {total} | Selected / Alternative / Rejected |
```

### Template: Stack Specification (OUT-17)

```markdown
# Stack Specification

## Languages & Frameworks

| Layer | Technology | Version | Purpose | License |
|:---|:---|:---|:---|:---|
| {layer} | {technology} | {version} | {purpose} | {license} |

## Infrastructure & Data

| Component | Technology | Version | Purpose | Hosting |
|:---|:---|:---|:---|:---|
| {component} | {technology} | {version} | {purpose} | {hosting} |

## DevOps & Tooling

| Category | Tool | Version | Purpose |
|:---|:---|:---|:---|
| {category} | {tool} | {version} | {purpose} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technology Stack Decision

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
