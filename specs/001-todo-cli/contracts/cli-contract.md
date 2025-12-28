# CLI Contract: Todo Manager

## Command Interface

### Interactive Menu Mode (Default)

The application runs in an interactive menu loop until the user exits.

```
$ python main.py
=== Todo CLI ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter choice (1-6): _
```

### Input/Output Specifications

#### Add Task

| Field | Type | Required | Format |
|-------|------|----------|--------|
| Title | string | Yes | 1-200 characters, non-empty |
| Description | string | No | 0-1000 characters, optional |

**Output:** `Task added with ID {id}` or `Error: {message}`

#### View Tasks

**Output:**
```
{index}. [{status}] {title}
   Description: {description}
```

Status indicators: `[ ]` = incomplete, `[x]` = complete

#### Update Task

| Field | Type | Required | Format |
|-------|------|----------|--------|
| Task ID | integer | Yes | Valid existing ID |
| New Title | string | No | 1-200 characters (current value kept if empty) |
| New Description | string | No | 0-1000 characters (current value kept if empty) |

**Output:** `Task updated successfully` or `Error: {message}`

#### Delete Task

| Field | Type | Required | Format |
|-------|------|----------|--------|
| Task ID | integer | Yes | Valid existing ID |

**Output:** `Task deleted successfully` or `Error: {message}`

#### Mark Complete/Incomplete

| Field | Type | Required | Format |
|-------|------|----------|--------|
| Task ID | integer | Yes | Valid existing ID |
| Confirm | character | Yes | 'y' or 'n' |

**Output:** `Task marked complete` or `Task marked incomplete` or `Error: {message}`

#### Exit

**Output:** `Goodbye!`

## Error Messages

| Condition | Message |
|-----------|---------|
| Empty title | `Error: Title cannot be empty` |
| Invalid task ID | `Error: Task with ID {id} not found` |
| Invalid menu choice | `Invalid choice. Please enter 1-6.` |
| Invalid confirmation | `Please enter 'y' or 'n'.` |

## Session Lifecycle

```
Start → Main Menu Loop → Operation → Main Menu Loop → ... → Exit → End
                                      ↑_____________________|
```
