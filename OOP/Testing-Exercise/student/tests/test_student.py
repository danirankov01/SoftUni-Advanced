from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Dani")
        self.student_with_course = Student("Ceco", {'C#': ['notes']})

    def test_initializing(self):
        self.assertEqual(self.student.name, "Dani")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student_with_course.name, "Ceco")
        self.assertEqual(self.student_with_course.courses, {'C#': ['notes']})

    def test_if_course_name_in_courses(self):
        result = self.student_with_course.enroll('C#', ['another_notes'])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(self.student_with_course.courses, {'C#': ['notes', 'another_notes']})
        self.assertEqual(result, expected)

    def test_if_course_name_not_in_courses_and_notes_equal_to_empty(self):
        result = self.student.enroll('python', ['notes'])
        self.assertEqual(self.student.courses, {'python': ['notes']})
        self.assertEqual("Course and course notes have been added.", result)

    def test_if_course_name_not_in_courses_and_notes_equal_to_Y(self):
        result = self.student.enroll('python', ['notes'], "Y")
        self.assertEqual(self.student.courses, {'python': ['notes']})
        self.assertEqual("Course and course notes have been added.", result)

    def test_adding_course_to_a_student(self):
        result = self.student.enroll('python', ['last_notes'], 'add')
        self.assertEqual(self.student.courses, {'python': []})
        self.assertEqual("Course has been added.", result)

    def test_add_notes_if_course_in_student_courses(self):
        result = self.student_with_course.add_notes('C#', 'notes')
        self.assertEqual(self.student_with_course.courses['C#'], ['notes', 'notes'])
        self.assertEqual("Notes have been updated", result)

    def test_add_if_course_not_in_student_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.add_notes('python', 'notes')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_in_students_courses(self):
        result = self.student_with_course.leave_course('C#')
        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual("Course has been removed", result)

    def test_leave_course_if_course_not_in_students_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course('python')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
