import copy
import re
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Spring:
    springs: list[str]
    segments: list[int]

    @classmethod
    def from_string(cls, string: str):
        _springs, _segments = string.split(" ", maxsplit=1)
        return cls(
            [part for part in _springs], [int(num) for num in _segments.split(",")]
        )

    @property
    def permute_string(self):
        need = sum(self.segments)
        have = len([i for i in self.springs if i == "#"])
        possibilities = list(combinations(self.mystery_springs, need - have))
        permutations = []
        for possibility in possibilities:
            new = copy.copy(self.springs)
            for loc in possibility:
                new[loc] = "#"
                new = ["." if i == "?" else i for i in new]
            permutations.append(new)
        return permutations

    @property
    def mystery_springs(self):
        return [ndx for ndx, spring in enumerate(self.springs) if spring == "?"]

    @property
    def valid_permutations(self):
        strings = ["".join(str_list) for str_list in self.permute_string]
        valid_springs = []
        for string in strings:
            cont_springs = [len(spring) for spring in re.findall("#{1,}", string)]
            if cont_springs == self.segments:
                valid_springs.append(string)
        return valid_springs


# Sample
sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

sample_springs = [Spring.from_string(string) for string in sample.split("\n")]
assert sum([len(spring.valid_permutations) for spring in sample_springs]) == 21

# Actual
with open("2023-12-12.txt") as file:
    actual = file.read()

actual_springs = [Spring.from_string(string) for string in actual.split("\n")]
sum([len(spring.valid_permutations) for spring in actual_springs])
