# Tools & MCP Tools -- tl-technical-decision-making

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research technology options, benchmarks, comparisons |
| TL-002 | Web Fetch | Retrieve documentation, pricing pages, feature matrices |
| TL-003 | File Read/Write | Read project files, write ADRs, decision documents |
| TL-004 | Bash / Shell | Run benchmarks, test configurations, validate options |
| TL-005 | Glob / Grep | Search codebase for existing patterns, dependencies |
| TL-006 | Task (Sub-agent) | Delegate parallel research or evaluation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date library documentation and comparisons |
| MCP-002 | GitHub (via gh CLI) | Inspect library repositories, issues, release activity |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific technology standards |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology research and comparison in Step 3
- Use **Web Fetch** to gather pricing, feature matrices, and benchmark data
- Use **GitHub CLI** to assess library health (stars, issues, release frequency)
- Use **Bash** to run proof-of-concept tests and benchmarks
- Use **File Write** to produce ADRs, decision registers, and trade-off analyses
