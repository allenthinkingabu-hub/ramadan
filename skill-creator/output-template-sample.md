# Output Template Sample (Compact) -- Any Skill

```yaml
# Trigger Config -- {skill_name} Agent
# Task: {task_id} | Generated: {timestamp}
metadata:
  task_id: "{task_id}"
  task_name: "{task_name}"
  role: "{role}"
triggers:
  - id: "TRG-001"
    event: "user_invocation"
    source: "User"
  - id: "TRG-002"
    event: "pm_assignment"
    source: "PM Agent"
    condition: "{task_id} assigned via RACI"
  - id: "TRG-003"
    event: "upstream_completion"
    source: "Previous Wave"
```

```yaml
# DoD Checklist -- {skill_name} Agent
metadata:
  task_id: "{task_id}"
items:
  - id: "DoD-01"
    check: "config/triggers.yaml exists"
    status: "PENDING"
  - id: "DoD-02"
    check: "config/raci.yaml exists"
    status: "PENDING"
  # ... DoD-03 through DoD-12 (config + logs)
  - id: "DoD-13"
    check: "Self-verification complete"
    status: "PENDING"
  - id: "DoD-14"
    check: "Primary report exists"
    status: "PENDING"
```

```markdown
## Conversation Log -- {task_id}
| # | Phase | Question | Answer | Confirmed |
|---|-------|----------|--------|-----------|
| 1 | 1     | {q}      | {a}    | Yes/No    |
```

```markdown
## Work Log -- {task_id}
| Timestamp | Phase | Action | Details |
|-----------|-------|--------|---------|
| {ts}      | 0     | Init   | Created output directory |
```
