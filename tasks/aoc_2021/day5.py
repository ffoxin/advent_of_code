import re
from collections import defaultdict
from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    items = [tuple(map(int, pattern.match(entry).groups())) for entry in entries]

    max_x, max_y = 0, 0
    field = defaultdict(int)
    for item in items:
        x1, y1, x2, y2 = item
        if x1 != x2 and y1 != y2:
            continue
        max_x = max(max_x, x1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y1)
        max_y = max(max_y, y2)

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                field[(x1, y)] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                field[(x, y1)] += 1
        else:
            raise RuntimeError("hmmm...")

        # print(item)

    # for y in range(max_y + 1):
    #     print(''.join(str(field.get((x, y), '.')) for x in range(max_x + 1)))

    result = sum(value > 1 for value in field.values())

    print(result)


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    items = [tuple(map(int, pattern.match(entry).groups())) for entry in entries]

    max_x, max_y = 0, 0
    field = defaultdict(int)
    for item in items:
        x1, y1, x2, y2 = item
        max_x = max(max_x, x1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y1)
        max_y = max(max_y, y2)

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                field[(x1, y)] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                field[(x, y1)] += 1
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for x in range(x1, x2 + 1):
                if y1 < y2:
                    field[(x, y1 + (x - x1))] += 1
                else:
                    field[(x, y1 - (x - x1))] += 1

        # print(item)

    # for y in range(max_y + 1):
    #     print(''.join(str(field.get((x, y), '.')) for x in range(max_x + 1)))

    result = sum(value > 1 for value in field.values())

    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
