# Tools & MCP Tools -- sa-security-review

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research security review methodologies, best practices, industry standards |
| TL-002 | Web Fetch | Retrieve detailed guides, OWASP documentation, CVE databases |
| TL-003 | File Read/Write | Read project files, write deliverables, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing security artifacts, configurations |
| TL-006 | Task (Sub-agent) | Delegate parallel research or deliverable generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for security frameworks and tools |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing security configurations, pull requests |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific security standards and policies |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for security review methodology research in Step 3
- Use **File Write** to produce deliverable documents and configuration files
- Use **Glob/Grep** to find existing security review artifacts in the codebase
- Use **Task sub-agents** to parallelize independent deliverable tasks
- Save all research results locally per requirement
