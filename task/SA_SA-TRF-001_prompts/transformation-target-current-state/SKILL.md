---
name: transformation-target-current-state
description: >
  Deep-dive current state analysis of a specific code transformation target (method, class, module,
  or service) before refactoring, extraction, migration, or feature addition begins. Produces 7
  structured deliverables: Code Structure Map, Responsibility Analysis, Dependency Map, Data Flow
  Analysis, Test Coverage Assessment, Technical Debt Register, and a consolidated Current State
  Report (user-confirmed before transformation proceeds).

  USE when: (1) PM Agent assigns SA-TRF-001 via RACI, (2) a refactor/migration/rewrite is planned
  and the target must be deeply understood first, (3) a feature is being added to a complex component
  needing risk assessment, (4) SA-DISC-001 has identified a transformation target, (5) a full picture
  of a component's responsibilities, dependencies, and transformation risks is needed.

  DO NOT USE for full project scans (use SA-DISC-001) or lightweight code reading without structured
  deliverables.
---

# Transformation Target Current State Analysis (SA-TRF-001)

## Workflow Overview

This is a 5-step interactive workflow. Steps 0-3 are conversational. Step 4 is investigative.
Step 5 is verification and handoff.

```
Step 0: Target Intake (confirm project_path, target, intent, scope)
   ↓
Step 1: Understand Task Purpose (confirm WHY the transformation is needed)
   ↓
Step 2: Understand the Target (tech stack, size, framework, architecture)
   ↓
Step 3: Research & Question Generation (industry practices, validated requirements)
   ↓
Step 4: Investigate & Produce Deliverables (OUT-01 through OUT-07)
   ↓
Step 5: DoD Self-Verification & Handoff (supervisor + PM Agent notification)
```

For detailed sub-steps, memory operations, and cross-step rules: **`references/sop.md`**

---

## Step 0: Target Intake

Required parameters (collect interactively if missing from trigger payload):

| Parameter | Validation |
|-----------|-----------|
| `project_path` | `ls {project_path}` succeeds |
| `target_name` | Non-empty string |
| `target_path` | `ls {target_path}` succeeds |
| `transformation_intent` | Non-empty, describes concrete change type |
| `analysis_scope` | One of: `target-only` / `include-direct-dependencies` / `broad` |
| `project_name` | Can infer from directory |
| `known_constraints` | Optional |

Run all DoR checks before proceeding. See **`references/dor.md`**.

**Session ID format**: `SA-TRF-001-{YYYYMMDD-HHMMSS}`
**Output directory**: `outputs/analysis-{YYYYMMDD-HHMMSS}/`
**Initialize DB**: `python scripts/init_memory.py --session-id {SESSION_ID} ...`

---

## Step 4: Produce Deliverables

Produce outputs in order. Save each to `outputs/analysis-{YYYYMMDD-HHMMSS}/`:

| Output | Filename | Template | Key Tools |
|--------|---------|---------|-----------|
| OUT-01 | `OUT-01-code-structure-map.md` | `templates/code-structure-map-template.md` | Glob, Bash (wc -l, tree) |
| OUT-02 | `OUT-02-responsibility-analysis.md` | `templates/responsibility-analysis-template.md` | Read (key files) |
| OUT-03 | `OUT-03-dependency-map.md` | `templates/dependency-map-template.md` | Grep (callers), Read (imports) |
| OUT-04 | `OUT-04-data-flow-analysis.md` | `templates/data-flow-analysis-template.md` | Read, Grep, IDE Diagnostics |
| OUT-05 | `OUT-05-test-coverage-report.md` | `templates/test-coverage-report-template.md` | Glob (test files), Read |
| OUT-06 | `OUT-06-tech-debt-risk-register.md` | `templates/tech-debt-risk-register-template.md` | Grep (TODO/FIXME/HACK) |
| OUT-07 | `OUT-07-current-state-report.md` | `templates/current-state-report-template.md` | Consolidate OUT-01~06 |

**Template rule**: Copy template, populate every `{placeholder}`, write to output dir. Never leave `{placeholder}` in final output (DoD-08).

**OUT-07 requires explicit user confirmation before Step 5.**

---

## Memory Protocol

Use `MemoryOps` from `scripts/memory_ops.py` throughout the session.

**Write on every significant finding** — don't batch at the end:

- `record_finding()` — each investigation finding (Step 4)
- `record_constraint()` — each hard/soft constraint
- `record_risk()` — each risk or debt item
- `record_decision()` — each confirmed user decision (Steps 1-3)
- `record_knowledge()` — tech stack, interfaces, architecture facts
- `record_lesson()` — insights for future sessions (Step 5)
- `record_dod_check()` — each DoD check result (Step 5)

**Read at session start** to avoid redundant questions:
- `load_history()` → detect re-analysis mode
- `load_knowledge()` → pre-fill known answers (with confidence decay applied)
- `query_memory(type="risk")` → present prior risks in Step 3

For memory schema, SQL examples, and decay protocol: **`memory/index.md`**

---

## Step 5: DoD Self-Verification

```bash
python scripts/verify_dod.py \
    --output-dir outputs/analysis-{YYYYMMDD-HHMMSS} \
    --session-id {SESSION_ID} \
    --round 1 \
    --save-report
```

20 checks must pass. Fix failures and re-run (max 3 rounds). See **`references/dod.md`** for all 20 checks and failure remediation actions.

After 20/20 pass:
1. Trigger `transformation-target-supervisor` skill — pass all deliverable paths + DoD report path
2. Notify PM Agent with deliverables path, OUT-01~07 file list, RACI matrix path, target summary

---

## MCP Tools

| Tool | When to Use |
|------|------------|
| `context7` (resolve → query) | Framework lifecycle, annotation semantics, library conventions |
| `mcp__ide__getDiagnostics` | Type errors, unresolved imports, deprecated API warnings |
| `mcp__ide__executeCode` | Verify behavior of Python data transformation functions |

See **`config/mcp-tools.md`** for usage patterns.

---

## Key Reference Files

| File | Purpose |
|------|---------|
| `references/sop.md` | Full sub-steps for all 5 phases |
| `references/dor.md` | 10 Definition of Ready checks |
| `references/dod.md` | 20 Definition of Done checks + remediation |
| `references/output-templates.md` | Template registry + usage rules |
| `memory/index.md` | SQLite schema + memory operation examples |
| `config/raci.md` | Role assignments + downstream task triggers |
| `config/triggers.md` | Skill activation triggers (TRG-01 through TRG-05) |
| `config/skills-and-knowledge.md` | Required agent skills and domain knowledge |

---

## Logging Requirements

- **`logs/conversation-log.md`**: Append all interactive Q&A (Steps 0-4)
- **`logs/work-log.md`**: Append timestamped action entries (Steps 0-5)
- Both are required for DoD-14 and DoD-15.
