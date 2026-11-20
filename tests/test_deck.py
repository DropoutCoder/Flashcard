import os
import tempfile
import unittest

from deck import Deck


class TestDeck(unittest.TestCase):
    def test_add_card_increases_length(self):
        deck = Deck()
        deck.add_card("Q1", "A1")
        deck.add_card("Q2", "A2")
        self.assertEqual(len(deck), 2)

    def test_pick_from_empty_deck_raises_error(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.pick_card()

    def test_weight_never_goes_below_one(self):
        deck = Deck()
        card = deck.add_card("Q", "A")
        card.times_right = 10
        self.assertEqual(deck.weight_of(card), 1)

    def test_wrong_answers_increase_weight(self):
        deck = Deck()
        card = deck.add_card("Q", "A")
        card.times_wrong = 4
        self.assertEqual(deck.weight_of(card), 5)

    def test_save_and_load(self):
        deck = Deck()
        card = deck.add_card("Q", "A")
        card.times_wrong = 2
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "cards.json")
            deck.save(path)
            loaded = Deck.load(path)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded.cards[0].question, "Q")
        self.assertEqual(loaded.cards[0].times_wrong, 2)

    def test_load_missing_file_gives_empty_deck(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "does_not_exist.json")
            loaded = Deck.load(path)
        self.assertEqual(len(loaded), 0)


if __name__ == "__main__":
    unittest.main()