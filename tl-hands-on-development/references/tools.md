# Tools & MCP Tools -- tl-hands-on-development

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research implementation patterns, framework documentation, best practices |
| TL-002 | Web Fetch | Retrieve detailed API docs, library documentation, code examples |
| TL-003 | File Read/Write | Read/write source code, documentation, configuration files |
| TL-004 | Bash / Shell | Execute build tools, run tests, compile code, manage dependencies |
| TL-005 | Glob / Grep | Search codebase for existing patterns, dependencies, usage |
| TL-006 | Task (Sub-agent) | Delegate parallel implementation or research tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and libraries |
| MCP-002 | GitHub (via gh CLI) | Manage branches, PRs, code review, repository operations |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal libraries |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for framework/library research in Step 3
- Use **Bash** to run builds, tests, and validate implementations
- Use **File Read/Write** for all code creation and modification
- Use **Glob/Grep** to understand existing codebase patterns before implementing
- Use **GitHub CLI** for branch management and PR creation
- Use **Task sub-agents** to parallelize independent implementation tasks
