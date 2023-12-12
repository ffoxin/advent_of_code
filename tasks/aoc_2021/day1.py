from pathlib import Path

DATA = (Path(__file__).parent / "data" / "day1.txt").read_text()


def puzzle1() -> None:
    entries = list(map(int, filter(bool, DATA.split("\n"))))
    result = sum(entries[i] < entries[i + 1] for i in range(len(entries) - 1))
    print(result)


def puzzle2() -> None:
    entries = list(map(int, filter(bool, DATA.split("\n"))))
    result = sum(
        sum(entries[i : i + 3]) < sum(entries[i + 1 : i + 4]) for i in range(len(entries) - 3)
    )
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
