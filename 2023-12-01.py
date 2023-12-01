import re

# Sample data
sample_doc = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def extract_sum(doc: str):
    strings = doc.splitlines()
    numbers = []
    for string in strings:
        num_str = re.sub("[^0-9]", "", string)
        numbers.append(int(num_str[0] + num_str[-1]))
    return sum(numbers)


extract_sum(sample_doc)

# Actual data
with open("2023-12-01.txt") as file:
    actual_doc = file.read()

extract_sum(actual_doc)
