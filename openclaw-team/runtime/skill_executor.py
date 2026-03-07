"""
Skill Executor — Parses SKILL.md and executes Phase 0-5 in strict order.

Each phase interacts with the user via Telegram and uses the configured LLM for
research, Q&A generation, and deliverable production.

Phase 0: Initialization — create output dir, init logs, check DoR
Phase 1: Understand Task Purpose — present understanding, get user confirmation
Phase 2: Understand the Topic — deep-dive context, get user confirmation
Phase 3: Research & Q&A — Claude research + interactive Q&A with user
Phase 4: Execute & Deliver — produce deliverables, self-check DoD
Phase 5: Completion & Handoff — verify DoD, invoke supervisor, report
"""

import logging
from datetime import datetime
from pathlib import Path
from .telegram_bot import TelegramBot
from .llm_client import LLMClient
from .state_manager import StateManager
from .event_protocol import (
    PhaseUpdateEvent,
    SupervisorTriggeredEvent,
)

logger = logging.getLogger(__name__)


class SkillExecutor:
    """Executes a skill's Phase 0-5 workflow with Telegram user interaction."""

    def __init__(
        self,
        bot: TelegramBot,
        llm: LLMClient,
        state: StateManager,
        workspace_dir: str,
        skills_base_dir: str,
        role: str,
    ):
        self.bot = bot
        self.llm = llm
        self.state = state
        self.workspace_dir = Path(workspace_dir)
        self.skills_base_dir = Path(skills_base_dir)
        self.role = role.upper()

    async def execute(
        self,
        task_id: str,
        task_name: str,
        skill_dir_name: str,
        upstream_inputs: dict = None,
    ) -> dict:
        """Execute a skill end-to-end through Phase 0-5.

        Args:
            task_id: Task identifier (e.g., "IPM-INC-003").
            task_name: Human-readable task name.
            skill_dir_name: Skill directory name (e.g., "ipm-brd-writing").
            upstream_inputs: Dict of upstream task outputs to incorporate.

        Returns:
            Dict with keys: status, artifacts, supervisor_result.
        """
        skill_dir = self.skills_base_dir / skill_dir_name
        output_dir = self.workspace_dir / "outputs" / task_id

        if not skill_dir.exists():
            await self.bot.send_to_group(
                f"❌ [{self.role}] Skill directory not found: {skill_dir_name}"
            )
            return {"status": "FAILED", "artifacts": [], "supervisor_result": ""}

        # Build system prompt from SKILL.md + references
        system_prompt = LLMClient.build_system_prompt(
            str(skill_dir), str(self.workspace_dir)
        )

        # Track conversation for Claude context
        messages = []

        self.state.start_task(task_id)

        try:
            # ── Phase 0: Initialization ──
            await self._phase0(task_id, task_name, skill_dir, output_dir)

            # ── Phase 1: Understand Task Purpose ──
            messages = await self._phase1(
                task_id, task_name, system_prompt, messages, output_dir
            )

            # ── Phase 2: Understand the Topic ──
            messages = await self._phase2(
                task_id, task_name, system_prompt, messages,
                output_dir, upstream_inputs
            )

            # ── Phase 3: Research & Q&A ──
            messages = await self._phase3(
                task_id, task_name, system_prompt, messages, output_dir
            )

            # ── Phase 4: Execute & Deliver ──
            messages = await self._phase4(
                task_id, task_name, system_prompt, messages,
                skill_dir, output_dir
            )

            # ── Phase 5: Completion & Handoff ──
            result = await self._phase5(
                task_id, task_name, system_prompt, messages,
                skill_dir, output_dir
            )

            self.state.complete_task(task_id, result.get("artifacts", []))
            return result

        except TimeoutError as e:
            logger.error(f"[{self.role}] Timeout in {task_id}: {e}")
            await self.bot.send_to_group(
                f"⏰ [{self.role}] Task {task_id} timed out waiting for user input."
            )
            self.state.fail_task(task_id, str(e))
            return {"status": "FAILED", "artifacts": [], "supervisor_result": ""}

        except Exception as e:
            logger.error(f"[{self.role}] Error in {task_id}: {e}", exc_info=True)
            await self.bot.send_to_group(
                f"❌ [{self.role}] Task {task_id} failed: {e}"
            )
            self.state.fail_task(task_id, str(e))
            return {"status": "FAILED", "artifacts": [], "supervisor_result": ""}

    # ══════════════════════════════════════════════════════════════
    # Phase Implementations
    # ══════════════════════════════════════════════════════════════

    async def _phase0(self, task_id, task_name, skill_dir, output_dir):
        """Phase 0: Initialization — create output dir, init logs, check DoR."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=0, phase_name="Initialization",
            message=f"Setting up {task_name}..."
        ))

        output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize log files
        now = datetime.now().isoformat()
        for log_name in ["conversation-log.md", "work-log.md",
                         "question-lists.md", "research-log.md"]:
            log_file = output_dir / log_name
            if not log_file.exists():
                log_file.write_text(
                    f"# {log_name.replace('.md', '').replace('-', ' ').title()}\n\n"
                    f"Task: {task_id} — {task_name}\n"
                    f"Created: {now}\n\n---\n\n",
                    encoding="utf-8"
                )

        # Check DoR
        dor_file = skill_dir / "references" / "dor.md"
        if dor_file.exists():
            self._append_log(output_dir / "work-log.md",
                             f"[{now}] Phase 0: DoR checked — {dor_file.name}")

        self._append_log(output_dir / "work-log.md",
                         f"[{now}] Phase 0: Initialization complete")

    async def _phase1(self, task_id, task_name, system_prompt, messages, output_dir):
        """Phase 1: Understand Task Purpose — clarify why this task is needed."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=1, phase_name="Understand Task Purpose"
        ))

        # Ask Claude to summarize the task purpose
        messages.append({
            "role": "user",
            "content": (
                f"You are starting task {task_id}: {task_name}.\n\n"
                "Phase 1: Analyze and summarize WHY this task is needed. "
                "What is its purpose in the project lifecycle? "
                "Provide a clear, concise summary (2-3 paragraphs) that I can "
                "present to the user for confirmation."
            )
        })

        purpose_summary = self.llm.chat(system_prompt, messages)
        messages.append({"role": "assistant", "content": purpose_summary})

        # Present to user and get confirmation
        confirmed = False
        while not confirmed:
            reply = await self.bot.wait_for_user_reply(
                f"💬 [{self.role}] Phase 1 — Task Purpose\n\n{purpose_summary}\n\n"
                f"Does this correctly describe the purpose of this task? "
                f"(Reply 'yes' to confirm, or provide corrections)"
            )

            if reply.strip().lower() in ("yes", "y", "ok", "confirm", "确认", "是", "对"):
                confirmed = True
                await self.bot.send_to_group(f"✅ [{self.role}] Phase 1 confirmed.")
            else:
                # User provided corrections — refine
                messages.append({
                    "role": "user",
                    "content": f"The user provided corrections: {reply}\n\n"
                               "Please revise your understanding based on this feedback."
                })
                purpose_summary = self.llm.chat(system_prompt, messages)
                messages.append({"role": "assistant", "content": purpose_summary})

        self._append_log(
            output_dir / "conversation-log.md",
            f"## Phase 1: Task Purpose\n\n{purpose_summary}\n\n"
            f"**User Confirmation**: Confirmed\n"
        )
        return messages

    async def _phase2(self, task_id, task_name, system_prompt, messages,
                       output_dir, upstream_inputs):
        """Phase 2: Understand the Topic — deep-dive into context."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=2, phase_name="Understand the Topic"
        ))

        # Include upstream inputs in context
        upstream_context = ""
        if upstream_inputs:
            parts = []
            for key, value in upstream_inputs.items():
                parts.append(f"### {key}\n{value}")
            upstream_context = (
                "\n\nUpstream task outputs to incorporate:\n\n" +
                "\n\n".join(parts)
            )

        messages.append({
            "role": "user",
            "content": (
                f"Phase 2: Deep-dive into the topic for {task_id}: {task_name}.\n"
                "Analyze WHO, WHAT, WHY, WHEN, WHERE, HOW.\n"
                "Provide a structured topic analysis (use headers and bullet points)."
                f"{upstream_context}"
            )
        })

        topic_analysis = self.llm.chat(system_prompt, messages)
        messages.append({"role": "assistant", "content": topic_analysis})

        # Present to user and get confirmation
        confirmed = False
        while not confirmed:
            reply = await self.bot.wait_for_user_reply(
                f"💬 [{self.role}] Phase 2 — Topic Understanding\n\n{topic_analysis}\n\n"
                f"Is this analysis correct? (Reply 'yes' to confirm, or provide corrections)"
            )

            if reply.strip().lower() in ("yes", "y", "ok", "confirm", "确认", "是", "对"):
                confirmed = True
                await self.bot.send_to_group(f"✅ [{self.role}] Phase 2 confirmed.")
            else:
                messages.append({
                    "role": "user",
                    "content": f"User corrections: {reply}\nPlease revise your analysis."
                })
                topic_analysis = self.llm.chat(system_prompt, messages)
                messages.append({"role": "assistant", "content": topic_analysis})

        self._append_log(
            output_dir / "conversation-log.md",
            f"## Phase 2: Topic Understanding\n\n{topic_analysis}\n\n"
            f"**User Confirmation**: Confirmed\n"
        )
        return messages

    async def _phase3(self, task_id, task_name, system_prompt, messages, output_dir):
        """Phase 3: Research & Q&A — conduct research and interactive Q&A."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=3, phase_name="Research & Q&A"
        ))

        # Ask Claude to generate research findings and questions
        messages.append({
            "role": "user",
            "content": (
                "Phase 3: Based on your understanding from Phases 1-2, "
                "generate a list of critical questions that need to be answered "
                "to complete this task successfully. "
                "Format as a numbered list. Focus on information gaps."
            )
        })

        questions_text = self.llm.chat(system_prompt, messages)
        messages.append({"role": "assistant", "content": questions_text})

        # Log research
        self._append_log(output_dir / "research-log.md",
                         f"## Phase 3 Research\n\n{questions_text}\n")

        # Interactive Q&A with user
        await self.bot.send_to_group(
            f"💬 [{self.role}] Phase 3 — I have questions for you.\n"
            f"I'll ask them one at a time. Let's begin."
        )

        # Ask Claude to conduct the Q&A interactively
        messages.append({
            "role": "user",
            "content": (
                "Now ask the user your most important question. "
                "Ask ONE question at a time. Be specific and clear."
            )
        })

        qa_rounds = 0
        max_rounds = 10

        while qa_rounds < max_rounds:
            question = self.llm.chat(system_prompt, messages)
            messages.append({"role": "assistant", "content": question})

            # Check if Claude indicates all questions answered
            if any(phrase in question.lower() for phrase in [
                "all questions answered", "no more questions",
                "sufficient information", "ready to proceed",
                "move to phase 4", "we have enough"
            ]):
                await self.bot.send_to_group(
                    f"✅ [{self.role}] Phase 3 — All questions answered. "
                    f"Moving to Phase 4."
                )
                break

            # Ask user
            user_answer = await self.bot.wait_for_user_reply(
                f"❓ [{self.role}] Q{qa_rounds + 1}:\n\n{question}"
            )

            messages.append({
                "role": "user",
                "content": (
                    f"User's answer: {user_answer}\n\n"
                    "If you have more questions, ask the next one. "
                    "If you have enough information, say 'All questions answered, "
                    "ready to proceed to Phase 4.'"
                )
            })

            self._append_log(
                output_dir / "question-lists.md",
                f"### Q{qa_rounds + 1}\n**Q:** {question}\n**A:** {user_answer}\n\n"
            )

            qa_rounds += 1

        self._append_log(
            output_dir / "conversation-log.md",
            f"## Phase 3: Research & Q&A\n\nCompleted {qa_rounds} Q&A rounds.\n"
        )
        return messages

    async def _phase4(self, task_id, task_name, system_prompt, messages,
                       skill_dir, output_dir):
        """Phase 4: Execute & Deliver — produce deliverables using templates."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=4, phase_name="Execute & Deliver",
            message="Generating deliverables..."
        ))

        # Read output template if available
        template_file = skill_dir / "references" / "output-templates.md"
        template_context = ""
        if template_file.exists():
            template_context = (
                f"\n\nUse this template structure:\n\n"
                f"{template_file.read_text(encoding='utf-8')}"
            )

        # Read DoD for self-check
        dod_file = skill_dir / "references" / "dod.md"
        dod_context = ""
        if dod_file.exists():
            dod_context = (
                f"\n\nSelf-check against these DoD criteria:\n\n"
                f"{dod_file.read_text(encoding='utf-8')}"
            )

        messages.append({
            "role": "user",
            "content": (
                f"Phase 4: Now produce the deliverable for {task_id}: {task_name}.\n"
                "Use all information gathered in Phases 1-3.\n"
                "Follow the template structure exactly.\n"
                "Write the Executive Summary LAST.\n"
                "Ensure NO TBD, TODO, or placeholder text remains."
                f"{template_context}"
                f"{dod_context}"
            )
        })

        deliverable = self.llm.chat(
            system_prompt, messages, max_tokens=MAX_TOKENS_LARGE
        )
        messages.append({"role": "assistant", "content": deliverable})

        # Save deliverable
        deliverable_file = output_dir / f"{task_id.lower()}-deliverable.md"
        deliverable_file.write_text(deliverable, encoding="utf-8")

        await self.bot.send_to_group(
            f"📄 [{self.role}] Phase 4 — Deliverable generated.\n"
            f"File: {deliverable_file.name}\n"
            f"Size: {len(deliverable)} chars"
        )

        self._append_log(
            output_dir / "work-log.md",
            f"[{datetime.now().isoformat()}] Phase 4: Deliverable saved to "
            f"{deliverable_file.name}"
        )

        return messages

    async def _phase5(self, task_id, task_name, system_prompt, messages,
                       skill_dir, output_dir):
        """Phase 5: Completion & Handoff — verify DoD, invoke supervisor."""
        await self.bot.send_event(PhaseUpdateEvent(
            task_id=task_id, source_role=self.role,
            phase=5, phase_name="Completion & Handoff",
            message="Running DoD self-check..."
        ))

        # DoD self-verification
        dod_file = skill_dir / "references" / "dod.md"
        if dod_file.exists():
            messages.append({
                "role": "user",
                "content": (
                    "Phase 5: Verify the deliverable against ALL DoD criteria.\n"
                    "List each criterion and whether it PASSES or FAILS.\n"
                    "If any critical/high items fail, list what needs fixing."
                )
            })
            dod_check = self.llm.chat(system_prompt, messages)
            messages.append({"role": "assistant", "content": dod_check})

            self._append_log(
                output_dir / "work-log.md",
                f"[{datetime.now().isoformat()}] Phase 5: DoD self-check completed"
            )

        # Collect artifacts
        artifacts = [str(f.relative_to(output_dir.parent.parent))
                     for f in output_dir.iterdir() if f.is_file()]

        # Trigger supervisor
        supervisor_dir_name = f"{skill_dir.name}-supervisor"
        supervisor_dir = skill_dir.parent / supervisor_dir_name

        supervisor_result = ""
        if supervisor_dir.exists():
            await self.bot.send_event(SupervisorTriggeredEvent(
                task_id=task_id,
                source_role=self.role,
                output_dir=str(output_dir),
                skill_dir=str(skill_dir),
            ))

            # Run supervisor via Claude
            from .supervisor_runner import SupervisorRunner
            runner = SupervisorRunner(self.llm, self.bot, self.role)
            sup_result = await runner.run(
                task_id=task_id,
                supervisor_dir=str(supervisor_dir),
                skill_dir=str(skill_dir),
                output_dir=str(output_dir),
            )

            supervisor_result = (
                f"{sup_result['passed']}/{sup_result['total']} "
                f"({sup_result['pass_rate']:.0f}%)"
            )

            if not sup_result["is_pass"]:
                await self.bot.send_to_group(
                    f"⚠️ [{self.role}] Supervisor found issues. Remediating..."
                )
                # Remediation loop (max 2 attempts)
                for attempt in range(2):
                    messages.append({
                        "role": "user",
                        "content": (
                            f"The supervisor found these failures:\n"
                            f"{chr(10).join(sup_result['failures'])}\n\n"
                            "Fix these issues in the deliverable and regenerate."
                        )
                    })
                    fix = self.llm.chat(system_prompt, messages, max_tokens=MAX_TOKENS_LARGE)
                    messages.append({"role": "assistant", "content": fix})

                    # Save fixed deliverable
                    deliverable_file = output_dir / f"{task_id.lower()}-deliverable.md"
                    deliverable_file.write_text(fix, encoding="utf-8")

                    # Re-run supervisor
                    sup_result = await runner.run(
                        task_id=task_id,
                        supervisor_dir=str(supervisor_dir),
                        skill_dir=str(skill_dir),
                        output_dir=str(output_dir),
                    )
                    supervisor_result = (
                        f"{sup_result['passed']}/{sup_result['total']} "
                        f"({sup_result['pass_rate']:.0f}%)"
                    )
                    if sup_result["is_pass"]:
                        break
        else:
            supervisor_result = "No supervisor found"

        # Notify user
        await self.bot.send_to_group(
            f"✅ [{self.role}] Task {task_id} ({task_name}) completed.\n"
            f"Supervisor: {supervisor_result}\n"
            f"Artifacts: {len(artifacts)} files"
        )

        return {
            "status": "DONE",
            "artifacts": artifacts,
            "supervisor_result": supervisor_result,
        }

    # ── Helpers ──

    @staticmethod
    def _append_log(log_file: Path, entry: str):
        """Append an entry to a log file."""
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{entry}\n")


# Large token limit for deliverable generation
MAX_TOKENS_LARGE = 32768
