# Output Content List & Templates -- sa-technical-standards

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
| OUT-13 | Technical Standards Report | `technical-standards-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Standards Documentation | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | Standards Enforcement View | `diagrams/standards-enforcement-view.md` | Markdown + Mermaid |
| OUT-18 | NFR Alignment Note | `nfr-alignment.md` | Markdown |

All paths are relative to the `technical-standards/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-technical-standards Agent
# Task: IA-REQ-005 Technical Standards
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-005"
  task_name: "Technical Standards"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Technical Standards (IA-REQ-005)

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
# Work Log -- Technical Standards (IA-REQ-005)

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

### Template: Technical Standards Report (OUT-13)

```markdown
# Technical Standards Report

## 1. Executive Summary
{One-paragraph overview of technical standards decisions and approach}

## 2. Standards Scope & Objectives
- **Purpose**: {why these technical standards were created}
- **Scope**: {what technologies/teams are covered}
- **Constraints**: {organizational constraints and limitations}
- **Upstream References**: {links to SAD, Technology Blueprint}

## 3. Coding Standards
### 3.1 Naming Conventions
{Variable, function, class, file, and module naming rules}

### 3.2 Code Formatting
{Indentation, line length, braces, imports ordering}

### 3.3 File Organization
{Directory structure, module layout, package conventions}

### 3.4 Commenting & Documentation
{Inline comments, docstrings, API documentation standards}

## 4. Design Patterns Catalog
### 4.1 Presentation Layer Patterns
{Approved patterns for UI/API layer}

### 4.2 Business Logic Patterns
{Domain model, service layer, CQRS, event sourcing patterns}

### 4.3 Data Access Patterns
{Repository, Unit of Work, Active Record patterns}

### 4.4 Integration Patterns
{API gateway, circuit breaker, retry, message broker patterns}

## 5. Architectural Guidelines
### 5.1 Layer Boundaries & Dependencies
{Dependency rules, import restrictions, layer isolation}

### 5.2 Module Structure
{Module decomposition, coupling/cohesion guidelines}

### 5.3 API Design Standards
{REST/gRPC conventions, versioning, pagination, error responses}

## 6. Error Handling Standards
### 6.1 Exception Hierarchy
{Exception classes, error categorization}

### 6.2 Error Codes & Messages
{Error code schema, user-facing vs. internal messages}

### 6.3 Retry & Recovery
{Retry policies, circuit breaker configuration, fallback strategies}

## 7. Logging & Observability Standards
### 7.1 Log Levels & Usage
{DEBUG, INFO, WARN, ERROR, FATAL usage guidelines}

### 7.2 Structured Logging
{Log format, required fields, correlation IDs}

### 7.3 Tracing & Metrics
{Distributed tracing, metric naming, dashboard standards}

## 8. Testing Standards
### 8.1 Test Types & Coverage
{Unit, integration, e2e, performance test expectations and coverage thresholds}

### 8.2 Test Naming & Organization
{Test naming conventions, fixture management, mock/stub guidelines}

## 9. Security Coding Standards
### 9.1 Input Validation & Output Encoding
{Validation rules, sanitization, XSS/injection prevention}

### 9.2 Secrets Management
{Secrets handling, environment variables, vault integration}

## 10. Standards Enforcement View
See: `diagrams/standards-enforcement-view.md`

## 11. NFR Alignment Note
See: `nfr-alignment.md`

## 12. Architecture Decision Records
| ADR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| ADR-001 | {decision} | {rationale} | Accepted |

## 13. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 14. Appendices
- A: Language-specific guidelines
- B: Research references
- C: Stakeholder input summary
- D: Alternative standards considered
```

### Template: Standards Enforcement View (OUT-17)

```markdown
# Standards Enforcement View -- Technical Standards

## Generated: {timestamp}

## 1. Linting & Static Analysis

| Tool | Scope | Configuration | Enforcement |
|:---|:---|:---|:---|
| {linter_name} | {language/framework} | {config_file} | CI gate / Warning |

## 2. Code Review Checklist

| # | Check Item | Category | Required |
|:---|:---|:---|:---|
| 1 | {check_item} | {naming/structure/security} | Yes / No |

## 3. CI/CD Quality Gates

| Gate | Tool | Threshold | Action on Failure |
|:---|:---|:---|:---|
| Build | {build_tool} | Must pass | Block merge |
| Unit Tests | {test_framework} | {coverage_threshold}% | Block merge |
| Security Scan | {sast_tool} | No critical findings | Block merge |
| Code Quality | {quality_tool} | {quality_threshold} | Warning / Block |

## 4. Automated vs. Manual Enforcement

| Standard | Automated | Manual | Tool/Process |
|:---|:---:|:---:|:---|
| {standard_name} | Yes / No | Yes / No | {tool_or_process} |

## 5. Enforcement Flow

\`\`\`mermaid
{enforcement flow diagram source}
\`\`\`
```

### Template: NFR Alignment Note (OUT-18)

```markdown
# NFR Alignment Note -- Technical Standards

## Generated: {timestamp}

## NFR-to-Standards Mapping

| NFR Category | NFR Requirement | Standard/Guideline | How Addressed |
|:---|:---|:---|:---|
| Performance | {nfr_requirement} | {standard} | {explanation} |
| Security | {nfr_requirement} | {standard} | {explanation} |
| Maintainability | {nfr_requirement} | {standard} | {explanation} |
| Reliability | {nfr_requirement} | {standard} | {explanation} |

## Code Quality SLO/SLI Targets

| Metric | SLI Definition | SLO Target | Alert Threshold |
|:---|:---|:---|:---|
| Test coverage | {definition} | {target} | {threshold} |
| Cyclomatic complexity | {definition} | {target} | {threshold} |
| Code duplication | {definition} | {target} | {threshold} |
| Vulnerability count | {definition} | {target} | {threshold} |

## Constraints

| Constraint ID | Description | Impact | Mitigation |
|:---|:---|:---|:---|
| CON-001 | {constraint} | {impact} | {mitigation} |

## Assumptions

| Assumption ID | Description | Risk if Invalid |
|:---|:---|:---|
| ASM-001 | {assumption} | {risk} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Technical Standards

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
