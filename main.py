# main.py
# Author: Shankar.K (Person 5 - Project Leader)
# Role: Entry Point + All Tests
# Description: Run the app or run all tests from this single file
#
# HOW TO RUN:
#   Launch app  → python main.py
#   Run tests   → python main.py test

import sys
import os
import unittest


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

def print_welcome():
    """Prints a welcome banner in terminal when the app starts."""
    print("=" * 50)
    print("  Student Grade Management System")
    print("=" * 50)
    print("  Team Members:")
    print("    Person 1 — Alice   → student.py")
    print("    Person 2 — Ben     → database.py")
    print("    Person 3 — Clara   → calculator.py")
    print("    Person 4 — David   → ui.py")
    print("    Person 5 — Eva     → main.py (this file)")
    print("=" * 50)
    print("  Starting app... please wait.")
    print("=" * 50)


def run_app():
    """Launch the Student Grade Management System GUI."""
    from ui import App
    print_welcome()
    app = App()
    app.mainloop()
    print("\nApp closed. Goodbye!")


# ─────────────────────────────────────────────
# TESTS
# ─────────────────────────────────────────────

class TestStudent(unittest.TestCase):
    """Tests for student.py — Alice's file"""

    def setUp(self):
        from student import Student
        self.Student = Student
        self.s = Student("S001", "Alice")

    def test_initial_state(self):
        self.assertEqual(self.s.student_id, "S001")
        self.assertEqual(self.s.name, "Alice")
        self.assertEqual(self.s.grades, {})

    def test_add_grade_valid(self):
        self.s.add_grade("Math", 85)
        self.assertEqual(self.s.grades["Math"], 85)

    def test_add_grade_over_100(self):
        with self.assertRaises(ValueError):
            self.s.add_grade("Math", 110)

    def test_add_grade_below_0(self):
        with self.assertRaises(ValueError):
            self.s.add_grade("Math", -5)

    def test_remove_grade(self):
        self.s.add_grade("Math", 85)
        self.s.remove_grade("Math")
        self.assertNotIn("Math", self.s.grades)

    def test_remove_missing_grade(self):
        with self.assertRaises(KeyError):
            self.s.remove_grade("Physics")

    def test_get_grade_count(self):
        self.s.add_grade("Math", 85)
        self.s.add_grade("Science", 90)
        self.assertEqual(self.s.get_grade_count(), 2)

    def test_get_passed_subjects(self):
        self.s.add_grade("Math", 85)
        self.s.add_grade("Science", 40)
        passed = self.s.get_passed_subjects()
        self.assertIn("Math", passed)
        self.assertNotIn("Science", passed)

    def test_to_dict_and_from_dict(self):
        from student import Student
        self.s.add_grade("Math", 90)
        s2 = Student.from_dict(self.s.to_dict())
        self.assertEqual(s2.name, "Alice")
        self.assertEqual(s2.grades["Math"], 90)


class TestCalculator(unittest.TestCase):
    """Tests for calculator.py — Clara's file"""

    def setUp(self):
        from student import Student
        self.Student = Student

    def test_average_normal(self):
        from calculator import calculate_average
        self.assertEqual(calculate_average({"Math": 80, "Science": 90}), 85.0)

    def test_average_empty(self):
        from calculator import calculate_average
        self.assertEqual(calculate_average({}), 0.0)

    def test_letter_grade(self):
        from calculator import get_letter_grade
        self.assertEqual(get_letter_grade(95), "A+")
        self.assertEqual(get_letter_grade(82), "A")
        self.assertEqual(get_letter_grade(72), "B")
        self.assertEqual(get_letter_grade(62), "C")
        self.assertEqual(get_letter_grade(52), "D")
        self.assertEqual(get_letter_grade(40), "F")

    def test_status(self):
        from calculator import get_status
        self.assertEqual(get_status(50), "Pass")
        self.assertEqual(get_status(49), "Fail")

    def test_highest_subject(self):
        from calculator import get_highest_subject
        self.assertEqual(get_highest_subject({"Math": 90, "English": 70}), "Math")

    def test_lowest_subject(self):
        from calculator import get_lowest_subject
        self.assertEqual(get_lowest_subject({"Math": 90, "English": 70}), "English")

    def test_class_average(self):
        from calculator import get_class_average
        s1 = self.Student("S001", "Alice"); s1.add_grade("Math", 80)
        s2 = self.Student("S002", "Bob");   s2.add_grade("Math", 60)
        self.assertEqual(get_class_average([s1, s2]), 70.0)

    def test_top_student(self):
        from calculator import get_top_student
        s1 = self.Student("S001", "Alice"); s1.add_grade("Math", 90)
        s2 = self.Student("S002", "Bob");   s2.add_grade("Math", 60)
        self.assertEqual(get_top_student([s1, s2]).name, "Alice")

    def test_grade_summary(self):
        from calculator import get_grade_summary
        s1 = self.Student("S001", "A"); s1.add_grade("Math", 95)
        s2 = self.Student("S002", "B"); s2.add_grade("Math", 40)
        summary = get_grade_summary([s1, s2])
        self.assertEqual(summary["A+"], 1)
        self.assertEqual(summary["F"],  1)

    def test_pass_fail_count(self):
        from calculator import get_pass_fail_count
        s1 = self.Student("S001", "A"); s1.add_grade("Math", 80)
        s2 = self.Student("S002", "B"); s2.add_grade("Math", 30)
        result = get_pass_fail_count([s1, s2])
        self.assertEqual(result["Pass"], 1)
        self.assertEqual(result["Fail"], 1)


class TestDatabase(unittest.TestCase):
    """Tests for database.py — Ben's file"""

    def setUp(self):
        from student import Student
        self.Student = Student
        self.DATA_FILE = "students_data.json"
        if os.path.exists(self.DATA_FILE):
            os.remove(self.DATA_FILE)
        self.students = []

    def tearDown(self):
        if os.path.exists(self.DATA_FILE):
            os.remove(self.DATA_FILE)

    def test_save_and_load(self):
        from database import save_students, load_students
        s = self.Student("S001", "Alice"); s.add_grade("Math", 85)
        save_students([s])
        loaded = load_students()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Alice")

    def test_add_student(self):
        from database import add_student
        add_student(self.students, self.Student("S001", "Alice"))
        self.assertEqual(len(self.students), 1)

    def test_add_duplicate(self):
        from database import add_student
        add_student(self.students, self.Student("S001", "Alice"))
        with self.assertRaises(ValueError):
            add_student(self.students, self.Student("S001", "Bob"))

    def test_delete_student(self):
        from database import add_student, delete_student
        add_student(self.students, self.Student("S001", "Alice"))
        delete_student(self.students, "S001")
        self.assertEqual(len(self.students), 0)

    def test_delete_missing(self):
        from database import delete_student
        with self.assertRaises(ValueError):
            delete_student(self.students, "S999")

    def test_find_student(self):
        from database import add_student, find_student
        add_student(self.students, self.Student("S001", "Alice"))
        self.assertIsNotNone(find_student(self.students, "S001"))

    def test_find_missing(self):
        from database import find_student
        self.assertIsNone(find_student(self.students, "S999"))

    def test_update_grade(self):
        from database import add_student, update_student_grade, find_student
        add_student(self.students, self.Student("S001", "Alice"))
        update_student_grade(self.students, "S001", "Math", 95)
        self.assertEqual(find_student(self.students, "S001").grades["Math"], 95)

    def test_get_all_ids(self):
        from database import add_student, get_all_ids
        add_student(self.students, self.Student("S001", "Alice"))
        add_student(self.students, self.Student("S002", "Bob"))
        self.assertIn("S001", get_all_ids(self.students))

    def test_get_student_count(self):
        from database import add_student, get_student_count
        add_student(self.students, self.Student("S001", "Alice"))
        self.assertEqual(get_student_count(self.students), 1)


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop()
        print("=" * 50)
        print("  Running All Tests")
        print("=" * 50)
        unittest.main(verbosity=2)
    else:
        run_app()
