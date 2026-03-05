# Tools & MCP Tools — tl-technology-stack-decision

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research technology options, benchmarks, community metrics, licensing |
| TL-002 | Web Fetch | Retrieve detailed technology documentation, release notes, comparison guides |
| TL-003 | File Read/Write | Read project files, write decision documents, output configs |
| TL-004 | Bash / Shell | Execute verification scripts, test tool installations, check versions |
| TL-005 | Glob / Grep | Search codebase for existing technology usage, dependency files |
| TL-006 | Task (Sub-agent) | Delegate parallel technology research or evaluation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for candidate frameworks and libraries |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, check stars/issues/activity, review dependency files |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific APIs, approved technology registries |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for technology research and documentation in Step 3
- Use **File Read** to inspect existing package.json, pom.xml, requirements.txt for current stack
- Use **Glob/Grep** to find technology usage patterns across the codebase
- Use **Task sub-agents** to parallelize evaluation of different technology categories
- Save all research results locally per logging requirements
