# student.py
# Author: Manikandan.S (Person 1)
# Role: Student Class (OOP)
# Description: Define the Student class with all attributes and methods
# TODO: Fill in all the code below


class Student:
    """Represents a single student with name, ID, and grades."""

    def __init__(self, student_id, name):
        # TODO: Store student_id, name, and an empty grades dictionary
        pass

    def add_grade(self, subject, mark):
        """Add or update a grade for a subject.
        Raise ValueError if mark is not between 0 and 100."""
        pass

    def remove_grade(self, subject):
        """Remove a subject grade.
        Raise KeyError if subject doesn't exist."""
        pass

    def get_grades(self):
        """Return a copy of the grades dictionary."""
        pass

    def get_grade_count(self):
        """Return total number of subjects this student has grades for.
        Example: {"Math": 85, "Science": 90} → returns 2"""
        pass

    def get_passed_subjects(self):
        """Return list of subjects where student scored 50 or above.
        Example: {"Math": 85, "Science": 40} → ["Math"]"""
        pass

    def to_dict(self):
        """Convert student object to dictionary for saving to file.
        Must return: {"student_id": ..., "name": ..., "grades": ...}"""
        pass

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary loaded from file."""
        pass

    def __str__(self):
        """Return a readable string of the student."""
        pass

    def __repr__(self):
        return self.__str__()
