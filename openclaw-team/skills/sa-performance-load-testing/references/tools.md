# Tools & MCP Tools -- sa-performance-load-testing

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research performance testing methodologies, tool documentation, benchmarking practices |
| TL-002 | Web Fetch | Retrieve detailed guides on load testing tools, cloud performance tuning |
| TL-003 | File Read/Write | Read project files, write test plans, output documents and configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for existing performance test artifacts, NFR documents |
| TL-006 | Task (Sub-agent) | Delegate parallel research or scenario generation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for testing frameworks and tools |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing test configurations, CI/CD pipelines |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific performance baselines and SLA definitions |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for performance testing methodology research in Step 3
- Use **File Write** to produce test scenario definitions and benchmark documents
- Use **Glob/Grep** to find existing performance test artifacts in the codebase
- Use **Task sub-agents** to parallelize independent scenario design tasks
- Save all research results locally per requirement
