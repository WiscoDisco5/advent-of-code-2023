import re


def number_coordinates(string) -> list[tuple[int, tuple[int, int]]]:
    resultlist = []
    pos = 0
    prior_end = 0

    while True:
        result = re.search("\d{1,}", string)
        if result is None:
            break
        number = string[result.start() : result.end()]
        start = prior_end + result.start()
        end = start + result.end() - result.start()
        resultlist.append((number, (start, end)))

        prior_end = prior_end + result.end() + 1
        pos = result.end() + 1
        string = string[pos:]
    return resultlist


def check_char(location: int, string: str, n: int):
    next_row = [n, n + 1, n + 2]
    prior_row = [-n, -n - 1, -n - 2]

    search = [*next_row, *prior_row, -1, 1]

    chars = [
        string[loc + location]
        for loc in search
        if loc + location >= 0 and loc + location <= len(string)
    ]

    return re.search("[^0-9A-z\.\n]", "".join(chars)) is not None


def check_number(number: int, start: int, end: int, string: str, n: int):
    for i in range(start, end):
        if check_char(i, string, n):
            return int(number)
    return 0


# Check on sample
sample = """467..114..
...*......
..35..633.
abc...#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
sample_key = number_coordinates(sample)
check_sample = sum(
    check_number(number, start, end, sample, 10) for number, (start, end) in sample_key
)

assert check_sample == 4361

# Actual
with open("2023-12-03.txt") as file:
    actual = file.read()

n = re.search("\n", actual).start()
actual_key = number_coordinates(actual)
sum(check_number(number, start, end, actual, n) for number, (start, end) in actual_key)
