# Output Content List & Templates — tl-technical-vision-direction

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
| OUT-13 | Technical Vision Direction Report | `technical-vision-direction-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Technical Vision Statement | `technical-vision-statement.md` | Markdown |
| OUT-17 | Guiding Principles | `guiding-principles.md` | Markdown |
| OUT-18 | Business-Technology Alignment Matrix | `alignment-matrix.md` | Markdown |
| OUT-19 | Technology Roadmap Overview | `technology-roadmap.md` | Markdown |

All paths are relative to the `technical-vision-direction/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — tl-technical-vision-direction Agent
# Task: TL-INC-001 Technical Vision & Direction
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-INC-001"
  task_name: "Technical Vision & Direction"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technical Vision & Direction (TL-INC-001)

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
# Work Log — Technical Vision & Direction (TL-INC-001)

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

### Template: Technical Vision Direction Report (OUT-13)

```markdown
# Technical Vision & Direction Report

## 1. Executive Summary
{One-paragraph overview of the technical vision and its alignment with business objectives}

## 2. Vision Scope & Objectives
- **Purpose**: {why this technical vision was created}
- **Scope**: {what systems/teams/products are covered}
- **Time Horizon**: {short-term, mid-term, long-term milestones}
- **Upstream References**: {links to IA-INC-001..008 reports}

## 3. Technical Vision Statement
{Clear, concise articulation of the target technical state}
See: `technical-vision-statement.md`

## 4. Guiding Principles
{Core principles that guide all technical decisions}
See: `guiding-principles.md`

## 5. Business-Technology Alignment
{How technical direction supports business objectives}
See: `alignment-matrix.md`

## 6. Technology Roadmap
{High-level evolution plan with key milestones}
See: `technology-roadmap.md`

## 7. Key Technical Decisions
| Decision# | Decision | Rationale | Impact |
|:---|:---|:---|:---|
| TD-001 | {decision} | {rationale} | {impact} |

## 8. Risks & Dependencies
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 9. Success Metrics
| Metric | Target | Measurement Method |
|:---|:---|:---|
| {metric} | {target_value} | {how_measured} |

## 10. Appendices
- A: Research references
- B: Stakeholder input summary
- C: Alternative approaches considered
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technical Vision & Direction

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```

### Template: Technical Vision Statement (OUT-16)

```markdown
# Technical Vision Statement

## Vision
{One to three paragraphs describing the desired future technical state}

## Time Horizon
- **Short-term (0-6 months)**: {immediate technical direction}
- **Mid-term (6-18 months)**: {evolution targets}
- **Long-term (18-36 months)**: {aspirational technical state}

## Alignment with Business Strategy
{How this vision enables the business strategy}
```

### Template: Guiding Principles (OUT-17)

```markdown
# Guiding Principles — Technical Vision & Direction

## Core Principles

| Principle ID | Principle | Description | Rationale |
|:---|:---|:---|:---|
| GP-001 | {principle_name} | {description} | {why_this_matters} |

## Trade-off Decision Framework

| Trade-off | Preferred Direction | When to Deviate | Approval Required |
|:---|:---|:---|:---|
| {trade_off} | {default_choice} | {exception_conditions} | {who_approves} |
```

### Template: Business-Technology Alignment Matrix (OUT-18)

```markdown
# Business-Technology Alignment Matrix

## Objective-to-Capability Mapping

| Business Objective | Technical Capability | Current State | Target State | Gap | Investment Priority |
|:---|:---|:---|:---|:---|:---|
| {objective} | {capability} | {current} | {target} | {gap_description} | High/Med/Low |
```

### Template: Technology Roadmap (OUT-19)

```markdown
# Technology Roadmap Overview

## Roadmap Timeline

| Phase | Timeline | Key Initiatives | Dependencies | Success Criteria |
|:---|:---|:---|:---|:---|
| Phase 1 | {dates} | {initiatives} | {dependencies} | {criteria} |

## Key Decision Points

| Decision Point | Timeline | Decision Needed | Stakeholders |
|:---|:---|:---|:---|
| {decision_point} | {date} | {decision_description} | {who_decides} |
```
