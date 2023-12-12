from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()


def puzzle1() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    result = 0
    for entry in entries:
        left = next(filter(str.isdigit, entry))
        right = next(filter(str.isdigit, reversed(entry)))
        result += int(left + right)

    print(result)


def puzzle2() -> None:
    entries = list(filter(bool, DATA.split("\n")))
    valid_values = {str(i): i for i in range(10)}
    valid_values.update(
        {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
    )
    result = 0
    entry: str
    for entry in entries:
        left, right = None, None
        for pos in range(0, len(entry)):
            for value in valid_values:
                if left is None and entry.startswith(value, pos):
                    left = valid_values[value]
                if right is None and entry.startswith(value, -1 * pos - 1):
                    right = valid_values[value]
            if left and right:
                break

        assert left is not None
        assert right is not None

        result += left * 10 + right

    print(result)


# pylint: disable=duplicate-code
if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
