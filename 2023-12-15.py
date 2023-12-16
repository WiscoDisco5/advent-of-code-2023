def hash_this(string: str):
    current_value = 0
    for char in string:
        current_value = current_value + ord(char)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value


sample = "HASH"
assert hash_this(sample) == 52

with open("2023-12-15.txt") as file:
    actual = file.read()

words = actual.split(",")
sum(hash_this(word) for word in words)

# sample
sample = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def sort_lenses(string: str):
    key = {}
    for step in string.split(","):
        if "=" in step:
            char, lens = step.split("=")
            drawer = key.get(hash_this(char), {})
            drawer[char] = lens
            key[hash_this(char)] = drawer
        else:
            char = step[:-1]
            drawer = key.get(hash_this(char), {})
            if drawer:
                drawer.pop(char, None)
                key[hash_this(char)] = drawer

    score = 0
    for drawer_id, drawer in key.items():
        for ndx, focal in enumerate(drawer.values(), 1):
            score = score + (drawer_id + 1) * ndx * int(focal)
    return score


assert sort_lenses(sample) == 145

sort_lenses(actual)
