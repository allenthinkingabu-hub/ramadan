# Tools & MCP Tools -- sa-risk-identification

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research risk patterns, failure modes, industry risk frameworks |
| TL-002 | Web Fetch | Retrieve detailed risk assessment guides, vendor documentation, CVE databases |
| TL-003 | File Read/Write | Read project files, write risk register, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing risk artifacts, dependency manifests, config files |
| TL-006 | Task (Sub-agent) | Delegate parallel research or risk analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks, known issues, deprecations |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, dependency graphs, security advisories, open issues |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific risk databases, internal standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for risk pattern research in Step 3
- Use **File Write** to produce Mermaid dependency map diagram source files
- Use **Glob/Grep** to find existing dependency manifests, lock files, and config in the codebase
- Use **Task sub-agents** to parallelize independent risk category assessments
- Save all research results locally per requirement #17
