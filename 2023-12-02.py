from dataclasses import dataclass

from numpy import prod

KEY = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@dataclass
class Draw:
    color: str
    count: int

    @classmethod
    def from_string(cls, string: str):
        _count, _color = string.split(" ", maxsplit=2)
        return cls(_color, int(_count))

    def valid_draw(self, key: dict[str, int] = KEY):
        theoretical_max = key.get(self.color, None)
        if theoretical_max:
            return self.count <= theoretical_max
        return False


@dataclass
class Game:
    id: int
    draws: list[Draw]

    @classmethod
    def from_string(cls, string: str):
        _id = string.split(":")[0].split(" ")[-1]
        _raw_draws = string.split(": ")[-1].split("; ")
        _temp_draws = [draw.split(", ") for draw in _raw_draws]
        # Observation: it doesn't matter what set a particular observation of a certain
        # color occurs in.
        _draws = [Draw.from_string(obs) for draw in _temp_draws for obs in draw]

        return cls(id=int(_id), draws=_draws)

    def valid_game(self, key: dict[str, int] = KEY) -> bool:
        for draw in self.draws:
            if not draw.valid_draw(key):
                return False
        return True

    def minimum_bag(self) -> dict[str, int]:
        min_bag = {}
        for draw in self.draws:
            current = min_bag.get(draw.color, None)
            if current is None or draw.count > current:
                min_bag[draw.color] = draw.count
        return min_bag

    def power_bag(self) -> int:
        min_bag = self.minimum_bag()
        return prod(list(min_bag.values()))


# Test
test_games_str = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test_games = [Game.from_string(test_game) for test_game in test_games_str.split("\n")]
valid_test_games = [game.id for game in test_games if game.valid_game()]

assert sum(valid_test_games) == 8

power_test_games = [game.power_bag() for game in test_games]
assert sum(power_test_games) == 2286

# Actual
with open("2023-12-02.txt") as file:
    raw_games_str = file.read()

raw_games = [Game.from_string(raw_game) for raw_game in raw_games_str.split("\n")]
valid_raw_games = [game.id for game in raw_games if game.valid_game()]
sum(valid_raw_games)

power_raw_games = [game.power_bag() for game in raw_games]
sum(power_raw_games)
