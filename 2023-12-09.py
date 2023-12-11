sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def decode(line: str):
    delta = [int(val) for val in line.split(" ")]
    last = [delta[-1]]
    while not all(val == 0 for val in delta):
        delta = [left - right for left, right in zip(delta[1:], delta[:-1])]
        last.append(delta[-1])

    return sum(last)


def decode_first(line: str):
    delta = [int(val) for val in line.split(" ")]
    first = [delta[0]]
    while not all(val == 0 for val in delta):
        delta = [left - right for left, right in zip(delta[1:], delta[:-1])]
        first.append(delta[0])
    return sum(first[::2]) - sum(first[1::2])


assert sum(decode(line) for line in sample.split("\n")) == 114
assert sum(decode_first(line) for line in sample.split("\n")) == 2


# Actual
with open("2023-12-09.txt") as file:
    actual = file.read()

sum(decode(line) for line in actual.split("\n"))
sum(decode_first(line) for line in actual.split("\n"))
