# Prompt 02 — Output Templates, SOP, DoD, and DoR

## Context

You are continuing the creation of the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 2 of 5. Step 1 has already created the directory structure, SKILL.md skeleton, and all config files.

## Scope — Requirements 7 through 10

This prompt covers ONLY the following:
- Requirement 7: Output deliverable templates (OUT-01 through OUT-06)
- Requirement 8: SOP process
- Requirement 9: DoD quality gates
- Requirement 10: DoR prerequisites

## Pre-requisites

Verify these exist before proceeding (created by prompt-01):
- `project-structure-scan/SKILL.md`
- `project-structure-scan/config/` (with 5 config files)
- `project-structure-scan/templates/` (directory exists, empty)
- `project-structure-scan/references/` (directory exists, empty)

If any are missing, STOP and report the issue.

## Instructions

### 1. Create templates/structure-tree-template.md (OUT-01)

Template for the Project Structure Tree deliverable:

```markdown
# Project Structure Tree — {project_name}

- **Scan Date**: {date}
- **Scanned By**: SA-DISC-001 Agent (Session: {session_id})
- **Project Root**: {project_root_path}
- **Total Directories**: {count}
- **Total Files**: {count}
- **Estimated LOC**: {count}

## Directory Hierarchy

<!-- Annotated tree output. Each directory has a one-line purpose description. -->

{project_root}/
├── {dir_1}/                  ← {purpose: e.g., "Application entry point and configuration"}
│   ├── {sub_dir_1}/          ← {purpose}
│   └── {sub_dir_2}/          ← {purpose}
├── {dir_2}/                  ← {purpose}
│   ├── ...
...

## Key Files at Root Level

| File | Purpose |
|------|---------|
| {file_name} | {purpose} |
| ... | ... |

## Directory Purpose Summary

| Directory | Layer/Role | Purpose | Key Contents |
|-----------|-----------|---------|-------------|
| {dir} | {e.g., Controller/Service/Repository/Config} | {purpose} | {notable files or patterns} |
| ... | ... | ... | ... |

## Observations

- {observation_1: e.g., "Standard Maven project structure detected"}
- {observation_2}
- ...
```

### 2. Create templates/module-relationship-template.md (OUT-02)

Template for the Module Relationship Diagram deliverable:

```markdown
# Module Relationship Diagram — {project_name}

- **Scan Date**: {date}
- **Total Modules Identified**: {count}

## Module Dependency Diagram (Mermaid)

<!-- Direction: top-down shows layering; left-right shows peer communication -->

\`\`\`mermaid
graph TD
    subgraph "{layer_name: e.g., Presentation Layer}"
        A["{module_name}"]
    end

    subgraph "{layer_name: e.g., Business Logic Layer}"
        B["{module_name}"]
        C["{module_name}"]
    end

    subgraph "{layer_name: e.g., Data Access Layer}"
        D["{module_name}"]
    end

    A --> B
    A --> C
    B --> D
    C --> D
\`\`\`

## Module Dependency Matrix

| Module (depends on →) | {Module A} | {Module B} | {Module C} | {Module D} |
|----------------------|:---:|:---:|:---:|:---:|
| **{Module A}** | — | ✅ | ✅ | ❌ |
| **{Module B}** | ❌ | — | ❌ | ✅ |
| **{Module C}** | ❌ | ❌ | — | ✅ |
| **{Module D}** | ❌ | ❌ | ❌ | — |

## Dependency Details

| From Module | To Module | Dependency Type | Evidence (file/import) |
|-------------|-----------|----------------|----------------------|
| {module_A} | {module_B} | {compile/runtime/test/optional} | {import statement or config reference} |
| ... | ... | ... | ... |

## Circular Dependencies (if any)

- {module_X} ↔ {module_Y}: {description of circular dependency and risk}
- ...

## Observations

- {observation_1}
- ...
```

### 3. Create templates/layering-analysis-template.md (OUT-03)

Template for the Layering Pattern Analysis deliverable:

```markdown
# Layering Pattern Analysis — {project_name}

- **Scan Date**: {date}
- **Identified Primary Pattern**: {pattern_name: e.g., "Layered Architecture with DDD Tactical Patterns"}
- **Confidence Level**: {high/medium/low}

## Pattern Identification Summary

| Candidate Pattern | Evidence Found | Confidence | Verdict |
|-------------------|---------------|------------|---------|
| MVC | {evidence or "not found"} | {high/medium/low/none} | {✅ Match / ❌ No Match / ⚠️ Partial} |
| MVP | ... | ... | ... |
| MVVM | ... | ... | ... |
| Layered Architecture | ... | ... | ... |
| Hexagonal (Ports & Adapters) | ... | ... | ... |
| Clean Architecture | ... | ... | ... |
| Onion Architecture | ... | ... | ... |
| DDD (Domain-Driven Design) | ... | ... | ... |
| Microservices | ... | ... | ... |
| Modular Monolith | ... | ... | ... |

## Primary Pattern Analysis

### Pattern: {identified_pattern_name}

**Definition**: {brief definition of the pattern}

**Evidence from Codebase**:
1. {evidence_1: e.g., "Separate `domain/`, `application/`, `infrastructure/` packages found"}
2. {evidence_2: e.g., "Repository interfaces defined in domain layer, implementations in infrastructure"}
3. ...

**Layer Mapping**:

| Architecture Layer | Codebase Mapping | Key Files/Packages |
|-------------------|-----------------|-------------------|
| {e.g., Domain Layer} | {e.g., `src/main/java/com/example/domain/`} | {key files} |
| {e.g., Application Layer} | {e.g., `src/main/java/com/example/application/`} | {key files} |
| ... | ... | ... |

**Layer Dependency Rules**:
- {rule_1: e.g., "Domain layer has no outward dependencies — VERIFIED ✅"}
- {rule_2: e.g., "Application layer depends only on Domain — VERIFIED ✅"}
- {rule_3: e.g., "Infrastructure depends on Domain via interfaces — VIOLATION ❌: direct entity usage found in XxxRepository.java:42"}

## Secondary Patterns (if applicable)

### {secondary_pattern_name}
- **Where**: {which part of the codebase}
- **Evidence**: {evidence}

## Pattern Violations & Risks

| Violation | Location | Severity | Description |
|-----------|----------|----------|-------------|
| {type} | {file:line} | {high/medium/low} | {description} |
| ... | ... | ... | ... |

## Recommendations

1. {recommendation_1}
2. ...
```

### 4. Create templates/dependency-map-template.md (OUT-04)

Template for the Package Dependency Map deliverable:

```markdown
# Package Dependency Map — {project_name}

- **Scan Date**: {date}
- **Package Manager**: {e.g., Maven/Gradle/npm/pip/cargo/go mod}
- **Manifest File**: {e.g., pom.xml, package.json, requirements.txt}

## Dependency Summary

| Category | Count |
|----------|-------|
| Direct dependencies | {count} |
| Dev/Test dependencies | {count} |
| Transitive dependencies (estimated) | {count} |
| Internal module dependencies | {count} |

## Third-Party Dependencies

| Dependency | Version | Category | Purpose | License |
|------------|---------|----------|---------|---------|
| {name} | {version} | {core/utility/framework/testing/logging/security} | {what it does} | {license} |
| ... | ... | ... | ... | ... |

## Internal Module Dependencies

| Module | Depends On | Dependency Mechanism |
|--------|-----------|---------------------|
| {module_A} | {module_B, module_C} | {e.g., Maven module dependency, import statements} |
| ... | ... | ... |

## Dependency Diagram (Mermaid)

\`\`\`mermaid
graph LR
    subgraph "Internal Modules"
        A["{module}"]
        B["{module}"]
    end
    subgraph "Third-Party"
        C["{library}"]
        D["{framework}"]
    end
    A --> B
    A --> C
    B --> D
\`\`\`

## Dependency Risks

| Risk | Dependency | Severity | Description |
|------|-----------|----------|-------------|
| Outdated version | {dep_name} | {high/medium/low} | {current vs latest version} |
| Known CVE | {dep_name} | {high/medium/low} | {CVE ID and description} |
| License conflict | {dep_name} | {high/medium/low} | {license issue} |
| Single point of failure | {dep_name} | {high/medium/low} | {critical dependency with no alternative} |

## Observations

- {observation_1}
- ...
```

### 5. Create templates/module-summary-template.md (OUT-05)

Template for the Module Responsibility Summary deliverable:

```markdown
# Module Responsibility Summary — {project_name}

- **Scan Date**: {date}
- **Total Modules**: {count}

## Module Overview

| # | Module Name | Layer | Primary Responsibility | LOC (est.) | Key Technologies |
|---|------------|-------|----------------------|------------|-----------------|
| 1 | {name} | {layer} | {one-line responsibility} | {loc} | {tech} |
| 2 | ... | ... | ... | ... | ... |

## Detailed Module Descriptions

### Module: {module_name}

- **Path**: `{path}`
- **Layer**: {architectural layer}
- **Primary Responsibility**: {responsibility}
- **Key Files**:
  | File | Purpose |
  |------|---------|
  | {file} | {purpose} |
- **Inbound Dependencies**: {who depends on this module}
- **Outbound Dependencies**: {what this module depends on}
- **Public Interfaces**: {exported APIs, interfaces, or contracts}
- **Notes**: {any observations, risks, or recommendations}

---

(Repeat for each module)

## Module Cohesion Assessment

| Module | Cohesion Level | Reasoning |
|--------|---------------|-----------|
| {module} | {high/medium/low} | {why} |

## Module Coupling Assessment

| Module Pair | Coupling Level | Type | Reasoning |
|-------------|---------------|------|-----------|
| {A} ↔ {B} | {tight/moderate/loose} | {content/common/control/data/message} | {why} |
```

### 6. Create templates/scan-report-template.md (OUT-06)

Template for the comprehensive final scan report:

```markdown
# Project Structure Scan Report — {project_name}

- **Report Date**: {date}
- **Task ID**: SA-DISC-001
- **Agent Session**: {session_id}
- **Project Path**: {project_root_path}

## Executive Summary

{2-3 paragraph summary of the project structure scan findings, key architecture pattern identified, major risks or observations, and recommendations.}

## 1. Project Overview

- **Project Name**: {name}
- **Domain**: {business domain}
- **Technology Stack**: {languages, frameworks, databases}
- **Scale**: {LOC, file count, module count}
- **Build System**: {build tool}
- **Repository Type**: {monorepo/polyrepo, mono/micro}

## 2. Project Structure Tree

{Reference or inline OUT-01 content}

## 3. Module Relationships

{Reference or inline OUT-02 content}

## 4. Architecture Pattern Analysis

{Reference or inline OUT-03 content}

## 5. Dependency Map

{Reference or inline OUT-04 content}

## 6. Module Responsibility Summary

{Reference or inline OUT-05 content}

## 7. Key Findings

| # | Finding | Category | Severity | Affected Area |
|---|---------|----------|----------|---------------|
| 1 | {finding} | {structure/pattern/dependency/risk} | {high/medium/low/info} | {module or area} |
| ... | ... | ... | ... | ... |

## 8. Risks & Technical Debt

| # | Risk/Debt | Impact | Likelihood | Mitigation |
|---|-----------|--------|------------|------------|
| 1 | {risk} | {impact} | {high/medium/low} | {suggested mitigation} |
| ... | ... | ... | ... | ... |

## 9. Recommendations

1. {recommendation_1}
2. {recommendation_2}
3. ...

## 10. Appendices

- **A**: Full directory tree listing
- **B**: Complete dependency list
- **C**: Scan methodology and tools used

## Approval

| Role | Name | Date | Status |
|------|------|------|--------|
| IT Architect (SA) | {name} | {date} | {Draft/Reviewed/Approved} |
| Solutions Architect | {name} | {date} | {status} |
| Technical Lead | {name} | {date} | {status} |
```

### 7. Create references/sop.md (Requirement 8)

Research and produce the SOP process for the Project Structure Scan task:

```markdown
# SOP — Project Structure Scan (SA-DISC-001)

## Process Flow

Phase 0: Initialization & Project Intake
  → Verify DoR → **collect project info from user (local path, git URL, branch, project name, scan scope, exclusions, purpose)** → user confirms intake summary → create output directory → init memory DB → load history

Phase 1: Understand Task Purpose (Interactive)
  → Present purpose understanding → user confirms → log to memory

Phase 2: Understand Target Project (Interactive)
  → Analyze codebase basics → present understanding → user confirms → log

Phase 3: Research & Question Generation (Interactive)
  → Industry research → generate questions → iterative dialogue → validated requirements

Phase 4: Execute & Produce Deliverables
  → Scan codebase → produce OUT-01~06 → DoD self-verify → log all findings to memory

Phase 5: Completion & Handoff
  → Trigger supervisor → remediate if needed → notify PM → trigger downstream tasks
```

Include detailed sub-steps for each phase, specifying:
- Inputs required
- Actions to perform
- Memory operations (what to read/write at each step)
- Outputs produced
- Success criteria for proceeding to next phase

### 8. Create references/dod.md (Requirement 9)

Research and produce DoD quality gates. Each item must be checkable (pass/fail):

Include at minimum:
- OUT-01 through OUT-06 are all produced and non-empty
- All templates are fully populated (no remaining placeholder fields like `{project_name}`)
- Module relationship diagram renders valid Mermaid syntax
- At least one architecture pattern is identified with evidence
- All identified modules have responsibility descriptions
- Dependency map covers both internal and third-party dependencies
- Circular dependencies (if any) are flagged
- Conversation log contains at least Phase 1-3 dialogue
- Work log contains timestamped entries for all phases
- All findings are recorded in SQLite memory database
- Scan history is recorded in SQLite
- RACI matrix is ready for PM Agent handoff

### 9. Create references/dor.md (Requirement 10)

Research and produce DoR prerequisites:

Include at minimum:
- **Project Intake completed**: User has confirmed the Project Intake Summary (local path, project name, scan scope, purpose)
- **Project local path is valid**: Path exists, is a directory, and contains files (`ls {path}` succeeds)
- **Git repository verified** (if applicable): `git -C {path} status` succeeds, correct branch checked out
- Target codebase is accessible (local clone or remote access configured)
- Project root path is specified and validated
- At least one build/manifest file exists (pom.xml, package.json, build.gradle, requirements.txt, go.mod, Cargo.toml, etc.)
- Read permissions are available for all project files
- Scan scope is defined (full project or specific modules)
- Directories to exclude are specified (if scan scope is partial/exclude)
- Purpose of scan is communicated (why this scan is needed)
- Memory database directory is writable
- Output directory is writable

### 10. Create references/output-templates.md

A reference file that indexes all output templates:

| Output ID | Name | Template Path | Description |
|-----------|------|--------------|-------------|
| OUT-01 | Project Structure Tree | templates/structure-tree-template.md | ... |
| OUT-02 | Module Relationship Diagram | templates/module-relationship-template.md | ... |
| ... | ... | ... | ... |

## Validation Checklist

After completing all files, verify:
- [ ] 6 template files exist in `templates/` (OUT-01 through OUT-06)
- [ ] Each template contains a complete structure with placeholder fields
- [ ] Each template contains tables, sections, and Mermaid diagram blocks where applicable
- [ ] `references/sop.md` exists with 5 phases and detailed sub-steps
- [ ] `references/dod.md` exists with at least 12 checkable items
- [ ] `references/dor.md` exists with at least 8 prerequisites
- [ ] `references/output-templates.md` exists with index of all 6 templates

If any item fails, fix it before reporting completion.
