# Tools & MCP Tools -- sa-data-privacy-governance

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research privacy regulations, governance frameworks, compliance best practices |
| TL-002 | Web Fetch | Retrieve detailed regulatory texts, GDPR articles, compliance guides |
| TL-003 | File Read/Write | Read project files, write governance documents, output configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing privacy policies, data handling code |
| TL-006 | Task (Sub-agent) | Delegate parallel research or governance section generation |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for privacy frameworks, IAM tools |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing privacy configurations, access control configs |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific compliance databases, internal governance standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for regulatory and governance research in Step 3
- Use **File Write** to produce governance documents and classification diagrams
- Use **Glob/Grep** to find existing privacy policies and access control configurations
- Use **Task sub-agents** to parallelize independent governance section research
- Save all research results locally per requirement #17
