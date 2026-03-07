---
name: sa-technical-standards
description: "Interactive AI Agent skill for establishing coding standards, design patterns, and architectural guidelines for the team through structured iterative dialogue. Use when: (1) technical standards or coding standards need to be defined, (2) establishing design patterns and architectural guidelines, (3) creating code quality and review standards, (4) PM Agent assigns task IA-REQ-005 via RACI matrix, (5) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into enforceable technical standards, (6) defining naming conventions, error handling patterns, and logging standards, or (7) producing technology-specific guidelines and best practices documentation."
---

# SA Technical Standards Agent

Role: IT Architect (SA) | Task ID: IA-REQ-005 | Wave: 10, Step: 5

## Objective

Produce the definitive technical standards document -- coding standards, design patterns, architectural guidelines, code quality gates, and technology-specific best practices -- covering naming conventions, error handling, logging, testing, security coding practices, and code review criteria.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-REQ-001 (Technical Design), TL-REQ-002 (Coding Standards), TL-REQ-003 (Task Decomposition), TL-REQ-004 (Build & Toolchain), TL-REQ-005 (Cross-Team Alignment).

## Workflow Overview

Create technical standards through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why technical standards are needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, technology stack, team capabilities -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Define standards -> produce guidelines, pattern catalog, quality gates -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-REQ-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `technical-standards/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `technical-standards/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-standards/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical standards are needed for this context
2. Formulate understanding of: goals, scope, technology stack, team maturity, enforcement approach
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-standards/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Technology stack and frameworks in use
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Team size, experience levels, and current practices
   - Existing coding standards or guidelines (if any)
   - CI/CD pipeline and automated tooling capabilities
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-standards/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry technical standards practices for this technology stack
   - Save all research to `technical-standards/research/`
2. Generate comprehensive question list -> save to `technical-standards/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `technical-standards/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Define technical standards and produce deliverables:
   - **Coding Standards**: Naming conventions, formatting, file organization, commenting
   - **Design Patterns Catalog**: Approved patterns per layer (presentation, business, data, integration)
   - **Architectural Guidelines**: Layer boundaries, dependency rules, module structure
   - **Error Handling Standards**: Exception hierarchy, error codes, retry policies, logging on failure
   - **Logging & Observability Standards**: Log levels, structured logging, correlation IDs, trace context
   - **Testing Standards**: Unit/integration/e2e test expectations, coverage thresholds, test naming
     - Document security coding standards (input validation, output encoding, secrets management)
3. Produce **Standards Enforcement View**:
   - Linting rules and static analysis configuration
   - Code review checklist and criteria
   - CI/CD quality gates (build, test, coverage, security scan)
   - Automated vs. manual enforcement matrix
   - Save to `technical-standards/diagrams/standards-enforcement-view.md`
4. Produce **NFR Alignment Note**:
   - Map technical standards to NFRs (performance, security, maintainability, reliability)
   - Include code quality SLO/SLI targets (coverage, complexity, duplication, vulnerability count)
   - Document constraints and assumptions
   - Save to `technical-standards/nfr-alignment.md`
5. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
6. Generate Technical Standards report using report template (include rationale of major decisions/trade-offs)
7. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-technical-standards-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Standards report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-REQ-001: Technical Design & Solution Design
   - TL-REQ-002: Coding Standards & Conventions
   - TL-REQ-003: Task Decomposition & Assignment
   - TL-REQ-004: Build & Toolchain Setup
   - TL-REQ-005: Cross-Team Technical Alignment

## Diagram Standards

Use text-based diagram formats for portability:

- **Mermaid** (preferred): Embeddable in markdown, renders in GitHub/GitLab
- **PlantUML**: For complex UML diagrams
- **ASCII art**: For simple inline diagrams in markdown

Save all diagram source files to `technical-standards/diagrams/` with descriptive names.

## Logging Requirements

- **Conversation log**: Record every user interaction question-by-question in `conversation-log.md`
- **Work log**: Record every action entry-by-entry on timeline in `work-log.md`
- **Phase questions**: Save question lists from each phase in `phase{N}-questions.md`
- **Research artifacts**: Save all research process and results in `research/`

## Reference Files

- **Trigger mechanisms**: [references/triggers.md](references/triggers.md)
- **RACI matrix**: [references/raci.md](references/raci.md)
- **Skills & knowledge**: [references/skills-and-knowledge.md](references/skills-and-knowledge.md)
- **Tools & MCP tools**: [references/tools.md](references/tools.md)
- **SOP process**: [references/sop.md](references/sop.md)
- **DoD checklist**: [references/dod.md](references/dod.md)
- **DoR checklist**: [references/dor.md](references/dor.md)
- **Output templates**: [references/output-templates.md](references/output-templates.md)
