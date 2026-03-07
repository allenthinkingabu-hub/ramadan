# Tools & MCP Tools — sa-technical-guidance

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research design patterns, framework documentation, best practices |
| TL-002 | Web Fetch | Retrieve detailed pattern guides, technology documentation |
| TL-003 | File Read/Write | Read project files, write guidance documents, output configs |
| TL-004 | Bash / Shell | Inspect codebase structure, run verification scripts |
| TL-005 | Glob / Grep | Search codebase for existing patterns, architecture artifacts |
| TL-006 | Task (Sub-agent) | Delegate parallel research or pattern analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and libraries |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing code patterns, PRs |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal coding standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for design pattern research in Step 3
- Use **File Read** to analyze existing codebase patterns and architecture artifacts
- Use **Glob/Grep** to find existing patterns and anti-patterns in the codebase
- Use **Task sub-agents** to parallelize independent pattern analysis
- Save all research results locally per logging requirements
