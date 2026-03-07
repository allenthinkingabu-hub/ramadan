# Output Content List & Templates -- sa-cost-estimation-support

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
| OUT-13 | Cost Estimation Report | `cost-estimation-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Cost Breakdown Structure | `cost-breakdown.md` | Markdown |
| OUT-17 | TCO Projection | `tco-projection.md` | Markdown |
| OUT-18 | FinOps Guardrails | `finops-guardrails.md` | Markdown |

All paths are relative to the `cost-estimation/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-cost-estimation-support Agent
# Task: IA-INC-005 Cost Estimation Support
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-005"
  task_name: "Cost Estimation Support"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Cost Estimation Support (IA-INC-005)

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
# Work Log -- Cost Estimation Support (IA-INC-005)

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

### Template: Cost Estimation Report (OUT-13)

```markdown
# Cost Estimation Report

## 1. Executive Summary
{One-paragraph overview of cost estimates, key cost drivers, and ROM confidence level}

## 2. Estimation Scope & Objectives
- **Purpose**: {why this cost estimation was performed}
- **Scope**: {what systems/components are covered}
- **Estimation Method**: {ROM methodology and confidence range}
- **Upstream References**: {links to SAD, Technology Blueprint, Technical Discovery reports}

## 3. Cost Breakdown Summary
### 3.1 Cost by Category
| Category | Monthly | Year 1 | Year 2 | Year 3 |
|:---|---:|---:|---:|---:|
| Infrastructure | ${n} | ${n} | ${n} | ${n} |
| Licensing | ${n} | ${n} | ${n} | ${n} |
| Development | -- | ${n} | ${n} | ${n} |
| Operations | ${n} | ${n} | ${n} | ${n} |
| Integration | ${n} | ${n} | ${n} | ${n} |
| **Total** | **${n}** | **${n}** | **${n}** | **${n}** |

See: `cost-breakdown.md` for detailed breakdown

## 4. TCO Projection
### 4.1 3-Year Total Cost of Ownership
{Summary of TCO with build vs. buy analysis}

### 4.2 Cost Scaling Model
{How costs grow with usage/scale}

See: `tco-projection.md`

## 5. FinOps Guardrails
### 5.1 Budget Thresholds
{Monthly/quarterly budget limits and alert triggers}

### 5.2 Cost Optimization Opportunities
{Reserved instances, right-sizing, spot instances recommendations}

See: `finops-guardrails.md`

## 6. Estimation Assumptions & Risks
### 6.1 Key Assumptions
{Assumptions underlying the estimates}

### 6.2 Cost Risk Factors
{Factors that could cause estimates to vary}

### 6.3 Sensitivity Analysis
{Impact of key variable changes on total cost}

See: `estimation-assumptions.md`

## 7. Recommendations
1. {recommendation_1}
2. {recommendation_2}

## 8. Appendices
- A: Detailed cost breakdown worksheets
- B: Vendor pricing references
- C: Research references
- D: Stakeholder input summary
```

### Template: Cost Breakdown Structure (OUT-16)

```markdown
# Cost Breakdown Structure -- Cost Estimation (IA-INC-005)

## Generated: {timestamp}

## Infrastructure Costs
| Item | Unit | Quantity | Unit Cost | Monthly | Annual | Notes |
|:---|:---|---:|---:|---:|---:|:---|
| {compute_instance} | instances | {n} | ${n} | ${n} | ${n} | {notes} |
| {storage} | GB | {n} | ${n} | ${n} | ${n} | {notes} |
| {networking} | GB transfer | {n} | ${n} | ${n} | ${n} | {notes} |

## Licensing Costs
| Software/Service | Model | Annual Cost | Notes |
|:---|:---|---:|:---|
| {software_name} | Per-seat / Per-core / Flat | ${n} | {notes} |

## Development Effort
| Role | Count | Duration (months) | Monthly Rate | Total |
|:---|---:|---:|---:|---:|
| {role} | {n} | {n} | ${n} | ${n} |

## Operational Costs
| Item | Monthly | Annual | Notes |
|:---|---:|---:|:---|
| {ops_item} | ${n} | ${n} | {notes} |
```

### Template: TCO Projection (OUT-17)

```markdown
# TCO Projection -- Cost Estimation (IA-INC-005)

## Generated: {timestamp}

## 3-Year TCO Summary
| Year | Infrastructure | Licensing | Development | Operations | Total |
|:---|---:|---:|---:|---:|---:|
| Year 1 | ${n} | ${n} | ${n} | ${n} | ${n} |
| Year 2 | ${n} | ${n} | ${n} | ${n} | ${n} |
| Year 3 | ${n} | ${n} | ${n} | ${n} | ${n} |
| **Total** | **${n}** | **${n}** | **${n}** | **${n}** | **${n}** |

## Build vs. Buy Analysis
| Option | Year 1 | Year 2 | Year 3 | 3-Year Total | Pros | Cons |
|:---|---:|---:|---:|---:|:---|:---|
| Build | ${n} | ${n} | ${n} | ${n} | {pros} | {cons} |
| Buy | ${n} | ${n} | ${n} | ${n} | {pros} | {cons} |

## Cost Scaling Model
{Description of how costs scale with usage growth}
```

### Template: FinOps Guardrails (OUT-18)

```markdown
# FinOps Guardrails -- Cost Estimation (IA-INC-005)

## Generated: {timestamp}

## Budget Thresholds
| Environment | Monthly Budget | Alert at 80% | Alert at 100% | Hard Cap |
|:---|---:|---:|---:|---:|
| Production | ${n} | ${n} | ${n} | ${n} |
| Staging | ${n} | ${n} | ${n} | ${n} |
| Development | ${n} | ${n} | ${n} | ${n} |

## Cost Optimization Recommendations
| Recommendation | Potential Savings | Effort | Priority |
|:---|---:|:---|:---|
| {recommendation} | ${n}/month | Low/Med/High | P1/P2/P3 |

## Cost Allocation Tags
| Tag Key | Values | Purpose |
|:---|:---|:---|
| {tag_key} | {values} | {purpose} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Cost Estimation

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
