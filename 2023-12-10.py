import copy
from typing import Optional

import numpy as np


def make_matrix(doc: str):
    return np.matrix([[char for char in line] for line in doc.split("\n")])


def connected_cells(
    matrix, x: int, y: int
) -> Optional[tuple[tuple[int, int], tuple[int, int]]]:
    turn = matrix[x, y]
    if turn == "|":
        return (x - 1, y), (x + 1, y)
    if turn == "-":
        return (x, y - 1), (x, y + 1)
    if turn == "L":
        return (x - 1, y), (x, y + 1)
    if turn == "J":
        return (x, y - 1), (x - 1, y)
    if turn == "7":
        return (x, y - 1), (x + 1, y)
    if turn == "F":
        return (x + 1, y), (x, y + 1)
    return None


def start_connected_cells(matrix):
    x, y = np.where(matrix == "S")
    cells = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    connected = []
    for cell in cells:
        try:
            matrix[cell]
        except:
            continue
        conn_cells = connected_cells(matrix, *cell)
        if conn_cells and (int(x), int(y)) in conn_cells:
            connected.append(cell)
    return connected


def trace(matrix):
    start, _ = start_connected_cells(matrix)
    next_cell = copy.copy(start)
    prior = copy.copy(np.where(matrix == "S"))
    path = [prior, next_cell]
    while True:
        cells = connected_cells(matrix, *next_cell)
        if cells is None:
            raise ValueError(f"problem at {next_cell}")
        if cells[0] == prior:
            prior = copy.copy(next_cell)
            next_cell = copy.copy(cells[1])
        else:
            prior = copy.copy(next_cell)
            next_cell = copy.copy(cells[0])
        path.append(next_cell)
        if matrix[next_cell] == "S":
            break
    return path


sample = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
sample_mat = make_matrix(sample)

assert (len(trace(sample_mat)) - 1) // 2 == 8

sample1 = """.....
.S-7.
.|.|.
.L-J.
....."""
sample1_mat = make_matrix(sample1)

assert (len(trace(sample1_mat)) - 1) // 2 == 4

# actual
with open("2023-12-10.txt") as file:
    actual = file.read()

actual_mat = make_matrix(actual)

(len(trace(actual_mat)) - 1) // 2
