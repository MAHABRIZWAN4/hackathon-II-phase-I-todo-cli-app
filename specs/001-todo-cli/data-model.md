# Data Model: Todo CLI

## Task Entity

```python
class Task:
    """Represents a single todo item."""
    id: int                    # Unique identifier (1, 2, 3...)
    title: str                 # Brief description (required, non-empty)
    description: str           # Detailed information (optional)
    is_complete: bool          # Completion status (default: False)
```

### Field Specifications

| Field | Type | Constraints | Validation |
|-------|------|-------------|------------|
| id | int | > 0, unique, auto-increment | System-generated |
| title | str | 1-200 chars, non-empty | Required |
| description | str | 0-1000 chars, optional | Can be empty |
| is_complete | bool | True/False | Default: False |

### State Transitions

```
incomplete --[mark_complete]--> complete
complete --[mark_incomplete]--> incomplete
```

## TodoManager Entity

```python
class TodoManager:
    """Manages a collection of tasks in memory."""
    _tasks: list[Task]         # In-memory task list
    _next_id: int              # Next available ID (auto-increment)
```

### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| add_task | title: str, description: str = "" | Task | Creates new task with unique ID |
| delete_task | task_id: int | bool | Removes task by ID, returns success |
| update_task | task_id: int, title: str = None, description: str = None | bool | Updates fields, returns success |
| get_task | task_id: int | Task \| None | Returns task or None |
| list_tasks | None | list[Task] | Returns all tasks in creation order |
| mark_complete | task_id: int | bool | Toggles status to complete |
| mark_incomplete | task_id: int | bool | Toggles status to incomplete |

### Validation Rules

1. **Empty title**: Reject with error message "Title cannot be empty"
2. **Invalid ID**: Reject with error message "Task with ID {id} not found"
3. **ID stability**: IDs never change during session (no renumbering)

## Error Taxonomy

| Error Condition | Message | User Action |
|-----------------|---------|-------------|
| Empty title | "Error: Title cannot be empty" | Provide non-empty title |
| Invalid ID | "Error: Task with ID {id} not found" | Use valid ID from list |
| Delete success | "Task deleted successfully" | Confirmation |
| Update success | "Task updated successfully" | Confirmation |
