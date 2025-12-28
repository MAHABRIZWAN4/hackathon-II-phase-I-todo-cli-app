"""Integration tests for CLI interface."""

import subprocess
import sys
from io import StringIO
from unittest.mock import patch

import pytest

from main import main


class TestCLI:
    """Integration tests for CLI operations."""

    def test_add_task_and_view(self) -> None:
        """Test adding a task and viewing it."""
        inputs = ["1", "Test Task", "Test Description", "2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Task added with ID 1" in result.stdout
        assert "1. [ ] Test Task" in result.stdout
        assert result.returncode == 0

    def test_add_multiple_tasks(self) -> None:
        """Test adding multiple tasks and viewing all."""
        inputs = ["1", "Task 1", "", "1", "Task 2", "Description 2", "2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Task added with ID 1" in result.stdout
        assert "Task added with ID 2" in result.stdout
        assert "Task 1" in result.stdout
        assert "Task 2" in result.stdout

    def test_mark_task_complete(self) -> None:
        """Test marking a task as complete."""
        inputs = ["1", "Complete Me", "", "5", "1", "y", "2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Task marked complete" in result.stdout
        assert "1. [x] Complete Me" in result.stdout

    def test_delete_task(self) -> None:
        """Test deleting a task."""
        inputs = ["1", "To Delete", "", "4", "1", "2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Task deleted successfully" in result.stdout
        assert "No tasks found" in result.stdout

    def test_update_task(self) -> None:
        """Test updating a task."""
        inputs = ["1", "Original Title", "", "3", "1", "New Title", "", "2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Task updated successfully" in result.stdout
        assert "New Title" in result.stdout

    def test_empty_list_message(self) -> None:
        """Test that empty list shows appropriate message."""
        inputs = ["2", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "No tasks found" in result.stdout

    def test_invalid_id_error(self) -> None:
        """Test error handling for invalid task ID."""
        inputs = ["4", "999", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Error: Task with ID 999 not found" in result.stdout

    def test_empty_title_error(self) -> None:
        """Test error handling for empty title."""
        inputs = ["1", "", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Error: Title cannot be empty" in result.stdout

    def test_invalid_menu_choice(self) -> None:
        """Test error handling for invalid menu choice."""
        inputs = ["7", "6"]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        assert "Invalid choice" in result.stdout


class TestFullWorkflow:
    """Full workflow integration tests."""

    def test_complete_user_journey(self) -> None:
        """Test a complete user workflow: add, view, update, complete, delete."""
        inputs = [
            "1", "Buy Groceries", "Milk and bread",
            "1", "Call Mom", "",
            "2",
            "3", "1", "Buy groceries and milk", "",
            "5", "1", "y",
            "2",
            "4", "2",
            "2",
            "6",
        ]
        result = subprocess.run(
            [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import main
main()
"""],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
            cwd="/mnt/d/Hackathon-II/phase-I",
        )

        # Verify all operations worked
        assert "Task added with ID 1" in result.stdout
        assert "Task added with ID 2" in result.stdout
        assert "Task updated successfully" in result.stdout
        assert "Task marked complete" in result.stdout
        assert "Task deleted successfully" in result.stdout
        assert "Goodbye!" in result.stdout
        assert result.returncode == 0
