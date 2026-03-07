# Tools & MCP Tools -- tl-unblocking-the-team

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research solutions, known issues, stack overflow answers |
| TL-002 | Web Fetch | Retrieve documentation, issue trackers, release notes |
| TL-003 | File Read/Write | Read logs, code, configs; write resolution documents |
| TL-004 | Bash / Shell | Execute debugging commands, test fixes, inspect environments |
| TL-005 | Glob / Grep | Search codebase for errors, patterns, configuration issues |
| TL-006 | Task (Sub-agent) | Delegate parallel investigation tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query library docs for known issues and workarounds |
| MCP-002 | GitHub (via gh CLI) | Inspect issues, PRs, CI logs, repository state |
| MCP-003 | Custom MCP servers (if configured) | Access internal monitoring, logging, alerting systems |

## Tool Usage Guidelines

- Use **Web Search** to research error messages and known issues
- Use **Bash** for debugging commands, log analysis, environment inspection
- Use **Glob/Grep** to search for error patterns and configuration issues
- Use **GitHub CLI** to inspect CI/CD failures and related issues
- Use **Context7** for library-specific issue research
