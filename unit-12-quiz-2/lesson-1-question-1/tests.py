import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_1(self):
        s1 = Student("John", "Doe", 25)
        s2 = Student("Richard", "Mc Cabe", 30, "England")
        s3 = Student("Michael", "Moore", 30, "United States")

        self.assertTrue(hasattr(Student, 'full_name'))

        self.assertEqual(s1.full_name, "John Doe")
        self.assertEqual(s1.country, "United States")

        self.assertEqual(s2.full_name, "Richard Mc Cabe")
        self.assertEqual(s3.full_name, "Michael Moore")
