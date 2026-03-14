# Prompt 03 — Long-Term Memory Architecture & Utilization Protocol

## Context

You are continuing the creation of the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 3 of 5. Steps 1-2 have created the directory structure, config files, templates, SOP, DoD, and DoR.

## Scope

This prompt covers the **Long-Term Memory Architecture (Hybrid: Markdown + SQLite)** and the **Memory Utilization Protocol** — ensuring the agent has persistent memory across sessions and actively uses that memory to improve its behavior.

## Pre-requisites

Verify these exist before proceeding:
- `project-structure-scan/SKILL.md` (skeleton from prompt-01)
- `project-structure-scan/config/` (5 files from prompt-01)
- `project-structure-scan/templates/` (6 files from prompt-02)
- `project-structure-scan/references/` (4 files from prompt-02)
- `project-structure-scan/memory/` (empty directory)
- `project-structure-scan/scripts/` (empty directory)

If any are missing, STOP and report the issue.

## Instructions

### 1. Create scripts/init_memory.py

Create a Python script that initializes the SQLite memory database. Requirements:

- Accept an optional argument for the database path (default: `memory/agent_memory.db`)
- Create the database file if it does not exist
- Create 4 tables with the exact schemas below
- Be idempotent — safe to run multiple times without data loss (use `CREATE TABLE IF NOT EXISTS`)
- Print confirmation of tables created
- Include error handling

**Table Schemas**:

```sql
-- Task execution memory: records findings, decisions, and lessons per session
CREATE TABLE IF NOT EXISTS task_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    project_name TEXT,
    phase TEXT,
    memory_type TEXT NOT NULL CHECK(memory_type IN ('finding', 'decision', 'lesson', 'question', 'risk')),
    title TEXT,
    content TEXT NOT NULL,
    context TEXT,
    tags TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DoD check records
CREATE TABLE IF NOT EXISTS dod_checks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    check_round INTEGER NOT NULL,
    check_item TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pass', 'fail', 'pending')),
    evidence TEXT,
    notes TEXT,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-session knowledge base
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    category TEXT NOT NULL CHECK(category IN ('pattern', 'dependency', 'risk', 'insight', 'tech_stack', 'convention')),
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    confidence REAL DEFAULT 0.8 CHECK(confidence >= 0.0 AND confidence <= 1.0),
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scan history
CREATE TABLE IF NOT EXISTS scan_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    project_name TEXT NOT NULL,
    project_path TEXT NOT NULL,
    scan_scope TEXT CHECK(scan_scope IN ('full', 'partial', 'incremental')),
    status TEXT NOT NULL CHECK(status IN ('in_progress', 'completed', 'failed')),
    deliverables_path TEXT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
```

Add indexes for common query patterns:
```sql
CREATE INDEX IF NOT EXISTS idx_task_memory_project ON task_memory(project_name, task_id);
CREATE INDEX IF NOT EXISTS idx_task_memory_type ON task_memory(memory_type);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_project ON knowledge_base(project_name, category);
CREATE INDEX IF NOT EXISTS idx_scan_history_project ON scan_history(project_name);
CREATE INDEX IF NOT EXISTS idx_dod_checks_session ON dod_checks(session_id, task_id);
```

### 2. Create scripts/memory_ops.py

Create a Python library providing memory CRUD operations. The agent will call these functions during execution. Required functions:

```python
# --- Startup Operations ---

def load_project_history(db_path: str, project_name: str) -> dict:
    """Query scan_history for previous scans of this project.
    Returns: { 'scan_count': int, 'last_scan': dict|None, 'scans': list[dict] }"""

def load_project_knowledge(db_path: str, project_name: str) -> list[dict]:
    """Query knowledge_base for accumulated knowledge about this project.
    Returns entries sorted by confidence DESC."""

def load_lessons_learned(db_path: str, task_id: str, project_name: str = None) -> list[dict]:
    """Query task_memory for lessons learned.
    If project_name given, filter by project. Otherwise, return all lessons for this task_id."""

def generate_memory_summary(db_path: str, project_name: str) -> str:
    """Generate a human-readable markdown summary of all memory about this project.
    Used to present context to user on startup."""

# --- During Execution ---

def record_finding(db_path: str, session_id: str, task_id: str, project_name: str,
                   phase: str, title: str, content: str, context: str = None, tags: str = None):
    """Insert a finding into task_memory."""

def record_decision(db_path: str, session_id: str, task_id: str, project_name: str,
                    phase: str, title: str, content: str, context: str = None):
    """Insert a decision into task_memory."""

def record_question(db_path: str, session_id: str, task_id: str, project_name: str,
                    phase: str, title: str, content: str):
    """Insert a user Q&A exchange into task_memory."""

def record_risk(db_path: str, session_id: str, task_id: str, project_name: str,
                phase: str, title: str, content: str, context: str = None):
    """Insert a risk into task_memory."""

def record_knowledge(db_path: str, project_name: str, category: str, key: str,
                     value: str, confidence: float = 0.8, source: str = None):
    """Insert or update a knowledge_base entry. If key already exists for this project+category,
    update the value and confidence instead of inserting a duplicate."""

# --- On Completion ---

def start_scan(db_path: str, session_id: str, task_id: str, project_name: str,
               project_path: str, scan_scope: str = 'full') -> int:
    """Insert a new scan_history entry with status='in_progress'. Returns the scan ID."""

def complete_scan(db_path: str, scan_id: int, deliverables_path: str):
    """Update scan_history entry to status='completed' and set completed_at."""

def fail_scan(db_path: str, scan_id: int):
    """Update scan_history entry to status='failed' and set completed_at."""

def record_dod_check(db_path: str, session_id: str, task_id: str, check_round: int,
                     check_item: str, status: str, evidence: str = None, notes: str = None):
    """Insert a DoD check result."""

def record_lesson(db_path: str, session_id: str, task_id: str, project_name: str,
                  title: str, content: str):
    """Insert a lesson learned into task_memory."""

# --- Memory Maintenance ---

def apply_confidence_decay(db_path: str, days_threshold: int = 90, decay_amount: float = 0.2):
    """Reduce confidence by decay_amount for knowledge_base entries not updated in days_threshold days.
    Minimum confidence is 0.1."""

def detect_contradictions(db_path: str, project_name: str, category: str, key: str,
                          new_value: str) -> dict | None:
    """Check if a new value contradicts an existing knowledge_base entry.
    Returns the existing entry if a contradiction is found, None otherwise."""

def prune_low_confidence(db_path: str, threshold: float = 0.3) -> list[dict]:
    """Return knowledge_base entries with confidence below threshold for user review."""

def get_similar_projects(db_path: str, tech_stack_tags: list[str]) -> list[dict]:
    """Query knowledge_base for projects with similar tech stack patterns.
    Used for cross-project knowledge transfer."""
```

Include proper docstrings, type hints, error handling, and connection management (use context managers).

### 3. Create memory/index.md

```markdown
# Memory Index — Project Structure Scan Agent

## Storage Architecture

This agent uses a **Hybrid Markdown + SQLite** memory strategy:

| Storage | Location | Purpose |
|---------|----------|---------|
| SQLite DB | `memory/agent_memory.db` | Structured data: task memory, DoD checks, knowledge base, scan history |
| Conversation Log | `logs/conversation-log.md` | Human-readable dialogue record |
| Work Log | `logs/work-log.md` | Human-readable timeline of agent actions |
| Research Files | `research/` | Research processes and results |
| Phase Questions | `phase{N}-questions.md` | Question lists per phase |

## SQLite Tables

| Table | Purpose | Key Queries |
|-------|---------|-------------|
| `task_memory` | Per-session findings, decisions, lessons, questions, risks | By project + phase + type |
| `dod_checks` | DoD verification results per round | By session + status |
| `knowledge_base` | Cross-session reusable knowledge with confidence scores | By project + category |
| `scan_history` | Record of every scan execution | By project, ordered by date |

## Memory Lifecycle

1. **On Startup**: Load history → generate summary → present to user
2. **During Execution**: Record findings, decisions, questions, risks in real-time
3. **On Completion**: Record lessons, update knowledge base, log scan history
4. **On Re-invocation**: Load previous context, offer incremental scan
5. **Maintenance**: Confidence decay (90 days), contradiction detection, low-confidence pruning

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/init_memory.py` | Initialize or verify SQLite database schema | `python scripts/init_memory.py [db_path]` |
| `scripts/memory_ops.py` | Memory CRUD operations library | Imported by SKILL.md workflow |
```

### 4. Append Memory Utilization Protocol to SKILL.md

Append the following content to `project-structure-scan/SKILL.md` under the `## Memory Utilization Protocol` section header (already exists as skeleton from prompt-01):

**Phase 0 (Startup): Memory-Driven Context Loading**
- Check if `memory/agent_memory.db` exists; if not, run `scripts/init_memory.py`
- Call `load_project_history()` → determine Re-scan Mode vs Fresh Scan Mode
- Re-scan Mode: call `generate_memory_summary()`, present to user, offer options (incremental/full/review)
- Fresh Scan Mode: call `get_similar_projects()`, if found present pattern hypothesis
- Call `apply_confidence_decay()` to maintain memory freshness
- Call `prune_low_confidence()`, report low-confidence entries to user

**Phase 1 (Understand Task Purpose): Memory-Enhanced Understanding**
- Query previous purpose records: `load_lessons_learned()` filtered by phase='phase1'
- If found, present previous purpose and ask if it still applies (skip redundant questions)
- If lessons exist about user preferences, proactively incorporate

**Phase 2 (Understand Target Project): Memory-Accelerated Discovery**
- Query `load_project_knowledge()` for known tech stack, patterns, conventions
- Pre-fill known answers, only ask about unknowns or changes
- Query previous phase2 questions to skip already-answered items

**Phase 3 (Research & Question Generation): Memory-Informed Research**
- Load previous research from `research/` directory
- Query findings from previous phase3 sessions
- Skip redundant research, focus on gaps and new risks
- Proactively revisit known risks and ask if resolved

**Phase 4 (Execute & Produce Deliverables): Memory-Optimized Execution**
- Incremental scan: compare current structure with previous OUT-01
- Pattern confirmation: verify previous patterns still hold, update confidence
- Smart dependency diff: compare current manifest with previous OUT-04
- Quality improvement: query previous failed DoD items, prioritize fixing them

**Cross-Project Knowledge Transfer**
- Query all high-confidence knowledge entries across projects
- Build pattern library, use for hypothesis-driven analysis on new projects
- Record prediction accuracy as lessons for future improvement

**Confidence Decay & Contradiction Detection**
- 90-day decay: reduce confidence by 0.2 for stale entries
- Contradiction detection: flag conflicts between new findings and existing knowledge
- Low-confidence pruning: report entries below 0.3 threshold for user review

## Validation Checklist

After completing all files, verify:
- [ ] `scripts/init_memory.py` exists and runs without error
- [ ] Running `init_memory.py` creates `agent_memory.db` with 4 tables and 5 indexes
- [ ] `scripts/memory_ops.py` exists with all required functions (18+ functions)
- [ ] Each function in `memory_ops.py` has proper docstring and type hints
- [ ] `memory/index.md` exists and documents all tables and scripts
- [ ] `SKILL.md` now contains a populated `## Memory Utilization Protocol` section
- [ ] The Memory Utilization Protocol section covers all 5 phases + cross-project + decay

If any item fails, fix it before reporting completion.
