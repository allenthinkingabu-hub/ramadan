# OUT-01: Transformation Target Code Structure Map

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Directory Layout

> Annotated tree of all files within the transformation target scope. Each file is tagged with its role and line count.

```
{target_path}/
├── {file_or_dir_1}                    [{role_1}] ({loc_1} lines)
│   ├── {file_1_1}                     [{role_1_1}] ({loc_1_1} lines)
│   └── {file_1_2}                     [{role_1_2}] ({loc_1_2} lines)
├── {file_or_dir_2}                    [{role_2}] ({loc_2} lines)
└── {file_or_dir_n}                    [{role_n}] ({loc_n} lines)
```

> Role tags: `[entry-point]` `[core-logic]` `[data-model]` `[interface]` `[config]` `[utility]` `[test]` `[migration]` `[bootstrap]`

---

## 2. File Inventory

| File | Role | Lines of Code | Language | Last Modified | Notes |
|------|------|--------------|----------|---------------|-------|
| {file_path_1} | {role_1} | {loc_1} | {language_1} | {last_modified_1} | {notes_1} |
| {file_path_2} | {role_2} | {loc_2} | {language_2} | {last_modified_2} | {notes_2} |
| {file_path_n} | {role_n} | {loc_n} | {language_n} | {last_modified_n} | {notes_n} |

**Total Files**: {total_files}
**Total LOC**: {total_loc}

---

## 3. Size & Complexity Summary

| Metric | Value |
|--------|-------|
| Total files in scope | {total_files} |
| Total lines of code | {total_loc} |
| Largest file | {largest_file} ({largest_file_loc} lines) |
| Average file size | {avg_file_loc} lines |
| Primary language | {primary_language} |
| Secondary language(s) | {secondary_languages} |

---

## 4. Top-Level Package / Module Structure

> High-level grouping of files by logical package or module. List each top-level package with its sub-packages and purpose.

| Package / Module | Sub-packages | Purpose | Files |
|-----------------|-------------|---------|-------|
| {package_1} | {subpackages_1} | {purpose_1} | {file_count_1} |
| {package_2} | {subpackages_2} | {purpose_2} | {file_count_2} |
| {package_n} | {subpackages_n} | {purpose_n} | {file_count_n} |

---

## 5. Entry Points

> All public-facing and framework-managed entry points into the transformation target.

| Entry Point | Type | File | Signature / Route | Description |
|------------|------|------|-------------------|-------------|
| {entry_name_1} | {type_1} | {file_1} | {signature_1} | {description_1} |
| {entry_name_2} | {type_2} | {file_2} | {signature_2} | {description_2} |
| {entry_name_n} | {type_n} | {file_n} | {signature_n} | {description_n} |

> Entry point types: `HTTP endpoint` `CLI command` `Queue consumer` `Event listener` `Scheduled job` `Framework lifecycle hook` `Public API method`

---

## 6. Analysis Scope Boundary

**Analysis Scope**: {analysis_scope}

| File | In Scope? | Reason |
|------|-----------|--------|
| {file_1} | {in_scope_1} | {reason_1} |
| {file_2} | {in_scope_2} | {reason_2} |

**Files Explicitly Excluded**:
- {excluded_file_1}: {exclusion_reason_1}
- {excluded_file_2}: {exclusion_reason_2}
