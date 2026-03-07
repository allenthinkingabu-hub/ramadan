# Tools & MCP Tools — sa-non-functional-requirements

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research NFR benchmarks, industry standards, compliance requirements |
| TL-002 | Web Fetch | Retrieve detailed NFR guides, SLA templates, security standards documentation |
| TL-003 | File Read/Write | Read project files, write NFR specifications, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing NFR artifacts, SLA definitions, config patterns |
| TL-006 | Task (Sub-agent) | Delegate parallel research or specification generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and cloud services |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing NFR docs, PRs |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal NFR standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for NFR benchmark research in Step 3
- Use **File Write** to produce NFR specification documents and YAML configs
- Use **Glob/Grep** to find existing NFR artifacts in the codebase
- Use **Task sub-agents** to parallelize independent NFR category research
- Save all research results locally per requirement #17
