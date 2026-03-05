# Output Content List & Templates -- tl-hands-on-development

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
| OUT-13 | Hands-On Development Report | `hands-on-development-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Implementation Patterns | `implementation-patterns.md` | Markdown |
| OUT-17 | Reference Implementations | `implementations/` | Code |

All paths are relative to the `hands-on-development/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- tl-hands-on-development Agent
# Task: TL-DEV-002 Hands-On Development
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "TL-DEV-002"
  task_name: "Hands-On Development"
  role: "Technical Lead (TL)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Hands-On Development (TL-DEV-002)

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
# Work Log -- Hands-On Development (TL-DEV-002)

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

### Template: Hands-On Development Report (OUT-13)

```markdown
# Hands-On Development Report

## 1. Executive Summary
{One-paragraph overview of what was implemented and key decisions}

## 2. Scope & Objectives
- **Purpose**: {why TL hands-on development was needed}
- **Scope**: {features/components implemented}
- **Critical paths**: {identified critical paths addressed}

## 3. Implementation Summary
### 3.1 Features Implemented
{List of features with brief descriptions}

### 3.2 Reference Patterns Established
{Patterns created for team adoption}

### 3.3 Technical Decisions
{Key decisions made during implementation}

## 4. Architecture Alignment
{How implementations align with IA-REQ-001 architecture design}

## 5. Testing
### 5.1 Unit Tests
{Summary of unit test coverage}

### 5.2 Integration Tests
{Summary of integration test approach}

## 6. Technical Debt
{Any technical debt introduced and remediation plan}

## 7. Appendices
- A: Code change summary
- B: Pattern documentation
- C: Test results
```

### Template: Implementation Patterns Document (OUT-16)

```markdown
# Implementation Patterns -- Hands-On Development

## Generated: {timestamp}

## Established Patterns

| Pattern ID | Pattern Name | Purpose | Location |
|:---|:---|:---|:---|
| PAT-001 | {pattern_name} | {purpose} | {file_path} |

## Pattern Details

### PAT-001: {Pattern Name}
- **Problem**: {what problem this solves}
- **Solution**: {pattern description}
- **Example**: {code reference}
- **Anti-patterns**: {what to avoid}

## Anti-Patterns to Avoid

| ID | Anti-Pattern | Why to Avoid | Preferred Alternative |
|:---|:---|:---|:---|
| AP-001 | {anti_pattern} | {reason} | {alternative} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Hands-On Development

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
