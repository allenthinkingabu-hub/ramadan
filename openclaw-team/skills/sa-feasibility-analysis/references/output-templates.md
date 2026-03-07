# Output Content List & Templates — SA-feasibility-analysis

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
| OUT-13 | Feasibility Analysis Report | `feasibility-analysis-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |

All paths are relative to the `feasibility-analysis/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — SA-feasibility-analysis Agent
# Task: IA-INC-002 Feasibility Analysis
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-002"
  task_name: "Feasibility Analysis"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
    # Add additional fields as appropriate for each config type
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Feasibility Analysis (IA-INC-002)

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
# Work Log — Feasibility Analysis (IA-INC-002)

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

### Template: Feasibility Analysis Report (OUT-13)

```markdown
# Feasibility Analysis Report

## 1. Executive Summary
{One-paragraph overview of feasibility findings and recommendation}

## 2. Analysis Scope & Objectives
- **Purpose**: {why this feasibility analysis was conducted}
- **Requirements Assessed**: {summary of client requirements}
- **Constraints**: {any limitations on the analysis}

## 3. Technical Feasibility
### 3.1 Technology Capability Assessment
{Can the required functionality be built with available/attainable technology?}

### 3.2 Architecture Viability
{Is the proposed architecture sound and achievable?}

### 3.3 Integration Feasibility
{Can the system integrate with required external systems?}

### 3.4 Technical Risks
{Technical risks and mitigation strategies}

## 4. Operational Feasibility
### 4.1 Organizational Readiness
{Can the organization support and operate the solution?}

### 4.2 Process Impact
{How will existing processes be affected?}

### 4.3 Change Management
{What change management is needed?}

## 5. Economic Feasibility
### 5.1 Cost Estimates
{Development costs, infrastructure costs, operational costs}

### 5.2 Benefit Analysis
{Expected tangible and intangible benefits}

### 5.3 ROI / Cost-Benefit Summary
{Return on investment and break-even analysis}

## 6. Schedule Feasibility
### 6.1 Timeline Estimate
{Estimated development and delivery timeline}

### 6.2 Resource Requirements
{Team size, skill requirements, external dependencies}

### 6.3 Schedule Risks
{Timeline risks and mitigation}

## 7. Legal & Compliance Feasibility
{Regulatory, licensing, and compliance considerations}

## 8. Risk Summary
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 9. Recommendation
{Go / No-Go / Conditional-Go with rationale}

## 10. Appendices
- A: Detailed cost breakdown
- B: Research references
- C: Stakeholder input summary
- D: Alternative solutions considered
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Feasibility Analysis

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
