#!/usr/bin/env python3
"""
Initialize a new OpenClaw agent team.

Usage:
    init_team.py <team-name> [--path <path>] [--template <template>] [--mode <normal|delegate>]

Examples:
    init_team.py my-dev-team
    init_team.py my-dev-team --path ~/projects/app
    init_team.py my-dev-team --template web-dev
    init_team.py my-dev-team --mode delegate
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime


TEAM_CONFIG_TEMPLATE = {
    "teamName": "",
    "teamId": "",
    "coordinationMode": "normal",
    "maxTeammates": 5,
    "defaultModel": "anthropic/claude-opus-4-5",
    "requirePlanApproval": False,
    "createdAt": "",
    "roles": []
}

SOUL_MD_TEMPLATE = """# {agent_name}

## Identity
{description}

## Personality
- Professional and focused on the task at hand
- Communicates clearly and concisely
- Proactively flags risks and blockers

## Boundaries
- Stay within the scope of assigned tasks
- Do not modify files outside the project workspace without approval
- Escalate decisions that affect other team members

## Capabilities
{capabilities}

## Handoffs
{handoffs}

## Workflow
{workflow}
"""

TASKS_TEMPLATE = {
    "tasks": [],
    "lastUpdated": ""
}


def slugify(name):
    """Convert a name to a URL-friendly slug."""
    return name.lower().strip().replace(" ", "-").replace("_", "-")


def init_team(team_name, base_path=None, coordination_mode="normal"):
    """Create a new OpenClaw team directory with config files."""
    team_id = slugify(team_name)

    if base_path:
        teams_dir = Path(base_path).resolve() / "teams"
    else:
        teams_dir = Path.home() / ".openclaw" / "teams"

    team_dir = teams_dir / team_id

    if team_dir.exists():
        print(f"Error: Team directory already exists: {team_dir}")
        return None

    # Create directory structure
    team_dir.mkdir(parents=True, exist_ok=False)
    (team_dir / "mailbox").mkdir()
    (team_dir / "teammates").mkdir()

    # Create config.json
    config = TEAM_CONFIG_TEMPLATE.copy()
    config["teamName"] = team_name
    config["teamId"] = team_id
    config["coordinationMode"] = coordination_mode
    config["createdAt"] = datetime.now().isoformat()

    config_path = team_dir / "config.json"
    config_path.write_text(json.dumps(config, indent=2))
    print(f"Created {config_path}")

    # Create tasks.json
    tasks = TASKS_TEMPLATE.copy()
    tasks["lastUpdated"] = datetime.now().isoformat()

    tasks_path = team_dir / "tasks.json"
    tasks_path.write_text(json.dumps(tasks, indent=2))
    print(f"Created {tasks_path}")

    print(f"\nTeam '{team_name}' initialized at {team_dir}")
    print(f"Team ID: {team_id}")
    print(f"Mode: {coordination_mode}")
    print("\nNext: Add agents with add_agent.py")
    return team_dir


def main():
    if len(sys.argv) < 2:
        print("Usage: init_team.py <team-name> [--path <path>] [--mode <normal|delegate>]")
        sys.exit(1)

    team_name = sys.argv[1]
    base_path = None
    mode = "normal"

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--path" and i + 1 < len(sys.argv):
            base_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--mode" and i + 1 < len(sys.argv):
            mode = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    result = init_team(team_name, base_path, mode)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
