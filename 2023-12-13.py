import numpy as np


def create_valleys(doc: str) -> list[np.matrix]:
    valleys = []
    docs = doc.split("\n\n")
    for doc in docs:
        valleys.append(np.matrix([[char for char in line] for line in doc.split("\n")]))
    return valleys


def find_mirror(string: str) -> list[int]:
    mirrors = []
    for i in range(1, len(string)):
        left = string[:i]
        right = string[i:]
        min_string = min(len(left), len(right))
        if min_string == len(left):
            right = right[:min_string]
        else:
            left = left[-min_string:]
        if left == right[::-1]:
            mirrors.append(i)
    return mirrors


def search_for_mirrors(matrix):
    strings = ["".join(line) for line in matrix.tolist()]
    mirrors_vert = [find_mirror(string) for string in strings]
    intersect_vert = set(mirrors_vert[0])
    for split in mirrors_vert:
        intersect_vert = intersect_vert.intersection(set(split))

    strings = ["".join(line) for line in matrix.T.tolist()]
    mirrors_hor = [find_mirror(string) for string in strings]
    intersect_hor = set(mirrors_hor[0])
    for split in mirrors_hor:
        intersect_hor = intersect_hor.intersection(set(split))

    if len(intersect_vert) != 1 and len(intersect_hor) != 1:
        raise ValueError("problem too many")
    if intersect_hor:
        return list(intersect_hor)[0] * 100
    return list(intersect_vert)[0]


# Sample
sample = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.\n
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
sample_matrices = create_valleys(sample)
assert sum(search_for_mirrors(matrix) for matrix in sample_matrices) == 405

# Actual
with open("2023-12-13.txt") as file:
    actual = file.read()
actual_matrices = create_valleys(actual)
sum(search_for_mirrors(matrix) for matrix in actual_matrices)
