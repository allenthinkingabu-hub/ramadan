# Tools & MCP Tools — sa-spike-poc-leadership

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research technologies, benchmarks, comparison data |
| TL-002 | Web Fetch | Retrieve detailed documentation, API specs, benchmark results |
| TL-003 | File Read/Write | Read project files, write PoC code, output documents and configs |
| TL-004 | Bash / Shell | Execute PoC code, run benchmarks, install dependencies |
| TL-005 | Glob / Grep | Search codebase for relevant patterns and existing implementations |
| TL-006 | Task (Sub-agent) | Delegate parallel research or PoC experiments |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks and services |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, sample implementations, library comparisons |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, internal benchmarks |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology research and comparison in Step 3
- Use **Bash** to execute PoC code, run benchmarks, and install dependencies
- Use **File Write** to produce PoC code artifacts and documentation
- Use **Glob/Grep** to find existing implementations for reference
- Use **Task sub-agents** to parallelize independent PoC experiments
- Save all research and benchmark results locally per logging requirements
