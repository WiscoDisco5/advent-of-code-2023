import numpy as np


def _expand(matrix, n: int = 2):
    ndx_offset = 0
    for ndx, row in enumerate(matrix):
        if np.all(row == "."):
            for _ in range(n - 1):
                matrix = np.insert(matrix, ndx + ndx_offset, ".", axis=0)
                ndx_offset = ndx_offset + 1
    return matrix


def expand_galaxy(doc: str, n: int = 2):
    temp_mat = np.matrix([[char for char in line] for line in doc.split("\n")])
    expand_row = _expand(temp_mat, n)
    expand_col = _expand(expand_row.T, n)
    return expand_col.T


def galaxies(matrix):
    gal_x, gal_y = np.where(matrix == "#")
    # nearest = {}
    steps = 0
    for x, y in zip(gal_x, gal_y):
        for check_x, check_y in zip(gal_x, gal_y):
            if x == check_x and y == check_y:
                continue
            # steps = abs(check_x - x) + abs(check_y - y)
            # nearest[(x, y)] = min(nearest.get((x, y), 1000000), steps)
            steps += abs(check_x - x) + abs(check_y - y)
    return int(steps / 2)


# sample
sample = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
sample_mat = expand_galaxy(sample)
assert galaxies(sample_mat) == 374

sample_mat = expand_galaxy(sample, 10)
assert galaxies(sample_mat) == 1030

sample_mat = expand_galaxy(sample, 100)
assert galaxies(sample_mat) == 8410

# actual
with open("2023-12-11.txt") as file:
    actual = file.read()
actual_mat = expand_galaxy(actual)
galaxies(actual_mat)

actual_mat = expand_galaxy(actual, 1000000)
galaxies(actual_mat)
