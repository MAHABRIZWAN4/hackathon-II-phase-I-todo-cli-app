#!/usr/bin/env python3
"""CLI interface for the Todo CLI application."""

import sys

from todo_manager import TodoManager


def print_menu() -> None:
    """Print the main menu."""
    print("\n=== Todo CLI ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print()


def print_tasks(manager: TodoManager) -> None:
    """Print all tasks in a formatted list."""
    tasks = manager.list_tasks()
    if not tasks:
        print("\nNo tasks found. Add some tasks to get started!")
        return

    print()
    for task in tasks:
        status = "[x]" if task.is_complete else "[ ]"
        print(f"{task.id}. {status} {task.title}")
        if task.description:
            print(f"   Description: {task.description}")
    print()


def add_task(manager: TodoManager) -> None:
    """Add a new task."""
    title = input("Title: ").strip()
    if not title:
        print("Error: Title cannot be empty")
        return

    description = input("Description (optional): ").strip()
    task = manager.add_task(title, description)
    print(f"Task added with ID {task.id}")


def update_task(manager: TodoManager) -> None:
    """Update an existing task with interactive prompts."""
    try:
        task_id = int(input("Task ID: "))
    except ValueError:
        print("Error: Invalid task ID")
        return

    task = manager.get_task(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found")
        return

    print(f"Current title: {task.title}")
    new_title = input("New title (press Enter to keep): ").strip()
    if not new_title:
        new_title = None

    print(f"Current description: {task.description}")
    new_description = input("New description (press Enter to keep): ").strip()
    if not new_description:
        new_description = None

    try:
        result = manager.update_task(task_id, new_title, new_description)
        if result:
            print("Task updated successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task(manager: TodoManager) -> None:
    """Delete a task by ID."""
    try:
        task_id = int(input("Task ID: "))
    except ValueError:
        print("Error: Invalid task ID")
        return

    result = manager.delete_task(task_id)
    if result:
        print("Task deleted successfully")
    else:
        print(f"Error: Task with ID {task_id} not found")


def mark_complete(manager: TodoManager) -> None:
    """Mark a task as complete or incomplete."""
    try:
        task_id = int(input("Task ID: "))
    except ValueError:
        print("Error: Invalid task ID")
        return

    task = manager.get_task(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found")
        return

    if task.is_complete:
        confirm = input("Task is already complete. Mark as incomplete? (y/n): ").lower()
        if confirm == "y":
            result = manager.mark_incomplete(task_id)
            if result:
                print("Task marked as incomplete")
    else:
        confirm = input("Mark as complete? (y/n): ").lower()
        if confirm == "y":
            result = manager.mark_complete(task_id)
            if result:
                print("Task marked complete")


def main() -> int:
    """Main CLI loop."""
    manager = TodoManager()

    while True:
        print_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_task(manager)
        elif choice == "2":
            print_tasks(manager)
        elif choice == "3":
            update_task(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            mark_complete(manager)
        elif choice == "6":
            print("Goodbye!")
            return 0
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    sys.exit(main())
