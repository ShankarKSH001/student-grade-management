# student.py
# Author: Manikandan.S (Person 1)
# Role: Student Class (OOP)
# Description: Define the Student class with all attributes and methods
# Commit Message: Implemented Student class with all methods - Alice

class Student:
    """Represents a single student with name, ID, and grades."""

    def __init__(self, student_id, name):
        self.student_id = student_id      # Unique ID e.g. "S001"
        self.name = name                  # Student full name
        self.grades = {}                  # {"Math": 85, "Science": 90}

    def add_grade(self, subject, mark):
        """Add or update a grade. Raise ValueError if mark not 0–100."""
        if not (0 <= mark <= 100):
            raise ValueError(f"Mark must be between 0 and 100, got {mark}")
        self.grades[subject] = mark

    def remove_grade(self, subject):
        """Remove a subject grade. Raise KeyError if not found."""
        if subject in self.grades:
            del self.grades[subject]
        else:
            raise KeyError(f"Subject '{subject}' not found for {self.name}")

    def get_grades(self):
        """Return a copy of the grades dictionary."""
        return dict(self.grades)

    def get_grade_count(self):
        """Return total number of subjects this student has grades for.
        Example: {"Math": 85, "Science": 90} → 2"""
        return len(self.grades)

    def get_passed_subjects(self):
        """Return list of subjects where student scored 50 or above.
        Example: {"Math": 85, "Science": 40} → ["Math"]"""
        return [subject for subject, mark in self.grades.items() if mark >= 50]

    def to_dict(self):
        """Convert student object to dictionary for saving to file."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary loaded from file."""
        s = Student(data["student_id"], data["name"])
        s.grades = data.get("grades", {})
        return s

    def __str__(self):
        return f"Student({self.student_id}, {self.name}, Grades: {self.grades})"

    def __repr__(self):
        return self.__str__()
