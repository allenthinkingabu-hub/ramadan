# OpenClaw Team Templates

Pre-built team configurations for common use cases. Use as starting points for custom teams.

## Web Development Team

```yaml
teamName: "Web Dev Team"
coordinationMode: normal
maxTeammates: 5
roles:
  - id: pm
    name: "Product Manager"
    description: "Define requirements, manage backlog, coordinate deliverables"
    workflow:
      - step: "Gather requirements from user"
        action: "Create user stories and acceptance criteria"
        output: "requirements.md"
      - step: "Break down into tasks"
        action: "Create tasks in task ledger with priorities and dependencies"
        output: "tasks.json"
      - step: "Review deliverables"
        action: "Validate output against requirements"
        output: "review-notes.md"
  - id: frontend-dev
    name: "Frontend Developer"
    description: "Build UI components, pages, and client-side logic"
    dependsOn: [pm]
    tools:
      allow: [read, write, exec, browser]
    workflow:
      - step: "Review assigned tasks"
        action: "Read requirements and design specs"
      - step: "Implement UI"
        action: "Write components, styles, tests"
      - step: "Test and iterate"
        action: "Run tests, fix issues"
  - id: backend-dev
    name: "Backend Developer"
    description: "Build APIs, database schemas, and server-side logic"
    dependsOn: [pm]
    tools:
      allow: [read, write, exec]
    workflow:
      - step: "Review assigned tasks"
        action: "Read requirements and API specs"
      - step: "Implement API"
        action: "Write endpoints, models, migrations"
      - step: "Test and iterate"
        action: "Run tests, fix issues"
  - id: qa
    name: "QA Tester"
    description: "Write and run tests, report bugs, validate quality"
    dependsOn: [frontend-dev, backend-dev]
    tools:
      allow: [read, write, exec, browser]
    workflow:
      - step: "Review requirements"
        action: "Create test plan from acceptance criteria"
      - step: "Write tests"
        action: "Create unit, integration, and e2e tests"
      - step: "Execute and report"
        action: "Run tests, file bugs, verify fixes"

## Data Pipeline Team

```yaml
teamName: "Data Pipeline Team"
coordinationMode: delegate
maxTeammates: 4
roles:
  - id: data-architect
    name: "Data Architect"
    description: "Design schemas, data models, and pipeline architecture"
    workflow:
      - step: "Analyze data sources"
      - step: "Design schema and models"
      - step: "Document pipeline architecture"
  - id: etl-dev
    name: "ETL Developer"
    description: "Build data extraction, transformation, and loading pipelines"
    dependsOn: [data-architect]
  - id: analyst
    name: "Data Analyst"
    description: "Write queries, create dashboards, generate reports"
    dependsOn: [etl-dev]
  - id: data-qa
    name: "Data QA"
    description: "Validate data quality, consistency, and completeness"
    dependsOn: [etl-dev]
```

## DevOps Team

```yaml
teamName: "DevOps Team"
coordinationMode: normal
maxTeammates: 3
roles:
  - id: infra-engineer
    name: "Infrastructure Engineer"
    description: "Provision and manage cloud infrastructure, networking, and security"
  - id: ci-cd-engineer
    name: "CI/CD Engineer"
    description: "Build and maintain CI/CD pipelines, automated deployments"
    dependsOn: [infra-engineer]
  - id: sre
    name: "Site Reliability Engineer"
    description: "Monitor, alert, and maintain system reliability and performance"
    dependsOn: [infra-engineer]
```

## Research Team

```yaml
teamName: "Research Team"
coordinationMode: delegate
maxTeammates: 4
roles:
  - id: lead-researcher
    name: "Lead Researcher"
    description: "Define research questions, coordinate analysis, synthesize findings"
  - id: literature-reviewer
    name: "Literature Reviewer"
    description: "Search, read, and summarize relevant papers and articles"
    dependsOn: [lead-researcher]
  - id: data-collector
    name: "Data Collector"
    description: "Gather data from APIs, web, and databases"
    dependsOn: [lead-researcher]
  - id: analyst
    name: "Analyst"
    description: "Analyze data, generate visualizations, write reports"
    dependsOn: [literature-reviewer, data-collector]
```
