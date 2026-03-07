"""
Orchestrator — PM-only wave execution engine.

Reads tasks-index.json, organizes tasks by wave, triggers them via Telegram,
tracks completions, and advances to the next wave when all tasks complete.
"""

import json
import logging
from pathlib import Path
from typing import Optional

from .telegram_bot import TelegramBot
from .event_protocol import (
    TaskTriggeredEvent,
    TaskCompletedEvent,
    EventType,
    parse_task_completed,
)
from .state_manager import StateManager, TaskStatus

logger = logging.getLogger(__name__)


class Orchestrator:
    """PM orchestration engine for wave-based task execution."""

    def __init__(
        self,
        bot: TelegramBot,
        state: StateManager,
        tasks_index_path: str,
        skills_base_dir: str,
        model_key: str = None,
    ):
        self.bot = bot
        self.state = state
        self.skills_base_dir = Path(skills_base_dir)
        self.model_key = model_key
        self.tasks = self._load_tasks(tasks_index_path)
        self.waves = self._organize_waves()

        # Map task_id → task_def for quick lookup
        self.task_map = {t["task_id"]: t for t in self.tasks}

        # Track which role handles which task prefix
        self._role_prefix_map = {
            "PM": "PM-",
            "IPM": "IPM-",
            "SA": "IA-",
        }

    def _load_tasks(self, path: str) -> list:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data.get("tasks", [])

    def _organize_waves(self) -> dict:
        """Group tasks by wave number. Returns {wave_num: [task_defs]}."""
        waves = {}
        for task in self.tasks:
            w = task.get("wave", 1)
            if w not in waves:
                waves[w] = []
            waves[w].append(task)
        return dict(sorted(waves.items()))

    def get_role_for_task(self, task_id: str) -> str:
        """Determine which role agent should handle a task based on ID prefix."""
        for role, prefix in self._role_prefix_map.items():
            if task_id.startswith(prefix):
                return role
        return "PM"  # Default

    async def start_project(self, project_description: str):
        """Begin project execution — trigger Wave 1 tasks.

        Called when a user sends a project start command.
        """
        await self.bot.send_to_group(
            f"📋 [PM] Project received. Starting execution.\n\n"
            f"Project: {project_description}\n\n"
            f"Total waves: {len(self.waves)}\n"
            f"Total tasks: {len(self.tasks)}"
        )

        # Initialize all tasks in state
        self.state.initialize_tasks([t["task_id"] for t in self.tasks])

        # Start Wave 1
        await self.trigger_wave(1)

    async def trigger_wave(self, wave_num: int):
        """Trigger all tasks in a wave."""
        if wave_num not in self.waves:
            await self.bot.send_to_group(
                f"✅ [PM] All waves completed! Project execution finished."
            )
            return

        wave_tasks = self.waves[wave_num]
        await self.bot.send_to_group(
            f"📋 [PM] Starting Wave {wave_num} — "
            f"{len(wave_tasks)} task(s)"
        )

        for task in wave_tasks:
            # Skip already completed tasks (idempotent restart)
            if self.state.is_task_done(task["task_id"]):
                logger.info(f"Skipping already completed: {task['task_id']}")
                continue

            target_role = self.get_role_for_task(task["task_id"])

            # For PM's own tasks, execute locally
            if target_role == "PM":
                await self._execute_own_task(task)
            else:
                # Send TaskTriggered to the group for the target agent
                event = TaskTriggeredEvent(
                    task_id=task["task_id"],
                    task_name=task["name"],
                    skill_dir=task["skill_dir"],
                    source_role="PM",
                    target_role=target_role,
                )
                await self.bot.send_event(event)

    async def handle_task_completed(self, text: str):
        """Handle a TaskCompleted message from another agent.

        Checks if the current wave is fully complete, then triggers next wave.
        """
        event = parse_task_completed(text)
        if not event:
            return

        task_id = event.task_id
        logger.info(f"[PM] Task completed: {task_id} status={event.status}")

        # Update state
        if event.status == "DONE":
            self.state.complete_task(task_id)
        else:
            self.state.fail_task(task_id, "Reported FAILED by agent")

        # Check if current wave is complete
        current_wave = self._find_wave_for_task(task_id)
        if current_wave is not None:
            if self._is_wave_complete(current_wave):
                await self.bot.send_to_group(
                    f"✅ [PM] Wave {current_wave} completed!"
                )
                # Trigger next wave
                next_wave = current_wave + 1
                await self.trigger_wave(next_wave)

    def _find_wave_for_task(self, task_id: str) -> Optional[int]:
        """Find which wave a task belongs to."""
        task = self.task_map.get(task_id)
        if task:
            return task.get("wave")
        return None

    def _is_wave_complete(self, wave_num: int) -> bool:
        """Check if all tasks in a wave are done."""
        if wave_num not in self.waves:
            return True
        for task in self.waves[wave_num]:
            if not self.state.is_task_done(task["task_id"]):
                return False
        return True

    async def _execute_own_task(self, task: dict):
        """Execute a PM task locally using the skill executor."""
        # Import here to avoid circular dependency
        from .skill_executor import SkillExecutor
        from .llm_client import LLMClient

        llm = LLMClient(model_key=self.model_key)
        executor = SkillExecutor(
            bot=self.bot,
            llm=llm,
            state=self.state,
            workspace_dir=str(Path.home() / ".openclaw" / "workspace-pm"),
            skills_base_dir=str(self.skills_base_dir),
            role="PM",
        )

        result = await executor.execute(
            task_id=task["task_id"],
            task_name=task["name"],
            skill_dir_name=task["skill_dir"],
        )

        # If PM completes its own task, check wave completion
        if result["status"] == "DONE":
            current_wave = task.get("wave")
            if current_wave and self._is_wave_complete(current_wave):
                next_wave = current_wave + 1
                await self.trigger_wave(next_wave)
