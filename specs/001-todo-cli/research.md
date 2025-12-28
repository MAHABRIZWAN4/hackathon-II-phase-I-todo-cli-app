# Research: Todo CLI Implementation

## Architecture Decisions

### File Structure

| Decision | Chosen Approach | Rationale |
|----------|-----------------|-----------|
| Structure | Flat files (main.py, todo_manager.py, task.py) | Simple CLI app doesn't need package hierarchy |
| Tests | Separate tests/ directory | Clean separation, follows Python testing conventions |

**Alternatives considered:**
- Package-based structure (rejected: overkill for single-user CLI)
- Combined single-file (rejected: violates single responsibility principle)

### Class Design

| Decision | Chosen Approach | Rationale |
|----------|-----------------|-----------|
| Task class | Single class with id, title, description, is_complete | Clear data model, easy to test |
| TodoManager class | Wrapper around in-memory list with CRUD methods | Encapsulates business logic |
| Separation | Task = data model, TodoManager = operations | Follows SRP |

**Alternatives considered:**
- Dataclass for Task (accepted: Python 3.10+ feature, cleaner code)
- Dictionary-based storage (rejected: less type safety, harder to test)

### CLI Interface

| Decision | Chosen Approach | Rationale |
|----------|-----------------|-----------|
| Style | Menu-driven loop | User-friendly, clear options |
| Input handling | input() with validation | Stdlib only, no dependencies |
| View format | Numbered list | Simple, matches todo.txt style |

**Alternatives considered:**
- Argparse-based (rejected: user requested menu-driven)
- Interactive prompt for all operations (accepted: update uses this per clarification)

### Data Storage

| Decision | Chosen Approach | Rationale |
|----------|-----------------|-----------|
| Storage | In-memory list | Per constitution: memory-only constraint |
| ID generation | Auto-incrementing integer | Simple, user-friendly IDs |

**Alternatives considered:**
- UUID (rejected: less user-friendly, violates "simple" principle)
- Persistent storage (rejected: violates memory-only constraint)

## Best Practices Applied

1. **PEP 8 Compliance**: Clean, readable code with meaningful names
2. **Single Responsibility**: Each class has one purpose
3. **Testability**: Business logic separated from CLI concerns
4. **Stdlib Only**: No external dependencies per constitution

## Technical Stack

- Python 3.13+ (constitution requirement)
- UV package manager (constitution requirement)
- pytest for testing (or stdlib unittest if needed)
- No external dependencies
