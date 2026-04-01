# calculator.py
# Author: Lakshmi.C (Person 3)
# Role: Grade Logic & Calculations
# Description: All functions for calculating averages, grades, and reports
# TODO: Fill in all the code below


def calculate_average(grades: dict) -> float:
    """Calculate and return the average mark from a grades dictionary.
    Return 0.0 if grades is empty."""
    pass


def get_letter_grade(average: float) -> str:
    """Convert a numeric average to a letter grade.
    90+ = A+, 80+ = A, 70+ = B, 60+ = C, 50+ = D, below 50 = F"""
    pass


def get_status(average: float) -> str:
    """Return 'Pass' if average is 50 or above, otherwise 'Fail'."""
    pass


def get_highest_subject(grades: dict) -> str:
    """Return the subject name with the highest mark.
    Return 'N/A' if grades is empty."""
    pass


def get_lowest_subject(grades: dict) -> str:
    """Return the subject name with the lowest mark.
    Return 'N/A' if grades is empty."""
    pass


def get_class_average(students: list) -> float:
    """Calculate the average mark across all students.
    Return 0.0 if no students have grades."""
    pass


def get_top_student(students: list):
    """Return the student object with the highest average.
    Return None if list is empty."""
    pass


def get_full_report(student) -> dict:
    """Generate and return a full grade report for one student.
    Must include: name, id, grades, average, letter, status,
    best_subject, weak_subject"""
    pass


def get_grade_summary(students: list) -> dict:
    """Return a dict counting how many students fall in each letter grade.
    Example: {"A+": 2, "A": 3, "B": 1, "C": 0, "D": 1, "F": 0}"""
    pass


def get_pass_fail_count(students: list) -> dict:
    """Return how many students passed and failed.
    Example: {"Pass": 8, "Fail": 2}"""
    pass
