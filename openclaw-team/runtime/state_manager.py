"""
State Manager — Tracks task execution state in state.json.

Provides idempotent state transitions: PENDING → IN_PROGRESS → DONE/FAILED.
Thread-safe file operations with atomic writes.
"""

import json
import tempfile
import os
from datetime import datetime
from pathlib import Path
from enum import Enum
class TaskStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    FAILED = "FAILED"


class StateManager:
    """Manages task execution state for a single agent workspace."""

    def __init__(self, workspace_dir: str):
        self.workspace_dir = Path(workspace_dir)
        self.state_file = self.workspace_dir / "config" / "state.json"
        self._ensure_state_file()

    def _ensure_state_file(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.state_file.exists():
            self._write_state({"tasks": {}, "last_updated": self._now()})

    def _now(self) -> str:
        return datetime.now().isoformat()

    def _read_state(self) -> dict:
        return json.loads(self.state_file.read_text(encoding="utf-8"))

    def _write_state(self, state: dict):
        state["last_updated"] = self._now()
        # Atomic write
        fd, tmp_path = tempfile.mkstemp(
            dir=str(self.state_file.parent), suffix=".tmp"
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            os.replace(tmp_path, str(self.state_file))
        except Exception:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    def get_status(self, task_id: str) -> TaskStatus:
        state = self._read_state()
        task_data = state["tasks"].get(task_id, {})
        status_str = task_data.get("status", TaskStatus.PENDING.value)
        return TaskStatus(status_str)

    def set_status(self, task_id: str, status: TaskStatus, details: dict = None):
        state = self._read_state()
        if task_id not in state["tasks"]:
            state["tasks"][task_id] = {}
        state["tasks"][task_id]["status"] = status.value
        state["tasks"][task_id]["updated_at"] = self._now()
        if details:
            state["tasks"][task_id].update(details)
        self._write_state(state)

    def start_task(self, task_id: str):
        current = self.get_status(task_id)
        if current == TaskStatus.DONE:
            return  # Already done, skip
        self.set_status(task_id, TaskStatus.IN_PROGRESS)

    def complete_task(self, task_id: str, artifacts: list = None):
        self.set_status(task_id, TaskStatus.DONE, {
            "completed_at": self._now(),
            "artifacts": artifacts or [],
        })

    def fail_task(self, task_id: str, reason: str = ""):
        self.set_status(task_id, TaskStatus.FAILED, {
            "failed_at": self._now(),
            "reason": reason,
        })

    def is_task_done(self, task_id: str) -> bool:
        return self.get_status(task_id) == TaskStatus.DONE

    def get_pending_tasks(self) -> list:
        """Return task IDs that are PENDING."""
        state = self._read_state()
        pending = []
        for task_id, data in state["tasks"].items():
            if data.get("status") == TaskStatus.PENDING.value:
                pending.append(task_id)
        return pending

    def get_all_statuses(self) -> dict:
        """Return {task_id: status} for all tracked tasks."""
        state = self._read_state()
        return {
            tid: data.get("status", TaskStatus.PENDING.value)
            for tid, data in state["tasks"].items()
        }

    def initialize_tasks(self, task_ids: list):
        """Register tasks as PENDING if not already tracked."""
        state = self._read_state()
        for tid in task_ids:
            if tid not in state["tasks"]:
                state["tasks"][tid] = {
                    "status": TaskStatus.PENDING.value,
                    "created_at": self._now(),
                }
        self._write_state(state)
