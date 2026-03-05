# Tools & MCP Tools -- sa-stakeholder-alignment

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research stakeholder alignment frameworks, workshop facilitation techniques |
| TL-002 | Web Fetch | Retrieve detailed governance guides, decision framework documentation |
| TL-003 | File Read/Write | Read project files, write alignment records, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing governance artifacts, stakeholder records |
| TL-006 | Task (Sub-agent) | Delegate parallel research or stakeholder analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for governance frameworks, compliance standards |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing decision records, architecture governance docs |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific stakeholder databases, org charts |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for stakeholder alignment framework research in Step 3
- Use **File Write** to produce Mermaid stakeholder influence diagrams
- Use **Glob/Grep** to find existing governance artifacts and decision records in the codebase
- Use **Task sub-agents** to parallelize independent stakeholder group analysis
- Save all research results locally per requirement #17
