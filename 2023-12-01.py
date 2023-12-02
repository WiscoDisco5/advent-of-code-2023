import re

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIGITS_RE = "|".join(DIGITS)
DIGITS_DICT = {digit: str(i) for i, digit in enumerate(DIGITS, start=1)}
DIGITS_DICT.get("sdf", 1)


def overlapping_findall(pattern: str, string: str) -> list[str]:
    # Adjusted from https://mail.python.org/pipermail/tutor/2005-September/041120.html
    resultlist = []
    pos = 0

    while True:
        result = re.search(pattern, string)
        if result is None:
            break
        resultlist.append(string[result.start() : result.end()])
        pos = result.start() + 1
        string = string[pos:]
    return resultlist


def extract_sum(doc: str, convert_digits: bool = False) -> int:
    strings = doc.split("\n")
    if convert_digits:
        digits = [
            overlapping_findall(f"({DIGITS_RE}|[0-9])", string) for string in strings
        ]
        numbers = [[DIGITS_DICT.get(d, d) for d in string] for string in digits]
    else:
        numbers = [re.findall("[0-9]", string) for string in strings]
    return sum(int(i[0] + i[-1]) for i in numbers)


# Sample data
sample_doc = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

assert extract_sum(sample_doc) == 142

sample_doc_digits = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

assert extract_sum(sample_doc_digits, convert_digits=True) == 281

# Actual data
with open("2023-12-01.txt") as file:
    actual_doc = file.read()

extract_sum(actual_doc)
extract_sum(actual_doc, convert_digits=True)
