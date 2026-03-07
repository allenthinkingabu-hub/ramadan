# Tools & MCP Tools — tl-technical-vision-direction

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research technology trends, industry best practices, vision frameworks |
| TL-002 | Web Fetch | Retrieve detailed technology documentation, strategy guides |
| TL-003 | File Read/Write | Read project files, write vision documents, output configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing technical documentation, standards |
| TL-006 | Task (Sub-agent) | Delegate parallel research or document generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and platforms |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing technical docs, architecture decisions |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal technology standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology trend research in Step 3
- Use **File Write** to produce vision documents and configuration files
- Use **Glob/Grep** to find existing technical documentation in the codebase
- Use **Task sub-agents** to parallelize independent research tasks
- Save all research results locally per logging requirements
