---
name: openclaw-team
description: "Create, configure, and manage OpenClaw agent teams. Use when users want to: (1) Create a new multi-agent team with defined roles, (2) Add or update agents in an existing team, (3) Load and initialize a saved team configuration, (4) Set up agent workflows, dependencies, and communication, or any task involving OpenClaw agent team orchestration. Triggers include phrases like 'create a dev team', 'add an agent to my team', 'set up an OpenClaw team', 'load my team config'."
---

# OpenClaw Team

Create and manage OpenClaw agent teams with persistent YAML/JSON configs that can be reused across sessions.

## Workflow Decision Tree

1. Determine the operation type:
   **Creating a new team?** → Follow "Create Team" below
   **Adding/updating agents?** → Follow "Manage Agents" below
   **Loading an existing team?** → Follow "Load Team" below

## Create Team

Creating a new team involves these steps:

1. Gather requirements (team name, purpose, coordination mode)
2. Initialize team directory (run `scripts/init_team.py`)
3. Add agent roles (run `scripts/add_agent.py` for each role)
4. Verify team config (run `scripts/load_team.py`)

### Step 1: Gather Requirements

Ask the user:
- **Team name**: What should the team be called?
- **Purpose**: What will this team work on?
- **Coordination mode**: `normal` (lead works alongside teammates) or `delegate` (lead coordinates only)?
- **Roles needed**: What agent roles are required?

If the user is unsure about roles, suggest a template from [references/team-templates.md](references/team-templates.md).

### Step 2: Initialize Team

```bash
python3 scripts/init_team.py "<team-name>" --path <output-path> --mode <normal|delegate>
```

Default path: `~/.openclaw/teams`. Override with `--path` for project-local teams.

### Step 3: Add Agents

For each role, run:

```bash
python3 scripts/add_agent.py <team-path> \
  --role-id <id> \
  --name "<display-name>" \
  --description "<what-this-agent-does>" \
  --depends-on "<comma-separated-role-ids>" \
  --tools-allow "<comma-separated-tools>" \
  --tools-deny "<comma-separated-tools>"
```

This creates:
- Role entry in `config.json`
- `teammates/<role-id>/SOUL.md` (agent persona)
- `teammates/<role-id>/status.json` (agent state)

After adding agents, customize each `SOUL.md` to refine the agent's personality, boundaries, and workflow for the specific use case.

### Step 4: Verify

```bash
python3 scripts/load_team.py <team-path>
```

## Manage Agents

**Adding a new agent** to an existing team:
1. Run `scripts/add_agent.py` with the team path and role details
2. Customize the generated `SOUL.md` as needed

**Updating an existing agent**:
1. Edit `teammates/<role-id>/SOUL.md` directly for persona changes
2. Edit `config.json` directly for role metadata changes (dependencies, tools, model)

**Removing an agent**:
1. Delete the role entry from `config.json`
2. Delete the `teammates/<role-id>/` directory

## Load Team

Load and initialize a saved team configuration:

```bash
python3 scripts/load_team.py <team-path>
```

This displays all roles, their dependencies, statuses, and pending tasks. Use this when restarting a team to restore context.

## Agent Config Structure

Each agent is defined by:

- **Role ID**: Unique identifier within the team
- **Name**: Display name
- **Description**: What this agent does
- **Model**: Optional LLM override (default: team's `defaultModel`)
- **Tools**: Allowed/denied tool lists
- **Dependencies**: Which roles this agent depends on
- **Workflow**: Sequential steps the agent follows
- **SOUL.md**: Full persona file with identity, personality, boundaries, capabilities, handoffs

For full schema details, see [references/agent-config-schema.md](references/agent-config-schema.md).

## Directory Structure

Teams follow the OpenClaw convention:

```
teams/<team-id>/
├── config.json          # Team metadata, roles, settings
├── tasks.json           # Shared task ledger
├── mailbox/             # Inter-agent messages
└── teammates/
    └── <role-id>/
        ├── SOUL.md      # Agent persona
        └── status.json  # Agent state
```

For the full OpenClaw folder layout, see [references/folder-structure.md](references/folder-structure.md).

## Team Templates

Pre-built templates are available for common team types:
- **Web Development**: PM, Frontend Dev, Backend Dev, QA
- **Data Pipeline**: Data Architect, ETL Dev, Analyst, Data QA
- **DevOps**: Infra Engineer, CI/CD Engineer, SRE
- **Research**: Lead Researcher, Literature Reviewer, Data Collector, Analyst

See [references/team-templates.md](references/team-templates.md) for full template definitions.
