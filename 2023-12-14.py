def shift_rocks(doc: str, print_shift: bool = False):
    lines = doc.split("\n")
    cols = []
    for i in range(len(lines[0])):
        cols.append("".join(line[i] for line in lines))
    shifted_cols = [shift_string(col) for col in cols]
    if print_shift:
        new_lines = []
        for i in range(len(lines[0])):
            new_lines.append("".join(col[i] for col in shifted_cols))
        print("\n".join(new_lines))
    scores = [score_string(shifted_col) for shifted_col in shifted_cols]
    return sum(scores)


def shift_string(line: str):
    line_list = list(line)
    for ndx, char in enumerate(line):
        # Don't need to shift these
        if char in [".", "#"]:
            continue
        # Nowhere to shift these
        if ndx == 0 or line_list[ndx - 1] in ["#", "O"]:
            continue

        # Find the next place you hit a rock.
        lefts = "".join(line_list)[:ndx][::-1]
        line_list[ndx] = "."
        if "#" not in lefts and "O" not in lefts:
            line_list[0] = "O"
        else:
            for left_ndx, left in enumerate(lefts):
                if left in ["#", "O"]:
                    break
            line_list[ndx - left_ndx] = "O"
    return "".join(line_list)


def score_string(line: str):
    if "O" not in line:
        return 0
    line_bw = line[::-1]
    return sum(ndx for ndx, char in enumerate(line_bw, 1) if char == "O")


# Sample
sample = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

assert shift_rocks(sample, print_shift=True) == 136


# Actuals
with open("2023-12-14.txt") as file:
    actual = file.read()

shift_rocks(actual)
