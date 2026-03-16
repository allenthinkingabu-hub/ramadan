# Memory Index — SA-TRF-001: Transformation Target Current State Analysis

> Quick reference for the agent's SQLite memory system. Database file: `memory/agent_memory.db`
> Run `scripts/init_memory.py` to initialize. Run `scripts/memory_ops.py` for CLI queries.

---

## Database Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `task_memory` | All findings, decisions, risks, constraints, lessons, Q&A within a session | session_id, memory_type, phase, category, confidence |
| `dod_checks` | Per-check pass/fail records for DoD verification rounds | session_id, check_id, check_round, status |
| `knowledge_base` | Cross-session project/target knowledge (persists, decays) | project_name, target_name, category, key, value, confidence |
| `analysis_history` | One record per analysis session with status and deliverables | session_id, target_name, status, output_dir, dod_passed |

---

## Memory Types (task_memory.memory_type)

| Type | When to Write | Example Use |
|------|--------------|-------------|
| `finding` | Step 4 — each significant investigation finding | "PaymentService.process() has N+1 query on line 42" |
| `decision` | Steps 1-3 — confirmed user decisions | "Scope confirmed: include-direct-dependencies" |
| `risk` | Steps 3-4 — identified risks and debt items | "Missing test coverage on error path" |
| `constraint` | Step 4 — hard/soft constraints identified | "DB schema for payments_table cannot change" |
| `lesson` | Step 5 — insights for future sessions | "Spring @Transactional boundary was non-obvious" |
| `question` | Steps 0-3 — Q&A from interactive dialogue | "Q: What transformation? A: Extract to microservice" |
| `research` | Step 3 — findings from context7/WebSearch | "Strangler Fig pattern best practices from Martin Fowler" |

---

## Memory Operations Quick Reference

### Write Operations (use MemoryOps class in memory_ops.py)

```python
from scripts.memory_ops import MemoryOps

mem = MemoryOps(db_path="memory/agent_memory.db", session_id=SESSION_ID)

# Step 1-2: Record confirmed decisions
mem.record_decision("Purpose confirmed", "Extracting PaymentService to microservice", phase="phase1")

# Step 3: Record research and questions
mem.record_research("Strangler Fig pattern", "...", phase="phase3", category="architecture")
mem.record_question("Q: Transformation intent?", "A: Extract to separate service", phase="phase3")

# Step 4: Record investigation findings
mem.record_finding("N+1 query on line 42", "SELECT inside loop...", phase="phase4",
                   category="performance", severity="high", source_file="PaymentService.java", source_line=42)
mem.record_constraint("DB schema frozen", "payments_table columns cannot change", phase="phase4",
                      category="dependency", severity="critical")
mem.record_risk("Missing test coverage", "Error path has no tests", phase="phase4",
                severity="high", category="coverage")

# Step 4: Record knowledge for cross-session reuse
mem.record_knowledge("MyApp", "tech_stack", "primary_language", "Java 17", target_name="PaymentService")

# Step 5: DoD checks and lessons
mem.record_dod_check("DoD-01", "pass", "OUT-01 size=4521 bytes", check_round=1)
mem.record_lesson("Check @Transactional early", "Spring TX boundary affects test strategy", phase="phase5")

# Step 5: Mark analysis complete
mem.update_history_status("completed", deliverables=["OUT-01-...", "OUT-07-..."],
                          dod_passed=20, summary_stats={"total_loc": 1240})
```

### Read Operations

```python
# Step 0B: Load previous analysis history
history = mem.load_history("MyApp", "PaymentService")

# Step 0B: Apply confidence decay to knowledge_base entries
knowledge = mem.load_knowledge("MyApp", target_name="PaymentService", category="tech_stack")

# Step 1-3: Load prior decisions/lessons
decisions = mem.query_memory(memory_type="decision", phase="phase1")
lessons = mem.query_memory(memory_type="lesson")

# Step 3: Load prior risks
risks = mem.query_memory(memory_type="risk")

# Step 5: Verify memory was recorded
count = mem.get_memory_count()  # must be > 0 for DoD-16
```

---

## Confidence Decay Protocol

- `knowledge_base` entries have `confidence` starting at 1.0
- Confidence decreases by 0.2 for every 90-day interval since `recorded_at`
- `load_knowledge()` applies decay automatically at read time
- Entries with confidence < 0.4 should be flagged for re-verification
- **Present to user**: "I have prior knowledge about this target (confidence: {X:.0%}). Is this still accurate?"

---

## Session ID Convention

Format: `SA-TRF-001-{YYYYMMDD-HHMMSS}` (e.g., `SA-TRF-001-20260315-143022`)

Generated at Step 0B-2 alongside the output directory timestamp.

---

## Re-analysis Mode

When `load_history()` returns prior records for the same project+target:

1. Present Memory Summary to user: prior session date, scope, key findings count
2. Offer options:
   - **Incremental**: focus on files changed since prior session (diff-based)
   - **Full re-analysis**: ignore prior findings, start fresh
   - **Review previous findings**: display OUT-07 from prior session, user decides
3. If incremental: use prior OUT-01 as baseline, only re-investigate changed files
4. Apply confidence decay to prior knowledge_base entries before reuse
