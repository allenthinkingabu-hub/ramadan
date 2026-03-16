# OUT-03: Dependency Map (Inbound & Outbound)

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Dependency Overview

| Metric | Count |
|--------|-------|
| Inbound callers (components that depend on this target) | {inbound_count} |
| Outbound dependencies (components this target depends on) | {outbound_count} |
| Circular dependencies detected | {circular_count} |
| Direct dependencies | {direct_count} |
| Transitive dependencies (1 hop) | {transitive_count} |

---

## 2. Inbound Dependencies (Who Calls This Target)

> Components, modules, or external systems that invoke or depend on this target.

| Caller | Location | Coupling Type | Interface Used | Call Frequency | Notes |
|--------|----------|--------------|----------------|----------------|-------|
| {caller_1} | {location_1} | {coupling_type_1} | {interface_1} | {frequency_1} | {notes_1} |
| {caller_2} | {location_2} | {coupling_type_2} | {interface_2} | {frequency_2} | {notes_2} |
| {caller_n} | {location_n} | {coupling_type_n} | {interface_n} | {frequency_n} | {notes_n} |

> **Note**: {no_inbound_statement_if_none}
> Coupling types: `Direct import` `Interface contract` `Dependency injection` `Event subscription` `Configuration reference` `Shared database table`

---

## 3. Outbound Dependencies (What This Target Depends On)

### 3.1 Internal Dependencies (Within the Same Repository)

| Dependency | Type | Location | Interface Contract | Used For | Removable? |
|-----------|------|----------|-------------------|---------|------------|
| {dep_1} | {type_1} | {location_1} | {contract_1} | {used_for_1} | {removable_1} |
| {dep_2} | {type_2} | {location_2} | {contract_2} | {used_for_2} | {removable_2} |

### 3.2 External Dependencies (Third-Party Libraries / Frameworks)

| Dependency | Version | Package Manager | Used For | Optional? | License |
|-----------|---------|----------------|---------|-----------|---------|
| {ext_dep_1} | {version_1} | {pm_1} | {used_for_1} | {optional_1} | {license_1} |
| {ext_dep_2} | {version_2} | {pm_2} | {used_for_2} | {optional_2} | {license_2} |

### 3.3 Infrastructure Dependencies (Databases, Message Queues, External Services)

| Dependency | Type | Connection Method | Required? | Fallback | Notes |
|-----------|------|------------------|-----------|----------|-------|
| {infra_dep_1} | {type_1} | {connection_1} | {required_1} | {fallback_1} | {notes_1} |
| {infra_dep_2} | {type_2} | {connection_2} | {required_2} | {fallback_2} | {notes_2} |

---

## 4. Interface Contracts

> Documented contracts for each inbound interface this target exposes.

### Interface: {interface_name_1}

**Type**: {interface_type_1}
**Defined In**: `{file_path}:{line_number}`
**Callers**: {callers_list_1}

**Input Contract**:
```
{input_schema_1}
```

**Output Contract**:
```
{output_schema_1}
```

**Error Contract**:
```
{error_schema_1}
```

**Breaking Change Risk**: {breaking_change_risk_1}

---

### Interface: {interface_name_2}

**Type**: {interface_type_2}
**Defined In**: `{file_path}:{line_number}`
**Callers**: {callers_list_2}

**Input Contract**:
```
{input_schema_2}
```

**Output Contract**:
```
{output_schema_2}
```

**Error Contract**:
```
{error_schema_2}
```

**Breaking Change Risk**: {breaking_change_risk_2}

---

## 5. Coupling Analysis

| Dependency | Coupling Level | Coupling Type | Transformation Impact | Recommended Action |
|-----------|---------------|--------------|----------------------|-------------------|
| {dep_1} | {level_1} | {type_1} | {impact_1} | {action_1} |
| {dep_2} | {level_2} | {type_2} | {impact_2} | {action_2} |

> Coupling levels: `Tight` `Moderate` `Loose`
> Coupling types: `Content` `Common` `Control` `Stamp` `Data` `Message`

---

## 6. Circular Dependencies

| Cycle | Files Involved | Risk Level | Notes |
|-------|--------------|------------|-------|
| {cycle_1} | {files_1} | {risk_1} | {notes_1} |

> If no circular dependencies exist, state: "No circular dependencies detected in this target."

---

## 7. Dependency Change Impact Matrix

> For the planned transformation, which dependencies will be affected?

| Dependency | Impact Type | Transformation Required | Risk Level | Notes |
|-----------|------------|------------------------|------------|-------|
| {dep_1} | {impact_type_1} | {transformation_1} | {risk_1} | {notes_1} |
| {dep_2} | {impact_type_2} | {transformation_2} | {risk_2} | {notes_2} |

> Impact types: `No change` `Interface update` `Contract renegotiation` `Full replacement` `Removal`
