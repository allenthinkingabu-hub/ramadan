# Tools & MCP Tools -- sa-cost-estimation-support

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research cloud pricing, licensing models, vendor pricing pages |
| TL-002 | Web Fetch | Retrieve detailed pricing calculators, vendor documentation, rate cards |
| TL-003 | File Read/Write | Read project files, write cost breakdowns, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing cost artifacts, infrastructure configs, dependency manifests |
| TL-006 | Task (Sub-agent) | Delegate parallel research or cost analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for cloud services, pricing APIs |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, infrastructure-as-code files, existing cost models |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific pricing databases, internal rate cards |

## Tool Usage Guidelines

- Use **Web Search** and **Web Fetch** for cloud pricing research and vendor rate cards in Step 3
- Use **Context7** for up-to-date cloud service documentation and pricing changes
- Use **Glob/Grep** to find existing IaC files (Terraform, CloudFormation) for infrastructure sizing
- Use **Task sub-agents** to parallelize independent cost category estimations
- Save all research results locally per requirement #17
