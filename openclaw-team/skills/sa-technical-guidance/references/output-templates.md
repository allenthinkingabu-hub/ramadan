# Output Content List & Templates — sa-technical-guidance

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
| OUT-13 | Technical Guidance Report | `technical-guidance-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Pattern Catalog | `patterns/pattern-catalog.md` | Markdown |
| OUT-17 | Architecture-to-Code Mapping | `architecture-code-mapping.md` | Markdown |
| OUT-18 | Guidance Decision Log | `guidance-decision-log.md` | Markdown |

All paths are relative to the `technical-guidance/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-technical-guidance Agent
# Task: IA-DEV-001 Technical Guidance
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-DEV-001"
  task_name: "Technical Guidance"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Technical Guidance (IA-DEV-001)

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
# Work Log — Technical Guidance (IA-DEV-001)

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

### Template: Technical Guidance Report (OUT-13)

```markdown
# Technical Guidance Report

## 1. Executive Summary
{One-paragraph overview of guidance provided and key decisions}

## 2. Guidance Scope & Objectives
- **Purpose**: {why technical guidance was needed}
- **Scope**: {components/modules/areas covered}
- **Constraints**: {implementation constraints and limitations}
- **Upstream References**: {links to Architecture Design, SAD, Technology Blueprint}

## 3. Architectural Decision Guidance
### 3.1 Component/Module Guidance
{Per-component architectural guidance and implementation direction}

### 3.2 Design Pattern Recommendations
{Recommended patterns with rationale}
See: `patterns/pattern-catalog.md`

### 3.3 Anti-Patterns to Avoid
{Common anti-patterns with explanations of why to avoid them}

## 4. Architecture-to-Code Mapping
### 4.1 Component-to-Module Mapping
{How architecture components map to code packages/modules}

### 4.2 Interface Contracts
{Interfaces developers must implement}

### 4.3 Dependency Rules
{Allowed and prohibited dependencies between modules}

See: `architecture-code-mapping.md`

## 5. Implementation Guidelines
### 5.1 Technology-Specific Guidance
{Framework-specific and technology-specific implementation notes}

### 5.2 NFR Implementation Patterns
{How to implement performance, security, resilience requirements in code}

### 5.3 Error Handling & Resilience
{Error handling patterns, retry strategies, circuit breaker usage}

## 6. Guidance Decision Log
| Decision# | Decision | Rationale | Impact | Status |
|:---|:---|:---|:---|:---|
| GD-001 | {decision} | {rationale} | {impact} | Accepted |

See: `guidance-decision-log.md`

## 7. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 8. Appendices
- A: Full pattern catalog
- B: Research references
- C: Developer Q&A summary
```

### Template: Pattern Catalog (OUT-16)

```markdown
# Pattern Catalog — Technical Guidance

## Generated: {timestamp}

## Patterns

### Pattern: {pattern_name}
- **Category**: Creational / Structural / Behavioral / Architectural
- **Problem**: {problem_description}
- **Solution**: {solution_description}
- **Applicability**: {where_to_apply}
- **Trade-offs**: {pros_and_cons}
- **Example**: {code_or_pseudocode_example}
- **References**: {links_to_documentation}
```

### Template: Architecture-to-Code Mapping (OUT-17)

```markdown
# Architecture-to-Code Mapping — Technical Guidance

## Generated: {timestamp}

## Component Mapping

| Architecture Component | Code Module/Package | Responsibility | Interface |
|:---|:---|:---|:---|
| {component_name} | {module_path} | {responsibility} | {interface_contract} |

## Dependency Rules

| Source Module | Allowed Dependencies | Prohibited Dependencies |
|:---|:---|:---|
| {module} | {allowed} | {prohibited} |
```

### Template: Guidance Decision Log (OUT-18)

```markdown
# Guidance Decision Log — Technical Guidance

## Generated: {timestamp}

## Decisions

| Decision ID | Topic | Decision | Rationale | Alternatives Considered | Status |
|:---|:---|:---|:---|:---|:---|
| GD-001 | {topic} | {decision} | {rationale} | {alternatives} | Accepted |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Technical Guidance

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
