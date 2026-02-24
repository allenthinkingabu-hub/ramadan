# BRD Writer Agent - Standard Operating Procedure (SOP)

## Overview

This SOP defines the step-by-step process the BRD Writer AI Agent follows from receiving a topic to delivering a complete BRD. Each phase must be completed before proceeding to the next.

---

## Phase 1: Task Understanding & Confirmation

**Goal**: Ensure the agent fully understands the task purpose before proceeding.

| Step | Action | Output |
|------|--------|--------|
| 1.1 | Receive the topic/business problem from user | Raw topic recorded |
| 1.2 | Analyze and summarize understanding of the **task purpose** | Task purpose summary |
| 1.3 | Present understanding to user and ask for confirmation | User confirmation |
| 1.4 | If user disagrees → return to 1.2 and re-analyze | Revised understanding |
| 1.5 | If user agrees → proceed to Phase 2 | Confirmed task purpose |

**Log**: Record all exchanges in conversation log (question-by-question).

---

## Phase 2: Topic Understanding & Confirmation

**Goal**: Ensure the agent deeply understands the specific topic/business problem.

| Step | Action | Output |
|------|--------|--------|
| 2.1 | Analyze the topic in depth (who, what, why, when, where, how) | Topic analysis |
| 2.2 | Present understanding of the topic to user | Topic summary |
| 2.3 | Ask user for confirmation | User confirmation |
| 2.4 | If user disagrees → return to 2.1, refine understanding | Revised topic analysis |
| 2.5 | If user agrees → proceed to Phase 3 | Confirmed topic understanding |

**Log**: Record all exchanges in conversation log.

---

## Phase 3: Research & Requirements Elicitation

**Goal**: Gather comprehensive information to build a real requirements list.

| Step | Action | Output |
|------|--------|--------|
| 3.1 | Research the topic on the internet and authoritative knowledge bases | Research findings |
| 3.2 | **Save research process and results to `research-log.md`** (tool, query, findings, sources) | Research log entry |
| 3.3 | Analyze how this is done in the industry (best practices, benchmarks) | Industry analysis |
| 3.4 | Generate a structured question list based on research and topic | Question list |
| 3.5 | **Save the question list to `question-lists.md`** for future review | Question list logged |
| 3.6 | Present industry findings and question list to user | Presented findings |
| 3.7 | Conduct interactive Q&A with user (one question at a time or grouped) | Q&A responses |
| 3.8 | Iterate on questions until all critical information is gathered | Complete Q&A |
| 3.9 | **Save each round's question list and answered summaries to `question-lists.md`** | Updated question lists log |
| 3.10 | Consolidate answers into a validated requirements list | Requirements list |
| 3.11 | Present requirements list to user for confirmation | User confirmation |
| 3.12 | If user has changes → revise and re-confirm | Revised requirements |
| 3.13 | If user agrees → proceed to Phase 4 | Confirmed requirements list |

**Log**: Record all Q&A exchanges in conversation log. Record all research in research log. Record all question lists in question lists log.

---

## Phase 4: BRD Drafting

**Goal**: Produce a complete BRD document following the output template.

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Read the BRD output template (`references/brd-output-template.md`) | Template loaded |
| 4.2 | Read the DoD checklist (`references/dod-checklist.yaml`) | DoD loaded |
| 4.3 | Research additional details as needed for specific sections — **log all research to `research-log.md`** | Supplemental research |
| 4.4 | Draft all BRD sections following the template structure | BRD draft v0.1 |
| 4.5 | Write Executive Summary last (summarizes entire document) | Executive Summary |
| 4.6 | Self-review against DoD checklist | Self-review notes |
| 4.7 | Fix any issues found in self-review | BRD draft v1.0 |
| 4.8 | Save BRD to the designated output location | Saved BRD file |

**Log**: Record all actions in work log with timestamps.

---

## Phase 5: Quality Verification (DoD Check)

**Goal**: Verify the BRD meets all quality gates defined in the DoD.

| Step | Action | Output |
|------|--------|--------|
| 5.1 | Load DoD checklist (`references/dod-checklist.yaml`) | DoD criteria loaded |
| 5.2 | Check each completeness criterion | Completeness results |
| 5.3 | Check each requirement quality criterion | Quality results |
| 5.4 | Check each document quality criterion | Document results |
| 5.5 | Check each process quality criterion | Process results |
| 5.6 | Generate DoD verification report | DoD report |
| 5.7 | If any critical/high items fail → return to Phase 4 to fix | Fixes applied |
| 5.8 | Repeat 5.1–5.7 until all checks pass | All checks passed |

**Log**: Record verification results in work log.

---

## Phase 6: Handoff & Completion

**Goal**: Deliver the BRD and notify downstream agents.

| Step | Action | Output |
|------|--------|--------|
| 6.1 | Save final BRD document to output directory | Final BRD file |
| 6.2 | Generate completion summary for user | Completion summary |
| 6.3 | Signal BRD Supervisor Agent for independent review | Signal sent |
| 6.4 | If supervisor returns issues → fix and re-submit | Fixes applied |
| 6.5 | Once supervisor approves → notify Project Manager Agent | PM notification |
| 6.6 | Send PM the BRD file path, RACI matrix, and final report | Handoff package |

**Log**: Record handoff actions in work log.

---

## Logging Requirements

### Conversation Log
- Record every user interaction as an individual entry
- Format: `[Question #{N}] {timestamp} — User: {question/response} | Agent: {question/response}`
- Store in the output directory as `conversation-log.md`

### Work Log
- Record every agent action on a timeline
- Format: `[{timestamp}] {action_description} — Status: {completed/in-progress/failed}`
- Store in the output directory as `work-log.md`

### Question Lists Log
- Record every question list generated during each phase for future review
- Format: `## Phase {N}: {phase_name} — {timestamp}` followed by numbered questions and answered summaries
- Store in the output directory as `question-lists.md`
- Capture question lists from all phases (Task Understanding, Topic Understanding, Research & Elicitation)

### Research Log
- Record every research action: tool invoked, search query/URL, purpose, key findings, and source
- Format: `## Research #{seq} — {timestamp}` with structured fields (Tool, Query/URL, Purpose, Key Findings, Source)
- Store in the output directory as `research-log.md`
- Log every web search, Context7 query, web fetch, and other research tool invocations
