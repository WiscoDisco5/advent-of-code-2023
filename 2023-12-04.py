import re
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winning_numbers: list[int]
    observed_numbers: list[int]

    @classmethod
    def from_string(cls, string: str):
        strip_string = re.sub("\s{1,}", " ", string)
        _id, obs = strip_string.split(sep=":")

        _id = int(_id.split(" ")[-1])

        _winning_numbers, _observed_numbers = obs.split(" | ")
        _winning_numbers = [int(win) for win in _winning_numbers.strip().split(" ")]
        _observed_numbers = [int(num) for num in _observed_numbers.strip().split(" ")]
        return cls(_id, _winning_numbers, _observed_numbers)

    @property
    def observed_winning_numbers(self):
        return [
            number for number in self.observed_numbers if number in self.winning_numbers
        ]

    @property
    def score(self):
        if self.observed_winning_numbers:
            return 2 ** (len(self.observed_winning_numbers) - 1)
        return 0

    def additional_cards_won(self, max_id: int):
        wins = self.observed_winning_numbers
        return [i + 1 for i in range(self.id, min(self.id + len(wins), max_id))]


# Sample
sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

sample_cards = [Card.from_string(card) for card in sample.split("\n")]
assert sum(card.score for card in sample_cards) == 13

cards = sample_cards


def count_cards(cards: list[Card]):
    cards_dict = {card.id: card for card in cards}
    cards_to_score = cards
    number_of_cards = 0
    while True:
        number_of_cards = number_of_cards + len(cards_to_score)
        if not cards_to_score:
            break

        cards_to_score = [
            cards_dict[id]
            for card in cards_to_score
            for id in card.additional_cards_won(len(cards))
        ]

    return number_of_cards


assert count_cards(sample_cards) == 30

# Actual
with open("2023-12-04.txt") as file:
    actual = file.read()

actual_cards = [Card.from_string(card) for card in actual.split("\n")]
sum(card.score for card in actual_cards)

count_cards(actual_cards)
