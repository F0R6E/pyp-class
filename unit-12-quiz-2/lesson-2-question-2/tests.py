import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_2(self):
        s1 = Student("John", "Doe", 25)
        s2 = Student("Richard", "Mc Cabe", 30, "England")
        s3 = Student("Michael", "Moore", 30, "United States")

        self.assertTrue(s1 < s2)
        self.assertTrue(s3 > s1)

        self.assertEqual(str(s1), "John Doe (25) from United States")
        self.assertEqual(str(s2), "Richard Mc Cabe (30) from England")
