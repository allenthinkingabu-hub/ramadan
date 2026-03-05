# Output Content List & Templates — tl-team-capability-assessment

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
| OUT-13 | Team Capability Assessment Report | `team-capability-assessment-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Team Skills Matrix | `skills-matrix.md` | Markdown |
| OUT-17 | Gap Analysis | `gap-analysis.md` | Markdown |
| OUT-18 | Development & Remediation Plan | `development-plan.md` | Markdown |
| OUT-19 | Team Readiness Assessment | `readiness-assessment.md` | Markdown |

All paths are relative to the `team-capability-assessment/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — tl-team-capability-assessment Agent
# Task: TL-INC-003 Team Capability Assessment
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-INC-003"
  task_name: "Team Capability Assessment"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Team Capability Assessment (TL-INC-003)

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
# Work Log — Team Capability Assessment (TL-INC-003)

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

### Template: Team Capability Assessment Report (OUT-13)

```markdown
# Team Capability Assessment Report

## 1. Executive Summary
{One-paragraph overview of team capability findings and key recommendations}

## 2. Assessment Scope & Objectives
- **Purpose**: {why this assessment was conducted}
- **Scope**: {team(s) assessed, skill domains covered}
- **Methodology**: {assessment approach used}
- **Upstream References**: {links to IA-INC-001..008 reports}

## 3. Team Composition
| Name/Role | Current Skills | Experience Level | Domain Expertise |
|:---|:---|:---|:---|
| {name_role} | {skills} | {level} | {domains} |

## 4. Skills Matrix
{Summary of individual and team-level skill ratings}
See: `skills-matrix.md`

## 5. Gap Analysis
{Identified capability gaps and impact assessment}
See: `gap-analysis.md`

## 6. Development & Remediation Plan
{Training, hiring, and knowledge transfer recommendations}
See: `development-plan.md`

## 7. Team Readiness Assessment
{Overall readiness score and risk areas}
See: `readiness-assessment.md`

## 8. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 9. Appendices
- A: Detailed skill assessment data
- B: Research references
- C: Training resource catalog
```

### Template: Team Skills Matrix (OUT-16)

```markdown
# Team Skills Matrix

## Skill Rating Scale
- 1: Novice | 2: Beginner | 3: Intermediate | 4: Advanced | 5: Expert

## Individual Skills Assessment

| Team Member | Role | {Skill 1} | {Skill 2} | {Skill 3} | Overall |
|:---|:---|:---:|:---:|:---:|:---:|
| {name} | {role} | {rating} | {rating} | {rating} | {avg} |

## Required vs. Current Proficiency

| Skill Domain | Required Level | Team Average | Gap |
|:---|:---:|:---:|:---:|
| {skill} | {required} | {current} | {gap} |
```

### Template: Gap Analysis (OUT-17)

```markdown
# Gap Analysis — Team Capability Assessment

## Identified Gaps

| Gap ID | Skill Domain | Required | Current | Severity | Impact | Recommendation |
|:---|:---|:---:|:---:|:---|:---|:---|
| GAP-001 | {domain} | {level} | {level} | Critical/High/Med/Low | {impact} | {recommendation} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Team Capability Assessment

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
