# Output Content List & Templates — SA-technical-discovery

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
| OUT-13 | Technical Discovery Report | `technical-discovery-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |

All paths are relative to the `technical-discovery/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — SA-technical-discovery Agent
# Task: IA-INC-001 Technical Discovery
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-INC-001"
  task_name: "Technical Discovery"
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
# Conversation Log — Technical Discovery (IA-INC-001)

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
# Work Log — Technical Discovery (IA-INC-001)

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

### Template: Technical Discovery Report (OUT-13)

```markdown
# Technical Discovery Report

## 1. Executive Summary
{One-paragraph overview of key findings}

## 2. Discovery Scope & Objectives
- **Purpose**: {why this discovery was conducted}
- **Scope**: {what was assessed}
- **Constraints**: {any limitations}

## 3. Current Technology Landscape
### 3.1 Technology Stack
{Detailed inventory of current technologies}

### 3.2 System Architecture
{Architecture diagrams and descriptions}

### 3.3 Infrastructure Environment
{Infrastructure components and configurations}

### 3.4 Integration Points & Dependencies
{System integrations and dependency map}

## 4. Assessment Findings
### 4.1 Strengths
{What works well}

### 4.2 Weaknesses & Risks
{Issues, technical debt, risks identified}

### 4.3 Gaps
{Missing capabilities or areas needing improvement}

## 5. Recommendations
{Prioritized actionable recommendations}

## 6. Appendices
- A: Full technology inventory
- B: Research references
- C: Stakeholder input summary
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technical Discovery

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
