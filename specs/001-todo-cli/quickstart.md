# Quickstart: Todo CLI

## Installation

```bash
# Initialize UV project
uv init --python 3.13

# Add no dependencies (stdlib only)
# No changes to pyproject.toml needed
```

## Running the Application

```bash
# Run with UV
uv run python main.py

# Or directly if Python 3.13+ is installed
python main.py
```

## Usage Guide

### Main Menu

```
=== Todo CLI ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter choice (1-6):
```

### Operations

#### Add Task
```
Enter choice: 1
Title: Buy groceries
Description (optional): Milk, eggs, bread
Task added with ID 1
```

#### View Tasks
```
Enter choice: 2
1. [ ] Buy groceries
   Description: Milk, eggs, bread

2. [ ] Call dentist
   Description: Appointment at 3pm
```

#### Update Task
```
Enter choice: 3
Task ID: 1
Current title: Buy groceries
New title (press Enter to keep): Buy organic groceries
Current description: Milk, eggs, bread
New description (press Enter to keep):
Task updated successfully
```

#### Delete Task
```
Enter choice: 4
Task ID: 1
Task deleted successfully
```

#### Mark Complete/Incomplete
```
Enter choice: 5
Task ID: 2
Mark as complete? (y/n): y
Task marked complete
```

#### Exit
```
Enter choice: 6
Goodbye!
```

## Examples

### Create and complete tasks

```bash
$ python main.py
=== Todo CLI ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter choice (1-6): 1
Title: Learn Python
Description: Complete the CLI todo app
Task added with ID 1

Enter choice (1-6): 1
Title: Write tests
Description:
Task added with ID 2

Enter choice (1-6): 2
1. [ ] Learn Python
   Description: Complete the CLI todo app

2. [ ] Write tests
   Description:

Enter choice (1-6): 5
Task ID: 1
Mark as complete? (y/n): y
Task marked complete

Enter choice (1-6): 2
1. [x] Learn Python
   Description: Complete the CLI todo app

2. [ ] Write tests
   Description:

Enter choice (1-6): 6
Goodbye!
```

## Notes

- Data is stored in-memory only and will be lost when the application exits
- Task IDs are auto-incremented and never reused
- All operations complete instantly (in-memory storage)
