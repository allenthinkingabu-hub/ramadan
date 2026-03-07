#!/usr/bin/env python3
"""
Agent — Main entry point for each OpenClaw AI Agent.

Each agent runs in its own terminal window as a Telegram bot.
Agents communicate via a shared Telegram group.

Usage:
    python3 -m runtime.agent --role pm
    python3 -m runtime.agent --role ipm
    python3 -m runtime.agent --role sa
"""

import argparse
import asyncio
import json
import logging
import signal
import sys
from pathlib import Path

from .telegram_bot import TelegramBot
from .llm_client import LLMClient
from .state_manager import StateManager
from .skill_executor import SkillExecutor
from .event_protocol import (
    EventType,
    parse_task_triggered,
)
from .orchestrator import Orchestrator

logger = logging.getLogger(__name__)

# Auto-detect package root (openclaw-team/)
PACKAGE_ROOT = Path(__file__).resolve().parent.parent


ROLE_CONFIG = {
    "pm": {
        "name": "IT Project Manager",
        "emoji": "📊",
        "workspace": "workspace-pm",
        "is_orchestrator": True,
        "role_code": "PM",
    },
    "ipm": {
        "name": "IT Product Manager",
        "emoji": "📋",
        "workspace": "workspace-ipm",
        "is_orchestrator": False,
        "role_code": "IPM",
    },
    "sa": {
        "name": "System Architect",
        "emoji": "🏗️",
        "workspace": "workspace-sa",
        "is_orchestrator": False,
        "role_code": "SA",
    },
}


class AgentRunner:
    """Main agent process."""

    def __init__(self, role: str, package_root: Path, model_override: str = None):
        self.role = role.lower()
        self.role_upper = role.upper()
        self.config = ROLE_CONFIG[self.role]
        self.package_root = package_root

        # Load Telegram config
        tg_config = self._load_telegram_config()
        bot_config = tg_config["bots"][self.role]
        self.group_chat_id = int(tg_config["group_chat_id"])

        # Determine which LLM model to use
        self.model_key = model_override or self._resolve_model_key()
        logger.info(f"[{self.role_upper}] Using model: {self.model_key}")

        # Initialize components
        self.bot = TelegramBot(
            token=bot_config["token"],
            group_chat_id=self.group_chat_id,
            role=self.role_upper,
        )
        self.llm = LLMClient(model_key=self.model_key)

        # Workspace
        self.workspace_dir = Path.home() / ".openclaw" / self.config["workspace"]
        self.state = StateManager(str(self.workspace_dir))

        # Skills base directory
        self.skills_base_dir = package_root / "skills"

        # Orchestrator (PM only)
        self.orchestrator = None
        if self.config["is_orchestrator"]:
            tasks_index = self.workspace_dir / "config" / "tasks-index.json"
            if tasks_index.exists():
                self.orchestrator = Orchestrator(
                    bot=self.bot,
                    state=self.state,
                    tasks_index_path=str(tasks_index),
                    skills_base_dir=str(self.skills_base_dir),
                    model_key=self.model_key,
                )

        # Skill executor
        self.executor = SkillExecutor(
            bot=self.bot,
            llm=self.llm,
            state=self.state,
            workspace_dir=str(self.workspace_dir),
            skills_base_dir=str(self.skills_base_dir),
            role=self.role_upper,
        )

        # Load task definitions for this role
        self.tasks_index = self._load_tasks_index()

    def _load_telegram_config(self) -> dict:
        config_path = self.package_root / "config" / "telegram.json"
        if not config_path.exists():
            print(f"ERROR: {config_path} not found.")
            print("Create config/telegram.json with your bot tokens first.")
            sys.exit(1)
        return json.loads(config_path.read_text(encoding="utf-8"))

    def _resolve_model_key(self) -> str:
        """Read agents-registry.json to get the model key for this role."""
        registry_path = self.package_root / "config" / "agents-registry.json"
        if registry_path.exists():
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            for agent in registry.get("agents", []):
                if agent.get("role_code") == self.config["role_code"]:
                    return agent.get("model", "claude-opus")
        return "claude-opus"

    def _load_tasks_index(self) -> dict:
        """Load and index tasks for this role."""
        tasks_file = self.workspace_dir / "config" / "tasks-index.json"
        if not tasks_file.exists():
            logger.warning(f"No tasks-index.json found at {tasks_file}")
            return {}
        data = json.loads(tasks_file.read_text(encoding="utf-8"))
        return {t["task_id"]: t for t in data.get("tasks", [])}

    async def start(self):
        """Start the agent: connect to Telegram, register handlers, enter loop."""
        # Register event handlers
        self.bot.on_event(self._handle_event)
        self.bot.on_user_message(self._handle_user_message)

        # Start the Telegram bot
        await self.bot.start()

        # Announce online with model info
        emoji = self.config["emoji"]
        await self.bot.send_to_group(
            f"{emoji} [{self.role_upper}] {self.config['name']} Agent online.\n"
            f"Model: {self.model_key} ({self.llm.model_id})"
        )

        logger.info(f"[{self.role_upper}] Agent started and listening.")

        # Keep running until shutdown
        stop_event = asyncio.Event()

        def _signal_handler():
            stop_event.set()

        loop = asyncio.get_event_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, _signal_handler)

        await stop_event.wait()

        # Graceful shutdown
        await self.bot.send_to_group(
            f"🔴 [{self.role_upper}] Agent going offline."
        )
        await self.bot.stop()

    async def _handle_event(self, event_type: EventType, text: str, update):
        """Handle structured event messages from other agents."""

        if event_type == EventType.TASK_TRIGGERED:
            event = parse_task_triggered(text)
            if not event:
                return

            # Check if this task is for us
            if event.target_role != self.role_upper:
                return

            logger.info(
                f"[{self.role_upper}] Received task: {event.task_id} ({event.task_name})"
            )
            await self.bot.send_to_group(
                f"📥 [{self.role_upper}] Received task {event.task_id}: "
                f"{event.task_name}. Starting..."
            )

            # Execute the skill
            result = await self.executor.execute(
                task_id=event.task_id,
                task_name=event.task_name,
                skill_dir_name=event.skill_dir,
            )

            # Report completion
            from .event_protocol import TaskCompletedEvent
            completed = TaskCompletedEvent(
                task_id=event.task_id,
                task_name=event.task_name,
                source_role=self.role_upper,
                status=result["status"],
                artifacts=result.get("artifacts", []),
                supervisor_result=result.get("supervisor_result", ""),
            )
            await self.bot.send_event(completed)

        elif event_type == EventType.TASK_COMPLETED:
            # PM handles task completions
            if self.orchestrator:
                await self.orchestrator.handle_task_completed(text)

    async def _handle_user_message(self, text: str, user_id: int, update):
        """Handle non-event messages from users."""

        # PM: check for project start commands
        if self.config["is_orchestrator"]:
            start_triggers = ["start project", "启动项目", "/start"]
            if any(trigger in text.lower() for trigger in start_triggers):
                if self.orchestrator:
                    await self.orchestrator.start_project(text)
                return

        # For non-orchestrator agents, user messages during skill execution
        # are handled by wait_for_user_reply in skill_executor
        # No action needed here


def main():
    parser = argparse.ArgumentParser(description="OpenClaw AI Agent")
    parser.add_argument(
        "--role",
        required=True,
        choices=["pm", "ipm", "sa"],
        help="Agent role: pm, ipm, or sa",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Override model key (e.g., claude-opus, gpt-4o, deepseek-chat). "
             "Defaults to value in agents-registry.json.",
    )
    parser.add_argument(
        "--package-root",
        type=str,
        default=None,
        help="Path to openclaw-team/ directory (auto-detected if not set)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format=f"%(asctime)s [{args.role.upper()}] %(name)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    package_root = Path(args.package_root) if args.package_root else PACKAGE_ROOT

    agent = AgentRunner(
        role=args.role,
        package_root=package_root,
        model_override=args.model,
    )
    asyncio.run(agent.start())


if __name__ == "__main__":
    main()
