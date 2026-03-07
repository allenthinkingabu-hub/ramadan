# Tools & MCP Tools — sa-technical-debt-management

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research debt management practices, refactoring patterns |
| TL-002 | Web Fetch | Retrieve detailed debt management guides, tool documentation |
| TL-003 | File Read/Write | Read codebase files, write debt reports and configs |
| TL-004 | Bash / Shell | Run static analysis tools, check dependency versions |
| TL-005 | Glob / Grep | Search codebase for debt indicators, anti-patterns, code smells |
| TL-006 | Task (Sub-agent) | Delegate parallel debt analysis for independent components |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and dependencies |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, issues tagged as tech debt, PR history |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific quality dashboards, SonarQube APIs |

## Tool Usage Guidelines

- Use **Glob/Grep** extensively for scanning codebase for code smells and debt indicators
- Use **Bash** to run static analysis tools and dependency checks
- Use **GitHub MCP** to inspect issue trackers for existing debt items
- Use **Web Search** and **Context7** for researching best practices
- Use **Task sub-agents** to parallelize analysis of independent components
- Save all analysis results locally per logging requirements
