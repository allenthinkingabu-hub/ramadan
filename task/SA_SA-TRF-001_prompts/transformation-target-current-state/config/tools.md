# Tools — Transformation Target Current State Analysis (SA-TRF-001)

> Configurable tools list for the Transformation Target Current State Analysis AI Agent.
> Edit this file to add or remove tools as the workflow evolves.

---

## Standard Tools

| # | Tool | Primary Use Cases | Example Invocations |
|---|------|------------------|---------------------|
| 1 | **Glob** | Locate all files within the target scope; find related components, test files, config files | `**/{target_name}*.{java,py,ts}` to find target files; `**/*test*/{target_name}*` for tests; `**/{pom.xml,package.json,build.gradle,requirements.txt,go.mod}` for manifests |
| 2 | **Grep** | Trace callers (inbound dependencies); find all usages of target's public API; locate TODO/FIXME/HACK markers; find environment variable references | `import.*{TargetClass}` to find importers; `{methodName}\s*\(` to find callers; `TODO\|FIXME\|HACK` for debt markers; `System.getenv\|os.environ\|process.env` for config deps |
| 3 | **Read** | Deep code reading — implementation files, test files, build manifests, config files | Read target's primary source file for core logic analysis; read test files for coverage assessment; read pom.xml/package.json for dependency inventory |
| 4 | **Bash** | Execute commands for coverage reports, dependency trees, build validation, LOC counting | `mvn test -pl {module} --also-make` for Java tests; `npm test -- --coverage` for JS coverage; `mvn dependency:tree -Dincludes={artifact}` for dep tree; `wc -l {file}` for LOC; `find {path} -name "*.java" \| xargs grep -l "{ClassName}"` for usage search |
| 5 | **Agent** | Dispatch parallel investigation sub-agents for independent analysis areas (e.g., simultaneous inbound + outbound dependency tracing on large codebases) | Use when target scope is large and multiple independent areas can be investigated concurrently |

---

## Tool Usage by Analysis Area

| Analysis Area | Primary Tool | Secondary Tool | What to Capture |
|---------------|-------------|---------------|-----------------|
| Code structure & file layout | Glob | Bash (tree) | Directory layout, file list with LOC, entry point identification |
| Core logic | Read | Grep | Main processing flow, decision branches, error handling strategies |
| Inbound dependencies (callers) | Grep | Read | All files that import/use/call the target's public types and methods |
| Outbound dependencies (callees) | Read | Glob | All imports and external calls inside the target scope |
| Public API surface | Grep | Read | All public/exported classes, methods, interfaces, REST endpoints |
| Shared state & data stores | Grep | Read | Database table access, cache key patterns, queue/topic access, shared singletons |
| Test coverage | Glob | Read | Test file discovery; read test classes to assess coverage quality |
| Technical debt | Grep | Read | TODO/FIXME/HACK markers, then read surrounding code for context |
| Configuration dependencies | Grep | Read | `getenv`, config key lookups, property file references, feature flag checks |
| Build & dependency manifest | Read | Bash | Parse pom.xml/package.json/requirements.txt for third-party and internal deps |
