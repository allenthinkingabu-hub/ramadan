# MCP Tools — Transformation Target Current State Analysis (SA-TRF-001)

> Configurable MCP tools list for the Transformation Target Current State Analysis AI Agent.
> Edit this file to add or remove MCP tools as integrations evolve.

---

## MCP Tool Definitions

| # | Tool Name | MCP Server | Primary Use | When to Use |
|---|-----------|-----------|-------------|-------------|
| 1 | **context7** | `plugin:context7:context7` | Look up authoritative documentation for frameworks, libraries, and APIs used by the transformation target | When the target uses a framework whose conventions, lifecycle, or extension patterns are needed to correctly interpret the code (e.g., Spring Boot lifecycle hooks, React hooks rules, Django ORM behavior) |
| 2 | **IDE Diagnostics** (`getDiagnostics`) | `mcp__ide` | Retrieve language server type errors, unresolved references, and symbol diagnostics for the target files | When type information is needed to understand a method's actual return type, parameter types, or when identifying broken references that indicate coupling issues |
| 3 | **IDE Code Execution** (`executeCode`) | `mcp__ide` | Execute code snippets in the current kernel for Jupyter-based Python projects; verify behavior of a code path | When the target is a Python data processing component and behavior verification requires execution |

---

## MCP Tool Usage Guidelines

### context7

Use `resolve-library-id` first, then `query-docs`:

```
1. mcp__plugin_context7_context7__resolve-library-id
   → libraryName: "{framework_name}"
   → query: "{what you need to understand about the framework}"

2. mcp__plugin_context7_context7__query-docs
   → libraryId: "{resolved_id}"
   → query: "{specific pattern or behavior to understand}"
```

**When most valuable**: Understanding framework lifecycle (Spring Bean lifecycle, React component lifecycle), identifying which methods are framework-managed vs. user-defined, understanding annotation semantics (e.g., `@Transactional` scope, `@Cacheable` behavior).

### IDE Diagnostics

```
mcp__ide__getDiagnostics
→ uri: "file://{absolute_path_to_target_file}"
```

**When most valuable**: Identifying unresolved imports (indicates missing dependencies), type mismatch errors (indicates interface contract violations), deprecated API warnings (indicates technical debt).

### IDE Execute Code

```
mcp__ide__executeCode
→ code: "{python code to verify target behavior}"
```

**When most valuable**: Verifying edge case behavior of pure functions or data transformation logic without modifying any files.
