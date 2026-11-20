class Card:
    """One flashcard: a question, its answer, and a score of how well you know it."""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.times_right = 0
        self.times_wrong = 0

    def check_answer(self, user_answer):
        """Return True if the answer is correct, and update the score."""
        if user_answer.strip().lower() == self.answer.strip().lower():
            self.times_right += 1
            return True
        self.times_wrong += 1
        return False
    def to_dict(self):
        """Turn this card into a plain dictionary so it can be saved as JSON."""
        return {
            "question": self.question,
            "answer": self.answer,
            "times_right": self.times_right,
            "times_wrong": self.times_wrong,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Card from a dictionary (the opposite of to_dict)."""
        card = cls(data["question"], data["answer"])
        card.times_right = data["times_right"]
        card.times_wrong = data["times_wrong"]
        return card
    def __str__(self):
        return f"{self.question} -> {self.answer} (right: {self.times_right}, wrong: {self.times_wrong})"


if __name__ == "__main__":
    card = Card("What is 2 + 2?", "4")
    print(card.check_answer("4"))
    print(card.check_answer("5"))
    print(card)