import copy


def map_location(doc: str, expand_seeds: bool = False):
    string = doc.split("\n")
    seeds = [int(i) for i in string[0].split(" ")[1:]]
    if expand_seeds:
        # too inefficient
        new_seeds = []
        for seed_start, seed_range_length in zip(seeds[::2], seeds[1::2]):
            new_seeds += [i for i in range(seed_start, seed_start + seed_range_length)]
        seeds = new_seeds

    location = []
    for seed in seeds:
        mapped = False
        for line in string[2:]:
            if line == "":
                continue
            if line.split(" ")[-1] == "map:":
                mapped = False
                continue
            if mapped:
                continue
            destination, source, range_length = [int(i) for i in line.split(" ")]

            if seed >= source and seed < source + range_length:
                seed = destination + seed - source
                mapped = True
        location.append(seed)
    return seeds, location


# Sample
sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seeds, locations = map_location(sample)
assert min(locations) == 35

seeds, locations = map_location(sample, expand_seeds=True)
assert min(locations) == 46

# Actual
with open("2023-12-05.txt") as file:
    actual = file.read()

seeds, locations = map_location(actual)
min(locations)


seeds, locations = map_location(actual, expand_seeds=True)
min(locations)
