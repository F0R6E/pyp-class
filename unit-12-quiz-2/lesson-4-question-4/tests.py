import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_4(self):
        animals = [Cat('Michi'), Cat('Jerry'), Dog('Scooby'), Cow('Dolly')]
        talks = ['{}: {}'.format(a.name, a.talk()) for a in animals]
        expected = [
            'Michi: Meow!',
            'Jerry: Meow!',
            'Scooby: Woof! Woof!',
            'Dolly: Moo! Moo!',
        ]
        self.assertEqual(talks, expected)

        animal = Animal("No name")
        with self.assertRaises(NotImplementedError):
            animal.talk()
