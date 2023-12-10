from collections import Counter
from dataclasses import dataclass
from enum import IntEnum

Card = IntEnum(
    "Card", ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
)

JokerCard = IntEnum(
    "JokerCard", ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
)

HandClassification = IntEnum(
    "HandClassification",
    [
        "High Card",
        "One Pair",
        "Two Pair",
        "Three of a Kind",
        "Full House",
        "Four of a Kind",
        "Five of a Kind",
    ],
)


@dataclass
class Hand:
    cards: list[Card | JokerCard]
    bid: int

    @classmethod
    def from_string(cls, string: str, joker_deck: bool = False):
        _card_string, _bid = string.split(" ")
        if joker_deck:
            return cls([JokerCard[i] for i in _card_string], int(_bid))
        return cls([Card[i] for i in _card_string], int(_bid))

    @property
    def grouped_cards(self):
        return Counter(self.cards).most_common()

    @property
    def hand_classification(self):
        if all(isinstance(card, JokerCard) for card in self.cards):
            joker_count = len([card for card in self.cards if card == JokerCard.J])
            counts = [
                count for card, count in self.grouped_cards if card != JokerCard.J
            ]
            if counts:
                counts[0] = counts[0] + joker_count
            else:
                # All joker hand
                counts = [5]
        else:
            counts = [count for _, count in self.grouped_cards]
        if counts[0] == 5:
            return HandClassification["Five of a Kind"]
        if counts[0] == 4:
            return HandClassification["Four of a Kind"]
        if counts[0] == 3 and counts[1] == 2:
            return HandClassification["Full House"]
        if counts[0] == 3:
            return HandClassification["Three of a Kind"]
        if counts[0] == 2 and counts[1] == 2:
            return HandClassification["Two Pair"]
        if counts[0] == 2:
            return HandClassification["One Pair"]
        if counts[0] == 1:
            return HandClassification["High Card"]
        raise ValueError(f"No classification for {self.cards}")

    def __lt__(self, other):
        if self.hand_classification < other.hand_classification:
            return True
        if self.hand_classification == other.hand_classification:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card == other_card:
                    continue
                return self_card < other_card
        return False


# Sample
sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

sample_hands = [Hand.from_string(line) for line in sample.split("\n")]
sorted_sample_hands = sorted(sample_hands)
assert sum((n + 1) * hand.bid for n, hand in enumerate(sorted_sample_hands)) == 6440

sample_joker_hands = [
    Hand.from_string(line, joker_deck=True) for line in sample.split("\n")
]
sorted_sample_joker_hands = sorted(sample_joker_hands)
assert (
    sum((n + 1) * hand.bid for n, hand in enumerate(sorted_sample_joker_hands)) == 5905
)


# Actual
with open("2023-12-07.txt") as file:
    actual = file.read()

actual_hands = [Hand.from_string(line) for line in actual.split("\n")]
sorted_actual_hands = sorted(actual_hands)
sum((n + 1) * hand.bid for n, hand in enumerate(sorted_actual_hands))

# p2
actual_joker_hands = [
    Hand.from_string(line, joker_deck=True) for line in actual.split("\n")
]
sorted_actual_joker_hands = sorted(actual_joker_hands)
sum((n + 1) * hand.bid for n, hand in enumerate(sorted_actual_joker_hands))
