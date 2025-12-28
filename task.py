"""Task class for the Todo CLI application."""


class Task:
    """Represents a single todo item."""

    def __init__(self, id: int, title: str, description: str = "", is_complete: bool = False) -> None:
        """Initialize a Task.

        Args:
            id: Unique identifier for the task
            title: Brief description of the task (required, non-empty)
            description: Detailed information about the task (optional)
            is_complete: Completion status (default: False)
        """
        self.id = id
        self.title = title
        self.description = description
        self.is_complete = is_complete

    def __repr__(self) -> str:
        """Return string representation of the Task."""
        status = "x" if self.is_complete else " "
        return f"Task(id={self.id}, title={self.title!r}, is_complete={self.is_complete})"
