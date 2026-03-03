# OpenClaw Agent & Team Config Schemas

## Team config.json Schema

```yaml
teamName: "string"                    # Team display name
teamId: "string"                      # Unique identifier (auto-generated from name)
coordinationMode: "normal|delegate"   # Lead participates vs coordinates only
maxTeammates: 5                       # Max agents in team
defaultModel: "anthropic/claude-opus-4-5"  # Default LLM for teammates
requirePlanApproval: false            # Teammates must submit plans before acting
roles:
  - id: "string"                      # Role identifier
    name: "string"                    # Display name
    description: "string"            # What this role does
    model: "string"                   # Optional model override
    tools:
      allow: ["read", "write", "exec"]  # Allowed tools
      deny: ["browser"]              # Denied tools
    dependsOn: ["role-id"]           # Roles this one depends on
    workflow:                         # Sequential steps
      - step: "string"
        action: "string"
        output: "string"
```

## openclaw.json Agent Configuration

```json
{
  "agents": {
    "list": [
      {
        "id": "agent-id",
        "workspace": "~/.openclaw/workspace-agent-id",
        "agentDir": "~/.openclaw/agents/agent-id",
        "model": "anthropic/claude-opus-4-5"
      }
    ],
    "defaults": {
      "workspace": "~/clawd"
    },
    "teams": {
      "enabled": true,
      "maxTeammatesPerTeam": 5,
      "defaultModel": "anthropic/claude-opus-4-5",
      "storage": {
        "basePath": "~/.openclaw/teams"
      },
      "allowedModels": ["anthropic/claude-opus-4-5"],
      "teammateTools": {
        "allow": ["read", "write", "task_claim"],
        "deny": ["browser"]
      }
    }
  },
  "bindings": [
    {
      "agentId": "agent-id",
      "match": {
        "channel": "whatsapp",
        "accountId": "account"
      }
    }
  ]
}
```

## SOUL.md Structure

```markdown
# [Agent Name]

## Identity
[Who this agent is - role, expertise, background]

## Personality
[Tone, communication style, quirks]

## Boundaries
[What the agent should NOT do, safety constraints]

## Capabilities
[What the agent CAN do, tools and skills available]

## Handoffs
[Rules for communicating with other agents via @mentions]
- @AgentName: when to hand off and what context to provide

## Workflow
[Step-by-step process this agent follows]
1. Step one
2. Step two
...
```

## Task States

```
pending → blocked (dependencies unmet) → claimed → in-progress → completed / failed
```

Dependencies specified via `dependsOn: [taskId, ...]`. Auto-transitions from blocked→pending when all dependencies complete.

## Communication Primitives

- **Point-to-point**: `teammate_message(to: teammateId, message: string)`
- **Broadcast**: `teammate_broadcast(message: string)`
- **Shutdown**: `teammate_shutdown(force: boolean)`

Messages persist in `mailbox/` until read.
