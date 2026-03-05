# Tools & MCP Tools -- sa-dr-bcp-architecture

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research DR/BCP patterns, cloud DR services, chaos engineering practices |
| TL-002 | Web Fetch | Retrieve detailed DR documentation, cloud provider failover guides |
| TL-003 | File Read/Write | Read project files, write runbooks, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing DR configurations, backup scripts, health checks |
| TL-006 | Task (Sub-agent) | Delegate parallel research or diagram generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for cloud DR services, chaos tools |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing DR configs, runbooks, infrastructure code |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific DR playbooks, infrastructure inventory |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for DR/BCP pattern research in Step 3
- Use **File Write** to produce failover topology diagrams and runbook documents
- Use **Glob/Grep** to find existing DR configurations and backup scripts
- Use **Task sub-agents** to parallelize independent DR section research
- Save all research results locally per requirement #17
