# OUT-02: Current Responsibility & Behavior Analysis

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Executive Summary

> One-paragraph summary of what this target does and why it exists.

{executive_summary}

---

## 2. Responsibility Inventory

> Every distinct responsibility this target owns. Each responsibility must be traceable to one or more source files.

| ID | Responsibility | Category | Primary File(s) | Criticality |
|----|---------------|----------|-----------------|-------------|
| R-01 | {responsibility_1} | {category_1} | {files_1} | {criticality_1} |
| R-02 | {responsibility_2} | {category_2} | {files_2} | {criticality_2} |
| R-0N | {responsibility_n} | {category_n} | {files_n} | {criticality_n} |

> Categories: `Core Logic` `Data Transformation` `I/O` `Orchestration` `Validation` `Error Handling` `Caching` `Authorization` `Notification` `Configuration`
> Criticality: `Critical` `High` `Medium` `Low`

---

## 3. Behavioral Specifications

> For each major responsibility, document its concrete behavior: inputs, processing logic, outputs, and side effects.

### R-01: {responsibility_1}

**Trigger / Input Condition**: {trigger_1}
**Processing Logic**: {processing_logic_1}
**Output / Result**: {output_1}
**Side Effects**: {side_effects_1}
**Error Behavior**: {error_behavior_1}
**Source Reference**: `{file_path}:{line_number}`

---

### R-02: {responsibility_2}

**Trigger / Input Condition**: {trigger_2}
**Processing Logic**: {processing_logic_2}
**Output / Result**: {output_2}
**Side Effects**: {side_effects_2}
**Error Behavior**: {error_behavior_2}
**Source Reference**: `{file_path}:{line_number}`

---

*(Repeat for each responsibility)*

---

## 4. Entry Points & Exit Points

### Entry Points (How the target is invoked)

| Entry Point | Protocol | Caller Type | Input Contract | Description |
|------------|---------|------------|----------------|-------------|
| {entry_1} | {protocol_1} | {caller_type_1} | {input_contract_1} | {description_1} |
| {entry_2} | {protocol_2} | {caller_type_2} | {input_contract_2} | {description_2} |

### Exit Points (How the target returns results or signals)

| Exit Point | Type | Output Contract | Error Signals | Description |
|-----------|------|-----------------|---------------|-------------|
| {exit_1} | {type_1} | {output_contract_1} | {error_signals_1} | {description_1} |
| {exit_2} | {type_2} | {output_contract_2} | {error_signals_2} | {description_2} |

---

## 5. Side Effects Register

> All operations that affect external state (outside the target's own memory scope).

| Side Effect | Target System | Trigger Condition | Reversible? | Impact |
|------------|--------------|-------------------|-------------|--------|
| {side_effect_1} | {system_1} | {condition_1} | {reversible_1} | {impact_1} |
| {side_effect_2} | {system_2} | {condition_2} | {reversible_2} | {impact_2} |

---

## 6. State Management

| State Item | Storage Mechanism | Scope | Lifecycle | Notes |
|-----------|------------------|-------|-----------|-------|
| {state_1} | {mechanism_1} | {scope_1} | {lifecycle_1} | {notes_1} |
| {state_2} | {mechanism_2} | {scope_2} | {lifecycle_2} | {notes_2} |

> Scope: `In-memory` `Session` `Request` `Process` `Persistent` `Shared`

---

## 7. Framework-Managed Behaviors

> Behaviors that are injected or controlled by the framework rather than explicit code.

| Behavior | Framework | Mechanism | Configuration | Notes |
|---------|-----------|-----------|---------------|-------|
| {behavior_1} | {framework_1} | {mechanism_1} | {config_1} | {notes_1} |
| {behavior_2} | {framework_2} | {mechanism_2} | {config_2} | {notes_2} |

---

## 8. Responsibility Map (Ownership Matrix)

| File | Responsibilities Owned |
|------|----------------------|
| {file_1} | {responsibility_ids_1} |
| {file_2} | {responsibility_ids_2} |
| {file_n} | {responsibility_ids_n} |
