# ui.py
# Author: Karthikeyan.M (Person 4)
# Role: User Interface (Tkinter GUI)
# Description: Builds all windows, forms, buttons and the visual layout
# TODO: Fill in all the code below

import tkinter as tk
from tkinter import ttk, messagebox
from calculator import get_full_report, get_class_average, get_top_student, get_pass_fail_count
from database import (
    load_students, add_student, delete_student,
    find_student, update_student_grade, get_student_count
)
from student import Student

# TODO: Define colour theme variables here
# Suggested: BG, SURFACE, ACCENT, TEXT, GREEN, RED, YELLOW, BLUE
# Example: BG = "#1e1e2e"


class App(tk.Tk):
    """Main application window."""

    def __init__(self):
        super().__init__()
        # TODO: Set window title, size (960x660), background colour
        # Load students from database
        # Call self._build_ui()
        pass

    def _build_ui(self):
        """Build full UI — title bar, left form panel, right table panel."""
        # TODO: Create title bar with app name and all team member names
        # Create left panel (form) and right panel (table + stats)
        pass

    def _build_form(self, parent):
        """Left panel — Add Student, Add Grade, Delete Student forms."""
        # TODO: Build 3 sections:
        # 1. Add Student  → ID + Name fields + Add button
        # 2. Add Grade    → ID + Subject + Mark fields + Save button
        # 3. Delete       → ID field + Delete button
        pass

    def _build_table(self, parent):
        """Right panel — table showing all students and their grades."""
        # TODO: ttk.Treeview with columns:
        # ID | Name | Subjects | Average | Grade | Status
        # Add a Refresh button below
        pass

    def _build_stats(self, parent):
        """Bottom stats bar — totals, class average, top student, pass/fail."""
        # TODO: Show:
        # Total Students | Class Average | Top Student
        # Passed count | Failed count
        pass

    def _add_student(self):
        """Read form inputs and add a new student."""
        # TODO: Get ID and Name from entry fields
        # Call add_student() from database.py
        # Show success or error messagebox
        # Refresh table and stats
        pass

    def _add_grade(self):
        """Read form inputs and save a grade for a student."""
        # TODO: Get ID, Subject, Mark from entry fields
        # Validate mark is a valid number
        # Call update_student_grade() from database.py
        # Show success or error messagebox
        # Refresh table and stats
        pass

    def _delete_student(self):
        """Read ID input and delete that student."""
        # TODO: Get ID from entry field
        # Ask user to confirm with messagebox.askyesno()
        # Call delete_student() from database.py
        # Refresh table and stats
        pass

    def _refresh_table(self):
        """Clear and reload the student table from saved data."""
        # TODO: Clear all rows from self.tree
        # Reload students using load_students()
        # Insert each student as a new row
        pass

    def _update_stats(self):
        """Update the stats bar labels with latest data."""
        # TODO: Recalculate and display:
        # total students, class average, top student name
        # passed count, failed count
        pass
