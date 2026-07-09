"""
Utility Functions — Starter Code
=================================

Helper functions for the Task Manager application.
Some functions are complete; some are TODOs for the AI-assisted coding exercise.

This file demonstrates how a real project separates concerns:
- app.py = the main application logic
- utils.py = reusable helper functions

In a professional team, this separation makes code easier to
maintain, test, and review.
"""

from datetime import datetime


def validate_task_name(name):
    """
    Validate that a task name is acceptable.

    Args:
        name (str): The task name to validate

    Returns:
        bool: True if valid (non-empty string), False otherwise

    Example:
        >>> validate_task_name("Learn Git")
        True
        >>> validate_task_name("")
        False
        >>> validate_task_name("   ")
        False
    """
    if not isinstance(name, str):
        return False
    return len(name.strip()) > 0


def format_date(iso_string):
    """
    Convert an ISO datetime string to a human-readable format.

    Args:
        iso_string (str): ISO format datetime string (e.g., "2024-01-15T10:30:00")

    Returns:
        str: Human-readable date (e.g., "January 15, 2024 at 10:30 AM")

    Example:
        >>> format_date("2024-01-15T10:30:00")
        'January 15, 2024 at 10:30 AM'
    """
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except (ValueError, TypeError):
        return "Unknown date"


# ═══════════════════════════════════════════════════════════════
# EXERCISE: Implement the functions below using AI assistance
# ═══════════════════════════════════════════════════════════════

def priority_label(priority_number):
    """
    Convert a priority number to a human-readable label.

    TODO: Implement this function.

    Args:
        priority_number (int): 1=High, 2=Medium, 3=Low

    Returns:
        str: "High", "Medium", "Low", or "Unknown"

    Example:
        >>> priority_label(1)
        'High'
        >>> priority_label(3)
        'Low'
        >>> priority_label(99)
        'Unknown'
    """
    # TODO: Implement this with AI assistance
    pass


def truncate_text(text, max_length=50):
    """
    Truncate text to a maximum length, adding "..." if truncated.

    TODO: Implement this function.

    Args:
        text (str): The text to truncate
        max_length (int): Maximum length before truncation

    Returns:
        str: Truncated text with "..." if needed

    Example:
        >>> truncate_text("Hello World", 5)
        'He...'
        >>> truncate_text("Short", 50)
        'Short'
    """
    # TODO: Implement this with AI assistance
    pass
