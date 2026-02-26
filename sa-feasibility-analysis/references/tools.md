# Tools & MCP Tools — SA-feasibility-analysis

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research industry practices, technology costs, vendor comparisons |
| TL-002 | Web Fetch | Retrieve pricing pages, documentation, technical specifications |
| TL-003 | File Read/Write | Read project files, write output documents and configuration files |
| TL-004 | Bash / Shell | Execute scripts, inspect directory structures, run validation |
| TL-005 | Glob / Grep | Search codebase for patterns, dependencies, configurations |
| TL-006 | Task (Sub-agent) | Delegate parallel research or analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for technologies under evaluation |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, PRs, issues for project context |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, databases, or internal systems |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology capability research in Step 3
- Use **Web Fetch** for vendor pricing and technical specifications
- Use **Glob/Grep** to inspect existing codebase when assessing technical feasibility
- Use **File Write** for all output deliverables
- Use **Task sub-agents** to parallelize independent research queries
- Save all research results locally per requirement #17
