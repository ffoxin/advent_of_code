import re
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

line_template = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))
    result = 0
    for line in entries:
        from1, to1, from2, to2 = map(int, line_template.match(line).groups())
        if from1 <= from2 <= to2 <= to1 or from2 <= from1 <= to1 <= to2:
            result += 1
    print(result)


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    result = 0
    for line in entries:
        from1, to1, from2, to2 = map(int, line_template.match(line).groups())
        if from1 <= to2 and from2 <= to1:
            result += 1
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
