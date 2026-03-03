# OpenClaw Agent Team Folder Structure

## Global Layout

```
~/.openclaw/
├── openclaw.json              # Gateway config (agents, bindings, teams settings)
├── agents/
│   └── <agentId>/
│       ├── agent/             # Auth profiles, model registry
│       └── sessions/          # Chat history, routing state
├── teams/
│   └── <teamId>/
│       ├── config.json        # Team metadata & settings
│       ├── tasks.json         # Shared task ledger
│       ├── mailbox/           # Inter-agent messages
│       └── teammates/         # Per-teammate metadata
├── skills/                    # Shared skills across agents
│   └── <skill-name>/
│       └── SKILL.md
└── workspace-<agentId>/       # Per-agent workspace
    ├── SOUL.md                # Agent personality, boundaries, tone
    ├── AGENTS.md              # Operating instructions, memory
    ├── USER.md                # User-specific context
    ├── TOOLS.md               # Available tools
    └── skills/                # Agent-specific skills
```

## Team Directory Structure

Each team gets its own directory under `~/.openclaw/teams/`:

```
~/.openclaw/teams/<teamId>/
├── config.json                # Team configuration
│   ├── teamName               # Display name
│   ├── coordinationMode       # "normal" | "delegate"
│   ├── maxTeammates           # Max agents (default: 5)
│   ├── defaultModel           # LLM model for teammates
│   └── roles[]                # Role definitions
├── tasks.json                 # Shared task ledger
│   └── tasks[]
│       ├── id
│       ├── title
│       ├── status             # pending|blocked|claimed|in-progress|completed|failed
│       ├── assignTo           # Optional teammate ID
│       ├── dependsOn[]        # Task dependencies
│       └── priority           # critical|high|medium|low
├── mailbox/                   # Inter-agent messages
│   └── <agentId>.jsonl        # Messages for specific agent
└── teammates/
    └── <teammateId>/
        ├── SOUL.md            # Teammate persona
        └── status.json        # Current state
```

## Per-Agent Workspace

Each agent workspace contains:

```
workspace-<agentId>/
├── SOUL.md          # WHO the agent is (personality, boundaries, role)
├── AGENTS.md        # HOW the agent works (instructions, memory)
├── USER.md          # WHO the user is (preferences, context)
├── TOOLS.md         # WHAT tools are available
├── BOOTSTRAP.md     # First-run setup ritual (auto-generated)
├── IDENTITY.md      # Agent identity details
└── skills/          # Agent-specific installed skills
```
