# Trigger Mechanisms — Transformation Target Current State Analysis (SA-TRF-001)

> Configurable trigger definitions for the Transformation Target Current State Analysis AI Agent.
> Edit this file to add, modify, or remove triggers as the workflow evolves.

---

## Trigger Definitions

| Trigger ID | Trigger Type | Trigger Condition | Parameters Provided | Notes |
|------------|-------------|-------------------|---------------------|-------|
| TRG-01 | PM Agent Assignment | PM Agent assigns task SA-TRF-001 via RACI matrix | project_path, target_name, target_path, transformation_intent, analysis_scope | Primary trigger for planned transformation work |
| TRG-02 | User Designation | User explicitly names a method, class, component, or module for transformation | target_name, target_path (required); project_path, intent (collected via intake) | Direct user-initiated analysis |
| TRG-03 | Upstream Skill Handoff | Project Structure Scan (SA-DISC-001) completes and identifies a transformation target in OUT-07 | project_path, target_scope (from OUT-07), scan_output_dir | Chained trigger from discovery phase |
| TRG-04 | Refactoring Initiative | A refactoring initiative is initiated on a specific module (e.g., tech debt sprint, migration project) | project_path, module_name, initiative_description | Triggered by engineering team process |
| TRG-05 | Feature Addition | A new feature requires modifying an existing component and current state understanding is needed before design | project_path, target_component, feature_description | Pre-design investigation trigger |

---

## Required Trigger Parameters

The following parameters must be supplied either via the trigger payload or collected interactively during Target Intake (Step 0):

| Parameter | Required | Source | Description |
|-----------|:--------:|--------|-------------|
| `project_path` | YES | Trigger / Intake | Local file path to the project root |
| `project_name` | YES | Trigger / Intake (infer from dir) | Project name |
| `target_name` | YES | Trigger / Intake | Name of the method / class / component / module |
| `target_path` | YES | Trigger / Intake | File path(s) containing the target |
| `transformation_intent` | YES | Trigger / Intake | What change is intended (extract, migrate, refactor, add caching, etc.) |
| `analysis_scope` | YES | Trigger / Intake | `target-only` / `include-direct-dependencies` / `broad` |
| `known_constraints` | NO | Trigger / Intake | Upfront constraints the user is aware of |

---

## Trigger Validation

Before proceeding past Step 0, the agent validates:

1. `project_path` exists and is accessible: `ls {project_path}` succeeds
2. `target_path` exists and is readable: `ls {target_path}` succeeds
3. `transformation_intent` is non-empty
4. `analysis_scope` is one of: `target-only`, `include-direct-dependencies`, `broad`
