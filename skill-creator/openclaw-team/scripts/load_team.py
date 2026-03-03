#!/usr/bin/env python3
"""
Load and display an existing OpenClaw team configuration.

Usage:
    load_team.py <team-path>

Examples:
    load_team.py ~/.openclaw/teams/my-team
    load_team.py ./teams/dev-team
"""

import json
import sys
from pathlib import Path


def load_team(team_path):
    """Load and display a team's configuration and status."""
    team_dir = Path(team_path).resolve()
    config_path = team_dir / "config.json"

    if not config_path.exists():
        print(f"Error: Team config not found at {config_path}")
        return None

    config = json.loads(config_path.read_text())

    print(f"Team: {config['teamName']}")
    print(f"ID: {config['teamId']}")
    print(f"Mode: {config['coordinationMode']}")
    print(f"Max Teammates: {config['maxTeammates']}")
    print(f"Model: {config.get('defaultModel', 'default')}")
    print(f"Created: {config.get('createdAt', 'unknown')}")
    print()

    roles = config.get("roles", [])
    if roles:
        print(f"Roles ({len(roles)}):")
        for role in roles:
            deps = ", ".join(role.get("dependsOn", [])) or "none"
            print(f"  - {role['name']} [{role['id']}]")
            print(f"    {role['description']}")
            print(f"    Depends on: {deps}")

            # Check for SOUL.md
            soul_path = team_dir / "teammates" / role["id"] / "SOUL.md"
            if soul_path.exists():
                print(f"    SOUL.md: exists")

            # Check status
            status_path = team_dir / "teammates" / role["id"] / "status.json"
            if status_path.exists():
                status = json.loads(status_path.read_text())
                print(f"    Status: {status.get('status', 'unknown')}")
            print()
    else:
        print("No roles defined yet. Add agents with add_agent.py")

    # Load tasks
    tasks_path = team_dir / "tasks.json"
    if tasks_path.exists():
        tasks_data = json.loads(tasks_path.read_text())
        tasks = tasks_data.get("tasks", [])
        if tasks:
            print(f"\nTasks ({len(tasks)}):")
            for task in tasks:
                status = task.get("status", "pending")
                assigned = task.get("assignTo", "unassigned")
                print(f"  [{status}] {task['title']} -> {assigned}")

    return config


def main():
    if len(sys.argv) < 2:
        print("Usage: load_team.py <team-path>")
        sys.exit(1)

    result = load_team(sys.argv[1])
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
