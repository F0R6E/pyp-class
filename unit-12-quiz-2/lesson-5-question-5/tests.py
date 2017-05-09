import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_5(self):
        p1 = Photo("sunshine.jpg")
        p2 = Photo("landscape.jpg")
        p3 = Photo("car.jpg")

        pa = PhotoAlbum()
        pa.add_photo(p1)
        pa.add_photo(p2)
        pa.add_photo(p3)

        # supports both Python 2.x and 3.x
        self.assertTrue(isinstance(pa.__next__(), Photo))
        self.assertTrue(isinstance(pa.next(), Photo))

        # iterable with list comprehension
        self.assertEqual(len([p for p in pa]), 3)

        # iterable with a For loop
        results = []
        for photo in pa:
            results.append(str(photo))
        print(results)
        expected = [
            '/home/rmotr/photos/sunshine.jpg',
            '/home/rmotr/photos/landscape.jpg',
            '/home/rmotr/photos/car.jpg',
        ]
        self.assertEqual(results, expected)
