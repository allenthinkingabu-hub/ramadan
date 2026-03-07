# Integration Design Agent — MCP Tools Checklist

## MCP Server Integrations

| MCP ID | MCP Server | Tools Provided | Usage Context |
| :--- | :--- | :--- | :--- |
| MCP-001 | filesystem | read_file, write_file, list_directory, create_directory | Read input docs, save output artifacts |
| MCP-002 | web-search | search | Research integration patterns and best practices |
| MCP-003 | web-fetch | fetch | Fetch vendor API documentation and specs |
| MCP-004 | github | search_repositories, get_file_contents, search_code | Analyze existing codebase integration points |
| MCP-005 | memory | store, retrieve, list | Persist research results and conversation context |

## MCP Tool Usage by Phase

### Phase 1: Understand Task Purpose
- `web-search.search` — Research integration design methodologies
- `filesystem.read_file` — Read project documentation

### Phase 2: Understand Topic
- `filesystem.read_file` — Read architecture and tech stack documents
- `github.get_file_contents` — Analyze existing codebase
- `github.search_code` — Find current integration patterns

### Phase 3: Research & Question List
- `web-search.search` — Research industry best practices
- `web-fetch.fetch` — Fetch vendor API documentation
- `memory.store` — Save research results locally

### Phase 4: Execute & Output
- `filesystem.write_file` — Save all output artifacts
- `filesystem.create_directory` — Create integration-design output directory
- `memory.store` — Save work log and conversation log

## Configuration Notes

- Add new MCP servers by appending rows to the MCP Server Integrations table.
- Update tool usage per phase as workflow evolves.
