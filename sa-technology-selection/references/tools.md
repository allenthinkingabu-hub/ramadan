# Tools & MCP Tools — sa-technology-selection

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research technology options, vendor comparisons, benchmark data |
| TL-002 | Web Fetch | Retrieve detailed technology documentation, pricing pages, release notes |
| TL-003 | File Read/Write | Read project files, write evaluation reports, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing technology artifacts, dependencies |
| TL-006 | Task (Sub-agent) | Delegate parallel research or evaluation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and cloud services |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, community health metrics, release history |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal technology standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology evaluation research in Step 3
- Use **File Write** to produce scoring matrices, TCO analyses, and evaluation reports
- Use **Glob/Grep** to find existing technology dependencies and configurations in the codebase
- Use **Task sub-agents** to parallelize independent technology evaluations
- Save all research results locally per requirement #17
