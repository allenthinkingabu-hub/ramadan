# MCP Tools Checklist

## Role: Technical Lead (TL) — Technical Design & Solution Design Agent

### Available MCP Integrations

| # | MCP Server | Tool Name | Purpose | When to Use |
|:--|:--|:--|:--|:--|
| M1 | **context7** | `resolve-library-id` | Resolve a library/package name to a Context7-compatible library ID | Before querying documentation for any library or framework referenced in the design |
| M2 | **context7** | `query-docs` | Retrieve up-to-date documentation and code examples for any library | When designing components that use specific libraries — get current API patterns, configuration options, best practices |

### MCP Usage Guidelines

#### Context7 Integration

**When to invoke:**
- Designing a component that uses a specific framework (e.g., Spring Boot, Express.js, FastAPI)
- Specifying data access patterns for a specific database driver (e.g., Prisma, SQLAlchemy, TypeORM)
- Designing API endpoints using a specific framework's conventions
- Evaluating technology alternatives with up-to-date API information
- Verifying that the designed patterns align with the library's current version

**How to invoke:**
1. First call `resolve-library-id` with the library name and your query
2. Use the returned library ID to call `query-docs` with your specific question
3. Save the research results locally per Item 17

**Usage limits:**
- Maximum 3 calls to `resolve-library-id` per question
- Maximum 3 calls to `query-docs` per question
- If needed information is not found after 3 calls, use the best available result

#### Example Usage Scenarios

| Scenario | MCP Call Sequence |
|:--|:--|
| Designing a REST API with Express.js | 1. `resolve-library-id("express")` → 2. `query-docs("/expressjs/express", "middleware pattern and error handling")` |
| Designing data access with Prisma | 1. `resolve-library-id("prisma")` → 2. `query-docs("/prisma/docs", "relation queries and transactions")` |
| Designing message handling with Kafka | 1. `resolve-library-id("kafkajs")` → 2. `query-docs("/tulios/kafkajs", "consumer group and partition assignment")` |

### Future MCP Extensions

| # | Potential MCP Server | Purpose | Status |
|:--|:--|:--|:--|
| F1 | **GitHub** | Access repository structure, existing code, PR history | Planned |
| F2 | **Jira / Linear** | Read task details, acceptance criteria, linked requirements | Planned |
| F3 | **Confluence / Notion** | Access existing design documents, wiki pages | Planned |
| F4 | **OpenAPI** | Parse and validate API specifications | Planned |

## Configuration Notes

- Add new MCP integrations by appending rows to the Available MCP Integrations table
- Update usage guidelines when new MCP tools are added
- Future MCP extensions should be moved to the main table when they become available
- All MCP tool results must be saved locally for future reference (Item 17)
