# MCP Tools — Project Structure Scan Agent

## Available MCP Tools

| # | MCP Tool | Tool ID | Purpose | When to Use |
|---|----------|---------|---------|-------------|
| 1 | **IDE Diagnostics** | `mcp__ide__getDiagnostics` | Get language diagnostics (errors, warnings, hints) from the IDE | During Phase 4 to assess code quality signals per module, identify compilation issues, and detect potential structural problems |
| 2 | **Context7 Resolve Library** | `mcp__plugin_context7_context7__resolve-library-id` | Look up a library/package name and get the Context7-compatible library ID | During Phase 3 (Research) when identifying framework conventions — resolve library names to get documentation |
| 3 | **Context7 Query Docs** | `mcp__plugin_context7_context7__query-docs` | Query up-to-date documentation for a specific library/framework | During Phase 3 to research framework-specific project structure conventions (e.g., "Spring Boot recommended project layout", "Next.js app directory structure") |

## Usage Patterns

### Research Phase (Phase 3)
1. Identify framework from build files (e.g., `spring-boot-starter-web` in pom.xml)
2. Call `resolve-library-id` with the framework name → get library ID
3. Call `query-docs` with the library ID and question about project structure conventions
4. Use documentation to inform question generation and pattern analysis

### Execution Phase (Phase 4)
1. Call `getDiagnostics` on key source files to identify code quality issues
2. Use diagnostics to enrich the Module Responsibility Summary (OUT-05)
3. Flag modules with high diagnostic counts as potential risk areas

### Example Workflow
```
[Phase 3: Research Spring Boot conventions]
→ resolve-library-id("spring boot", "project structure conventions")
→ Returns: /spring-projects/spring-boot
→ query-docs("/spring-projects/spring-boot", "recommended project structure and package layout")
→ Agent learns: Spring Boot recommends package-by-feature with @Component scanning
→ Agent incorporates into Phase 4 analysis
```
