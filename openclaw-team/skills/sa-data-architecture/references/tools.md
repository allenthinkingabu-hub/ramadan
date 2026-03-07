# Tools & MCP Tools -- sa-data-architecture

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research data architecture patterns, database documentation, best practices |
| TL-002 | Web Fetch | Retrieve detailed data modelling guides, storage technology documentation |
| TL-003 | File Read/Write | Read project files, write diagrams, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing data models, schema definitions, migration scripts |
| TL-006 | Task (Sub-agent) | Delegate parallel research or diagram generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for databases, data platforms, ETL frameworks |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing data models, schema definitions |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific data catalogs, internal data standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for data architecture pattern research in Step 3
- Use **File Write** to produce Mermaid/PlantUML ER diagram source files
- Use **Glob/Grep** to find existing data models and schema artifacts in the codebase
- Use **Task sub-agents** to parallelize independent diagram creation
- Save all research results locally per requirement #17
