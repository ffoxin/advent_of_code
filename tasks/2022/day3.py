from pathlib import Path

DATA = (Path(__file__).parent / "data" / (Path(__file__).stem + ".txt")).read_text()

priorities = {
    **{chr(i + ord("a")): i + 1 for i in range(26)},
    **{chr(i + ord("A")): i + 27 for i in range(26)},
}


def puzzle1():
    entries = list(filter(bool, DATA.split("\n")))
    result = 0
    for line in entries:
        assert len(line) % 2 == 0
        left, right = line[: len(line) // 2], line[len(line) // 2 :]
        common = set(left) & set(right)
        assert len(common) == 1
        result += priorities[list(common)[0]]
    print(result)


def puzzle2():
    entries = list(filter(bool, DATA.split("\n")))
    result = 0
    for a, b, c in zip(entries[::3], entries[1::3], entries[2::3]):
        common = set(a) & set(b) & set(c)
        assert len(common) == 1
        result += priorities[list(common)[0]]
    print(result)


if __name__ == "__main__":
    try:
        puzzle2()
    except NameError as e:
        if str(e) != "name 'puzzle2' is not defined":
            raise
        puzzle1()
