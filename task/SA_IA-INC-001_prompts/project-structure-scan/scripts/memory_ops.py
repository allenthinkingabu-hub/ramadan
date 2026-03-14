#!/usr/bin/env python3
"""Memory CRUD operations for Project Structure Scan Agent.

Provides functions for reading/writing to the SQLite memory database.
All functions use context managers for database connections and include
proper error handling, type hints, and docstrings.
"""

import json
import sqlite3
from datetime import datetime, timedelta
from typing import Optional


def _dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """Convert sqlite3 row to dictionary."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def _connect(db_path: str) -> sqlite3.Connection:
    """Create a database connection with row_factory set to dict."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = _dict_factory
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn


# ---------------------------------------------------------------------------
# Startup Operations
# ---------------------------------------------------------------------------


def load_project_history(db_path: str, project_name: str) -> dict:
    """Query scan_history for previous scans of a project.

    Args:
        db_path: Path to the SQLite database file.
        project_name: Name of the project to look up.

    Returns:
        Dictionary with keys:
            - scan_count (int): Total number of scans for this project.
            - last_scan (dict | None): Most recent scan record, or None.
            - scans (list[dict]): All scan records ordered by started_at DESC.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM scan_history WHERE project_name = ? ORDER BY started_at DESC;",
            (project_name,),
        )
        scans = cursor.fetchall()

    return {
        "scan_count": len(scans),
        "last_scan": scans[0] if scans else None,
        "scans": scans,
    }


def load_project_knowledge(db_path: str, project_name: str) -> list[dict]:
    """Query knowledge_base for all knowledge about a project.

    Args:
        db_path: Path to the SQLite database file.
        project_name: Name of the project.

    Returns:
        List of knowledge records sorted by confidence descending.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM knowledge_base WHERE project_name = ? ORDER BY confidence DESC;",
            (project_name,),
        )
        return cursor.fetchall()


def load_lessons_learned(
    db_path: str, task_id: str, project_name: Optional[str] = None
) -> list[dict]:
    """Query task_memory for lessons learned.

    Args:
        db_path: Path to the SQLite database file.
        task_id: Task identifier to filter by.
        project_name: Optional project name to further filter results.

    Returns:
        List of lesson records ordered by created_at descending.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        if project_name:
            cursor.execute(
                "SELECT * FROM task_memory WHERE memory_type = 'lesson' "
                "AND task_id = ? AND project_name = ? ORDER BY created_at DESC;",
                (task_id, project_name),
            )
        else:
            cursor.execute(
                "SELECT * FROM task_memory WHERE memory_type = 'lesson' "
                "AND task_id = ? ORDER BY created_at DESC;",
                (task_id,),
            )
        return cursor.fetchall()


def generate_memory_summary(db_path: str, project_name: str) -> str:
    """Generate a markdown summary of all memory about a project.

    Combines scan history, knowledge base entries, and task memory
    into a human-readable markdown report.

    Args:
        db_path: Path to the SQLite database file.
        project_name: Name of the project.

    Returns:
        Markdown-formatted string summarizing all project memory.
    """
    history = load_project_history(db_path, project_name)
    knowledge = load_project_knowledge(db_path, project_name)

    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT memory_type, COUNT(*) as count FROM task_memory "
            "WHERE project_name = ? GROUP BY memory_type;",
            (project_name,),
        )
        memory_counts = {row["memory_type"]: row["count"] for row in cursor.fetchall()}

        cursor.execute(
            "SELECT * FROM task_memory WHERE project_name = ? "
            "AND memory_type = 'risk' ORDER BY created_at DESC LIMIT 10;",
            (project_name,),
        )
        recent_risks = cursor.fetchall()

    lines = [
        f"# Memory Summary: {project_name}",
        "",
        "## Scan History",
        f"- Total scans: {history['scan_count']}",
    ]

    if history["last_scan"]:
        last = history["last_scan"]
        lines.append(f"- Last scan: {last['started_at']} (status: {last['status']})")
        lines.append(f"- Last scope: {last.get('scan_scope', 'N/A')}")
    else:
        lines.append("- No previous scans recorded.")

    lines += ["", "## Knowledge Base", f"- Total entries: {len(knowledge)}"]
    if knowledge:
        # Group by category
        categories: dict[str, list[dict]] = {}
        for entry in knowledge:
            categories.setdefault(entry["category"], []).append(entry)
        for cat, entries in categories.items():
            lines.append(f"  - {cat}: {len(entries)} entries")

    lines += ["", "## Task Memory"]
    for mtype in ("finding", "decision", "lesson", "question", "risk"):
        lines.append(f"- {mtype}s: {memory_counts.get(mtype, 0)}")

    if recent_risks:
        lines += ["", "## Recent Risks"]
        for risk in recent_risks:
            lines.append(f"- **{risk.get('title', 'Untitled')}**: {risk['content']}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# During Execution
# ---------------------------------------------------------------------------


def _record_task_memory(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    phase: str,
    memory_type: str,
    title: str,
    content: str,
    context: Optional[str] = None,
    tags: Optional[str] = None,
) -> int:
    """Internal helper to insert a task_memory record.

    Returns:
        The id of the inserted row.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO task_memory "
            "(session_id, task_id, project_name, phase, memory_type, title, content, context, tags) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (session_id, task_id, project_name, phase, memory_type, title, content, context, tags),
        )
        conn.commit()
        return cursor.lastrowid


def record_finding(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    phase: str,
    title: str,
    content: str,
    context: Optional[str] = None,
    tags: Optional[str] = None,
) -> int:
    """Record a finding in task memory.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project being scanned.
        phase: Current workflow phase (e.g., 'phase-1').
        title: Short title for the finding.
        content: Detailed finding content.
        context: Optional additional context.
        tags: Optional comma-separated tags.

    Returns:
        The id of the inserted row.
    """
    return _record_task_memory(
        db_path, session_id, task_id, project_name, phase, "finding", title, content, context, tags
    )


def record_decision(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    phase: str,
    title: str,
    content: str,
    context: Optional[str] = None,
) -> int:
    """Record a decision in task memory.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project being scanned.
        phase: Current workflow phase.
        title: Short title for the decision.
        content: Detailed decision content and rationale.
        context: Optional additional context.

    Returns:
        The id of the inserted row.
    """
    return _record_task_memory(
        db_path, session_id, task_id, project_name, phase, "decision", title, content, context
    )


def record_question(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    phase: str,
    title: str,
    content: str,
) -> int:
    """Record a question in task memory.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project being scanned.
        phase: Current workflow phase.
        title: Short title for the question.
        content: Full question text.

    Returns:
        The id of the inserted row.
    """
    return _record_task_memory(
        db_path, session_id, task_id, project_name, phase, "question", title, content
    )


def record_risk(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    phase: str,
    title: str,
    content: str,
    context: Optional[str] = None,
) -> int:
    """Record a risk in task memory.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project being scanned.
        phase: Current workflow phase.
        title: Short title for the risk.
        content: Risk description and potential impact.
        context: Optional additional context.

    Returns:
        The id of the inserted row.
    """
    return _record_task_memory(
        db_path, session_id, task_id, project_name, phase, "risk", title, content, context
    )


def record_knowledge(
    db_path: str,
    project_name: str,
    category: str,
    key: str,
    value: str,
    confidence: float = 0.8,
    source: Optional[str] = None,
) -> int:
    """Record or update a knowledge base entry (UPSERT).

    If a record with the same project_name, category, and key already exists,
    updates the value, confidence, and updated_at timestamp. Otherwise inserts
    a new record.

    Args:
        db_path: Path to the SQLite database file.
        project_name: Name of the project.
        category: Knowledge category (pattern, dependency, risk, insight, tech_stack, convention).
        key: Knowledge key identifier.
        value: Knowledge value content.
        confidence: Confidence score between 0.0 and 1.0 (default 0.8).
        source: Optional source of this knowledge.

    Returns:
        The id of the inserted or updated row.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        # Check for existing entry
        cursor.execute(
            "SELECT id FROM knowledge_base WHERE project_name = ? AND category = ? AND key = ?;",
            (project_name, category, key),
        )
        existing = cursor.fetchone()

        if existing:
            cursor.execute(
                "UPDATE knowledge_base SET value = ?, confidence = ?, source = ?, "
                "updated_at = CURRENT_TIMESTAMP WHERE id = ?;",
                (value, confidence, source, existing["id"]),
            )
            conn.commit()
            return existing["id"]
        else:
            cursor.execute(
                "INSERT INTO knowledge_base (project_name, category, key, value, confidence, source) "
                "VALUES (?, ?, ?, ?, ?, ?);",
                (project_name, category, key, value, confidence, source),
            )
            conn.commit()
            return cursor.lastrowid


# ---------------------------------------------------------------------------
# On Completion
# ---------------------------------------------------------------------------


def start_scan(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    project_path: str,
    scan_scope: str = "full",
) -> int:
    """Record the start of a new scan.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project being scanned.
        project_path: Filesystem path to the project.
        scan_scope: Scope of the scan ('full', 'partial', or 'incremental').

    Returns:
        The id of the new scan_history record.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO scan_history (session_id, task_id, project_name, project_path, scan_scope, status) "
            "VALUES (?, ?, ?, ?, ?, 'in_progress');",
            (session_id, task_id, project_name, project_path, scan_scope),
        )
        conn.commit()
        return cursor.lastrowid


def complete_scan(db_path: str, scan_id: int, deliverables_path: str) -> None:
    """Mark a scan as completed.

    Args:
        db_path: Path to the SQLite database file.
        scan_id: The id of the scan_history record to update.
        deliverables_path: Path to the generated deliverables.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE scan_history SET status = 'completed', deliverables_path = ?, "
            "completed_at = CURRENT_TIMESTAMP WHERE id = ?;",
            (deliverables_path, scan_id),
        )
        conn.commit()


def fail_scan(db_path: str, scan_id: int) -> None:
    """Mark a scan as failed.

    Args:
        db_path: Path to the SQLite database file.
        scan_id: The id of the scan_history record to update.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE scan_history SET status = 'failed', completed_at = CURRENT_TIMESTAMP WHERE id = ?;",
            (scan_id,),
        )
        conn.commit()


def record_dod_check(
    db_path: str,
    session_id: str,
    task_id: str,
    check_round: int,
    check_item: str,
    status: str,
    evidence: Optional[str] = None,
    notes: Optional[str] = None,
) -> int:
    """Record a Definition of Done check result.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        check_round: The round number for this DoD check.
        check_item: Description of the check item.
        status: Check result ('pass', 'fail', or 'pending').
        evidence: Optional evidence supporting the status.
        notes: Optional additional notes.

    Returns:
        The id of the inserted row.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dod_checks (session_id, task_id, check_round, check_item, status, evidence, notes) "
            "VALUES (?, ?, ?, ?, ?, ?, ?);",
            (session_id, task_id, check_round, check_item, status, evidence, notes),
        )
        conn.commit()
        return cursor.lastrowid


def record_lesson(
    db_path: str,
    session_id: str,
    task_id: str,
    project_name: str,
    title: str,
    content: str,
) -> int:
    """Record a lesson learned in task memory.

    Args:
        db_path: Path to the SQLite database file.
        session_id: Current session identifier.
        task_id: Current task identifier.
        project_name: Name of the project.
        title: Short title for the lesson.
        content: Detailed lesson content.

    Returns:
        The id of the inserted row.
    """
    return _record_task_memory(
        db_path, session_id, task_id, project_name, "completion", "lesson", title, content
    )


# ---------------------------------------------------------------------------
# Memory Maintenance
# ---------------------------------------------------------------------------


def apply_confidence_decay(
    db_path: str, days_threshold: int = 90, decay_amount: float = 0.2
) -> int:
    """Apply confidence decay to knowledge base entries older than threshold.

    Reduces confidence by decay_amount for entries not updated within
    days_threshold days. Confidence will not go below 0.0.

    Args:
        db_path: Path to the SQLite database file.
        days_threshold: Number of days after which decay applies (default 90).
        decay_amount: Amount to reduce confidence by (default 0.2).

    Returns:
        Number of rows affected.
    """
    cutoff = (datetime.now() - timedelta(days=days_threshold)).isoformat()
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE knowledge_base SET confidence = MAX(0.0, confidence - ?), "
            "updated_at = CURRENT_TIMESTAMP "
            "WHERE updated_at < ?;",
            (decay_amount, cutoff),
        )
        conn.commit()
        return cursor.rowcount


def detect_contradictions(
    db_path: str, project_name: str, category: str, key: str, new_value: str
) -> Optional[dict]:
    """Check if a new value contradicts an existing knowledge base entry.

    Args:
        db_path: Path to the SQLite database file.
        project_name: Name of the project.
        category: Knowledge category.
        key: Knowledge key to check.
        new_value: The proposed new value.

    Returns:
        Dictionary with contradiction details if found, None otherwise.
        Dict keys: 'existing_id', 'existing_value', 'existing_confidence',
                    'new_value', 'key', 'category'.
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, value, confidence FROM knowledge_base "
            "WHERE project_name = ? AND category = ? AND key = ?;",
            (project_name, category, key),
        )
        existing = cursor.fetchone()

    if existing and existing["value"] != new_value:
        return {
            "existing_id": existing["id"],
            "existing_value": existing["value"],
            "existing_confidence": existing["confidence"],
            "new_value": new_value,
            "key": key,
            "category": category,
        }
    return None


def prune_low_confidence(db_path: str, threshold: float = 0.3) -> list[dict]:
    """Remove knowledge base entries with confidence below threshold.

    Args:
        db_path: Path to the SQLite database file.
        threshold: Confidence threshold below which entries are removed (default 0.3).

    Returns:
        List of pruned records (for logging/audit purposes).
    """
    with _connect(db_path) as conn:
        cursor = conn.cursor()
        # Fetch records to be pruned before deleting
        cursor.execute(
            "SELECT * FROM knowledge_base WHERE confidence < ?;",
            (threshold,),
        )
        pruned = cursor.fetchall()

        if pruned:
            cursor.execute(
                "DELETE FROM knowledge_base WHERE confidence < ?;",
                (threshold,),
            )
            conn.commit()

    return pruned


def get_similar_projects(db_path: str, tech_stack_tags: list[str]) -> list[dict]:
    """Find projects with similar tech stacks in the knowledge base.

    Searches for projects that share tech_stack entries matching any of the
    provided tags. Results are ranked by the number of matching tags.

    Args:
        db_path: Path to the SQLite database file.
        tech_stack_tags: List of technology names to match against.

    Returns:
        List of dicts with keys 'project_name', 'matching_tags' (list),
        and 'match_count' (int), sorted by match_count descending.
    """
    if not tech_stack_tags:
        return []

    placeholders = ",".join("?" for _ in tech_stack_tags)
    query = (
        f"SELECT project_name, key, value FROM knowledge_base "
        f"WHERE category = 'tech_stack' AND key IN ({placeholders});"
    )

    with _connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, tech_stack_tags)
        rows = cursor.fetchall()

    # Group by project
    projects: dict[str, list[str]] = {}
    for row in rows:
        projects.setdefault(row["project_name"], []).append(row["key"])

    results = [
        {
            "project_name": name,
            "matching_tags": tags,
            "match_count": len(tags),
        }
        for name, tags in projects.items()
    ]
    results.sort(key=lambda x: x["match_count"], reverse=True)
    return results
