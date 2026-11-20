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

    def __str__(self):
        return f"{self.question} -> {self.answer} (right: {self.times_right}, wrong: {self.times_wrong})"


if __name__ == "__main__":
    card = Card("What is 2 + 2?", "4")
    print(card.check_answer("4"))
    print(card.check_answer("5"))
    print(card)