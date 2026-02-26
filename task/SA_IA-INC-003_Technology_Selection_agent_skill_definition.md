
# Create an AI Agent Skill for Completing the Technology Selection Task — Specification
# Role: System Architect (SA) | Task ID: IA-INC-003 | Task Name: Technology Selection
# Description: Recommending technology stacks, platforms, and frameworks aligned with project goals.

# Basic Requirements:
- First, collect what trigger mechanisms a qualified AI Agent for completing the Technology Selection task should have, then produce a configuration file that supports future modifications;
- Second, collect the RACI matrix for a qualified AI Agent completing the Technology Selection task — the RACI matrix must include role names and corresponding task names, then produce a configuration file. Purpose 1: so the AI Agent knows all stakeholders upon startup. Purpose 2: upon task completion, send this RACI matrix to the Project Manager AI Agent to trigger downstream tasks. Support future modifications;
- Third, collect what skills a qualified AI Agent for completing the Technology Selection task should possess, then produce a configuration file so the AI Agent knows its competencies upon startup. Support future modifications;
- Fourth, collect what knowledge domains a qualified AI Agent for completing the Technology Selection task should possess, then produce a knowledge base checklist so the AI Agent knows its required knowledge upon startup. Support future modifications;
- Fifth, collect what tools a qualified AI Agent for completing the Technology Selection task should use, then produce a tools checklist so the AI Agent knows its available tools upon startup. Support future modifications;
- Sixth, collect what MCP tools a qualified AI Agent for completing the Technology Selection task should use, then produce an MCP tools checklist so the AI Agent knows what MCP integrations to invoke upon startup. Support future modifications;
- Seventh, collect what output content list a qualified AI Agent for completing the Technology Selection task should produce, and create a template for each output item, so the AI Agent knows its output content list and templates upon startup and follows them strictly. Support future modifications;
- Eighth, collect the SOP process a qualified AI Agent for completing the Technology Selection task should follow, then produce an SOP process checklist so the AI Agent knows its operating procedure upon startup. Support future modifications;
- Ninth, collect the quality gates (DoD) a qualified AI Agent for completing the Technology Selection task should satisfy, then produce a DoD checklist so the AI Agent knows the quality thresholds upon startup. Support future modifications;
- Tenth, collect the Definition of Ready (DoR) a qualified AI Agent for completing the Technology Selection task should satisfy before activation, then produce a DoR checklist so the AI Agent knows its readiness prerequisites upon startup. Support future modifications;
- Eleventh, the AI Agent must record every user conversation, logged question by question in a document;
- Twelfth, the AI Agent must record its own work log, logged entry by entry on a timeline in a document;
- Thirteenth, the AI Agent must verify against the DoD checklist whether the task is complete; if any item fails, return to fix it, repeating until all items pass;
- Fourteenth, **[Supervisor AI Agent Skill Specification]** — produce an independent **Supervisor AI Agent Skill (Technology Selection Supervisor Agent)** for this task, responsible for end-to-end quality monitoring and closed-loop remediation of the Technology Selection AI Agent output. Specification as follows:

  ---

  ### 14.1 Role Definition
  - **Skill Name**: `SA-technology-selection-supervisor`
  - **Role**: Quality Supervisor — operates independently from the Technology Selection Agent; does not participate in the technology selection, only reviews and provides feedback.
  - **Trigger Timing**: Automatically triggered after the Technology Selection AI Agent completes one round of output.
  - **Operating Mechanism**: Upon activation, this Skill automatically inspects the Technology Selection AI Agent output and generates an inspection report.

  ---

  ### 14.2 Supervision Scope (Inspection Checklist)
  The Supervisor AI Agent inspects **items 1 through 13** above, verifying each has been fully executed:

  | Check Item | Verification Content |
  | :--- | :--- |
  | ✅ Item 1 | Trigger mechanism configuration file has been generated |
  | ✅ Item 2 | RACI matrix configuration file has been generated (with role names + task names) |
  | ✅ Item 3 | Skills list configuration file has been generated |
  | ✅ Item 4 | Knowledge base checklist has been generated |
  | ✅ Item 5 | Tools list has been generated |
  | ✅ Item 6 | MCP tools list has been generated |
  | ✅ Item 7 | Output content list and templates have been generated |
  | ✅ Item 8 | SOP process checklist has been generated |
  | ✅ Item 9 | DoD quality gates checklist has been generated |
  | ✅ Item 10 | DoR checklist has been generated |
  | ✅ Item 11 | User conversation log document exists (logged question by question) |
  | ✅ Item 12 | AI Agent work log document exists (logged entry by entry on timeline) |
  | ✅ Item 13 | DoD verification has passed with completed auto-remediation closed loop |

  ---

  ### 14.3 Inspection Process (Closed-Loop Mechanism)

  ```
  [Trigger] Technology Selection Agent completes output
       ↓
  [Inspect] Technology Selection Supervisor Agent verifies items 1 through 13
       ↓
  [Generate Report] Output inspection report (see 14.4)
       ↓
  [Decide] Report pass rate = 100%?
       ├── No → Return report to Technology Selection Agent for item-by-item remediation
       │         Agent completes fixes, then re-triggers Supervisor Agent
       │         (repeat this loop until 100% pass)
       └── Yes → Invoke Project Manager AI Agent, submit completion report
  ```

  ---

  ### 14.4 Inspection Report Format

  After each inspection round, generate a structured report in the following format:

  ```markdown
  # Technology Selection Supervisor Inspection Report

  - Inspection Time: {timestamp}
  - Inspection Round: #{N}
  - Technology Selection Report File Path: {file_path}

  ## Inspection Results Summary

  | Check Item | Status | Notes |
  | :--- | :---: | :--- |
  | Item 1: Trigger Mechanism Config | ✅ PASS / ❌ FAIL | {notes} |
  | Item 2: RACI Matrix Config | ✅ PASS / ❌ FAIL | {notes} |
  | ... | ... | ... |

  ## Overall Pass Rate: {X}% ({M}/{N} items passed)

  ## Issues Requiring Remediation
  1. {issue_description} — Suggested fix: {suggestion}
  2. ...

  ## Conclusion: [FAIL → Return for remediation | PASS → Invoke Project Manager AI Agent]
  ```

  ---

  ### 14.5 Post-Completion: Invoke Project Manager AI Agent
  - When the report pass rate reaches **100%**, the Supervisor Agent performs the following:
    1. Generate the final inspection report (marked "ALL PASSED").
    2. Invoke the **Project Manager AI Agent**, sending:
       - Technology Selection report file path and filename
       - RACI matrix configuration (for PM Agent to trigger downstream tasks)
       - Final inspection report
- Fifteenth, upon task completion, notify the Project Manager AI Agent that the task is done, and send the Technology Selection report file path and filename to the Project Manager AI Agent. The PM Agent then uses the RACI matrix to invoke the corresponding AI Agents to complete downstream RACI tasks.

- Sixteenth, record every question list generated during each phase for future review.
- Seventeenth, when invoking tools for research, save the research process and results locally for future use.

# Functional Requirements: An interactive AI Agent is expected. The AI Agent receives the client's project or system information, referred to as the Topic.

- Step 1: The AI Agent first attempts to understand the purpose of this task — why a technology selection is needed, what the goals and scope of the evaluation are. It presents its understanding, then asks for user confirmation. If the user agrees, proceed to Step 2; if not, repeat Step 1 until full understanding is achieved;

- Step 2: The AI Agent attempts to understand the Topic itself — the business context, project requirements, existing technology stack, infrastructure constraints, team capabilities, and budget boundaries. It presents its understanding, then asks for user confirmation. If the user agrees, proceed to Step 3; if not, return to Step 1 until full understanding is achieved;

- Step 3: Based on the Topic, research on the internet and authoritative knowledge bases for information about this task. Report how the industry conducts technology selection, and generate a question list. Engage in iterative dialogue with the user based on this question list, helping gather the expected results — a validated requirements list.
- Step 4: Based on the validated requirements list, research on the internet and authoritative knowledge bases for relevant information. The AI Agent completes the task per the "Basic Requirements" above, and outputs content according to the requirements list and templates. Finally, save the output to the `technology-selection` directory under the parent directory.
