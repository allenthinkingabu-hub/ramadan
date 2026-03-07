"""
Supervisor Runner — Executes supervisor inspection via Claude.

Reads the supervisor's SKILL.md + inspection-criteria.md, sends
the deliverable to Claude for independent quality review, and
returns structured pass/fail results.
"""

import logging
from pathlib import Path

from .llm_client import LLMClient
from .telegram_bot import TelegramBot
from .event_protocol import SupervisorCompletedEvent

logger = logging.getLogger(__name__)


class SupervisorRunner:
    """Runs supervisor inspection using Claude to evaluate deliverables."""

    def __init__(self, llm: LLMClient, bot: TelegramBot, role: str):
        self.llm = llm
        self.bot = bot
        self.role = role.upper()

    async def run(
        self,
        task_id: str,
        supervisor_dir: str,
        skill_dir: str,
        output_dir: str,
    ) -> dict:
        """Run supervisor inspection on task deliverables.

        Args:
            task_id: The task being inspected.
            supervisor_dir: Path to the supervisor skill directory.
            skill_dir: Path to the main skill directory (for reference files).
            output_dir: Path to the task output directory.

        Returns:
            Dict with keys: passed, total, pass_rate, is_pass, failures.
        """
        sup_path = Path(supervisor_dir)
        out_path = Path(output_dir)
        main_skill_path = Path(skill_dir)

        # Build supervisor system prompt
        system_prompt = LLMClient.build_supervisor_prompt(supervisor_dir)

        # Gather all artifacts for inspection
        artifacts_content = self._gather_artifacts(out_path)

        # Gather reference files from main skill
        references_content = self._gather_references(main_skill_path)

        # Build inspection request
        messages = [{
            "role": "user",
            "content": (
                f"You are the supervisor for task {task_id}.\n\n"
                f"## Deliverables to Inspect\n\n{artifacts_content}\n\n"
                f"## Reference Files\n\n{references_content}\n\n"
                "## Instructions\n\n"
                "Execute your full inspection checklist. For EACH check item:\n"
                "1. State the check ID and name\n"
                "2. State PASS or FAIL\n"
                "3. If FAIL, explain what is missing or incorrect\n\n"
                "At the end, provide a summary:\n"
                "- Total checks: N\n"
                "- Passed: N\n"
                "- Failed: N\n"
                "- Pass rate: N%\n"
                "- List of failed check IDs"
            )
        }]

        response = self.llm.chat(system_prompt, messages)

        # Parse results from Claude's response
        result = self._parse_inspection_result(response)

        # Send supervisor completed event
        await self.bot.send_event(SupervisorCompletedEvent(
            task_id=task_id,
            source_role=self.role,
            passed=result["passed"],
            total=result["total"],
            failures=result["failures"],
        ))

        return result

    def _gather_artifacts(self, output_dir: Path) -> str:
        """Read all files in the output directory."""
        parts = []
        if not output_dir.exists():
            return "(No output directory found)"

        for f in sorted(output_dir.iterdir()):
            if f.is_file() and f.suffix in (".md", ".txt", ".json"):
                content = f.read_text(encoding="utf-8")
                # Truncate very large files
                if len(content) > 20000:
                    content = content[:20000] + "\n\n... (truncated)"
                parts.append(f"### {f.name}\n\n{content}")

        return "\n\n---\n\n".join(parts) if parts else "(No artifacts found)"

    def _gather_references(self, skill_dir: Path) -> str:
        """Read reference files from the main skill directory."""
        refs_dir = skill_dir / "references"
        if not refs_dir.exists():
            return "(No references directory)"

        parts = []
        for f in sorted(refs_dir.iterdir()):
            if f.is_file() and f.suffix == ".md":
                content = f.read_text(encoding="utf-8")
                parts.append(f"### {f.name}\n\n{content}")

        return "\n\n---\n\n".join(parts) if parts else "(No reference files)"

    def _parse_inspection_result(self, response: str) -> dict:
        """Parse Claude's inspection response into structured results.

        Looks for patterns like:
        - "Total checks: 17" / "Passed: 15" / "Failed: 2"
        - "FAIL" mentions for individual checks
        """
        import re

        # Try to extract summary numbers
        total_match = re.search(r"Total\s*(?:checks)?:\s*(\d+)", response, re.I)
        passed_match = re.search(r"Passed:\s*(\d+)", response, re.I)
        failed_match = re.search(r"Failed:\s*(\d+)", response, re.I)

        # Extract individual failures
        failures = []
        fail_pattern = re.compile(
            r"((?:INS|INS-\w+)[-\s]*\d+[^\n]*?):\s*FAIL", re.I
        )
        for m in fail_pattern.finditer(response):
            failures.append(m.group(1).strip())

        # Also catch "FAIL" lines with check IDs
        fail_line_pattern = re.compile(
            r"(INS[-\w]*\d+)[^\n]*?(?:FAIL|❌)", re.I
        )
        for m in fail_line_pattern.finditer(response):
            check_id = m.group(1).strip()
            if check_id not in failures:
                failures.append(check_id)

        if total_match and passed_match:
            total = int(total_match.group(1))
            passed = int(passed_match.group(1))
        elif total_match and failed_match:
            total = int(total_match.group(1))
            passed = total - int(failed_match.group(1))
        else:
            # Fallback: count PASS/FAIL occurrences
            pass_count = len(re.findall(r"\bPASS\b", response))
            fail_count = len(re.findall(r"\bFAIL\b", response))
            total = pass_count + fail_count
            passed = pass_count

        total = max(total, 1)  # Avoid division by zero
        pass_rate = (passed / total) * 100

        return {
            "passed": passed,
            "total": total,
            "pass_rate": pass_rate,
            "is_pass": passed == total,
            "failures": failures,
        }
