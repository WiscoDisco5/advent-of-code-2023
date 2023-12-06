import re
from dataclasses import dataclass

from numpy import prod


@dataclass
class Race:
    time: int
    record_distance: int

    def distance(self, held_time: int) -> int:
        drive_time = self.time - held_time
        # held_time is velocity
        if drive_time > 0:
            return drive_time * held_time
        return 0

    @property
    def held_time_options(self):
        return [i + 1 for i in range(self.time)]

    @property
    def distance_possibilities(self):
        return [self.distance(time) for time in self.held_time_options]

    @property
    def winners(self):
        return [d for d in self.distance_possibilities if d > self.record_distance]


def prep_doc(doc: str):
    time, distance = [i.split()[1:] for i in doc.split("\n")]
    return [Race(int(i), int(j)) for i, j in zip(time, distance)]


# Sample
sample = """Time:      7  15   30
Distance:  9  40  200"""

sample_races = prep_doc(sample)
assert prod([len(race.winners) for race in sample_races]) == 288

# Actual
actual = """Time:        51     92     68     90
Distance:   222   2031   1126   1225"""

actual_races = prep_doc(actual)
prod([len(race.winners) for race in actual_races])

# Part 2
actual_2 = re.sub(" ", "", actual)
a_time, a_distance = [int(i) for i in re.sub("[^0-9\n]", "", actual_2).split("\n")]
a_race = Race(a_time, a_distance)
len(a_race.winners)
