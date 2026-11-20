from deck import Deck

DATA_FILE = "cards.json"

def build_sample_deck():
    """Make a small deck so we have something to practice with."""
    deck = Deck()
    deck.add_card("What is 7 * 8?", "56")
    deck.add_card("What word defines a function in Python?", "def")
    deck.add_card("Is a tuple mutable? (yes/no)", "no")
    deck.add_card("Which Git command downloads changes from GitHub?", "git pull")
    deck.add_card("What is the capital of Ethiopia?", "Addis Ababa")
    return deck


def print_summary(deck, asked, correct):
    """Show the score for this session and every card's record."""
    print("--- Session summary ---")
    print(f"Answered: {asked}, correct: {correct}")
    hardest_first = sorted(deck.cards, key=lambda card: card.times_wrong, reverse=True)
    for card in hardest_first:
        print(card)


def study(deck, rounds=5):
    """Ask up to `rounds` questions. Type 'q' to quit early."""
    if len(deck) == 0:
        print("The deck is empty. Add some cards first.")
        return

    asked = 0
    correct = 0
    print("Type your answer, or 'q' to quit.\n")

    for round_number in range(1, rounds + 1):
        card = deck.pick_card()
        user_answer = input(f"[{round_number}/{rounds}] {card.question}\n> ")

        if user_answer.strip().lower() == "q":
            break

        asked += 1
        if card.check_answer(user_answer):
            correct += 1
            print("Correct!\n")
        else:
            print(f"Wrong. The answer is: {card.answer}\n")

    print_summary(deck, asked, correct)


if __name__ == "__main__":
    deck = Deck.load(DATA_FILE)
    if len(deck) == 0:
        deck = build_sample_deck()
    study(deck)
    deck.save(DATA_FILE)
    print(f"\nProgress saved to {DATA_FILE}")