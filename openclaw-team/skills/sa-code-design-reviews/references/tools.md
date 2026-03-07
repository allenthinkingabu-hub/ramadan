# Tools & MCP Tools — sa-code-design-reviews

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research code review best practices, architectural compliance patterns |
| TL-002 | Web Fetch | Retrieve detailed review guidelines, coding standards documentation |
| TL-003 | File Read/Write | Read code files under review, write review findings and configs |
| TL-004 | Bash / Shell | Run static analysis tools, inspect codebase structure |
| TL-005 | Glob / Grep | Search codebase for patterns, anti-patterns, architectural violations |
| TL-006 | Task (Sub-agent) | Delegate parallel review of independent components |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and libraries |
| MCP-002 | GitHub (via gh CLI) | Inspect PRs, review comments, repository structure, CI/CD results |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific linting rules, internal standards |

## Tool Usage Guidelines

- Use **Glob/Grep** extensively for scanning code for pattern violations and architectural drift
- Use **File Read** to analyze specific files flagged for review
- Use **GitHub MCP** to inspect PR diffs, comments, and CI pipeline results
- Use **Web Search** and **Context7** for researching compliance criteria
- Use **Task sub-agents** to parallelize review of independent components
- Save all review findings locally per logging requirements
