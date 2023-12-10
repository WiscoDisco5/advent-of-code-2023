import re


def parse_doc(doc: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    path, *key = doc.split("\n")
    path = [1 if letter == "R" else 0 for letter in path]
    key_list = [re.findall("[0-9A-Z]{3}", line) for line in key if line != ""]
    key_lookup = {str(find): (str(left), str(right)) for find, left, right in key_list}
    return path, key_lookup


def search(doc):
    location = "AAA"
    path, key_lookup = parse_doc(doc)
    steps = 0
    while location != "ZZZ":
        for direction in path:
            steps = steps + 1
            location = key_lookup[location][direction]
            if location == "ZZZ":
                break
    return steps


def ghost_search(doc):
    path, key_lookup = parse_doc(doc)
    location = [key for key in key_lookup.keys() if key.endswith("A")]
    steps = 0
    while not all([loc.endswith("Z") for loc in location]):
        for direction in path:
            steps = steps + 1
            location = [key_lookup[loc][direction] for loc in location]
            if all([loc.endswith("Z") for loc in location]):
                break
    return steps


# Sample
sample1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


assert search(sample1) == 2

sample2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


assert search(sample2) == 6

sample_ghost = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


assert ghost_search(sample_ghost) == 6

# Actual
with open("2023-12-08.txt") as file:
    actual = file.read()

search(actual)
ghost_search(actual)
