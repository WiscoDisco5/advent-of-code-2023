import copy


def trace(doc: str):
    steps = doc.split("\n")
    directions = [step.split(" ") for step in steps]

    # Set grid:
    x = []
    y = []
    curr_x = 0
    curr_y = 0
    for direction, length, _ in directions:
        length = int(length)
        if direction == "R":
            curr_x = curr_x + length
        if direction == "L":
            curr_x = curr_x - length
        if direction == "U":
            curr_y = curr_y - length
        if direction == "D":
            curr_y = curr_y + length
        x.append(curr_x)
        y.append(curr_y)

    line_len = max(x) - min(x) + 1
    lines = max(y) - min(y) + 1
    # # ("." * line_len + "\n") * lines
    grid = [["." for _ in range(line_len)] for _ in range(lines)]

    # Get outside shape
    curr_x = 0 - min(x)
    curr_y = 0 - min(y)
    grid[curr_y][curr_x] = "#"
    for x_step, y_step in zip(x, y):
        if curr_x == x_step:
            start = min(curr_y, y_step)
            stop = max(curr_y, y_step)
            for line_y in range(start, stop + 1):
                grid[line_y][curr_x] = "#"
        if curr_y == y_step:
            start = min(curr_x, x_step)
            stop = max(curr_x, x_step)
            for line_x in range(start, stop):
                grid[curr_y][line_x] = "#"
        curr_y = copy.copy(y_step)
        curr_x = copy.copy(x_step)

    # Get inside shape
    polygon = [(x, y) for x, y in zip(x, y)]
    for x_pos in range(line_len):
        for y_pos in range(lines):
            if is_point_in_path(x_pos, y_pos, polygon):
                grid[y_pos][x_pos] = "#"

    return len([char for line in grid for char in line if char == "#"])


def is_point_in_path(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return True
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return True
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c


# Sample
sample = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

assert trace(sample) == 62

# Actual
with open("2023-12-18.txt") as file:
    actual = file.read()

trace(actual)
