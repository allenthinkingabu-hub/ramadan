# Output Content List & Templates — sa-spike-poc-leadership

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
| OUT-13 | Spike/PoC Report | `spike-poc-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Technology Comparison Matrix | `findings/technology-comparison.md` | Markdown |
| OUT-17 | Recommendation & Decision Record | `findings/recommendation-decision.md` | Markdown |
| OUT-18 | Risk Assessment Update | `findings/risk-assessment.md` | Markdown |
| OUT-19 | PoC Code Artifacts | `poc-code/` | Mixed |

All paths are relative to the `spike-poc/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-spike-poc-leadership Agent
# Task: IA-DEV-003 Spike & PoC Leadership
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-DEV-003"
  task_name: "Spike & PoC Leadership"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Spike & PoC Leadership (IA-DEV-003)

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
# Work Log — Spike & PoC Leadership (IA-DEV-003)

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

### Template: Spike/PoC Report (OUT-13)

```markdown
# Spike/PoC Report

## 1. Executive Summary
{One-paragraph overview of spike objectives, approach, and key findings}

## 2. Spike Scope & Objectives
- **Purpose**: {why this spike/PoC was conducted}
- **Uncertainty Area**: {what technical uncertainty is being investigated}
- **Hypothesis**: {the hypothesis being tested}
- **Time-box**: {duration allocated}
- **Success Criteria**: {measurable criteria for success}
- **Upstream References**: {links to Architecture Design, SAD, Technology Blueprint}

## 3. Approach & Methodology
### 3.1 Investigation Plan
{Step-by-step plan followed during the spike}

### 3.2 PoC Architecture
{Architecture of the proof-of-concept built}

### 3.3 Tools & Technologies Used
{Technologies and tools used in the PoC}

## 4. Findings & Results
### 4.1 Hypothesis Validation
| Hypothesis | Result | Evidence |
|:---|:---|:---|
| {hypothesis} | Confirmed / Refuted / Partially Confirmed | {evidence} |

### 4.2 Performance/Feasibility Measurements
| Metric | Target | Actual | Status |
|:---|:---|:---|:---|
| {metric} | {target} | {actual} | Pass / Fail |

### 4.3 Key Observations
{Detailed observations from the spike}

## 5. Technology Comparison (if applicable)
See: `findings/technology-comparison.md`

## 6. Recommendation
See: `findings/recommendation-decision.md`

## 7. Risk Assessment Update
See: `findings/risk-assessment.md`

## 8. Impact on Architecture
{How findings affect the architecture design (IA-REQ-001)}

## 9. Appendices
- A: PoC code location and instructions
- B: Benchmark results
- C: Research references
```

### Template: Technology Comparison Matrix (OUT-16)

```markdown
# Technology Comparison Matrix — Spike & PoC

## Generated: {timestamp}

## Evaluation Criteria

| Criteria | Weight | Description |
|:---|:---|:---|
| {criteria} | {weight} | {description} |

## Comparison

| Criteria | Option A: {name} | Option B: {name} | Option C: {name} |
|:---|:---|:---|:---|
| {criteria} | {score_and_notes} | {score_and_notes} | {score_and_notes} |

## Recommendation
{Recommended option with rationale}
```

### Template: Recommendation & Decision Record (OUT-17)

```markdown
# Recommendation & Decision Record — Spike & PoC

## Generated: {timestamp}

## Decision

| Field | Value |
|:---|:---|
| Decision ID | SPK-DEC-001 |
| Topic | {topic} |
| Decision | {decision} |
| Rationale | {rationale} |
| Alternatives Considered | {alternatives} |
| Impact on Architecture | {impact} |
| Status | Proposed / Accepted / Rejected |
```

### Template: Risk Assessment Update (OUT-18)

```markdown
# Risk Assessment Update — Spike & PoC

## Generated: {timestamp}

## Updated Risk Register

| Risk ID | Risk | Pre-Spike Impact | Pre-Spike Probability | Post-Spike Impact | Post-Spike Probability | Mitigation |
|:---|:---|:---|:---|:---|:---|:---|
| RSK-001 | {risk} | High/Med/Low | High/Med/Low | High/Med/Low | High/Med/Low | {mitigation} |

## Residual Risks
{Risks that remain after the spike}

## New Risks Identified
{New risks discovered during the spike}
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Spike & PoC Leadership

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
