import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_3(self):
        s1 = Student("John", "Doe", 25)
        s2 = Student("Richard", "Mc Cabe", 30, "England")
        s3 = Student("Michael", "Moore", 30, "United States")

        self.assertTrue(Student.compatriot(s1, s3))
        self.assertFalse(Student.compatriot(s2, s3))
