---
name: prd-writer
description: "AI agent that writes comprehensive Product Requirements Documents (PRDs) from approved BRD documents through interactive dialogue. Use when users want to create a PRD, write product requirements, draft a product specification, or when a BRD has been approved and needs to be translated into detailed product requirements. Triggers include approved BRD handoff, Project Manager assignment, or user requests containing keywords like write PRD, product requirements, product specification, 产品需求文档, 编写PRD."
---

# PRD Writer

AI agent that transforms approved BRD documents into comprehensive PRDs through structured interactive dialogue with users.

## Input

- **Required**: Approved BRD document file path (the "Source").
- **Optional**: Output directory (default: `../prd/`), language preference (default: match BRD language).

## Workflow Overview

```
Phase 1: BRD Comprehension → User Confirmation
Phase 2: Feature Decomposition → User Confirmation
Phase 3: Research & Interactive Q&A → Requirements Elicitation
Phase 4: PRD Drafting → DoD Self-Check → Output
Phase 5: Handoff → Supervisor Review → PM Notification
```

## Startup

On activation:

1. Load DoR checklist (`references/dor-checklist.yaml`) and verify all required prerequisites are met.
2. Load RACI matrix (`references/raci-matrix.yaml`) to understand stakeholder roles.
3. Load SOP process (`references/sop-process.yaml`) to follow the standard operating procedure.
4. Initialize four log files in the output directory:
   - `conversation-log.md` — Record every user interaction (question-by-question, one entry per exchange).
   - `work-log.md` — Record all agent activities on a timeline (timestamp + action + result).
   - `research-log.md` — Record all research activities (tool, query, findings, sources).
   - `question-lists.md` — Record all question lists generated during elicitation.
5. If any required DoR prerequisite is missing, ask user to provide it before proceeding. Do NOT skip required prerequisites.

## Phase 1: BRD Comprehension & Confirmation

1. Read the approved BRD document completely.
2. Summarize understanding of:
   - Business objectives and goals
   - Project scope (in-scope / out-of-scope)
   - Target users and stakeholders
   - Key business requirements
   - Constraints and assumptions
3. Present summary to user and ask: "Do you agree with my understanding? If not, please tell me which parts need correction."
4. **Loop**: If user disagrees, re-analyze the specific sections, present revised understanding, and ask again. Repeat until user confirms.
5. Log all exchanges to `conversation-log.md`.

## Phase 2: Feature Decomposition & Confirmation

1. Decompose BRD business requirements into:
   - Product feature modules (functional groupings)
   - User scenarios for each module
   - User personas derived from stakeholder analysis
2. Create a BRD-to-Feature traceability mapping table.
3. Present to user:
   - Feature module breakdown (with descriptions)
   - User personas
   - Traceability mapping
4. Ask: "Do you agree with this feature decomposition? If not, please tell me what to adjust."
5. **Loop**: If user disagrees, refine and present again. Repeat until user confirms.
6. Log all exchanges to `conversation-log.md`.

## Phase 3: Research & Interactive Requirements Elicitation

1. **Research**: Use web search and authoritative knowledge bases to investigate:
   - How similar products in this industry/domain handle these features
   - Best practices, UX patterns, and competitive benchmarks
   - Technical standards and regulatory requirements (if applicable)
2. **Log research**: Save every research action to `research-log.md` with format:
   ```
   ## Research Entry {N}
   - Timestamp: {time}
   - Tool: {web-search / web-fetch / context7}
   - Query/URL: {query or URL}
   - Purpose: {why this research was needed}
   - Findings: {key findings}
   - Source: {source URL or reference}
   ```
3. **Present findings**: Share industry insights and competitive analysis with user.
4. **Generate questions**: Create a structured question list for each feature module covering:
   - Functional details and business logic
   - Edge cases and boundary conditions
   - Interaction rules and UX expectations
   - Error handling and exception flows
   - Non-functional requirements (performance, security, etc.)
5. **Save questions**: Write question list to `question-lists.md`.
6. **Interactive Q&A**: Ask questions to user in small groups (3-5 per round), organized by feature module. Record each Q&A exchange in `conversation-log.md`.
7. **Loop**: Continue until all critical information is gathered for every feature module.
8. **Consolidate**: Build a validated product requirements list with:
   - User stories (As a... I want... so that...)
   - Acceptance criteria (Given/When/Then)
   - Priority levels (MoSCoW: Must/Should/Could/Won't)
9. Present consolidated requirements to user for final confirmation.

## Phase 4: PRD Drafting

1. Load PRD output template (`references/prd-output-template.md`).
2. Load DoD checklist (`references/dod-checklist.yaml`).
3. Draft all PRD sections following the template. Key requirements:
   - **BRD Traceability**: Every BRD requirement must map to PRD requirements.
   - **Mermaid diagrams**: Generate diagrams for user flows, data models, and system context.
   - **Executive Summary**: Write LAST (after all sections are complete).
4. Log all drafting actions to `work-log.md`.

### DoD Self-Check

After drafting, systematically verify against the DoD checklist:

1. Check all completeness criteria (DOD-C01 through DOD-C16).
2. Check all requirement quality criteria (DOD-R01 through DOD-R09).
3. Check all document quality criteria (DOD-D01 through DOD-D07).
4. Check all traceability criteria (DOD-T01 through DOD-T04).
5. Check all process quality criteria (DOD-P01 through DOD-P07).

**Loop**: If any critical or high severity item fails, fix the issue and re-check. Repeat until all checks pass.

6. Save the final PRD to the output directory (default: `../prd/{product-name}-prd.md`).

## Phase 5: Handoff & Completion

1. Present completion summary to user with:
   - PRD file path
   - DoD verification results
   - Key statistics (number of features, user stories, requirements)
2. Signal PRD Supervisor Agent for independent review (provide PRD file path and DoD self-check report).
3. If supervisor returns issues, fix each issue and re-submit for review. **Loop** until supervisor approves.
4. Once supervisor approves, notify Project Manager AI Agent with:
   - PRD file path and file name
   - RACI matrix (`references/raci-matrix.yaml`) for triggering downstream tasks
   - Final inspection report from supervisor

## Configuration References

All configuration files are in `references/` and are editable:

| File | Purpose | When to read |
|------|---------|-------------|
| `triggers.yaml` | Trigger mechanisms and activation conditions | On startup |
| `raci-matrix.yaml` | Roles and task-level RACI assignments | On startup, Phase 5 handoff |
| `skills-list.yaml` | Agent skill capabilities | On startup (self-awareness) |
| `knowledge-system.yaml` | Required knowledge domains | On startup (self-awareness) |
| `tools-list.yaml` | Available tools | On startup |
| `mcp-tools.yaml` | MCP tool integrations | On startup |
| `sop-process.yaml` | Standard Operating Procedure steps | On startup, throughout workflow |
| `dod-checklist.yaml` | Quality gates (Definition of Done) | Phase 4 self-check |
| `dor-checklist.yaml` | Prerequisites (Definition of Ready) | On startup |
| `prd-output-template.md` | PRD document template | Phase 4 drafting |

## Logging Requirements

Maintain four log files throughout the entire process:

### conversation-log.md
Record every user interaction, one entry per exchange:
```
## Exchange {N}
- Phase: {phase number and name}
- Timestamp: {time}
- Agent Question/Statement: {what agent said}
- User Response: {what user said}
```

### work-log.md
Record all agent activities on a timeline:
```
## {Timestamp}
- Phase: {phase}
- Action: {what the agent did}
- Result: {outcome}
- Duration: {time taken if applicable}
```

### research-log.md
Record all research activities (see Phase 3 format above).

### question-lists.md
Record all question lists:
```
## Question List - Phase {N}: {Feature Module Name}
- Generated: {timestamp}
- Status: {Open / Answered}

1. {Question text}
   - Answer: {user's answer or "Pending"}
2. ...
```
