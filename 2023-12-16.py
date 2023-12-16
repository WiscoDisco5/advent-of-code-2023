import copy


def project(doc: str, max_c: int = 1000):
    parsed_doc = doc.split("\n")
    beams = [((0, 0), "right")]
    score = [[char for char in line] for line in parsed_doc]
    score[0][0] = "#"
    counter = 0
    while True:
        new_beams = []
        for (x, y), direction in beams:
            # Next step
            if direction == "right":
                x = x + 1
            elif direction == "left":
                x = x - 1
            elif direction == "down":
                y = y + 1
            else:
                y = y - 1
            # Check if that is a valid spot
            if x < 0 or y < 0:
                continue
            if x > len(parsed_doc[0]) - 1 or y > len(parsed_doc) - 1:
                continue
            score[y][x] = "#"
            mirror = parsed_doc[y][x]
            if mirror == ".":
                new_beams.append(((x, y), direction))
            elif mirror == "-":
                if direction in ["up", "down"]:
                    new_beams.append(((x, y), "left"))
                    new_beams.append(((x, y), "right"))
                else:
                    new_beams.append(((x, y), direction))
            elif mirror == "|":
                if direction in ["left", "right"]:
                    new_beams.append(((x, y), "up"))
                    new_beams.append(((x, y), "down"))
                else:
                    new_beams.append(((x, y), direction))
            elif mirror == "/":
                if direction == "up":
                    new_beams.append(((x, y), "right"))
                elif direction == "left":
                    new_beams.append(((x, y), "down"))
                elif direction == "down":
                    new_beams.append(((x, y), "left"))
                else:
                    new_beams.append(((x, y), "up"))
            else:
                if direction == "up":
                    new_beams.append(((x, y), "left"))
                elif direction == "left":
                    new_beams.append(((x, y), "up"))
                elif direction == "down":
                    new_beams.append(((x, y), "right"))
                else:
                    new_beams.append(((x, y), "down"))
        counter = counter + 1
        if not new_beams or counter > max_c:
            break
        beams = copy.copy(list(set(new_beams)))
    score = "\n".join("".join(line) for line in score)
    print(score)
    return len([char for char in score if char == "#"])


# SAMPLE
sample = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

assert project(sample) == 46

with open("2023-12-16.txt") as file:
    actual = file.read()

project(actual, 1000)
project(actual, 2000)
project(actual, 542)
