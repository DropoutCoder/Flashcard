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


def add_cards(deck):
    """Let the user type new cards. Press Enter on an empty question to stop."""
    print("Add new cards. Press Enter on an empty question to stop.\n")
    added = 0

    while True:
        question = input("Question: ").strip()
        if question == "":
            break

        answer = input("Answer: ").strip()
        if answer == "":
            print("The answer can't be empty. Card not added.\n")
            continue

        deck.add_card(question, answer)
        added += 1
        print("Card added!\n")

    print(f"{added} card(s) added.")


def list_cards(deck):
    """Print every card with its number and score."""
    if len(deck) == 0:
        print("The deck is empty.")
        return

    for number, card in enumerate(deck.cards, start=1):
        print(f"{number}. {card}")


def show_menu():
    """Print the menu and return the user's choice."""
    print("\n=== Flashcards ===")
    print("1. Study")
    print("2. Add cards")
    print("3. List cards")
    print("q. Quit")
    return input("Choose: ").strip().lower()


def main():
    deck = Deck.load(DATA_FILE)
    if len(deck) == 0:
        deck = build_sample_deck()

    while True:
        choice = show_menu()

        if choice == "1":
            study(deck)
            deck.save(DATA_FILE)
        elif choice == "2":
            add_cards(deck)
            deck.save(DATA_FILE)
        elif choice == "3":
            list_cards(deck)
        elif choice == "q":
            break
        else:
            print("Please type 1, 2, 3 or q.")

    deck.save(DATA_FILE)
    print(f"Progress saved to {DATA_FILE}")


if __name__ == "__main__":
    main()