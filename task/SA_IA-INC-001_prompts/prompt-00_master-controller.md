# Master Controller — SA_IA-INC-001 Project Structure Scan Skill Generation

## Overview

This is the master controller prompt that orchestrates the sequential execution of 5 sub-prompts to generate the complete **Project Structure Scan AI Agent Skill**. Each sub-prompt produces a specific set of deliverables. The master controller ensures ordering, validation, and completeness.

## Source of Truth

All requirements come from: `task/SA_IA-INC-001_Project_Structure_Scan_agent_skill_definition.md`

## Target Skill Output Directory

```
project-structure-scan/
```

This directory should be created under the working directory specified by the user at runtime.

## Execution Sequence

```
prompt-01 → Validate → prompt-02 → Validate → prompt-03 → Validate → prompt-04 → Validate → prompt-05 → Validate → Final Cross-Check
```

## Step-by-Step Execution

### Step 1: Execute prompt-01_init-and-config.md
- **Scope**: Skill initialization + configuration files (Requirements 1–6)
- **Expected Deliverables**:
  - [ ] `project-structure-scan/` directory created
  - [ ] `SKILL.md` skeleton with frontmatter
  - [ ] `config/triggers.md`
  - [ ] `config/raci.md`
  - [ ] `config/skills-and-knowledge.md`
  - [ ] `config/tools.md`
  - [ ] `config/mcp-tools.md`
- **Validation**: Verify all 5 config files exist and contain substantive content (not empty placeholders). Verify SKILL.md has valid YAML frontmatter with `name` and `description`.
- **On Fail**: Re-execute prompt-01 for missing items only.
- **On Pass**: Proceed to Step 2.

### Step 2: Execute prompt-02_templates-and-sop.md
- **Scope**: Output templates + SOP + DoD + DoR (Requirements 7–10)
- **Expected Deliverables**:
  - [ ] `templates/structure-tree-template.md` (OUT-01)
  - [ ] `templates/module-relationship-template.md` (OUT-02)
  - [ ] `templates/layering-analysis-template.md` (OUT-03)
  - [ ] `templates/dependency-map-template.md` (OUT-04)
  - [ ] `templates/module-summary-template.md` (OUT-05)
  - [ ] `templates/scan-report-template.md` (OUT-06)
  - [ ] `references/sop.md`
  - [ ] `references/dod.md`
  - [ ] `references/dor.md`
  - [ ] `references/output-templates.md`
- **Validation**: Verify all 10 files exist. Each template must contain a complete structure with placeholder fields (not just a title). SOP must define a step-by-step process. DoD must contain checkable items. DoR must list prerequisites.
- **On Fail**: Re-execute prompt-02 for missing/incomplete items only.
- **On Pass**: Proceed to Step 3.

### Step 3: Execute prompt-03_memory-architecture.md
- **Scope**: Long-term memory architecture + utilization protocol
- **Expected Deliverables**:
  - [ ] `memory/index.md` (memory usage description)
  - [ ] `scripts/init_memory.py` (SQLite schema initialization script)
  - [ ] `scripts/memory_ops.py` (memory CRUD operations library)
  - [ ] Memory Utilization Protocol section appended to `SKILL.md`
- **Validation**: Run `python scripts/init_memory.py` to verify it creates a valid SQLite database with 4 tables (`task_memory`, `dod_checks`, `knowledge_base`, `scan_history`). Verify `memory_ops.py` contains functions for startup queries, insert operations, confidence decay, and contradiction detection. Verify SKILL.md now contains Memory Utilization Protocol section.
- **On Fail**: Fix script errors or missing sections, re-validate.
- **On Pass**: Proceed to Step 4.

### Step 4: Execute prompt-04_workflow-and-logging.md
- **Scope**: Interactive workflow + logging + DoD verification (Requirements 11–13, 16–17)
- **Expected Deliverables**:
  - [ ] `logs/conversation-log.md` (template)
  - [ ] `logs/work-log.md` (template)
  - [ ] `scripts/verify_dod.py` (DoD verification script)
  - [ ] Interactive workflow (Phase 1–4) written into `SKILL.md`
  - [ ] `research/` directory created
  - [ ] `diagrams/` directory created
- **Validation**: Verify `scripts/verify_dod.py` runs without errors and checks against `references/dod.md`. Verify SKILL.md contains complete Phase 1–4 workflow with memory utilization integration. Verify log templates contain proper structure.
- **On Fail**: Fix script errors or missing workflow sections, re-validate.
- **On Pass**: Proceed to Step 5.

### Step 5: Execute prompt-05_supervisor.md
- **Scope**: Supervisor AI Agent Skill (Requirements 14–15)
- **Expected Deliverables**:
  - [ ] `project-structure-scan-supervisor/SKILL.md` (complete supervisor skill)
  - [ ] `project-structure-scan-supervisor/scripts/inspect.py` (inspection script)
  - [ ] `project-structure-scan-supervisor/references/inspection-checklist.md`
  - [ ] `project-structure-scan-supervisor/templates/inspection-report-template.md`
- **Validation**: Verify supervisor SKILL.md contains valid frontmatter. Verify `inspect.py` checks all 13 requirements. Verify inspection report template matches the format defined in Requirement 14.4. Verify PM notification logic is included (Requirement 14.5 and 15).
- **On Fail**: Fix missing items, re-validate.
- **On Pass**: Proceed to Final Cross-Check.

### Final Cross-Check

After all 5 steps pass, perform a complete cross-check:

1. **File Completeness**: Verify the full directory tree matches the expected structure (see below).
2. **SKILL.md Completeness**: Verify SKILL.md contains all sections: frontmatter, workflow (Phase 0–4), memory utilization protocol, logging requirements, reference file links.
3. **Cross-Reference Integrity**: Verify all file paths referenced in SKILL.md actually exist.
4. **Script Execution**: Run `scripts/init_memory.py` and `scripts/verify_dod.py` to confirm they execute without errors.
5. **Supervisor Coverage**: Verify supervisor's inspection checklist covers all 13 requirements.

### Expected Final Directory Tree

```
project-structure-scan/
├── SKILL.md
├── config/
│   ├── triggers.md
│   ├── raci.md
│   ├── skills-and-knowledge.md
│   ├── tools.md
│   └── mcp-tools.md
├── templates/
│   ├── structure-tree-template.md
│   ├── module-relationship-template.md
│   ├── layering-analysis-template.md
│   ├── dependency-map-template.md
│   ├── module-summary-template.md
│   └── scan-report-template.md
├── references/
│   ├── sop.md
│   ├── dod.md
│   ├── dor.md
│   └── output-templates.md
├── scripts/
│   ├── init_memory.py
│   ├── memory_ops.py
│   └── verify_dod.py
├── memory/
│   └── index.md
├── logs/
│   ├── conversation-log.md
│   └── work-log.md
├── research/
├── diagrams/
├── phase1-questions.md          (created at runtime)
├── phase2-questions.md          (created at runtime)
├── phase3-questions.md          (created at runtime)
├── validated-requirements.md    (created at runtime)
└── project-structure-report.md  (created at runtime)

project-structure-scan-supervisor/
├── SKILL.md
├── scripts/
│   └── inspect.py
├── references/
│   └── inspection-checklist.md
└── templates/
    └── inspection-report-template.md
```

## Error Handling

- If any step fails validation 3 times consecutively, STOP and report the failure to the user with details of what is missing or broken.
- Never skip a step. Each step must pass validation before proceeding.
- Never overwrite files produced by a previous step unless explicitly fixing a validation failure in that file.
