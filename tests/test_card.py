import unittest

from card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("What is 2 + 2?", "4")

    def test_correct_answer_returns_true_and_updates_score(self):
        self.assertTrue(self.card.check_answer("4"))
        self.assertEqual(self.card.times_right, 1)
        self.assertEqual(self.card.times_wrong, 0)

    def test_wrong_answer_returns_false_and_updates_score(self):
        self.assertFalse(self.card.check_answer("5"))
        self.assertEqual(self.card.times_right, 0)
        self.assertEqual(self.card.times_wrong, 1)

    def test_answer_ignores_case_and_spaces(self):
        card = Card("Capital of France?", "Paris")
        self.assertTrue(card.check_answer("  pArIs "))

    def test_dict_round_trip(self):
        self.card.times_right = 3
        self.card.times_wrong = 2
        copy = Card.from_dict(self.card.to_dict())
        self.assertEqual(copy.question, "What is 2 + 2?")
        self.assertEqual(copy.answer, "4")
        self.assertEqual(copy.times_right, 3)
        self.assertEqual(copy.times_wrong, 2)


if __name__ == "__main__":
    unittest.main()