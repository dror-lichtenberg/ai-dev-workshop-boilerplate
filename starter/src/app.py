"""
Task Manager API — Starter Code
================================

This is the main application for the AI Dev Workshop.

It implements a simple in-memory task manager that supports:
  - Adding tasks
  - Listing tasks
  - Deleting tasks (Exercise: implement this with AI assistance)

The code is intentionally simple — no frameworks, no databases,
no web servers. The focus is on the DEVELOPMENT WORKFLOW,
not the code itself.

Run: python src/app.py
Test: pytest tests/
"""

from datetime import datetime
from utils import format_date, validate_task_name


class TaskManager:
    """
    A simple in-memory task manager.

    Think of this as a to-do list that lives in your computer's memory.
    In a real application, this would connect to a database.

    Analogy: It's like a sticky-note board.
    - add_task() = writing a new sticky note and pinning it
    - list_tasks() = looking at all the notes on the board
    - delete_task() = removing a note from the board
    """

    def __init__(self):
        """Initialize an empty task manager."""
        self.tasks = []
        self._next_id = 1

    def add_task(self, title, description=""):
        """
        Add a new task to the manager.

        Args:
            title (str): The task title (required, must not be empty)
            description (str): Optional task description

        Returns:
            dict: The created task with an assigned ID and timestamp

        Raises:
            ValueError: If title is empty or not a string

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Learn Git")
            >>> task['title']
            'Learn Git'
        """
        if not validate_task_name(title):
            raise ValueError("Task title cannot be empty")

        task = {
            "id": self._next_id,
            "title": title.strip(),
            "description": description.strip(),
            "created_at": datetime.now().isoformat(),
            "completed": False,
        }
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        """
        List all tasks in the manager.

        Returns:
            list: A list of all task dictionaries (empty list if no tasks)

        Example:
            >>> manager = TaskManager()
            >>> manager.list_tasks()
            []
            >>> manager.add_task("Learn Git")
            >>> len(manager.list_tasks())
            1
        """
        if not self.tasks:
            return []
        return self.tasks.copy()

    def get_task(self, task_id):
        """
        Get a single task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            dict or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    # ═══════════════════════════════════════════════════════════════
    # EXERCISE: Implement the methods below using AI assistance
    # (Copilot, Claude Code, or ChatGPT)
    # ═══════════════════════════════════════════════════════════════

    def delete_task(self, task_id):
        """
        Remove a task from the manager by its ID.

        TODO: Implement this method.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Learn Git")
            >>> manager.delete_task(task['id'])
            True
            >>> manager.delete_task(999)
            False
        """
        # TODO: Implement this with AI assistance
        # Hint: Ask Copilot to "complete the delete_task method"
        # or use Claude Code: "implement delete_task in app.py"
        pass

    def mark_complete(self, task_id):
        """
        Mark a task as completed.

        TODO: Implement this method.

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            dict or None: The updated task if found, None otherwise
        """
        # TODO: Implement this with AI assistance
        pass

    def search_tasks(self, keyword):
        """
        Search for tasks by keyword in title or description.

        TODO: Implement this method.

        Args:
            keyword (str): The search term

        Returns:
            list: Tasks matching the keyword (empty list if none match)
        """
        # TODO: Implement this with AI assistance
        pass


# ─────────────────────────────────────────────────────────────────
# Demo: Run this file directly to see the task manager in action
# ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("📋 Task Manager Demo")
    print("=" * 50)

    manager = TaskManager()

    # Add some tasks
    print("\n📝 Adding tasks...")
    t1 = manager.add_task("Set up GitHub account", "Create account and verify email")
    t2 = manager.add_task("Learn Git basics", "Clone, commit, push")
    t3 = manager.add_task("Try GitHub Copilot", "Use AI to complete an exercise")

    # List tasks
    print("\n📄 All tasks:")
    for task in manager.list_tasks():
        status = "✓" if task["completed"] else "○"
        print(f"  {status} #{task['id']}: {task['title']}")

    # Get a specific task
    print(f"\n🔍 Task #2: {manager.get_task(2)['title']}")

    # Delete a task (uncomment after implementing!)
    # print("\n🗑️  Deleting task #1...")
    # manager.delete_task(1)
    # print(f"  Tasks remaining: {len(manager.list_tasks())}")

    print("\n" + "=" * 50)
    print("✅ Demo complete! Now implement the TODO methods.")
    print("=" * 50)
