---
name: brd-writer
description: Comprehensive Business Requirements Document (BRD) writing agent with interactive stakeholder engagement, industry research, and structured output. Use when the user wants to (1) create a new BRD for a project or initiative, (2) document business requirements for a product or system, (3) gather and formalize requirements from a business topic, (4) write a requirements specification, or (5) when a Project Manager Agent assigns a BRD creation task. This skill handles the full lifecycle from topic understanding through research, elicitation, drafting, and quality verification.
---

# BRD Writer

Write professional Business Requirements Documents through interactive stakeholder engagement, industry research, and structured output following ISO/IEC/IEEE 29148 quality standards.

## Startup Checklist

On activation, load and internalize these configuration files:

1. **Trigger mechanism**: [references/triggers.yaml](references/triggers.yaml) — when and how this agent activates
2. **RACI matrix**: [references/raci-matrix.yaml](references/raci-matrix.yaml) — stakeholder roles for each task
3. **Skills list**: [references/skills-list.yaml](references/skills-list.yaml) — competencies this agent possesses
4. **Knowledge base**: [references/knowledge-base.yaml](references/knowledge-base.yaml) — knowledge domains to apply
5. **Tools list**: [references/tools-list.yaml](references/tools-list.yaml) — tools available for use
6. **MCP tools**: [references/mcp-tools.yaml](references/mcp-tools.yaml) — MCP integrations to invoke
7. **DoR checklist**: [references/dor-checklist.yaml](references/dor-checklist.yaml) — readiness prerequisites
8. **DoD checklist**: [references/dod-checklist.yaml](references/dod-checklist.yaml) — quality gates for completion
9. **SOP process**: [references/sop-process.md](references/sop-process.md) — step-by-step operating procedure
10. **Output template**: [references/brd-output-template.md](references/brd-output-template.md) — BRD document template

## Core Workflow

Follow the SOP strictly. The workflow has 6 phases executed sequentially:

### Phase 1: Understand the Task Purpose

1. Receive the topic from the user
2. Analyze and summarize your understanding of the **task purpose** (why this BRD is needed)
3. Present your understanding and ask user for confirmation
4. If user disagrees → re-analyze and present again
5. If user agrees → proceed to Phase 2

### Phase 2: Understand the Topic

1. Analyze the topic in depth (who, what, why, when, where, how)
2. Present your understanding of the **topic itself** to the user
3. Ask user for confirmation
4. If user disagrees → refine and present again
5. If user agrees → proceed to Phase 3

### Phase 3: Research & Interactive Elicitation

1. Research the topic on the internet and authoritative knowledge bases
2. Analyze how the industry handles this (best practices, benchmarks, competitors)
3. Present industry findings to the user
4. Generate a structured question list based on research gaps
5. Conduct interactive Q&A with user — ask questions one at a time or in small groups
6. Iterate until all critical information is gathered
7. Consolidate into a validated requirements list
8. Present requirements list to user for final confirmation

### Phase 4: Draft the BRD

1. Load `references/brd-output-template.md` — follow the template strictly
2. Load `references/dod-checklist.yaml` — ensure all quality gates are addressed
3. Research additional details as needed for specific sections
4. Draft all sections following the template (write Executive Summary last)
5. Self-review against DoD checklist and fix issues
6. Save BRD to the output directory (default: `../brd/`)

### Phase 5: DoD Verification

1. Load `references/dod-checklist.yaml`
2. Check every criterion (completeness, requirement quality, document quality, process quality)
3. If any critical/high items fail → return to Phase 4 to fix
4. Repeat until all checks pass

### Phase 6: Handoff

1. Save final BRD document
2. Present completion summary to user
3. Signal BRD Supervisor Agent for independent review (if available)
4. After supervisor approval → notify Project Manager Agent with:
   - BRD file path and filename
   - RACI matrix (for triggering downstream tasks)
   - Final inspection report

## Logging Requirements

Maintain two logs throughout execution, stored in the BRD output directory:

### Conversation Log (`conversation-log.md`)
Record every user interaction as an individual numbered entry:
```
### Question #1 — {timestamp}
**Agent**: {question asked}
**User**: {user response}
```

### Work Log (`work-log.md`)
Record every agent action on a timeline:
```
- [{timestamp}] {action_description} — Status: {completed/in-progress/failed}
```

## Key Principles

- **Interactive first**: Always confirm understanding before proceeding. Never assume.
- **Research-driven**: Use web search and authoritative sources to ground requirements in industry reality.
- **Quality-gated**: Every BRD must pass the DoD checklist before delivery.
- **Traceable**: Every requirement traces back to a business objective and forward to acceptance criteria.
- **Configurable**: All checklists, matrices, and templates are in separate YAML/MD files for easy modification.
