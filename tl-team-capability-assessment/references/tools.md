# Tools & MCP Tools — tl-team-capability-assessment

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research team assessment methodologies, training resources, capability frameworks |
| TL-002 | Web Fetch | Retrieve detailed training platform information, certification guides |
| TL-003 | File Read/Write | Read project files, write assessment documents, output configs |
| TL-004 | Bash / Shell | Execute verification scripts, inspect directory structures |
| TL-005 | Glob / Grep | Search codebase for contributor patterns, technology usage indicators |
| TL-006 | Task (Sub-agent) | Delegate parallel research or assessment tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query documentation for technologies requiring team skills |
| MCP-002 | GitHub (via gh CLI) | Inspect commit history, PR reviews, contributor activity |
| MCP-003 | Custom MCP servers (if configured) | Access organization HR systems, skill tracking platforms |

## Tool Usage Guidelines

- Use **Web Search** for training resource research and industry capability frameworks
- Use **GitHub** to analyze team contribution patterns and code review participation
- Use **File Read** to inspect existing team documentation and skill records
- Use **Task sub-agents** to parallelize research on different skill domains
- Save all research results locally per logging requirements
