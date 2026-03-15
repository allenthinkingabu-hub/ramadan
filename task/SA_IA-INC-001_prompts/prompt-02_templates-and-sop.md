# Prompt 02 — Output Templates, SOP, DoD, and DoR

## Context

You are continuing the creation of the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 2 of 5. Step 1 has already created the directory structure, SKILL.md skeleton, and all config files.

## Scope — Requirements 7 through 10

This prompt covers ONLY the following:
- Requirement 7: Output deliverable templates (OUT-01 through OUT-07)
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

## Module Dependency Diagram (draw.io)

<!-- The Agent must produce a .drawio file saved to diagrams/module-relationship.drawio
     Open with: draw.io desktop app, app.diagrams.net, or VS Code draw.io extension.
     Replace every {placeholder} with actual module names and layer names. -->

> **Diagram file**: `diagrams/module-relationship.drawio` — open with draw.io

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{timestamp}" agent="SA-DISC-001" version="21.0.0">
  <diagram id="module-relationship" name="Module Relationship — {project_name}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ══ SWIMLANE: {Layer Name, e.g., Presentation Layer} — fillColor varies per layer ══ -->
        <mxCell id="swim_1" value="{Layer Name}"
          style="swimlane;startSize=30;horizontal=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1080" height="130" as="geometry" />
        </mxCell>

        <!-- Module node — repeat for each module in this layer -->
        <mxCell id="mod_1" value="&lt;b&gt;{ModuleName}&lt;/b&gt;&lt;br/&gt;&lt;i&gt;{one-line responsibility}&lt;/i&gt;"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;arcSize=10;"
          vertex="1" parent="swim_1">
          <mxGeometry x="60" y="45" width="200" height="60" as="geometry" />
        </mxCell>

        <!-- ══ SWIMLANE: {Layer Name, e.g., Business Logic Layer} ══ -->
        <mxCell id="swim_2" value="{Layer Name}"
          style="swimlane;startSize=30;horizontal=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="40" y="190" width="1080" height="130" as="geometry" />
        </mxCell>

        <mxCell id="mod_2" value="&lt;b&gt;{ModuleName}&lt;/b&gt;&lt;br/&gt;&lt;i&gt;{one-line responsibility}&lt;/i&gt;"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;arcSize=10;"
          vertex="1" parent="swim_2">
          <mxGeometry x="60" y="45" width="200" height="60" as="geometry" />
        </mxCell>

        <!-- ══ SWIMLANE: {Layer Name, e.g., Data Access Layer} ══ -->
        <mxCell id="swim_3" value="{Layer Name}"
          style="swimlane;startSize=30;horizontal=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontStyle=1;fontSize=13;"
          vertex="1" parent="1">
          <mxGeometry x="40" y="340" width="1080" height="130" as="geometry" />
        </mxCell>

        <mxCell id="mod_3" value="&lt;b&gt;{ModuleName}&lt;/b&gt;&lt;br/&gt;&lt;i&gt;{one-line responsibility}&lt;/i&gt;"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;arcSize=10;"
          vertex="1" parent="swim_3">
          <mxGeometry x="60" y="45" width="200" height="60" as="geometry" />
        </mxCell>

        <!-- ══ DEPENDENCY ARROWS — add one mxCell per dependency edge ══ -->
        <!-- Arrow style: solid = compile-time dependency; dashed = runtime / event -->
        <mxCell id="edge_1" value="{dependency label, e.g., calls / uses / depends-on}"
          style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;
                 exitX=0.5;exitY=1;exitDx=0;exitDy=-1;entryX=0.5;entryY=0;entryDx=0;entryDy=-1;
                 endArrow=block;endFill=1;"
          edge="1" source="mod_1" target="mod_2" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="edge_2" value="{dependency label}"
          style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;
                 endArrow=block;endFill=1;"
          edge="1" source="mod_2" target="mod_3" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

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

## Dependency Diagram (draw.io)

<!-- The Agent must produce a .drawio file saved to diagrams/dependency-map.drawio
     Open with: draw.io desktop app, app.diagrams.net, or VS Code draw.io extension.
     Solid arrows = compile-time dependency. Dashed arrows = runtime / optional dependency. -->

> **Diagram file**: `diagrams/dependency-map.drawio` — open with draw.io

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{timestamp}" agent="SA-DISC-001" version="21.0.0">
  <diagram id="dependency-map" name="Package Dependency Map — {project_name}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ══ GROUP: Internal Modules ══ -->
        <mxCell id="grp_internal" value="Internal Modules"
          style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="480" height="320" as="geometry" />
        </mxCell>

        <!-- Internal module node — repeat per module -->
        <mxCell id="mod_a" value="&lt;b&gt;{module-name}&lt;/b&gt;"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
          vertex="1" parent="grp_internal">
          <mxGeometry x="40" y="60" width="180" height="50" as="geometry" />
        </mxCell>

        <mxCell id="mod_b" value="&lt;b&gt;{module-name}&lt;/b&gt;"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
          vertex="1" parent="grp_internal">
          <mxGeometry x="260" y="60" width="180" height="50" as="geometry" />
        </mxCell>

        <!-- ══ GROUP: Third-Party Dependencies ══ -->
        <mxCell id="grp_external" value="Third-Party Dependencies"
          style="swimlane;startSize=30;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="560" y="40" width="540" height="320" as="geometry" />
        </mxCell>

        <!-- Third-party dependency node — repeat per library/framework -->
        <mxCell id="dep_x" value="&lt;b&gt;{library-name}&lt;/b&gt;&lt;br/&gt;{version} | {category}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;"
          vertex="1" parent="grp_external">
          <mxGeometry x="40" y="60" width="200" height="55" as="geometry" />
        </mxCell>

        <mxCell id="dep_y" value="&lt;b&gt;{library-name}&lt;/b&gt;&lt;br/&gt;{version} | {category}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;"
          vertex="1" parent="grp_external">
          <mxGeometry x="280" y="60" width="200" height="55" as="geometry" />
        </mxCell>

        <!-- ══ INTERNAL DEPENDENCY EDGES (solid arrow) ══ -->
        <mxCell id="int_edge_1" value="{usage}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;"
          edge="1" source="mod_a" target="mod_b" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ══ EXTERNAL DEPENDENCY EDGES (dashed arrow) ══ -->
        <mxCell id="ext_edge_1" value="{usage}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=0;dashed=1;"
          edge="1" source="mod_a" target="dep_x" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

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

### 7. Create templates/transformation-target-template.md (OUT-07)

Template for the Transformation Target Current State Report deliverable (produced ONLY when scan purpose involves transformation/refactoring):

```markdown
# Transformation Target Current State Report — {project_name}

- **Report Date**: {date}
- **Task ID**: SA-DISC-001
- **Agent Session**: {session_id}
- **Transformation Target**: {target_module_or_component}
- **Target Path**: {target_path}
- **Scan Purpose**: {transformation_purpose}

> **Note**: This report (OUT-07) is produced only when the scan purpose involves any form of change,
> refactoring, feature addition, or system evolution targeting a specific component.

## 1. Transformation Target Overview

- **Target Scope**: {exact module(s), component(s), file(s), or functional area(s)}
- **Confirmed By User**: {yes/no — user confirmed scope in Step 5}
- **Primary Responsibility**: {what the target does today}
- **Technology**: {language, framework, key libraries used within target}

## 2. Current Code Structure

<!-- File and directory layout within the transformation target scope -->

{target_root}/
├── {file_or_dir}/        ← {purpose}
│   ├── {sub_item}/       ← {purpose}
│   └── ...
...

### Key Files

| File | LOC (est.) | Purpose |
|------|-----------|---------|
| {file} | {loc} | {purpose} |
| ... | ... | ... |

## 3. Core Logic Description

<!-- How the transformation target's key logic works — narrate the main processing flow,
     decision branches, and non-obvious design intentions. -->

### 3.1 Overall Processing Flow

{2-5 sentence narrative describing what happens from trigger/entry to completion.
Example: "When a payment request arrives, the PaymentService first validates the order status,
then selects the appropriate payment gateway based on channel configuration, delegates
authorization to the gateway adapter, and finally persists the transaction record
and publishes a PaymentCompleted event."}

### 3.2 Key Logic Modules

| Module / Class / Function | Location | Core Logic Description |
|--------------------------|----------|----------------------|
| {class or function name} | {file:line} | {what it computes, decides, or transforms — not just what it is called} |
| ... | ... | ... |

### 3.3 Critical Decision Points & Branching Logic

<!-- Where does the code make important decisions? What are the conditions and outcomes? -->

| Decision Point | Location | Condition | Branch A | Branch B |
|---------------|----------|-----------|----------|----------|
| {e.g., "Gateway selection"} | {file:method:line} | {e.g., "channel == 'alipay'"} | {e.g., "use AlipayAdapter"} | {e.g., "use WechatPayAdapter"} |
| ... | ... | ... | ... | ... |

### 3.4 Error Handling & Edge Cases

| Scenario | Handling Strategy | Location |
|---------|------------------|----------|
| {e.g., "Payment gateway timeout"} | {e.g., "Retry 3× then throw PaymentException"} | {file:method} |
| ... | ... | ... |

## 4. Key Data Structures

<!-- The important models, entities, DTOs, and state objects that the transformation target
     owns, produces, or depends on. -->

### 4.1 Core Domain Models / Entities

For each key model, show its fields and describe its role:

```
{ModelName}
├── {field: type}       — {purpose of this field}
├── {field: type}       — {purpose of this field}
└── {field: type}       — {purpose of this field}
```

| Model / Entity | Owned By | Key Fields | Lifecycle | Notes |
|---------------|---------|------------|----------|-------|
| {class/struct name} | {which layer/module} | {field1, field2, field3} | {created by / consumed by / persisted where} | {notes} |
| ... | ... | ... | ... | ... |

### 4.2 DTOs / Transfer Objects

| DTO | Direction | Fields | Used Between |
|-----|----------|--------|-------------|
| {class name} | {inbound/outbound} | {key fields} | {which two layers/components} |
| ... | ... | ... | ... |

### 4.3 State / Enumerations

| Type | Values | Transitions | Notes |
|------|--------|------------|-------|
| {enum/state name} | {value1, value2, value3} | {valid transitions} | {business meaning} |
| ... | ... | ... | ... |

### 4.4 Persistence Schema (if applicable)

| Table / Collection | Key Columns / Fields | Indexes | Notes |
|-------------------|---------------------|---------|-------|
| {table name} | {col1 (PK), col2, col3} | {indexed columns} | {owned by target or shared?} |
| ... | ... | ... | ... |

## 5. Sequence Diagrams

<!-- The Agent must produce one .drawio file per significant flow, saved to diagrams/.
     Naming convention: diagrams/seq-{use-case-kebab-case}.drawio
     Open with: draw.io desktop app, app.diagrams.net, or VS Code draw.io extension.
     Participants = header boxes. Lifelines = vertical dashed lines.
     Solid arrow = synchronous call. Dashed arrow = return message.
     Alt/opt/loop frames = mxgraph.uml.frame shapes. -->

### 5.1 Main Flow — {primary use case name}

> **Diagram file**: `diagrams/seq-{use-case-name}-main.drawio` — open with draw.io

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{timestamp}" agent="SA-DISC-001" version="21.0.0">
  <diagram id="seq-main" name="{use_case_name} — Main Flow">
    <mxGraphModel dx="1422" dy="762" grid="0" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ══ PARTICIPANT HEADER BOXES ══
             Space participants ~200px apart horizontally (center x = 100, 300, 500, 700 ...) -->

        <!-- Actor / external caller -->
        <mxCell id="p_caller" value="{Caller, e.g., API Client}"
          style="shape=mxgraph.uml.actor2;html=1;whiteSpace=wrap;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;"
          vertex="1" parent="1">
          <mxGeometry x="60" y="20" width="60" height="80" as="geometry" />
        </mxCell>
        <!-- Lifeline: vertical dashed line extending downward -->
        <mxCell id="ll_caller" value=""
          style="endArrow=none;dashed=1;strokeColor=#666666;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="90" y="100" as="sourcePoint" />
            <mxPoint x="90" y="720" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Component A (e.g., Controller) -->
        <mxCell id="p_a" value="{Component A, e.g., Controller}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="220" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_a" value=""
          style="endArrow=none;dashed=1;strokeColor=#6c8ebf;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="300" y="70" as="sourcePoint" />
            <mxPoint x="300" y="720" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Component B — Transformation Target (highlighted) -->
        <mxCell id="p_b" value="{Component B (TARGET)}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;strokeWidth=2;"
          vertex="1" parent="1">
          <mxGeometry x="440" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_b" value=""
          style="endArrow=none;dashed=1;strokeColor=#d6b656;strokeWidth=2;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="520" y="70" as="sourcePoint" />
            <mxPoint x="520" y="720" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Component C (e.g., Repository / External) -->
        <mxCell id="p_c" value="{Component C, e.g., Repository}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="660" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_c" value=""
          style="endArrow=none;dashed=1;strokeColor=#82b366;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="740" y="70" as="sourcePoint" />
            <mxPoint x="740" y="720" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- ══ MESSAGES ══
             y position increases for each sequential message (start ~140, increment ~60).
             Solid arrow = synchronous call. Dashed arrow = return. -->

        <!-- Message 1: Caller → Component A -->
        <mxCell id="msg_1" value="1: {request / method call}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;fontStyle=1;"
          edge="1" source="p_caller" target="p_a" parent="1">
          <mxGeometry y="80" relative="1" as="geometry" />
        </mxCell>

        <!-- Message 2: Component A → Component B (TARGET) -->
        <mxCell id="msg_2" value="2: {method call with params}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
          edge="1" source="p_a" target="p_b" parent="1">
          <mxGeometry y="140" relative="1" as="geometry" />
        </mxCell>

        <!-- Message 3: Component B → Component C -->
        <mxCell id="msg_3" value="3: {data query / write}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
          edge="1" source="p_b" target="p_c" parent="1">
          <mxGeometry y="200" relative="1" as="geometry" />
        </mxCell>

        <!-- Return 3: Component C → Component B (dashed) -->
        <mxCell id="ret_3" value="4: {result}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_c" target="p_b" parent="1">
          <mxGeometry y="260" relative="1" as="geometry" />
        </mxCell>

        <!-- Return 2: Component B → Component A (dashed) -->
        <mxCell id="ret_2" value="5: {return value}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_b" target="p_a" parent="1">
          <mxGeometry y="320" relative="1" as="geometry" />
        </mxCell>

        <!-- Return 1: Component A → Caller (dashed) -->
        <mxCell id="ret_1" value="6: {HTTP response / callback}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_a" target="p_caller" parent="1">
          <mxGeometry y="380" relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### 5.2 Error / Alternative Flow — {scenario name}

> **Diagram file**: `diagrams/seq-{use-case-name}-error.drawio` — open with draw.io

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="{timestamp}" agent="SA-DISC-001" version="21.0.0">
  <diagram id="seq-error" name="{use_case_name} — Error Flow">
    <mxGraphModel dx="1422" dy="762" grid="0" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Participants — same structure as main flow, add only participants used in this flow -->
        <mxCell id="p_a" value="{Component A}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="100" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_a" value="" style="endArrow=none;dashed=1;strokeColor=#6c8ebf;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="180" y="70" as="sourcePoint" />
            <mxPoint x="180" y="620" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <mxCell id="p_b" value="{Component B (TARGET)}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;strokeWidth=2;"
          vertex="1" parent="1">
          <mxGeometry x="360" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_b" value="" style="endArrow=none;dashed=1;strokeColor=#d6b656;strokeWidth=2;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="440" y="70" as="sourcePoint" />
            <mxPoint x="440" y="620" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <mxCell id="p_ext" value="{External System / Gateway}"
          style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;"
          vertex="1" parent="1">
          <mxGeometry x="620" y="20" width="160" height="50" as="geometry" />
        </mxCell>
        <mxCell id="ll_ext" value="" style="endArrow=none;dashed=1;strokeColor=#b85450;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="700" y="70" as="sourcePoint" />
            <mxPoint x="700" y="620" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Messages -->
        <mxCell id="msg_1" value="1: {request}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
          edge="1" source="p_a" target="p_b" parent="1">
          <mxGeometry y="80" relative="1" as="geometry" />
        </mxCell>

        <mxCell id="msg_2" value="2: {external call}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
          edge="1" source="p_b" target="p_ext" parent="1">
          <mxGeometry y="140" relative="1" as="geometry" />
        </mxCell>

        <!-- Error response from external -->
        <mxCell id="err_resp" value="3: {error / timeout}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;strokeColor=#b85450;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_ext" target="p_b" parent="1">
          <mxGeometry y="200" relative="1" as="geometry" />
        </mxCell>

        <!-- ALT frame: shows retry-succeeds / max-retries-exceeded branches -->
        <mxCell id="alt_frame" value="alt: retry succeeds / max retries exceeded"
          style="shape=mxgraph.uml.frame;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;opacity=50;"
          vertex="1" parent="1">
          <mxGeometry x="280" y="240" width="520" height="200" as="geometry" />
        </mxCell>

        <!-- Branch label: retry succeeds -->
        <mxCell id="alt_label_a" value="[retry succeeds]"
          style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontStyle=2;"
          vertex="1" parent="1">
          <mxGeometry x="290" y="255" width="130" height="20" as="geometry" />
        </mxCell>

        <mxCell id="ret_success" value="4a: {success response}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_b" target="p_a" parent="1">
          <mxGeometry y="280" relative="1" as="geometry" />
        </mxCell>

        <!-- Branch separator line -->
        <mxCell id="alt_sep" value=""
          style="endArrow=none;strokeColor=#d6b656;dashed=1;"
          edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="285" y="350" as="sourcePoint" />
            <mxPoint x="795" y="350" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Branch label: max retries exceeded -->
        <mxCell id="alt_label_b" value="[max retries exceeded]"
          style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontStyle=2;"
          vertex="1" parent="1">
          <mxGeometry x="290" y="355" width="160" height="20" as="geometry" />
        </mxCell>

        <mxCell id="ret_error" value="4b: {error / exception}"
          style="edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;strokeColor=#b85450;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
          edge="1" source="p_b" target="p_a" parent="1">
          <mxGeometry y="380" relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

> Add additional `.drawio` sequence diagram files for other significant flows (async events, batch jobs, scheduled tasks). Name them `diagrams/seq-{flow-name}.drawio`.

## 6. Current Responsibilities & Behaviors

<!-- What the target does today: functions, endpoints, events handled, data processed -->

| Responsibility | Implementation Location | Notes |
|---------------|------------------------|-------|
| {what it does} | {file:function/class} | {notes} |
| ... | ... | ... |

## 7. Dependency Analysis

### 7.1 Inbound Dependencies (What depends on the target)

| Dependent Module/Component | Dependency Type | Entry Point |
|---------------------------|----------------|-------------|
| {module} | {compile/runtime/config/event} | {how it calls into target} |
| ... | ... | ... |

### 7.2 Outbound Dependencies (What the target depends on)

| Dependency | Type | Purpose | Can Replace? |
|-----------|------|---------|-------------|
| {module or lib} | {internal/third-party} | {why needed} | {yes/no/partial} |
| ... | ... | ... | ... |

## 8. Data Flows & Interfaces

### 8.1 APIs / Public Interfaces

| Interface | Type | Consumers | Contract |
|-----------|------|----------|---------|
| {function/endpoint/event} | {REST/gRPC/message/function call} | {who calls it} | {expected input/output contract} |
| ... | ... | ... | ... |

### 8.2 Shared State & Data Stores

| Data Store | Access Pattern | Shared With |
|-----------|----------------|-------------|
| {DB/cache/file/queue} | {read/write/read-write} | {other modules sharing this} |
| ... | ... | ... |

## 9. Test Coverage

| Test Type | Location | Coverage Level | Notes |
|-----------|----------|---------------|-------|
| Unit Tests | {path} | {high/medium/low/none} | {notes} |
| Integration Tests | {path} | {high/medium/low/none} | {notes} |
| E2E Tests | {path} | {high/medium/low/none} | {notes} |

**Overall Coverage Assessment**: {high/medium/low/none} — {reason}

## 10. Known Technical Debt & Anti-Patterns

| Issue | Location | Severity | Description |
|-------|----------|----------|-------------|
| {code smell / anti-pattern} | {file:line} | {high/medium/low} | {description} |
| ... | ... | ... | ... |

## 11. Configuration & Environment Dependencies

| Config Item | Source | Consumed By | Notes |
|------------|--------|-------------|-------|
| {env var / config key} | {env/.properties/vault/etc} | {which part of target} | {notes} |
| ... | ... | ... | ... |

## 12. Transformation Constraints

### 12.1 Hard Constraints (Cannot Change)

| Constraint | Reason | Impacted Area |
|-----------|--------|---------------|
| {public API / DB schema / SLA / contract} | {why immutable} | {what is affected} |
| ... | ... | ... |

### 12.2 Soft Constraints (Should Preserve If Possible)

| Constraint | Reason | Risk If Changed |
|-----------|--------|-----------------|
| {behavior / interface / convention} | {why preferred to keep} | {risk if violated} |
| ... | ... | ... |

### 12.3 Risk Areas

| Risk Area | Risk Type | Severity | Description |
|-----------|----------|----------|-------------|
| {high-coupling zone / untested code / shared state} | {coupling/fragility/blast-radius} | {high/medium/low} | {description} |
| ... | ... | ... | ... |

## 13. Transformation Readiness Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| Test Coverage | {1-5} | {why} |
| Coupling Level | {1-5 — 5 = highly coupled = harder} | {why} |
| Interface Clarity | {1-5} | {why} |
| Documentation Quality | {1-5} | {why} |
| Technical Debt Level | {1-5 — 5 = high debt = harder} | {why} |

**Overall Transformation Difficulty**: {low/medium/high/very-high}

## Approval

| Role | Name | Date | Status |
|------|------|------|--------|
| IT Architect (SA) | {name} | {date} | {Draft/Reviewed/Approved} |
| Technical Lead | {name} | {date} | {status} |
```

### 8. Create references/sop.md (Requirement 8)

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

Phase 5: Transformation Target Deep-Dive Investigation (Conditional)
  → Triggered when scan purpose involves transformation/refactoring → confirm target scope with user → investigate current state (structure, deps, interfaces, tests, debt, config) → identify constraints and risks → produce OUT-07 → save to memory (phase5) → user confirms Current State Report

Phase 6: Completion & Handoff
  → Trigger supervisor → remediate if needed → notify PM → trigger downstream tasks
```

Include detailed sub-steps for each phase, specifying:
- Inputs required
- Actions to perform
- Memory operations (what to read/write at each step)
- Outputs produced
- Success criteria for proceeding to next phase

### 9. Create references/dod.md (Requirement 9)

Research and produce DoD quality gates. Each item must be checkable (pass/fail):

Include at minimum:
- OUT-01 through OUT-06 are all produced and non-empty
- OUT-07 is produced and non-empty (CONDITIONAL: only required when scan purpose involves transformation/refactoring)
- All templates are fully populated (no remaining placeholder fields like `{project_name}`)
- Module relationship diagram draw.io file exists: `diagrams/module-relationship.drawio`, is valid XML, contains `<mxCell>` elements
- Dependency map draw.io file exists: `diagrams/dependency-map.drawio`, is valid XML, contains `<mxCell>` elements
- All `.drawio` files open without error (valid `<mxfile>` root element)
- At least one architecture pattern is identified with evidence
- All identified modules have responsibility descriptions
- Dependency map covers both internal and third-party dependencies
- Circular dependencies (if any) are flagged
- Transformation target sequence diagram draw.io file(s) exist in `diagrams/seq-*.drawio` (CONDITIONAL: only when OUT-07 is required)
- Transformation target scope confirmed by user (CONDITIONAL: only when OUT-07 is required)
- Conversation log contains at least Phase 1-3 dialogue
- Work log contains timestamped entries for all phases
- All findings are recorded in SQLite memory database
- Scan history is recorded in SQLite
- RACI matrix is ready for PM Agent handoff

### 10. Create references/dor.md (Requirement 10)

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

### 11. Create references/output-templates.md

A reference file that indexes all output templates:

| Output ID | Name | Template Path | When Produced | Description |
|-----------|------|--------------|---------------|-------------|
| OUT-01 | Project Structure Tree | templates/structure-tree-template.md | Always | ... |
| OUT-02 | Module Relationship Diagram | templates/module-relationship-template.md | Always | ... |
| OUT-03 | Layering Pattern Analysis | templates/layering-analysis-template.md | Always | ... |
| OUT-04 | Package Dependency Map | templates/dependency-map-template.md | Always | ... |
| OUT-05 | Module Responsibility Summary | templates/module-summary-template.md | Always | ... |
| OUT-06 | Project Structure Scan Report | templates/scan-report-template.md | Always | ... |
| OUT-07 | Transformation Target Current State Report | templates/transformation-target-template.md | Conditional (transformation scan only) | ... |

## Validation Checklist

After completing all files, verify:
- [ ] 7 template files exist in `templates/` (OUT-01 through OUT-07)
- [ ] Each template contains a complete structure with placeholder fields
- [ ] Each template contains tables, sections, and Mermaid diagram blocks where applicable
- [ ] `templates/transformation-target-template.md` (OUT-07) includes sections for: current code structure, **core logic description** (processing flow + decision points + error handling), **key data structures** (domain models + DTOs + state enums + persistence schema), **sequence diagrams** (Mermaid sequenceDiagram for main flow and error flow), responsibilities, inbound/outbound dependencies, data flows, test coverage, technical debt, configuration, hard/soft constraints, risk areas, and transformation readiness assessment
- [ ] `references/sop.md` exists with 6 phases (including Phase 5 Transformation Target Deep-Dive) and detailed sub-steps
- [ ] `references/dod.md` exists with at least 13 checkable items (including 2 conditional OUT-07 items)
- [ ] `references/dor.md` exists with at least 8 prerequisites
- [ ] `references/output-templates.md` exists with index of all 7 templates (OUT-01 through OUT-07)

If any item fails, fix it before reporting completion.
