import json
import random
from card import Card


class Deck:
    """A collection of cards that picks the hard ones more often."""

    def __init__(self):
        self.cards = []

    def add_card(self, question, answer):
        """Create a Card, store it in the deck, and return it."""
        card = Card(question, answer)
        self.cards.append(card)
        return card

    def __len__(self):
        return len(self.cards)

    def weight_of(self, card):
        """A higher weight means the card is picked more often."""
        return max(1, 1 + card.times_wrong - card.times_right)

    def pick_card(self):
        """Pick one card at random, favoring cards you get wrong."""
        if not self.cards:
            raise ValueError("The deck is empty. Add some cards first.")
        weights = [self.weight_of(card) for card in self.cards]
        return random.choices(self.cards, weights=weights, k=1)[0]
    def save(self, filename):
        """Write all cards and their scores to a JSON file."""
        data = [card.to_dict() for card in self.cards]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, filename):
        """Read cards from a JSON file. If the file doesn't exist yet, return an empty deck."""
        deck = cls()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return deck
        deck.cards = [Card.from_dict(item) for item in data]
        return deck

if __name__ == "__main__":
    from collections import Counter

    deck = Deck()
    deck.add_card("What is 2 + 2?", "4")
    deck.add_card("Capital of France?", "Paris")
    deck.add_card("Limit of 1/x as x -> infinity?", "0")

    hard_card = deck.cards[1]
    hard_card.times_wrong = 5

    picks = Counter(deck.pick_card().question for _ in range(1000))
    print("Cards in deck:", len(deck))
    print(picks)