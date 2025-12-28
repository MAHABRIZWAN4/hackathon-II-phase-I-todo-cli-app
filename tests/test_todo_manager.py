"""Unit tests for TodoManager class."""

import pytest

from todo_manager import TodoManager


class TestAddTask:
    """Tests for add_task method."""

    def test_add_task_creates_task_with_correct_fields(self) -> None:
        """Test that add_task creates a task with correct ID, title, and description."""
        manager = TodoManager()
        task = manager.add_task("Buy groceries", "Milk, eggs, bread")

        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert task.is_complete is False

    def test_add_task_assigns_unique_ids(self) -> None:
        """Test that each task gets a unique ID."""
        manager = TodoManager()
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        task3 = manager.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_with_only_title(self) -> None:
        """Test adding task with only title (no description)."""
        manager = TodoManager()
        task = manager.add_task("Simple task")

        assert task.title == "Simple task"
        assert task.description == ""
        assert task.is_complete is False

    def test_add_task_rejects_empty_title(self) -> None:
        """Test that add_task rejects empty title."""
        manager = TodoManager()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.add_task("")

    def test_add_task_rejects_whitespace_only_title(self) -> None:
        """Test that add_task rejects whitespace-only title."""
        manager = TodoManager()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.add_task("   ")

    def test_add_task_is_incomplete_by_default(self) -> None:
        """Test that new tasks are incomplete by default."""
        manager = TodoManager()
        task = manager.add_task("New task")

        assert task.is_complete is False


class TestListTasks:
    """Tests for list_tasks method."""

    def test_list_empty_returns_empty_list(self) -> None:
        """Test that list_tasks returns empty list when no tasks."""
        manager = TodoManager()
        tasks = manager.list_tasks()

        assert tasks == []

    def test_list_returns_all_tasks(self) -> None:
        """Test that list_tasks returns all tasks."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

        tasks = manager.list_tasks()

        assert len(tasks) == 3
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"

    def test_list_returns_tasks_in_creation_order(self) -> None:
        """Test that list_tasks returns tasks in creation order."""
        manager = TodoManager()
        manager.add_task("First")
        manager.add_task("Second")
        manager.add_task("Third")

        tasks = manager.list_tasks()

        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3


class TestDeleteTask:
    """Tests for delete_task method."""

    def test_delete_task_removes_task(self) -> None:
        """Test that delete_task removes the task."""
        manager = TodoManager()
        manager.add_task("Task to delete")
        result = manager.delete_task(1)

        assert result is True
        assert len(manager.list_tasks()) == 0

    def test_delete_task_returns_false_for_nonexistent_id(self) -> None:
        """Test that delete_task returns False for nonexistent ID."""
        manager = TodoManager()
        manager.add_task("Task 1")
        result = manager.delete_task(999)

        assert result is False
        assert len(manager.list_tasks()) == 1

    def test_delete_task_only_removes_specified_task(self) -> None:
        """Test that deleting one task doesn't affect others."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

        manager.delete_task(2)

        tasks = manager.list_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[1].id == 3


class TestUpdateTask:
    """Tests for update_task method."""

    def test_update_task_title(self) -> None:
        """Test updating task title."""
        manager = TodoManager()
        manager.add_task("Old title")
        result = manager.update_task(1, title="New title")

        assert result is True
        task = manager.get_task(1)
        assert task.title == "New title"

    def test_update_task_description(self) -> None:
        """Test updating task description."""
        manager = TodoManager()
        manager.add_task("Task", "Old description")
        result = manager.update_task(1, description="New description")

        assert result is True
        task = manager.get_task(1)
        assert task.description == "New description"

    def test_update_task_title_and_description(self) -> None:
        """Test updating both title and description."""
        manager = TodoManager()
        manager.add_task("Title", "Description")
        result = manager.update_task(1, title="New Title", description="New Description")

        assert result is True
        task = manager.get_task(1)
        assert task.title == "New Title"
        assert task.description == "New Description"

    def test_update_task_keeps_current_values_when_not_specified(self) -> None:
        """Test that current values are kept when not specified."""
        manager = TodoManager()
        manager.add_task("Title", "Description")
        manager.update_task(1, description="New Description")

        task = manager.get_task(1)
        assert task.title == "Title"
        assert task.description == "New Description"

    def test_update_task_returns_false_for_nonexistent_id(self) -> None:
        """Test that update_task returns False for nonexistent ID."""
        manager = TodoManager()
        result = manager.update_task(999, title="New title")

        assert result is False

    def test_update_task_rejects_empty_title(self) -> None:
        """Test that update_task rejects empty title."""
        manager = TodoManager()
        manager.add_task("Task")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.update_task(1, title="")


class TestMarkComplete:
    """Tests for mark_complete and mark_incomplete methods."""

    def test_mark_complete_sets_status(self) -> None:
        """Test that mark_complete sets is_complete to True."""
        manager = TodoManager()
        manager.add_task("Task")
        result = manager.mark_complete(1)

        assert result is True
        task = manager.get_task(1)
        assert task.is_complete is True

    def test_mark_incomplete_sets_status(self) -> None:
        """Test that mark_incomplete sets is_complete to False."""
        manager = TodoManager()
        manager.add_task("Task")
        manager.mark_complete(1)
        result = manager.mark_incomplete(1)

        assert result is True
        task = manager.get_task(1)
        assert task.is_complete is False

    def test_mark_complete_returns_false_for_nonexistent_id(self) -> None:
        """Test that mark_complete returns False for nonexistent ID."""
        manager = TodoManager()
        result = manager.mark_complete(999)

        assert result is False

    def test_mark_incomplete_returns_false_for_nonexistent_id(self) -> None:
        """Test that mark_incomplete returns False for nonexistent ID."""
        manager = TodoManager()
        result = manager.mark_incomplete(999)

        assert result is False


class TestGetTask:
    """Tests for get_task method."""

    def test_get_task_returns_task(self) -> None:
        """Test that get_task returns the correct task."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        task = manager.get_task(2)

        assert task is not None
        assert task.id == 2
        assert task.title == "Task 2"

    def test_get_task_returns_none_for_nonexistent_id(self) -> None:
        """Test that get_task returns None for nonexistent ID."""
        manager = TodoManager()
        task = manager.get_task(999)

        assert task is None


class TestIdStability:
    """Tests for ID stability requirement."""

    def test_ids_remain_stable_after_deletions(self) -> None:
        """Test that IDs don't change after deletions."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.delete_task(2)

        task1 = manager.get_task(1)
        task3 = manager.get_task(3)

        assert task1.id == 1
        assert task3.id == 3

    def test_next_id_continues_after_deletions(self) -> None:
        """Test that _next_id continues incrementing after deletions."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.delete_task(1)
        task = manager.add_task("Task 3")

        assert task.id == 3
