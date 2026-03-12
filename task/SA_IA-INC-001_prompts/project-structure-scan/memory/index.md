# Memory Index — Project Structure Scan Agent

## Storage Architecture

| Storage | Location | Purpose |
|---------|----------|---------|
| SQLite DB | memory/agent_memory.db | Structured: task memory, DoD checks, knowledge base, scan history |
| Conversation Log | logs/conversation-log.md | Human-readable dialogue |
| Work Log | logs/work-log.md | Human-readable action timeline |
| Research Files | research/ | Research processes and results |
| Phase Questions | phase{N}-questions.md | Question lists per phase |

## SQLite Tables

| Table | Purpose | Key Queries |
|-------|---------|-------------|
| task_memory | Per-session findings, decisions, lessons, questions, risks | By project + phase + type |
| dod_checks | DoD verification results per round | By session + status |
| knowledge_base | Cross-session reusable knowledge with confidence scores | By project + category |
| scan_history | Record of every scan execution | By project, ordered by date |

## Memory Lifecycle

1. On Startup: Load history → generate summary → present to user
2. During Execution: Record findings, decisions, questions, risks in real-time
3. On Completion: Record lessons, update knowledge base, log scan history
4. On Re-invocation: Load previous context, offer incremental scan
5. Maintenance: Confidence decay (90 days), contradiction detection, low-confidence pruning

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| scripts/init_memory.py | Initialize/verify SQLite database schema | python scripts/init_memory.py [db_path] |
| scripts/memory_ops.py | Memory CRUD operations library | Imported by SKILL.md workflow |
