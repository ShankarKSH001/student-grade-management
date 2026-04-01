# database.py
# Author: R.S.Muralikrishnan (Person 2)
# Role: Database / File Handling
# Description: Save and load student data using JSON file handling
# TODO: Fill in all the code below

import json
import os
from student import Student

DATA_FILE = "students_data.json"


def load_students():
    """Load all students from the JSON file.
    Return empty list if file doesn't exist yet."""
    pass


def save_students(students):
    """Save a list of Student objects to the JSON file."""
    pass


def add_student(students, student):
    """Add a new student and save.
    Raise ValueError if student ID already exists."""
    pass


def delete_student(students, student_id):
    """Remove a student by ID and save.
    Raise ValueError if ID not found."""
    pass


def find_student(students, student_id):
    """Find and return a student by ID.
    Return None if not found."""
    pass


def update_student_grade(students, student_id, subject, mark):
    """Find student by ID, update their grade for a subject, and save.
    Raise ValueError if student not found."""
    pass


def get_all_ids(students):
    """Return a list of all student IDs in the system.
    Example: ["S001", "S002", "S003"]"""
    pass


def get_student_count(students):
    """Return the total number of students in the system."""
    pass
