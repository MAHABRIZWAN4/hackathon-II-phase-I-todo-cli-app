"""TodoManager class for the Todo CLI application."""

from typing import Optional

from task import Task


class TodoManager:
    """Manages a collection of tasks in memory."""

    def __init__(self) -> None:
        """Initialize the TodoManager with an empty task list."""
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task.

        Args:
            title: Brief description of the task (required, non-empty)
            description: Detailed information about the task (optional)

        Returns:
            The created Task object

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> bool:
        """Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (if None, keep current)
            description: New description (if None, keep current)

        Returns:
            True if task was updated, False if not found

        Raises:
            ValueError: If title is empty
        """
        if title is not None and not title.strip():
            raise ValueError("Title cannot be empty")
        for task in self._tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID.

        Args:
            task_id: The ID of the task to get

        Returns:
            The Task object or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> list[Task]:
        """List all tasks in creation order.

        Returns:
            List of all tasks
        """
        return list(self._tasks)

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was marked complete, False if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                task.is_complete = True
                return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                task.is_complete = False
                return True
        return False
