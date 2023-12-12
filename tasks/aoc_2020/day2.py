import re
from pathlib import Path


DATA = (Path(__file__).parent / "data" / "day2.txt").read_text()


def puzzle1() -> None:
    entries = [i for i in DATA.split("\n") if i]
    valid = 0
    for entry in entries:
        count_min, count_max, char, phrase = re.match(
            r"(\d+)-(\d+) ([a-z]): ([a-z]+)", entry
        ).groups()
        is_valid = int(count_min) <= phrase.count(char) <= int(count_max)
        if is_valid:
            valid += 1

    print(valid)


def puzzle2() -> None:
    entries = [i for i in DATA.split("\n") if i]
    valid = 0
    for entry in entries:
        first, second, char, phrase = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", entry).groups()
        count = [phrase[int(i) - 1] == char for i in (first, second)]
        is_valid = sum(count) == 1
        if is_valid:
            valid += 1
    print(valid)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
