# Tools & MCP Tools — sa-architecture-design

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research architecture patterns, technology documentation, best practices |
| TL-002 | Web Fetch | Retrieve detailed architecture guides, cloud service documentation |
| TL-003 | File Read/Write | Read project files, write diagrams, output documents and configs |
| TL-004 | Bash / Shell | Execute diagram generation scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing architecture artifacts, patterns |
| TL-006 | Task (Sub-agent) | Delegate parallel research or diagram generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and cloud services |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing architecture docs, PRs |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal architecture standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for architecture pattern research in Step 3
- Use **File Write** to produce Mermaid/PlantUML diagram source files
- Use **Glob/Grep** to find existing architecture artifacts in the codebase
- Use **Task sub-agents** to parallelize independent diagram creation
- Save all research results locally per requirement #17
