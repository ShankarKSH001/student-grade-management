# database.py
# Author: R.S.Muralikrishnan (Person 2)
# Role: Database / File Handling
# Description: Save and load student data using JSON file handling
# Commit Message: Implemented database file handling functions - Ben

import json
import os
from student import Student

DATA_FILE = "students_data.json"


def load_students():
    """Load all students from the JSON file.
    Return empty list if file doesn't exist yet."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return [Student.from_dict(d) for d in data]
    except (json.JSONDecodeError, KeyError):
        print("Warning: Could not read data file. Starting fresh.")
        return []


def save_students(students):
    """Save a list of Student objects to the JSON file."""
    data = [s.to_dict() for s in students]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_student(students, student):
    """Add a new student and save.
    Raise ValueError if student ID already exists."""
    for s in students:
        if s.student_id == student.student_id:
            raise ValueError(f"Student ID '{student.student_id}' already exists.")
    students.append(student)
    save_students(students)


def delete_student(students, student_id):
    """Remove a student by ID and save.
    Raise ValueError if ID not found."""
    for i, s in enumerate(students):
        if s.student_id == student_id:
            students.pop(i)
            save_students(students)
            return
    raise ValueError(f"Student ID '{student_id}' not found.")


def find_student(students, student_id):
    """Find and return a student by ID. Return None if not found."""
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def update_student_grade(students, student_id, subject, mark):
    """Find student by ID, update their grade for a subject, and save.
    Raise ValueError if student not found."""
    student = find_student(students, student_id)
    if student is None:
        raise ValueError(f"Student '{student_id}' not found.")
    student.add_grade(subject, mark)
    save_students(students)


def get_all_ids(students):
    """Return a list of all student IDs in the system.
    Example: ["S001", "S002", "S003"]"""
    return [s.student_id for s in students]


def get_student_count(students):
    """Return the total number of students in the system."""
    return len(students)
