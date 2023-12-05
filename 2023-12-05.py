def map_location(doc: str):
    string = doc.split("\n")
    seeds = [int(i) for i in string[0].split(" ")[1:]]

    maps = []
    map = {}
    for line in string[2:]:
        if line.split(" ")[-1] == "map:":
            maps.append(map)
            map = {}
            continue

        destination, source, range_length = [int(i) for i in line.split(" ")]
        source = range(source, source + range_length)
        destination = range(destination, destination + range_length)
        temp_map = {key: value for key, value in zip(source, destination)}
        map = {**map, **temp_map}

    location = []
    for seed in seeds:
        for map in maps:
            seed = map.get(seed, seed)
        location.append(seed)
    return location


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

assert min(map_location(sample)) == 35

# Actual
with open("2023-12-05.txt") as file:
    actual = file.read()

locations = map_location(actual)
min(locations)
