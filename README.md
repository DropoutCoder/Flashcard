# 
# Flashcard

A command-line flashcard trainer written in Python. It remembers your scores and shows the cards you get wrong more often.

## Features

- Study session in the terminal with a score summary
- Smart picking: cards you miss appear more often
- Add your own cards from a menu
- Progress saved automatically in `cards.json`
- Unit tests with `unittest`

## How to run

Requires Python 3.

```bash
git clone https://github.com/DropoutCoder/Flashcard.git
cd Flashcard
python main.py
```

## Run the tests

```bash
python -m unittest discover -v
```

## Project structure

| File | Purpose |
|------|---------|
| `card.py` | `Card` class: question, answer, score, checking |
| `deck.py` | `Deck` class: collection of cards, weighted picking, save and load |
| `main.py` | Menu and study session |
| `tests/` | Automatic tests |

## What I learned

Python classes, JSON files, exceptions, unit testing, and the Git workflow with branches and pull requests.

