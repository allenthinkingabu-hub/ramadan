"""
Event Protocol — Structured message format for inter-agent communication via Telegram.

Defines TaskTriggered, TaskCompleted, SupervisorTriggered, SupervisorCompleted events.
Messages are formatted for human readability in Telegram and machine-parseable by agents.
"""

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class EventType(str, Enum):
    TASK_TRIGGERED = "TaskTriggered"
    TASK_COMPLETED = "TaskCompleted"
    SUPERVISOR_TRIGGERED = "SupervisorTriggered"
    SUPERVISOR_COMPLETED = "SupervisorCompleted"
    AGENT_ONLINE = "AgentOnline"
    PHASE_UPDATE = "PhaseUpdate"


@dataclass
class TaskTriggeredEvent:
    task_id: str
    task_name: str
    skill_dir: str
    source_role: str
    target_role: str
    inputs: dict = field(default_factory=dict)

    def to_telegram(self) -> str:
        inputs_str = ""
        if self.inputs:
            items = [f"  - {k}: {v}" for k, v in self.inputs.items()]
            inputs_str = "\nInputs:\n" + "\n".join(items)
        return (
            f"📋 [TaskTriggered] {self.source_role} → {self.target_role}\n"
            f"Task: {self.task_id} ({self.task_name})\n"
            f"Skill: {self.skill_dir}"
            f"{inputs_str}"
        )


@dataclass
class TaskCompletedEvent:
    task_id: str
    task_name: str
    source_role: str
    status: str  # DONE or FAILED
    artifacts: list = field(default_factory=list)
    supervisor_result: str = ""

    def to_telegram(self) -> str:
        emoji = "✅" if self.status == "DONE" else "❌"
        artifacts_str = ""
        if self.artifacts:
            artifacts_str = "\nArtifacts:\n" + "\n".join(f"  - {a}" for a in self.artifacts)
        sup_str = f"\nSupervisor: {self.supervisor_result}" if self.supervisor_result else ""
        return (
            f"{emoji} [TaskCompleted] {self.source_role} → PM\n"
            f"Task: {self.task_id} ({self.task_name})\n"
            f"Status: {self.status}"
            f"{artifacts_str}"
            f"{sup_str}"
        )


@dataclass
class SupervisorTriggeredEvent:
    task_id: str
    source_role: str
    output_dir: str
    skill_dir: str

    def to_telegram(self) -> str:
        return (
            f"🔍 [SupervisorTriggered] {self.source_role}\n"
            f"Task: {self.task_id}\n"
            f"Output: {self.output_dir}\n"
            f"Skill: {self.skill_dir}"
        )


@dataclass
class SupervisorCompletedEvent:
    task_id: str
    source_role: str
    passed: int
    total: int
    failures: list = field(default_factory=list)

    @property
    def pass_rate(self) -> float:
        return (self.passed / self.total * 100) if self.total > 0 else 0

    @property
    def is_pass(self) -> bool:
        return self.passed == self.total

    def to_telegram(self) -> str:
        emoji = "✅" if self.is_pass else "⚠️"
        result = f"{self.passed}/{self.total} ({self.pass_rate:.0f}%)"
        msg = (
            f"{emoji} [SupervisorCompleted] {self.source_role}\n"
            f"Task: {self.task_id}\n"
            f"Result: {result}"
        )
        if self.failures:
            msg += "\nFailures:\n" + "\n".join(f"  - {f}" for f in self.failures[:5])
            if len(self.failures) > 5:
                msg += f"\n  ... and {len(self.failures) - 5} more"
        return msg


@dataclass
class PhaseUpdateEvent:
    task_id: str
    source_role: str
    phase: int
    phase_name: str
    message: str = ""

    def to_telegram(self) -> str:
        return (
            f"⚙️ [{self.source_role}] Phase {self.phase}: {self.phase_name}\n"
            f"Task: {self.task_id}"
            + (f"\n{self.message}" if self.message else "")
        )


# ── Message Parsing ──

# Pattern: emoji [EventType] ...
_EVENT_PATTERN = re.compile(r"^.?\s*\[(\w+)\]")
_TASK_ID_PATTERN = re.compile(r"Task:\s*([\w-]+)")
_STATUS_PATTERN = re.compile(r"Status:\s*(\w+)")
_SKILL_PATTERN = re.compile(r"Skill:\s*([\w-]+)")
_SOURCE_TARGET_PATTERN = re.compile(r"\[(\w+)\]\s+(\w+)\s*→\s*(\w+)")


def parse_event_type(text: str) -> Optional[EventType]:
    """Extract event type from a Telegram message."""
    m = _EVENT_PATTERN.search(text)
    if not m:
        return None
    try:
        return EventType(m.group(1))
    except ValueError:
        return None


def parse_task_triggered(text: str) -> Optional[TaskTriggeredEvent]:
    """Parse a TaskTriggered message."""
    task_match = _TASK_ID_PATTERN.search(text)
    skill_match = _SKILL_PATTERN.search(text)
    st_match = _SOURCE_TARGET_PATTERN.search(text)
    if not task_match:
        return None

    # Extract task name from "Task: ID (Name)"
    name_match = re.search(r"Task:\s*[\w-]+\s*\(([^)]+)\)", text)
    task_name = name_match.group(1) if name_match else ""

    return TaskTriggeredEvent(
        task_id=task_match.group(1),
        task_name=task_name,
        skill_dir=skill_match.group(1) if skill_match else "",
        source_role=st_match.group(2) if st_match else "",
        target_role=st_match.group(3) if st_match else "",
    )


def parse_task_completed(text: str) -> Optional[TaskCompletedEvent]:
    """Parse a TaskCompleted message."""
    task_match = _TASK_ID_PATTERN.search(text)
    status_match = _STATUS_PATTERN.search(text)
    st_match = _SOURCE_TARGET_PATTERN.search(text)
    if not task_match:
        return None

    name_match = re.search(r"Task:\s*[\w-]+\s*\(([^)]+)\)", text)

    return TaskCompletedEvent(
        task_id=task_match.group(1),
        task_name=name_match.group(1) if name_match else "",
        source_role=st_match.group(2) if st_match else "",
        status=status_match.group(1) if status_match else "UNKNOWN",
    )


def is_event_message(text: str) -> bool:
    """Check if a message is a structured event message."""
    return parse_event_type(text) is not None
