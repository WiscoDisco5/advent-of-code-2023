import re


def _xmas_dict(numbers: str):
    x, m, a, s = re.findall("[0-9]{1,}", numbers)
    return {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}


def _mapper(mappers: str):
    mappers = mappers[:-1]
    mappers_dict = [mapper.split("{") for mapper in mappers.split("}\n")]
    return {key: value.split(",") for key, value in mappers_dict}


def _apply_mapper(x: int, m: int, a: int, s: int, mapper: dict[str, list[str]]):
    location = "in"
    while True:
        checks = [step.split(":") for step in mapper[location]]
        for check in checks:
            if len(check) == 1:
                location = check[0]
            else:
                if eval(check[0]):
                    location = check[1]
                    break
        if location in ["A", "R"]:
            break
    return location


def parse_and_map(doc: str):
    mappers, codes = doc.split("\n\n")

    codes = [_xmas_dict(code) for code in codes.split("\n")]
    mappers = _mapper(mappers)

    return [(code, _apply_mapper(**code, mapper=mappers)) for code in codes]


# sample
sample = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}\n

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

sample_mapped = parse_and_map(sample)
assert (
    sum(sum(codes.values()) for codes, accept in sample_mapped if accept == "A")
    == 19114
)

# actual
with open("2023-12-19.txt") as file:
    actual = file.read()

actual_mapped = parse_and_map(actual)

sum(sum(codes.values()) for codes, accept in actual_mapped if accept == "A")
