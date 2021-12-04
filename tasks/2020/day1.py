from itertools import product
from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day1.txt").read_text()


def puzzle1():
    entries = [int(i) for i in DATA.split("\n") if i]
    set_entries = set(entries)
    for i in entries:
        if (2020 - i) in set_entries:
            print(i * (2020 - i))
            break


def puzzle2():
    entries = [int(i) for i in DATA.split("\n") if i]
    set_entries = set(entries)
    for i, j in product(entries, entries):
        if (2020 - i - j) in set_entries:
            print(i * j * (2020 - i - j))
            break


if __name__ == "__main__":
    try:
        puzzle2()
    except:
        puzzle1()
