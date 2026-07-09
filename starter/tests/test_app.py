"""
Task Manager Tests — Starter Code
==================================

These tests verify that the TaskManager class works correctly.

Some tests are written and PASSING (to show students what tests look like).
Some tests are written and FAILING (to motivate the AI-assisted coding exercise).
Some tests are SKIPPED (to be enabled after implementing TODO methods).

Run: pytest tests/ -v
"""

import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import TaskManager
from utils import validate_task_name, format_date


# ─────────────────────────────────────────────────────────────────
# PASSING TESTS — These demonstrate what good tests look like
# ─────────────────────────────────────────────────────────────────

class TestAddTask:
    """Tests for the add_task method."""

    def test_add_task_returns_dict_with_id(self):
        """Adding a task should return a dictionary with an assigned ID."""
        manager = TaskManager()
        result = manager.add_task("Learn Git")
        assert isinstance(result, dict)
        assert "id" in result
        assert result["id"] == 1

    def test_add_task_increments_id(self):
        """Each new task should get a unique, incrementing ID."""
        manager = TaskManager()
        t1 = manager.add_task("Task 1")
        t2 = manager.add_task("Task 2")
        t3 = manager.add_task("Task 3")
        assert t1["id"] == 1
        assert t2["id"] == 2
        assert t3["id"] == 3

    def test_add_task_strips_whitespace(self):
        """Task titles should have leading/trailing whitespace removed."""
        manager = TaskManager()
        result = manager.add_task("  Learn Git  ")
        assert result["title"] == "Learn Git"

    def test_add_task_with_description(self):
        """Tasks should accept an optional description."""
        manager = TaskManager()
        result = manager.add_task("Learn Git", "Clone, commit, push")
        assert result["description"] == "Clone, commit, push"

    def test_add_task_empty_title_raises_error(self):
        """Empty task titles should raise ValueError."""
        manager = TaskManager()
        with pytest.raises(ValueError):
            manager.add_task("")

    def test_add_task_whitespace_title_raises_error(self):
        """Whitespace-only task titles should raise ValueError."""
        manager = TaskManager()
        with pytest.raises(ValueError):
            manager.add_task("   ")


class TestListTasks:
    """Tests for the list_tasks method."""

    def test_list_tasks_empty(self):
        """Listing tasks on an empty manager should return an empty list."""
        manager = TaskManager()
        assert manager.list_tasks() == []

    def test_list_tasks_returns_all(self):
        """Listing tasks should return all added tasks."""
        manager = TaskManager()
        manager.add_task("Task A")
        manager.add_task("Task B")
        manager.add_task("Task C")
        assert len(manager.list_tasks()) == 3

    def test_list_tasks_returns_copy(self):
        """list_tasks should return a copy, not the internal list."""
        manager = TaskManager()
        manager.add_task("Task A")
        tasks = manager.list_tasks()
        tasks.clear()
        assert len(manager.list_tasks()) == 1  # Original unaffected


class TestGetTask:
    """Tests for the get_task method."""

    def test_get_task_by_id(self):
        """Should return the correct task by ID."""
        manager = TaskManager()
        manager.add_task("Task A")
        manager.add_task("Task B")
        result = manager.get_task(2)
        assert result["title"] == "Task B"

    def test_get_task_nonexistent_returns_none(self):
        """Should return None for a non-existent task ID."""
        manager = TaskManager()
        assert manager.get_task(999) is None


class TestValidateTaskName:
    """Tests for the validate_task_name utility."""

    def test_valid_name(self):
        assert validate_task_name("Learn Git") is True

    def test_empty_string(self):
        assert validate_task_name("") is False

    def test_whitespace_only(self):
        assert validate_task_name("   ") is False

    def test_non_string(self):
        assert validate_task_name(123) is False

    def test_none(self):
        assert validate_task_name(None) is False


class TestFormatDate:
    """Tests for the format_date utility."""

    def test_valid_date(self):
        result = format_date("2024-01-15T10:30:00")
        assert "January" in result
        assert "2024" in result

    def test_invalid_date(self):
        result = format_date("not-a-date")
        assert result == "Unknown date"

    def test_none(self):
        result = format_date(None)
        assert result == "Unknown date"


# ─────────────────────────────────────────────────────────────────
# FAILING TESTS — These motivate the AI-assisted coding exercise
# Students will implement the methods to make these pass
# ─────────────────────────────────────────────────────────────────

class TestDeleteTask:
    """Tests for the delete_task method — currently failing."""

    def test_delete_existing_task(self):
        """Deleting an existing task should return True."""
        manager = TaskManager()
        task = manager.add_task("Learn Git")
        result = manager.delete_task(task["id"])
        assert result is True

    def test_delete_nonexistent_task(self):
        """Deleting a non-existent task should return False."""
        manager = TaskManager()
        result = manager.delete_task(999)
        assert result is False

    def test_delete_removes_from_list(self):
        """After deletion, the task should not appear in list_tasks."""
        manager = TaskManager()
        task = manager.add_task("Learn Git")
        manager.delete_task(task["id"])
        assert len(manager.list_tasks()) == 0


class TestMarkComplete:
    """Tests for the mark_complete method — currently failing."""

    def test_mark_complete_existing(self):
        """Marking a task complete should set completed=True."""
        manager = TaskManager()
        task = manager.add_task("Learn Git")
        result = manager.mark_complete(task["id"])
        assert result is not None
        assert result["completed"] is True

    def test_mark_complete_nonexistent(self):
        """Marking a non-existent task complete should return None."""
        manager = TaskManager()
        result = manager.mark_complete(999)
        assert result is None


class TestSearchTasks:
    """Tests for the search_tasks method — currently failing."""

    def test_search_finds_matching(self):
        """Search should return tasks matching the keyword."""
        manager = TaskManager()
        manager.add_task("Learn Git", "Version control basics")
        manager.add_task("Learn Python", "Programming language")
        manager.add_task("Buy groceries", "Milk and bread")
        results = manager.search_tasks("Learn")
        assert len(results) == 2

    def test_search_no_match(self):
        """Search with no matches should return empty list."""
        manager = TaskManager()
        manager.add_task("Learn Git")
        results = manager.search_tasks("nonexistent")
        assert results == []

    def test_search_empty_manager(self):
        """Search on empty manager should return empty list."""
        manager = TaskManager()
        results = manager.search_tasks("anything")
        assert results == []

    def test_search_case_insensitive(self):
        """Search should be case-insensitive."""
        manager = TaskManager()
        manager.add_task("Learn Git")
        results = manager.search_tasks("git")
        assert len(results) == 1
