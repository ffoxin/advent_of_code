from operator import itemgetter
from pathlib import Path
from typing import Tuple, Set

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def print_it(d: Set[Tuple[int, int]]):
    for y in range(max(map(itemgetter(1), d)) + 1):
        print(
            "".join(
                [
                    "#" if (x, y) in d else "."
                    for x in range(max(map(itemgetter(0), d)) + 1)
                ]
            )
        )


def puzzle1():
    entries = DATA.split("\n")
    dots = set(
        map(lambda v: tuple(map(int, v.split(","))), entries[: entries.index("")])
    )
    instructions = list(
        map(
            lambda v: (
                v.split()[-1].split("=")[0],
                int(v.split()[-1].split("=")[1]),
            ),
            filter(bool, entries[entries.index("") + 1 :]),
        )
    )

    for along, line in instructions[:1]:
        if along == "y":
            dots = {(x, y if y < line else (line - (y - line))) for x, y in dots}
        elif along == "x":
            dots = {(x if x < line else (line - (x - line)), y) for x, y in dots}

    print(len(dots))


def puzzle2():
    entries = DATA.split("\n")
    dots = set(
        map(lambda v: tuple(map(int, v.split(","))), entries[: entries.index("")])
    )
    instructions = list(
        map(
            lambda v: (
                v.split()[-1].split("=")[0],
                int(v.split()[-1].split("=")[1]),
            ),
            filter(bool, entries[entries.index("") + 1 :]),
        )
    )

    for along, line in instructions:
        if along == "y":
            dots = {(x, y if y < line else (line - (y - line))) for x, y in dots}
        elif along == "x":
            dots = {(x if x < line else (line - (x - line)), y) for x, y in dots}

    print_it(dots)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
